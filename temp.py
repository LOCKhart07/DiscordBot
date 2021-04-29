import discord
from discord.ext import commands, tasks
from itertools import cycle
import random

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

client = commands.Bot(command_prefix = '.', intents = intents)



@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Watching Hentai'))
    print("Bot is Ulala")


status = cycle(['Watching Hentai','Wtaching more hentao','Not watching hentai'])

@tasks.loop(seconds=3)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_member_join(member):
    print(f'{member} has jhoined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has leftt a sever')

@client.command()
async def ulala(ctx):
    await ctx.send(f'Fuck Off and yi tuyi ping :{round(client.latency *1000)}ms')

@client.command(aliases=['badeball','8ball'])
async def bade_ball(ctx, *,question):
    responses =['Nai', 'Ha', 'Udya', 'Kal ana']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def nikal(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    print(ctx.author)
    await ctx.send(f'@{ctx.author} zun kadla')
    # await ctx.send(f'yaa {ctx.message.author.mention()} zun {amount} message kadle')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} was kicked.')

@client.command()
async def ban(ctx, member : discord.member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def unban(ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    memberName, memberDiscrim = member.split('#')
    for ban_entry in bannedUsers:
        user = ban_entry.user
        print(f'{user.name}\n{user.discriminator}')
        if (user.name, user.discriminator) == (memberName, memberDiscrim):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return




client.run('ODMwNzg1NjYxODk5NTA1NzA0.YHLvcQ.uLwn6xk_QBxa_24pWocjEOdsGt8')