from main import *

@bot.command(aliases=['SHOP', 'sh', 'SH', 's', 'S'])
async def shop(ctx):
    await ctx.message.delete(delay=0)
    user = getUser(ctx.message.author.id)
    if user is not False:
        Shop = Embed(title="Shop", description="Buy some NFTs! React with the number of the NFT you want to buy.", color=0x5bdef5)

        assasin1 = discord.File("images/nfts/assasin1.png", filename="assasin1.png")
        assasin2 = discord.File("images/nfts/assasin2.png", filename="assasin2.png")
        
        Shop.set_image(url="attachment://assasin1.png")
        Shop.set_image(url="attachment://assasin2.png")
        
        await ctx.send(embed=Shop)
        
        await msg.add_reaction("1️⃣")
    else:
        msg = await ctx.send(f'You are not a part of the tycoon, {user.name}')
        await deleteMessage(msg)