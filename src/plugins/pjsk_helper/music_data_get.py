from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from .config import Config
from nonebot import get_plugin_config
import time
import re
import json

config = get_plugin_config(Config)

def scroll_and_wait(driver, scroll_pause_time=1):
    last_height = driver.execute_script("return document.body.scrollHeight")  # 获取初始页面高度

    while True:
        # 滚动到页面底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # 等待加载新内容
        time.sleep(scroll_pause_time)
        
        # 获取新的页面高度
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        # 检查是否加载了新的内容，如果没有新的内容则退出循环
        if new_height == last_height:
            time.sleep(1)
            break
        last_height = new_height

def update_music():
    chromedriver_path = config.chromedriver_path
    service = Service(chromedriver_path)
    chrome_options = Options()

    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = 'https://sekai.best/music'
    driver.get(url)

    scroll_and_wait(driver)

    html = driver.page_source

    soup = BeautifulSoup(html, "lxml")
    music_info = []
    for item in soup.find_all("div", class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-md-4 MuiGrid-grid-lg-3 MuiGrid-grid-xl-3 css-1etv89n"):
        try:
            music_id_path = item.find("a")["href"]
            match = re.search(r'\d+', music_id_path)
            music_id = match.group()

            music_name = item.find("div", class_="MuiCardMedia-root css-bc9mfn")["title"].split("|")[0].strip()
            
            music_cover_raw=  item.find("div", class_="MuiCardMedia-root css-bc9mfn")["style"]
            music_cover_webp_re = re.search(r'url\("(.*?)"\)', music_cover_raw)
            music_cover_webp = music_cover_webp_re.group(1)
            music_cover_png = music_cover_webp.replace('.webp', '.png')

            music_info.append({
                "music_id":music_id,
                "music_name":music_name,
                "music_cover_png":music_cover_png
            })
        except:
            break
    with open("src/others/pjsk_music.json", "w",encoding="UTF-8") as json_file:
        json.dump(music_info, json_file, ensure_ascii=False, indent=4)