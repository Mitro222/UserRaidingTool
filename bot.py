from vkbottle.user import User, Message
from config import token, msg

client = User(token=token)

a = 1


@client.on.chat_message()
async def raid(event: Message):
    while a > 0:
        await event.answer(msg)

client.run_forever()
