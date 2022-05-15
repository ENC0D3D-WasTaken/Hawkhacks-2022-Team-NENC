from main import *

@bot.command(aliases=['HELP','h','H'])
async def help(ctx):
    Help = Embed(title="Help", description="List of commands. The bot currently has 5 coin types, BSD (BotStableDollar), ENX (Enfix), CAC (Catcoin), PLY (Ploy), and VSP (Vespine).", color=0x5bdef5)
    Help.set_thumbnail(url="https://media.discordapp.net/attachments/974847550039416902/975237671909748736/91D132C4-287C-4723-ADC9-09BA81331692.jpeg1.png?width=567&height=567")
    Help.add_field(name="`>help`", value="Sends this message", inline=True)
    Help.add_field(name="`>register`", value="Registers an account for you", inline=True)
    Help.add_field(name="`>mine`", value="'Mines' BSD by solving math problems", inline=True)
    Help.add_field(name="`>shop`", value="Allows you to buy fake NFTs", inline=True)
    Help.add_field(name="`>trade`", value="Send BSD to another user", inline=True)
    Help.add_field(name="`>leaderboard`", value="Shows global leaderboard for richest player", inline=True)
    Help.add_field(name="`>price`", value="Shows price of all coins", inline=True)
    Help.add_field(name="`>inventory`", value="Shows your coin balance and NFT collection", inline=True)
    Help.add_field(name="`>exchange`", value="Allows you to exchange BSD to a different coin and vice versa", inline=True)
    Help.add_field(name="`>about`", value="Bot info and credits", inline=True)
    await ctx.send(embed=Help)