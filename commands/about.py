from main import *

@bot.command(aliases=['ABOUT','a','A'])
async def about(ctx):

    About = Embed(title="About", url="https://devpost.com/software/crypto-tycoon-bot", description="Info about the bot", color=0x5bdef5)
    About.add_field(name="Developers", value="Chriss, ENC0D3D and Nooz", inline=True)
    await ctx.send(embed=About)