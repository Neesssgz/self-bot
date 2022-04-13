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

init()

class status(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
    @commands.command()
    async def stream(self, ctx, *, arg):
        """Установить статус Стримит"""
        await self.client.change_presence(activity=discord.Streaming(name=arg, url='https://twitch.tv/404%27'))
        await ctx.send(f'**Успешно** :white_check_mark: \n Теперь статус изменён на **Стримит `{arg}`**')
            
    @commands.command()
    async def competing(self, ctx, *, arg):
        """Установить статус Соревнуется"""
        await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(name=arg, type=discord.ActivityType.competing))
        await ctx.send(f'**Успешно** :white_check_mark:\nСтатус изменён на **Соревнуется в `{arg}`**')
            
    @commands.command()
    async def play_status(self, ctx, *, arg):
        """Установить статус Играет"""
        await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(name=arg))
        await ctx.send(f'**Успешно** :white_check_mark:\nСтатус изменён на **Играет в `{arg}`**')
            
    @commands.command()
    async def listen(self, ctx, *, arg):
        """Установить статус Слушает"""
        await self.client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(name=arg, type=discord.ActivityType.listening))
        await ctx.send(f'**Успешно** :white_check_mark:\nСтатус изменён на **Слушает `{arg}`**')
            

def setup(client):
    client.add_cog(status(client))