import discord
from discord.ext import commands
import requests
import random
import os
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)






@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("meme"))
    with open(f'meme/{img_name}', 'rb') as f:
        
        picture = discord.File(f)
    
    await ctx.send(file=picture)


#APIS
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


bot.run("MTI4ODMxNTQxODE3MTE1MDQ1OQ.Gc1WVZ.zitiHLdqhT-Dyi26wVVFlWGY08V-EgRq4Cqs1I")