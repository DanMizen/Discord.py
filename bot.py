import discord 
import random
from discord.ext import commands


client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('working')
    
@client.event 
async def on_member_join(member):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server!')



@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

client.run('your token')

