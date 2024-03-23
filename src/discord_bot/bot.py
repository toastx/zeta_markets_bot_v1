import hikari
import lightbulb
from time import sleep
from dotenv import load_dotenv
import os
load_dotenv()


TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = 1221075984262893629

bot = lightbulb.BotApp(token = TOKEN, prefix= "zm")


