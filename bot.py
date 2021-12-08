from vkbottle.user import User, Message
from config import token, msg

client = User(token=token)

@user.on.chat_message()
async def raid(event: Message);
  a = 1
  while a > 0:
    await event.answer(msg)

client.run_forever()
