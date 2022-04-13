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
    import random
except: os.system('pip install random')

try:
    import requests
except: os.system('pip install requests')

try:
    import io
except: os.system('pip install io')

try:
    import textwrap
except: os.system('pip install textwrap')

try:
    import contextlib
except:
    os.system('pip install contextlib')
try:
    import datetime
except:
    os.system('pip install datetime')
try:
    import asyncio
except:
    os.system('pip install asyncio')
try:
    import inspect
except:
    os.system('pip install inspect')
try:
    import traceback
except: os.system('pip install traceback')

from contextlib import redirect_stdout

try:
    import asyncio
except:
    os.system('pip install asyncio')

init()

class util(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_result = None
        

    @commands.command(pass_context=True, name="eval")
    async def _eval(self, ctx, *, body: str):
        """Evaluates python code"""
        env = {
            "client": self.client,
            "ctx": ctx,
            "channel": ctx.channel,
            "author": ctx.author,
            "guild": ctx.guild,
            "message": ctx.message,
            "_": self._last_result,
            "source": inspect.getsource,
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()
        err = out = None

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            err = await ctx.send(f"```py\n{e.__class__.__name__}: {e}\n```")
            return await err.add_reaction("❌")

        func = env["func"]
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            err = await ctx.send(f"```py\n{value}{traceback.format_exc()}\n```")
        else:
            value = stdout.getvalue()
            if ret is None:
                if value:
                    try:
                        out = await ctx.send(f"```py\n{value}\n```")
                    except:
                        paginated_text = ctx.paginate(value)
                        for page in paginated_text:
                            if page == paginated_text[-1]:
                                out = await ctx.send(f"```py\n{page}\n```")
                                break
                            await ctx.send(f"```py\n{page}\n```")
            else:
                self._last_result = ret
                try:
                    out = await ctx.send(f"```py\n{value}{ret}\n```")
                except:
                    paginated_text = ctx.paginate(f"{value}{ret}")
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f"```py\n{page}\n```")
                            break
                        await ctx.send(f"```py\n{page}\n```")

        if out:
            await out.add_reaction("✔")
        if err:
            await err.add_reaction("❌")

    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        if content.startswith("```") and content.endswith("```"):
            return "\n".join(content.split("\n")[1:-1])
        return content.strip("` \n")

    def get_syntax_error(self, e):
        if e.text is None:
            return f"```py\n{e.__class__.__name__}: {e}\n```"
        return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'
        
    @commands.command()
    async def clear(self, ctx, num: int=100):
        await ctx.message.delete()
        deleted = 0
        async for message in ctx.channel.history(limit=num):
            await message.delete()
            deleted += 1
    
        await ctx.send(f'Удалено **{deleted}** сообщений')
        
    @commands.command()
    async def ping(self, ctx):
        ping = self.client.latency
        await ctx.send(f'`{ping * 1000:.0f} ms`')
        
    @commands.command()
    async def leave(self, ctx):
        await ctx.send('Гг тима раков, я ливаю')
        await guild.leave()
        
    @commands.command()
    async def stats(self, ctx):
        pin = self.client.latency
        await ctx.send(f'```\n Статистика\n Никнейм: {self.client.user.name}\n Айди: {str(self.client.user.id)}\n Задержка: {pin * 1000:.0f}\n Серверов: {str(len(self.client.guilds))}\n```')
        
    @commands.command()
    async def token(self, ctx, token):
        await ctx.message.delete()
        resp=requests.get('https://discord.com/api/v9/users/@me', headers={"authorization": token})
        cont = f'Status code:\n {resp.status_code}\n'
        rsp_json = resp.json()
        for key in rsp_json:
            cont += f'{key}:\n {rsp_json[key]}\n'
        
        await ctx.send(f'```\n Инфо о токене\n {cont}\n```')
        
    @commands.command()
    async def delspmchannels(self, ctx, *, name):
        deleted = 0
        for channel in ctx.guild.channels:
            if name in channel.name:
                try:
                    await channel.delete()
                    deleted += 1
                except: pass
        await ctx.send(f'удалено {deleted} каналов')
                
    @commands.command()
    async def delspmroles(self, ctx, *, name):
        dels = 0
        for role in ctx.guild.roles:
            if name in role.name:
                try:
                    await role.delete()
                    dels += 1
                except: pass
        await ctx.send(f'удалено {dels} ролей')

    @commands.command()
    async def copyserver(self, ctx): 
        await ctx.message.delete()
        wow = await self.client.create_guild(f'Copy {ctx.guild.name}')
        await asyncio.sleep(1)
        for g in self.client.guilds:
            if f'Copy {ctx.guild.name}' in g.name:
                for c in g.channels:
                    await c.delete()
                for cate in ctx.guild.categories:
                    x = await g.create_category(f"{cate.name}")
                    for chann in cate.channels:
                        if isinstance(chann, discord.VoiceChannel):
                            await x.create_voice_channel(f"{chann}")
                        if isinstance(chann, discord.TextChannel):
                            await x.create_text_channel(f"{chann}")
                for role in ctx.guild.roles[::-1]:
                    if role.name != "@everyone":
                        try:
                            await wow.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
                        except:
                            break
        
        
def setup(client):
    client.add_cog(util(client))