#LingLing bot by LingRusher and Spird

import discord 
from discord.ext import commands
from discord.ext.commands import Bot 
import asyncio 

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print ("Execute order 66")

#ping test
@bot.command(pass_context = True)
async def ping(ctx):
    await bot.say(":ping_pong: ping")

#ree
@bot.command(pass_context = True)
async def ree(ctx):
    await bot.say("ree? REEEEEEEEEEEEEEEEEEEEEEEEEEE")

#reebit
@bot.command(pass_context = True)
async def rebit(ctx):
    await bot.say("rebit? you mean REEbit MAHEEKA!?! REEBIT!")

#stream info. *WORK IN PROGRESS*
@bot.command(pass_context = True)
async def streams(ctx):
    embed = discord.Embed(title= "Mapledino Stream", description= "https://www.twitch.tv/thetitaneater", color= 0x00ff00)
    embed.add_field(name= "LingLing Stream", value= "https://www.twitch.tv/spyhawk9", inline= True)
    embed.add_field(name= "Dad's Stream", value= "https://www.twitch.tv/coxki", inline= False)
    embed.set_footer(text= "")
    await bot.say(embed=embed)
    
bot.run("message me for ID")
