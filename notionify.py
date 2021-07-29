#Import all the utilities needed
import discord
from discord.ext import commands
from datetime import date,time, datetime
import calendar
from notion.client import NotionClient
from notion.block import TodoBlock
from notion.block import TextBlock
from notion.block import ToggleBlock

#Define Timestamps to log added data
now = datetime.now()
currentDay = date.today()
currDate = currentDay.strftime("%B %d, %Y")
time_and_day = now.strftime("%H:%M:%S")

    
#Init bot tokens
bot_client = discord.Client()
bot_client = commands.Bot(command_prefix='n-')

n_token = open("notion.txt", "r").read()
d_token = open("TOKEN.txt", "r").read()
n_client = NotionClient(token_v2=n_token)

chosen_page = n_client.get_block("link_to_page")

#On startup command
@bot_client.event
async def bootup():
    print('Bot is currently online')
    await bot_client.change_presence(activity=discord.Game(name="n-addTodo"))



#adding a todo box into notion
# also dm's you with date of addition
@bot_client.command()
async def addTodo(ctx, *, todoInfo):
    new_todo = chosen_page.children.add_new(TodoBlock, title = todoInfo)
    new_todo.checked = False
    
    user = bot_client.get_user(ctx.author.id)
    await user.send("Added todo labeled as : " + todoInfo + " on " + currDate + " and " + time_and_day)

bot_client.run(d_token)
