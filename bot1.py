
from highrise import BaseBot, __main__
from highrise.models import SessionMetadata, User
from highrise import _main_
from asyncio import run as arun

class Bot(BaseBot):
  
    async def on_start(self, session_metadata: SessionMetadata):
        print("hi im alive?") # this should output in the terminal

#    this function is called every time a user sends a message in the room with the bot
    async def on_chat(self, user: User, message: str):
#        we log this message to the terminal on your machine with print
        print(f"{user.username} said: {message}")

    async def run(self, room_id, token):
        await __main__.main(self, room_id, token)

if __name__ == "__main__":
    room_id = "66c9399a00cf1d85cefe5d1d"
    token = "da7e9a340ce6534f8fe47718dcb02bb5659cb6197284195c14cde1f2f53398ec"
    arun(Bot().run(room_id, token))