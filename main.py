import discord
from discord.ext import commands
from discord.utils import get
from os import getenv
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents().all()
activity = discord.Activity(type=discord.ActivityType.watching, name="Anything.")

bot = commands.Bot(command_prefix='!',intents=intents, activity=activity, status=discord.Status.online)

@bot.event
async def on_ready():
    print('Bot is ready.')
    
if __name__ == '__main__':
    TOKEN = getenv('TOKEN')
    bot.run(TOKEN)