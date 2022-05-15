from main import *

@bot.command(aliases=['RANK','ra','RA'])
async def balence(ctx):
    user = getUser(ctx.message.author.id)
    if user is not False:
        ctx.send(f'{user.name}, your balance is: {user.balance}BSD.')
    else:
        msg = await ctx.send(f'You are not a part of the tycoon, {user.name}.')
        deleteMessage(msg)