import discord
from datetime import datetime, timezone
from discord import Embed
from discord.ext import commands
from discord.utils import get
from database import User, CryptoCurrencies, NFTCollections, NFTCollectionItems, NFTMint,CryptoCurrencyTransactions, NFTforCryptoTrade,CryptoforNFTTrade, session as db
from random import randint,random,choice

intents = discord.Intents().all()
#activity = discord.Activity(type=discord.ActivityType.watching, name="Bored Apes the Movie")
#activity = discord.Game(name="with >help for help")
activity = discord.Listening(name='to `>help`')

bot = commands.Bot(command_prefix='>',intents=intents, activity=activity, status=discord.Status.online, help_command=None)

@bot.event
async def on_ready():
    print('Bot Init Success')

@bot.event
async def on_command_error(ctx, error):
    msg = ''
    if isinstance(error, commands.CommandNotFound):
        msg = await ctx.send('Invalid command, Use >help to see a list of commands.')
    elif isinstance(error, commands.MissingRequiredArgument):
        msg = await ctx.send('Missing Required Argument')
    
async def deleteMessage(message):
    await message.delete(delay=5)
    
def getUser(userId):
    user = db.query(User).filter(User.memberId == userId).first()
    if user is not None:
        return user
    return False
