from main import *

@bot.command(aliases=['LEADERBOARD', 'l', 'L'])
async def leaderboard(ctx):
    users = []
    ballist = db.query(User).all()
    prices = db.query(CryptoCurrencies).all()
    nfts = db.query(NFTs).all()
    enfixCourse = prices[0].price
    for user in ballist:
        print(234534675831)
        owned = [user.enfix,user.catcoin,user.ploy,user.vespine,user.xps]
        bal = 0
        for i in range(len(prices)):
            print(21286789731)
            if user.memberId in prices[i].holders:
                print(1543)
                bal +=  owned[i] * prices[i].price
                print(1321)
                print(bal) 
        if len(nfts) != 0:
            print('Buy some NFTs using >shop')
            for nft in nfts:
                print('dasda')
                if user.memberId == nft.holder:
                    print(23433443434334431)
                    bal += nft.mintPrice * enfixCourse
        else:
            pass
        list = []
        list.append(user.name)
        list.append(bal)
        list.append(user.avatar_url)
        for i in range(len(list)):
            print(list[i])
        users.append(list)
    users.sort(key=lambda x: x[1], reverse=False)
    leaderboard = Embed(title="Leaderboard", color=0x5bdef5)
    print(2334344343431)
    leaderboard.add_field(name="💰 The richest crypto magnates:", value="(Measured in total combined B$D value of all of their assets).", inline=False)
    for i in range(len(users)):
        print(233434431)
        leaderboard.add_field(name=f"{users[i]['name']}", value=f"{users[i]['balance']} B$D.", inline=True)
    leaderboard.set_thumbnail(url=f"{users[0]['url']}")
    leaderboard.set_footer(text=f"To see yourself here by mining, buying cryptocurrency and buying NFTs.", icon_url=f"https://media.discordapp.net/attachments/974847550039416902/975237671909748736/91D132C4-287C-4723-ADC9-09BA81331692.jpeg1.png?width=567&height=567")
    print(23134)
    msg = await ctx.send(embed=leaderboard)
    print(2314334)