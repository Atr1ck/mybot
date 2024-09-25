from nonebot import on 
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent

mute = on(type="message")

@mute.handle()
async def mute(bot: Bot,event: GroupMessageEvent):
    user_id = event.user_id
    group_id = event.group_id
    message_text = event.get_plaintext()

    if "晚安" in message_text:
        await bot.set_group_ban(group_id=group_id, user_id=user_id, duration=28800)
