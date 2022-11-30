#CoperBot Project
import discord
import random
import math
from discord.ext import commands
from function import sin_1
from function import cos_1
from function import caesar_chiper

intents=discord.Intents.default()
intents.message_content=True
coper=commands.Bot(command_prefix='c.', intents=intents)
amount=3

#bot on
@coper.event
async def on_ready():
    print('Bot is ready.')

#c.8_ball or c.8ball (question)
@coper.command(aliases=['8_ball'])
async def _8ball(ctx, question='No question?'):
    if question == 'No question?':
       await ctx.send('I can predict your future, maybe...\ncommand: `c.8_ball (question)`')
    else:
       responses=['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes – definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', "Don't count on it.", 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
       await ctx.send(f'{random.choice(responses)}')

#c.hi
@coper.command()
async def hi(ctx):
    await ctx.send(f'Hello fellow {format(ctx.author.mention)}.')
    
#c.ping
@coper.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(coper.latency*1000)}ms')

#c.sneeze
@coper.command()
async def sneeze(ctx):
    await ctx.send('God Bless You...')

#c.choose
@coper.command() 
async def choose(ctx, num1: int, num2: int):
    await ctx.send(f'I choose {random.randint(num1, num2)}.')

#c.add
@coper.command()
async def add(ctx, num1: float, num2: float):
    addition=num1+num2
    embed=discord.Embed(title="Answer:", description=str(addition), color=0x00FFFF)
    embed.set_footer(text="Good Luck!")
    await ctx.send(embed=embed)

#c.substract
@coper.command()
async def substract(ctx, num1: float, num2: float):
    substraction=num1-num2
    embed=discord.Embed(title="Answer:", description=str(substraction), color=0x00FFFF)
    embed.set_footer(text="Good Luck!")
    await ctx.send(embed=embed)

#c.multiply
@coper.command()
async def multiply(ctx, num1: float, num2: float):
    multiplication=num1*num2
    embed=discord.Embed(title="Answer:", description=str(round(multiplication, amount)), color=0x00FFFF)
    embed.set_footer(text="Good Luck!")
    await ctx.send(embed=embed)

#c.divide
@coper.command()
async def divide(ctx, num1: float, num2: float):
    division=num1/num2
    embed=discord.Embed(title="Answer:", description=str(round(division, amount)), color=0x00FFFF)
    embed.set_footer(text="Good Luck!")
    await ctx.send(embed=embed)

#c.sine_degree
@coper.command()
async def sine_degree(ctx, degree: float):
    sine=sin_1(degree)
    embed=discord.Embed(title="Answer:", description=str(round(sine, amount)), color=0x00FFFF)
    embed.set_footer(text="Good Luck!")
    await ctx.send(embed=embed)
    
#c.sine_radian
@coper.command()
async def sine_radian(ctx, radian: float):
    sine=round(math.sin(radian), amount)
    if sine == 0:
        embed=discord.Embed(title="Answer:", description=0, color=0x00FFFF)
        embed.set_footer(text="Good Luck!")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Answer:", description=str(sine), color=0x00FFFF)
        embed.set_footer(text="Good Luck!")
        await ctx.send(embed=embed)
    
#c.cosine_degree
@coper.command()
async def cosine_degree(ctx, degree: float):
    cosine=cos_1(degree)
    embed=discord.Embed(title="Answer:", description=str(cosine), color=0x00FFFF)
    embed.set_footer(text="Good Luck!")
    await ctx.send(embed=embed)
    
#c.cosine_radian
@coper.command()
async def cosine_radian(ctx, radian: float):
    cosine=round(math.cos(radian), amount)
    if cosine == 0:
        embed=discord.Embed(title="Answer:", description=0, color=0x00FFFF)
        embed.set_footer(text="Good Luck!")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Answer:", description=str(cosine), color=0x00FFFF)
        embed.set_footer(text="Good Luck!")
        await ctx.send(embed=embed)
    
#c.circle_area
@coper.command()
async def circle_area(ctx, r: float):
    if r > 0:
        area=math.pi*(r**2)
        embed=discord.Embed(title="Answer:", description=str(round(area, amount)), color=0x00FFFF)
        embed.set_footer(text="Good Luck!")
        await ctx.send(embed=embed)
    else:
        await ctx.send('The radius must be bigger than 0.')

#c.trapezoid_area
@coper.command()
async def trapezoid_area(ctx, a: float, b:float, h:float):
    if a > 0 and b > 0 and h > 0:
        area=0.5*(a+b)*h
        embed=discord.Embed(title="Answer:", description=str(round(area, amount)), color=0x00FFFF)
        embed.set_footer(text="Good Luck!")
        await ctx.send(embed=embed)
    else:
        await ctx.send('The high and bases values must be bigger than 0.')

#c.triangle_area
@coper.command()
async def triangle_area(ctx, b: float, h:float):
    if h > 0 and b > 0:
        area=0.5*b*h
        embed=discord.Embed(title="Answer:", description=str(round(area, amount)), color=0x00FFFF)
        embed.set_footer(text="Good Luck!")
        await ctx.send(embed=embed)
    else:
        await ctx.send('The high and below values must be bigger than 0.')
        
#c.circle_circumference
@coper.command()
async def circle_circumference(ctx, r: float):
    if r > 0:
        circumference=2*math.pi*r
        embed=discord.Embed(title="Answer:", description=str(round(circumference, amount)), color=0x00FFFF)
        embed.set_footer(text="Good Luck!")
        await ctx.send(embed=embed)
    else:
        await ctx.send('The radius must be bigger than 0.')
        
#c.sphere_volume
@coper.command()
async def sphere_volume(ctx, r: float):
    if r > 0:
        volume=(4*math.pi*(r**3))/3
        embed=discord.Embed(title="Answer:", description=str(round(volume, amount)), color=0x00FFFF)
        embed.set_footer(text="Good Luck!")
        await ctx.send(embed=embed)
    else:
        await ctx.send('The radius must be bigger than 0.')
        
#c.caesar
@coper.command()
async def caesar(ctx, word: str, s: int):
    chiper=caesar_chiper(word, s)
    embed=discord.Embed(title="Result:", description=chiper, color=0x00FFFF)
    embed.set_footer(text="Good Luck!")
    await ctx.send(embed=embed)
  
#c.clean and c.clean (amount)
@coper.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, amount=1):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send('Clean succeed. :)')
    await ctx.channel.purge(limit=1)

@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You can't do that...")
        await ctx.channel.purge(limit=1)

#c.commands
@coper.command()
async def commands(ctx):
    commands=open("commands.txt", "r")
    embed=discord.Embed(title="Commands:", description=commands.read(), color=0x00FFFF)
    embed.set_footer(text="CoperBot(c.)")
    await ctx.send(embed=embed)
    commands.close()

#TOKEN
coper.run(' ')