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


@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms')

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

client.run('ODg3NzY4OTIzMDc5MDc3OTM5.YUI9PQ.7JzLgHoPCi7U33Q5fO5FCbbvxLk')

