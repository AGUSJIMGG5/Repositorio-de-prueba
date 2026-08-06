import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def ayuda(ctx):
    await ctx.send(f'Para usar este bot puedes usar los siguientes comandos:\n$hello\n$add <left> <right>\n$heh <count>\n$grafica')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:

        print(os.listdir('images'))
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def animals(ctx):
    img_name = random.choice(os.listdir('images2'))
    with open(f'images2/{img_name}', 'rb') as f:

        print(os.listdir('images2'))
        picture = discord.File(f)
    await ctx.send(file=picture)    

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)    

bot.run("MTUwMTc0OTc5NzUxNjc0Mjc0Ng.GxYJai.ivHUYdsR8oj5Z9k1fKVOvFdGEo3ah34gpTnlV8")