from nonebot import on
from nonebot.adapters.onebot.v11 import Bot, MessageSegment, GroupMessageEvent

SOURCE_GROUP_ID = 856320339
TARGET_GRPUO_ID = 856320339

my_matcher = on(type="message")

@my_matcher.handle()
async def handle_group_message(bot: Bot, event: GroupMessageEvent):
    group_id = event.group_id
    user_id = event.user_id
    message_text = event.get_plaintext()

    if group_id == SOURCE_GROUP_ID:
        mention_message = MessageSegment.at(user_id) + f" 发送了：{message_text}"
        await bot.send_group_msg(group_id=TARGET_GRPUO_ID, message=mention_message)
