# Token read imports
from os import getenv
from dotenv import load_dotenv

#Main imports
from commands.register import *
from main import *
from commands.mine import *

load_dotenv()

if __name__ == '__main__':
    TOKEN = getenv('TOKEN')
    bot.run(TOKEN)