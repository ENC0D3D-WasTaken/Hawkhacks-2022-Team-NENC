import discord
from datetime import datetime
from discord import Embed
from discord.ext import commands
from discord.utils import get
from database import User, CryptoCurrencies, NFTCollections, NFTCollectionItems, NFTMint,CryptoCurrencyTransactions, NFTforCryptoTrade,CryptoforNFTTrade, session as db
from datetime import datetime

intents = discord.Intents().all()
activity = discord.Activity(type=discord.ActivityType.watching, name="Among Us R34")

bot = commands.Bot(command_prefix='$',intents=intents, activity=activity, status=discord.Status.online)

@bot.event
async def on_ready():
    print('Bot Init Success')

@bot.event
async def on_command_error(ctx, error):
    msg = ''
    if isinstance(error, commands.CommandNotFound):
        msg = await ctx.send('Invalid Command')
    elif isinstance(error, commands.MissingRequiredArgument):
        msg = await ctx.send('Missing required argument')
    await deleteMessage(msg)
    
async def deleteMessage(message):
    await message.delete(delay=5)