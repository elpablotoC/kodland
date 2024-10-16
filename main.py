import discord
from discord.ext import commands
import requests
import random
import os
from settings import settings

clasificacion_residuos = {
    "botellas plastico": "Las botellas de plastico van en la caneca verde o blanca.",
    "botellas vidrio": "Las botellas de vidrio van en la caneca verde",
    "bolsas de plastico": "Las bolsas de plastico van en la caneca azul o blanca ",
    "papel": "El papel va en la caneca azul ",
    "aluminio": "El aluminio va en la caneca azul o blanca",
    "curitas":"Las curitas van en la caneca negra",
    "papel higienico": "El papel higienico va en la caneca negra"




}

def clasificar_residuos(objeto):
    return clasificacion_residuos.get(objeto.lower(), "No tengo informacion sobre este objeto")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command('clasificar')
async def clasificar(ctx, *, objeto:str):
    respuesta = clasificar_residuos(objeto)
    await ctx.send(f"Clasificacion: {respuesta}")
    

bot.run(settings["TOKEN"])
