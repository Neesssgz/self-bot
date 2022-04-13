import os

try:
    import random
except: os.system('pip install random')

try:
    import discord
except: os.system('pip install discord')

from discord.ext import commands

try:
    from colorama import Fore, init
except: pass

init()

class other(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
    @commands.command()
    async def popit(self, ctx):
        """поп ит"""
        await ctx.send('''||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||
||🟨|||| 🟩 ||||🟦|||| 🟥 ||||🟨|||| 🟩 ||||🟦|||| 🟥 ||''')

    @commands.command()
    async def ball(self, ctx, *, arg):
        """Задать вопрос боту"""
        env = ["Спроси позже", "Уверен что да","можешь быть уверен в этом", "мне кажется нет", "уверен что нет"]
        rch = random.choice(env)
        await ctx.send(f'**{arg}** - {rch}')

    @commands.command()
    async def reactionall(self, ctx, count: int):
        await ctx.message.delete()
        messages = await ctx.channel.history(limit=count).flatten()
        reacted = 0
        for message in messages:
            await message.add_reaction("🤡")
            reacted += 1
        await ctx.send(f'поставлено **{reacted}** реакций')
  
            
def setup(client):
    client.add_cog(other(client))