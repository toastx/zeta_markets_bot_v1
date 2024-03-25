@bot.command
@lightbulb.command("place","place order")
@lightbulb.implements(lightbulb.SlashCommand)
async def place_order(ctx: lightbulb.SlashContext) -> None:
        account = Commands.retrieve(ctx.author.username)
        order_details = await Commands.create_order(account)
        await ctx.respond(order_details, flags=hikari.MessageFlag.EPHEMERAL)