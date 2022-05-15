from main import *

@bot.command(aliases=['SHOP', 'sh', 'SH', 's', 'S'])
async def shop(ctx):
    user = getUser(ctx.message.author.id)
    if user is not False:
        embed=discord.Embed(title="Shop", description="Buy some NFTs! React with the number of the NFT you want tp buy.", color=0x5bdef5)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/974847550039416902/975237671909748736/91D132C4-287C-4723-ADC9-09BA81331692.jpeg1.png?width=567&height=567")
        embed.add_field(name="undefined", value="ddssd", inline=False)
        await ctx.send(embed=embed)
    else:
        msg = await ctx.send(f'You are not a part of the tycoon, {user.name}')
        await deleteMessage(msg)