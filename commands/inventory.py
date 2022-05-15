from main import *

@bot.command(aliases=['INVENTORY', 'INV', 'i', 'I'])
async def inventory(ctx):
    await ctx.message.delete(delay=0)
    user = getUser(ctx.message.author.id)
    ownedCrypto = [
        user.enfix,
        user.catcoin,
        user.ploy,
        user.vespine,
        user.xps
    ]
    userValue = user.balance
    prices = []
    query = db.query(CryptoCurrencies).all()
    for crypto in query:
        prices.append([crypto.abr,crypto.price,crypto.name])
    nfts = db.query(NFTs).filter(NFTs.holder == user.memberId).all()
    if user is not False:
        currentBalanceEmbed = Embed(title=f"{user.name}", color=0x5bdef5)
        currentBalanceEmbed.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
        currentBalanceEmbed.add_field(name="💰 Balance", value=f"Your stable currency balance is {user.balance} B$D.", inline=False)
        for i in range(len(ownedCrypto)):
            userValue += ownedCrypto[i] * prices[i][1]
            currentBalanceEmbed.add_field(name=f"{prices[i][2]}", value=f"{prices[i][0]} worth {prices[i][1]*ownedCrypto[i]} B$D.", inline=False)
        currentBalanceEmbed.add_field(name="NFTs:", value=f"({len(nfts)} owned.)", inline=True)
        if len(nfts) > 0:
            for nft in nfts:
                currentBalanceEmbed.add_field(name=nft.name, value=f"Worth {nft.mintPrice} ENF", inline=False)
                currentBalanceEmbed.set_image(url=nft.url)
        else:
            pass
        currentBalanceEmbed.add_field(name="Total inventory value:", value=f"Your total inventory value is {userValue} B$D.", inline=False)
        msg = await ctx.send(embed=currentBalanceEmbed)
        await msg.delete(delay=10)
    else:
        msg = await ctx.send(f'You are not a part of the tycoon, {user.name}.')
        await deleteMessage(msg)