import discord
from logic_bot import *


intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$flip'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$emodji'):
        await message.channel.send(gen_emodji())
    else:
        await message.channel.send(message.content)

client.run("MTUwMTc0OTc5NzUxNjc0Mjc0Ng.GxYJai.ivHUYdsR8oj5Z9k1fKVOvFdGEo3ah34gpTnlV8")