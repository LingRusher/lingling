#LingLing bot by LingRusher and Spird

import discord 
from discord.ext import commands
from discord.ext.commands import Bot 
import asyncio 

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print ("Execute order 66")

@bot.command(pass_context = True)
async def ping(ctx):
    await bot.say(":ping_pong: ping")

@bot.command(pass_context = True)
async def ree(ctx):
    await bot.say("ree? REEEEEEEEEEEEEEEEEEEEEEEEEEE")

@bot.command(pass_context = True)
async def rebit(ctx):
    await bot.say("rebit? you mean REEbit MAHEEKA!?! REEBIT!")

bot.run("message me for bot id")
