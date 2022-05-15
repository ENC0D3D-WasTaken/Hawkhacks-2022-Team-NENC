from main import *

@bot.command(aliases=['EXCHANGE', 'e', 'E'])
async def exchange(ctx):
    await ctx.message.delete(delay=0)
    user = getUser(ctx.message.author.id)
    query = db.query(CryptoCurrencies).all()

    if user is not False:
        Shop = Embed(title="Shop", description="Buy some NFTs! React with the number of the NFT you want to buy.", color=0x5bdef5)

        Shop.set_thumbnail(url=f"{ctx.message.author.avatar_url}")
        
        Shop.add_field(name="💰 Balance", value=f"Your stable currency balance is {user.balance} B$D.", inline=False)
        Shop.add_field(name="💰 How to buy", value=f"Type buy (crypto number) (quantity).", inline=False)
        for i in range(len(query)):
            Shop.add_field(name=f"{i+1}.  {query[i].name}", value=f"{query[i].abr} worth {query[i].price} B$D.", inline=False)
        thismsg = await ctx.send(embed=Shop)
        await thismsg.delete(delay=30)
        answer = await bot.wait_for('message', check=lambda message: message.author == ctx.message.author)
        if answer.content.isdigit():
            answer2 = await bot.wait_for('message', check=lambda message: message.author == ctx.message.author)
            if answer2.content.isdigit() and int(answer2.content) <= user.balance * query[int(answer.content)-1].price:
                if int(answer.content) <= len(query) and int(answer.content) > 0:
                    if int(answer2.content) <= user.balance and int(answer2.content) > 0:
                        user.balance -= int(answer2.content)
                        abr = ''
                        if answer.content == 1:
                            user.enfix += int(answer2.content) * query[int(answer.content)-1].price
                            abr = 'ENF'
                        elif answer.content == 2:
                            user.catcoin += int(answer2.content) * query[int(answer.content)-1].price
                            abr = 'CTC'
                        elif answer.content == 3:
                            user.ploy += int(answer2.content) * query[int(answer.content)-1].price
                            abr = 'PLY'
                        elif answer.content == 4:
                            user.vespine += int(answer2.content) * query[int(answer.content)-1].price
                            abr = 'VPE'
                        else:
                            user.xps += int(answer2.content) * query[int(answer.content)-1].price    
                            abr = 'XPS'
                        await answer.delete(delay=0)
                        await answer2.delete(delay=0)
                        await thismsg.delete(delay=0)                        
                        db.commit()
                        embed = Embed(title="Success!", description=f"You bought {answer2.content} {query[int(answer.content)-1].name} for {answer2.content * query[int(answer.content)-1].price} B$D.", color=0x5bdef5)
                        msg = await ctx.send(embed=embed)
                        await deleteMessage(msg)
                    else:
                        embed = Embed(title="Oops..", description=f"You only have {user.balance} which is insufficient to purchase {answer2} {abr}.", color=0x5bdef5)
                        msg = await ctx.send(embed=embed)
                        await deleteMessage(msg)
                else:
                    embed = Embed(title="Oops..", description=f"That is not a valid option.", color=0x5bdef5)
                    msg = await ctx.send(embed=embed)
                    await deleteMessage(msg)
            else:
                msg = embed = Embed(title="Oops..", description=f"That is not a valid option.", color=0x5bdef5)
                msg = await ctx.send(embed=embed)
                await deleteMessage(msg)