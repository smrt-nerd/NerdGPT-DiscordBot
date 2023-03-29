import discord
import os

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ping'):
        await message.channel.send('pong!')

client.run('ODk1NTEzMDcyMTg0MjAxMjQ3.GhDIL-.7Kr4CoT_P6erZTisdg4ZYgTx_WPYru329zLzG0')