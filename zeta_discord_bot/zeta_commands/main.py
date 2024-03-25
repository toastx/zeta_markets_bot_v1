import hikari
import lightbulb
from time import sleep
from dotenv import load_dotenv
import os
from commands import Commands
import asyncio


load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
bot = lightbulb.BotApp(token = TOKEN, intents = hikari.Intents.ALL)

@bot.command
@lightbulb.option("privatekey","enter privatekey")
@lightbulb.command("store", "store")
@lightbulb.implements(lightbulb.SlashCommand)
async def store(ctx: lightbulb.SlashContext) -> None:
        Commands.store(ctx.author.username,ctx.options.privatekey)
        await ctx.respond("wallet stored successfully", flags = hikari.MessageFlag.EPHEMERAL)


@bot.command
@lightbulb.command("details", "details", auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def details(ctx: lightbulb.SlashContext) -> None:
        account = Commands.retrieve(ctx.author.username)
        account_details = await Commands.details(account)
        embed = hikari.Embed(
        title="Commands",
        description=f"Balance: ${account_details.balance}\n"
                f"Unrealized PnL: ${account_details.unrealized_pnl} \n"
                f"Equity: ${account_details.equity}\n"
                f"Position Value: ${account_details.position_value} \n "
                f"Initial Margin: ${account_details.initial_margin}\n "
                f"Maintenance Margin: ${account_details.maintenance_margin}\n"
                f"Margin Usage: {account_details.margin_utilization:.2%}\n"
                f"Leverage: {account_details.leverage}x \n"
        )
        await ctx.respond(embed, flags=hikari.MessageFlag.EPHEMERAL)

@bot.command
@lightbulb.command("place","place order",auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def place_order(ctx: lightbulb.SlashContext) -> None:
        account = Commands.retrieve(ctx.author.username)
        order_details = await Commands.create_order(account)
        
        await ctx.respond(order_details, flags=hikari.MessageFlag.EPHEMERAL)


@bot.command
@lightbulb.command("view","place order")
@lightbulb.implements(lightbulb.SlashCommand)
async def view_order(ctx: lightbulb.SlashContext) -> None:
        account = Commands.retrieve(ctx.author.username)
        order_details = await Commands.view_order(account)
        await ctx.respond(order_details, flags=hikari.MessageFlag.EPHEMERAL)





bot.run()
