#LingLing bot by LingRusher and Spird

import discord 
from discord.ext import commands
from discord.ext.commands import Bot 
import asyncio 

bot = commands.Bot(command_prefix='!')

extensions = (
    'cogs.Commands'
)

@bot.event
async def on_ready():
    print ("Execute order 66")

#ping test
#@bot.command(pass_context = True)
#async def ping(ctx):
 #   await bot.say(":ping_pong: ping")

#ree
@bot.command(pass_context = True)
async def ree(ctx):
    await bot.say("ree? REEEEEEEEEEEEEEEEEEEEEEEEEEE")

#reebit
@bot.command(pass_context = True)
async def rebit(ctx):
    await bot.say("rebit? you mean REEbit MAHEEKA!?! REEBIT!")

@bot.command()
async def coinflip(self, ctx):

    choices = ('Heads!', 'Tails!')
    await ctx.send(choice(choices))

#froggy maheeka
#@bot.command(pass_context = True)
#async def frog(ctx):
 #   embed = discord.Embed(url = "https://cdn.discordapp.com/attachments/387766302711742464/446928003587506177/froggy.png")
  #  await bot.send_file(channel, "filepath.png", content="general", filename= "...")

#stream info. *WORK IN PROGRESS*
@bot.command(pass_context = True)
async def streams(ctx):
    embed = discord.Embed(title= "Mapledino Stream", description= "https://www.twitch.tv/thetitaneater", color= 0x00ff00)
    embed.add_field(name= "LingLing Stream", value= "https://www.twitch.tv/spyhawk9", inline= True)
    embed.add_field(name= "Dad's Stream", value= "https://www.twitch.tv/coxki", inline= False)
    embed.set_footer(text= "")
    await bot.say(embed=embed)

#when they joined the server
@bot.command(pass_context = True)
async def age(ctx, user: discord.Member):
    await bot.say("You joined on: {}".format(user.joined_at))

#info when they joined the server
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

#Kicked from the server
@bot.command(pass_context=True)
@commands.has_role("Bot Power")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Don't fuck with the bed, {}!".format(user.name))
    await bot.kick(user)

bot.run("NDQ2NzA0MTkxMjcyOTEwODU4.Dd85Pw.Sv_Cl5cBzh81AhcyMxUAR_xw3nw")
