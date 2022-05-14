from main import *

@bot.command(aliases=['HELP', 'h', 'H'])
async def join(ctx):
    Help = Embed(title="Help", description=f"{user.name}, you have been successfully registered.", color=30646)
    Help.set_image(url=user.avatar_url)
    msg = await ctx.send(embed=Registered)