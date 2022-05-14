from main import *

@bot.command(aliases=['JOIN, j, J'])
async def join(ctx):
    user = ctx.message.author
    query = db.execute('SELECT FROM users WHERE name = :name', {'name': user.name})
    if query == None:
        newUser = User(name=user.name,memberId=user.id,timestamp=datetime.now(), balance=50)
        db.add(newUser)
        db.commit()
        Registered = Embed(title="Successfully Registered", description=f"{user.name}, you have been successfully registered.", color=30646)
        Registered.set_image(url=user.avatar_url)
        msg =  await ctx.send(embed=Registered)
    else:
        msg = await ctx.send('You are already a part of the tycoon, {user.name}.')
    await deleteMessage(msg)