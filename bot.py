import discord          #first install it, type, pip install discord.py, in cmd prompt
from discord.ext import commands

client = commands.Bot(command_prefix="?")   #bot command prefix to be set here

# on ready event declaration
@client.event
async def on_ready():
    print("BOT IS READY!!!")


@client.command()
async def hi(ctx):
    await ctx.send(f"Hey, {ctx.author}, hi!")


@client.command()
async def say(ctx,*,text):
    await ctx.send(f"{ctx.author} just said: {text}")


client.run("ODIxNjUwMzMzMDk1NjkwMjgw.YFGzgA.H5JKzahV1eAhgV0zW58ummEVpv0")  #paste Bot Token Here
