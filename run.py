# Token read imports
from os import getenv
from dotenv import load_dotenv

#Main imports
from main import *
from commands.mine import *
from commands.inventory import *
from commands.register import *

load_dotenv()

if __name__ == '__main__':
    TOKEN = getenv('TOKEN')
    bot.run(TOKEN)