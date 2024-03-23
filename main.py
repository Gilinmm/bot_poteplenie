
import discord
import json
from discord.ext import commands

file = open("config.json", "r")
config = json.load(file)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(config['prefix'], intents=intents)

@bot.event
async def on_ready():
    print('bot online')

@bot.command(name= 'world')
async def ping(ctx):
    await ctx.send(f'{ctx.massage.content} "ЗАГРЕЗНЕНИЕ ВОЗДУХА,ПРИРОДЫ,ВОДОЁМОВ"' )

    
@bot.command(name='healing')
async def ping(ctx: commands.context):
    await ctx.send(embed=discord.Embed(title=f"{ctx.massage.content}"), color='#00FF00')

bot.run(config['token'])