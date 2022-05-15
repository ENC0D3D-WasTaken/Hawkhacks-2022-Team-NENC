from main import *

@bot.command(aliases=[])
async def leaderboard(ctx):
    user = getUser(ctx.message.author.id)
    ballist = db.query(User).filter().all()