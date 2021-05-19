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

    
@client.command()
async def info(ctx, member: discord.Member):
    member_type = "HUMAN"

    if member.bot == True:
        member_type = "BOT"
    elif member.bot == False:
        member_type = " HUMAN"

    embed = discord.Embed(title=member.display_name, color=discord.Color.dark_teal())
    embed.add_field(name="ACCOUNT ID", value=member.id, inline=False)
    embed.add_field(name="ACCOUNT CREATED AT", value=member.created_at, inline=False)
    embed.add_field(name="JOINED SERVER AT", value=member.joined_at, inline=False)
    embed.add_field(name="STATUS", value=str(member.raw_status).title(), inline=False)
    embed.add_field(name="TYPE", value=member_type, inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested By {ctx.author}")

    await ctx.send(embed=embed)


client.run("ODIxNjUwMzMzMDk1NjkwMjgw.YFGzgA.H5JKzahV1eAhgV0zW58ummEVpv0")  #paste Bot Token Here
