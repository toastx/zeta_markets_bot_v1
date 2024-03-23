import hikari
import lightbulb
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = 1221075984262893629


bot = lightbulb.BotApp(token = TOKEN, prefix= '?')

@bot.command
@lightbulb.command("commands", "botcommands")
@lightbulb.implements(lightbulb.PrefixCommand)
async def commands(ctx):
    embed = hikari.Embed(
        title="Commands",
        description=f"**?fp collection_name** = basic details of collection \n"
                    f"**?crypto coinname** = current price of coin \n"
                    f"**?convert amount coin1 coin2** = converts amount of coin1 to coin 2 \n"
                    f"**?convertusd amount coin** = converts amount of coin to usd \n\n\n "
                    f"**DM COMMANDS**\n "
                    f"**?balance walletaddress** = balance of wallet \n"
                    f"**?buys walletaddress** = last 10 buys in ME\n"
                    f"**?sales walletaddress** = last 10 sales in ME\n"

    )
    await bot.rest.create_message(CHANNEL_ID, embed=embed)


bot.run()