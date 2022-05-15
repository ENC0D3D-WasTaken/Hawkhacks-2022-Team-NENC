from main import *

@bot.command(aliases=['REGISTER', 'REG', 'r', 'R'])
async def register(ctx):
    await ctx.message.delete(delay=0)
    user = ctx.message.author
    query = db.query(User).filter(User.memberId == user.id).first()
    print(query,type(query))
    if query is None:
        newUser = User(name=user.name,memberId=user.id,timestamp=datetime.utcnow(), balance=100,enfix=0,catcoin=0,ploy=0,vespine=0,xps=0)
        db.add(newUser)
        try:
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        Registered = Embed(title="Successfully Registered", description=f"{user.name}, you have been successfully registered.", color=0x5bdef5)
        Registered.set_image(url=user.avatar_url)
        msg = await ctx.send(embed=Registered)
        await deleteMessage(msg)
    else:
        msg = await ctx.send(f'You are already a part of the tycoon, {query.name}.')