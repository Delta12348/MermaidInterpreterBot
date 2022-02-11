from time import time
from discord.ext import commands
import discord
import os
import time
bot = commands.Bot(command_prefix='&')

@bot.command()
async def mermaid(ctx,*, arg):
    with open("input.mmd", "w") as f: f.write(arg)
    os.system("cd ./node_modules/.bin & start mmdc -i ./../../input.mmd -o ./../../graph.png")
    time.sleep(4)
    await ctx.send(file=discord.File(r"C:\Users\manus\Desktop\GraphBot\graph.png"))

@bot.event
async def on_ready(): 
    print("bot is ready")

    
bot.run(os.environ["bot_key"])