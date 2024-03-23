import hikari
import lightbulb
from time import sleep
from dotenv import load_dotenv
import os



load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')


bot = lightbulb.BotApp(token = TOKEN, intents = hikari.Intents.ALL)

@bot.command
@lightbulb.option("word","say a word")
@lightbulb.command("say", "say")
@lightbulb.implements(lightbulb.SlashCommand)
async def say(ctx: lightbulb.SlashContext) -> None:
        await ctx.respond(ctx.options.word, flags=hikari.MessageFlag.EPHEMERAL)



bot.run()