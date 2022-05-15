# Token read imports
from os import getenv
from dotenv import load_dotenv

#Main imports
from main import *

from commands.about import *
from commands.exchange import *
from commands.help import *
from commands.inventory import *
from commands.leaderboard import *
from commands.mine import *
from commands.price import *
from commands.register import *
from commands.shop import *
from commands.trade import *

load_dotenv()

if __name__ == '__main__':
    TOKEN = getenv('TOKEN')
    bot.run(TOKEN)