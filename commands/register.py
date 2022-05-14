from main import *

@bot.command(aliases=['JOIN', 'j', 'J'])
async def join(ctx):
    user = ctx.message.author
    query = db.query(User).filter(User.memberId == user.id).first()
    print(query,type(query))
    if query is None:
        newUser = User(name=user.name,memberId=user.id,timestamp=datetime.now(), balance=50)
        db.add(newUser)
        try:
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        Registered = Embed(title="Successfully Registered", description=f"{user.name}, you have been successfully registered.", color=0x93f5e9)
        Registered.set_image(url=user.avatar_url)
        msg = await ctx.send(embed=Registered)
        await deleteMessage(msg)
    else:
        msg = await ctx.send(f'You are already a part of the tycoon, {query.name}.')
        await deleteMessage(msg)