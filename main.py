import discord
from discord.ext import commands
from os import remove
from time import sleep

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def photo(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename # 'kodland.jpg'
            if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png'):
                await attachment.save(f'./images/{file_name}')
                ##
                ##
                sleep(5)
                ##
                ##
                remove(f'./images/{file_name}')
            else:
                await ctx.send('Неправильный формат файлов! (мне нужны картинки)')
                return
    else:
        await ctx.send('Кажется, ты забыл прикрепить фотографии ;c')


bot.run("MTE0NDk2MDE5MzEzNDg2MjM1Ng.G0bYfD.WZpU7lapB_Ng0XDeiwyFMUTHx1c_Io152YW3ng")