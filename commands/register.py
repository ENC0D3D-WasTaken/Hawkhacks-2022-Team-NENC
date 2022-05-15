from main import *

@bot.command(aliases=['REG', 'r', 'R'])
async def register(ctx):
    user = ctx.message.author
    query = db.query(User).filter(User.memberId == user.id).first()
    print(query,type(query))
    if query is None:
        newUser = User(name=user.name,memberId=user.id,timestamp=datetime.utcnow(), balance=100)
        db.add(newUser)
        try:
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        Registered = Embed(title="Successfully Registered", description=f"{user.name}, you have been successfully registered.", color=0x93f5e9)
        Registered.set_image(url=user.avatar_url)
        msg = await ctx.send(embed=Registered)
    else:
        msg = await ctx.send(f'You are already a part of the tycoon, {query.name}.')