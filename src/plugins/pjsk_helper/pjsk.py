from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment, Message
from nonebot.params import CommandArg
import time
from bs4 import BeautifulSoup
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import re
import json
from . import music_find
from nonebot import get_plugin_config
from .config import Config

config = get_plugin_config(Config)

pjsk_card = on_command("pjsk card")
pjsk_music = on_command("pjsk music")

@pjsk_card.handle()
async def handle_psjk_card(bot: Bot, event: GroupMessageEvent, args: Message = CommandArg()):
    if config.pjsk_plugin_enabled == False:
        print("插件已关闭")
        return
    group_id = event.group_id  
    if group_id not in config.monitored_group and config.monitored_group != []:
        return 
    arg_text = args.extract_plain_text().strip()
    if not arg_text:
        select = random.randint(0,1)
    elif arg_text == '1' or arg_text == '0':
        select = arg_text
    else:
        await bot.send_group_msg(group_id=group_id, message="参数错误")
        return 
    # await bot.send_group_msg(group_id=group_id,message=MessageSegment.at(event.user_id) + " 正在获取卡面，请稍等")
    chrome_driver_path = '/usr/bin/chromedriver'
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    card_num = random.randint(1, 996)
    url = f'https://sekai.best/card/{card_num}'
    driver.get(url)
    while 1:
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")
        item = soup.find('div', class_='MuiCardMedia-root card-img-root css-ugxqjx', role="img")
        if item != None:
            break
        else:
            time.sleep(1)
    card_url_webp = item["style"]
    card_normal_webp_re = re.search(r'url\("(.*?)"\)', card_url_webp)
    card_normal_webp = card_normal_webp_re.group(1)
    card_normal_png = card_normal_webp.replace('.webp', '.png')
    card_train_png = card_normal_png.replace('normal', 'after_training')
    png = {"0":card_normal_png, "1":card_train_png}
    driver.quit()
    try:
        await bot.send_group_msg(group_id=group_id, message=MessageSegment.image(png[select]))
    except:
        # await bot.send_group_msg(group_id=group_id, message="该卡无特训后角色图，将发送特训前角色图")
        await bot.send_group_msg(group_id=group_id, message=MessageSegment.image(png["0"]))

@pjsk_music.handle()
async def pjsk_music(bot:Bot, event: GroupMessageEvent, args: Message = CommandArg()):
    if config.pjsk_plugin_enabled == False:
        print("插件已关闭")
        return
    group_id = event.group_id
    with open("src/others/pjsk_music.json", "r", encoding="UTF-8") as json_file:
        music_info = json.load(json_file)

    arg_text = args.extract_plain_text().strip()
    difficulty, music_idorname= arg_text.split(" ")

    if difficulty not in ["easy", "normal", "hard", "expert", "master", "append"]:
        await bot.send_group_msg(group_id=group_id, message="难度输入错误，请重试")
        return
    elif music_idorname.isdigit():
        music = music_find.find_by_music_id(music_idorname, music_info)
        if not music:
            await bot.send_group_msg(group_id=group_id, message="id输入错误")
            return
    else:
        music = music_find.find_by_music_name(music_idorname, music_info)
        if not music:
            await bot.send_group_msg(group_id=group_id, message="歌曲名输入错误")
            return
    
    music_id = int(music["music_id"])
    music_sheet = f"https://storage.sekai.best/sekai-music-charts/jp/{music_id:04}/{difficulty}.png"
    message = f'歌曲名: {music["music_name"]}\n' + f'歌曲id: {music["music_id"]}' + MessageSegment.image(music["music_cover_png"]) + "\n" + f'难度:{difficulty}\n'
    try:
        message1 = message + MessageSegment.image(music_sheet)
        await bot.send_group_msg(group_id=group_id, message=message1)
    except:
        message2 = message + "暂无该谱"
        await bot.send_group_msg(group_id=group_id, message=message2)