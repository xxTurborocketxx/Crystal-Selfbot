class SELFBOT():
    __linecount__ = 1933
    __version__ = 3.0
     
import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging, time, nekos, httpx
import discord
import shutil
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
from os import system
import asyncio

from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
import pyPrivnote as pn
from gtts import gTTS
from random import randrange

ctypes.windll.kernel32.SetConsoleTitleW(f'[Crystal Selfbot v{SELFBOT.__version__}] | Loading...')

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')

giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')
nitro_sniper = config.get('nitro_sniper')
privnote_sniper = config.get('privnote_sniper')

stream_url = config.get('stream_url')
tts_language = config.get('tts_language')

bitly_key = config.get('bitly_key')
cat_key = config.get('cat_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')

width = os.get_terminal_size().columns
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:", 
    ":three:", 
    ":four:", 
    ":five:", 
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def startprint():
    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled" 
    
    print(f'''{Fore.RESET}

                                 {Fore.RED}██████╗██████╗ ██╗   ██╗███████╗████████╗ █████╗ ██╗     
                                {Fore.RED}██╔════╝██╔══██╗╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔══██╗██║     
                                {Fore.RED}██║     ██████╔╝ ╚████╔╝ ███████╗   ██║   ███████║██║     
                                {Fore.RED}██║     ██╔══██╗  ╚██╔╝  ╚════██║   ██║   ██╔══██║██║     
                                {Fore.RED}╚██████╗██║  ██║   ██║   ███████║   ██║   ██║  ██║███████╗
                                 {Fore.RED}╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝                                                                                                                                       
                                                            
                        
                       {Fore.CYAN}Crystal Selfbot {SELFBOT.__version__} | {Fore.GREEN}Logged in as: {Crystal.user.name}#{Crystal.user.discriminator} {Fore.CYAN}| ID: {Fore.GREEN}{Crystal.user.id}   
                       {Fore.CYAN}Privnote Sniper | {Fore.GREEN}{privnote}
                       {Fore.CYAN}Nitro Sniper | {Fore.GREEN}{nitro}
                       {Fore.CYAN}Giveaway Sniper | {Fore.GREEN}{giveaway}
                       {Fore.CYAN}SlotBot Sniper | {Fore.GREEN}{slotbot}
                       {Fore.CYAN}Prefix: {Fore.GREEN}{prefix}
                       {Fore.CYAN}Creator: {Fore.GREEN}xxTurborocketxx#7955
    '''+Fore.RESET)

def Clear():
    os.system('cls')
Clear()

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            Crystal.run(token, bot=False, reconnect=True)
            os.system(f'title (Crystal Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed"+Fore.RESET)
            os.system('pause >NUL')

def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW} Incorrect Password or gmail, make sure you've enabled less-secure apps access"+Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass

def GenAddress(addy: str):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    four_char = ''.join(random.choice(letters) for _ in range(4))
    should_abbreviate = random.randint(0,1)
    if should_abbreviate == 0:
        if "street" in addy.lower():
            addy = addy.replace("Street", "St.")
            addy = addy.replace("street", "St.")
        elif "st." in addy.lower():
            addy = addy.replace("st.", "Street")
            addy = addy.replace("St.", "Street")
        if "court" in addy.lower():
            addy = addy.replace("court", "Ct.")
            addy = addy.replace("Court", "Ct.")
        elif "ct." in addy.lower():
            addy = addy.replace("ct.", "Court")
            addy = addy.replace("Ct.", "Court")
        if "rd." in addy.lower():
            addy = addy.replace("rd.", "Road")
            addy = addy.replace("Rd.", "Road")
        elif "road" in addy.lower():
            addy = addy.replace("road", "Rd.")
            addy = addy.replace("Road", "Rd.")
        if "dr." in addy.lower():
            addy = addy.replace("dr.", "Drive")
            addy = addy.replace("Dr.", "Drive")
        elif "drive" in addy.lower():
            addy = addy.replace("drive", "Dr.")
            addy = addy.replace("Drive", "Dr.")
        if "ln." in addy.lower():
            addy = addy.replace("ln.", "Lane")
            addy = addy.replace("Ln.", "Lane")
        elif "lane" in addy.lower():
            addy = addy.replace("lane", "Ln.")
            addy = addy.replace("lane", "Ln.")
    random_number = random.randint(1,99)
    extra_list = ["Apartment", "Unit", "Room"]
    random_extra = random.choice(extra_list)
    return four_char + " " + addy + " " + random_extra + " " + str(random_number)

def BotTokens():
    with open('Data/Tokens/bot-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

def UserTokens():
    with open('Data/Tokens/user-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

def _masslogin(choice):
    if choice == 'user':
        for token in UserTokens():
            loop.run_until_complete(Login().start(token, bot=False))
    elif choice == 'bot':
        for token in BotTokens():
            loop.run_until_complete(Login().start(token, bot=True))
    else:
        return        

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f

def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url)+'\n')

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

colorama.init()
Crystal = discord.Client()
Crystal = commands.Bot(
    description='Crystal Selfbot',
    command_prefix=prefix,
    self_bot=True
)

@tasks.loop(seconds=3)
async def btc_status():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value = r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream = discord.Streaming(
        name="Current BTC price: "+value+"$ USD", 
        url="https://www.twitch.tv/monstercat", 
    )
    await Crystal.change_presence(activity=btc_stream)

@Crystal.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Couldnt send a empty message"+Fore.RESET)               
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{error_str}"+Fore.RESET)

@Crystal.event
async def on_message_edit(before, after):
    await Crystal.process_commands(after)

@Crystal.event
async def on_message(message):

    def GiveawayData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
    +Fore.RESET)

    def SlotBotData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"   
    +Fore.RESET)  

    def NitroData(elapsed, code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
        f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
        f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
    +Fore.RESET)

    def PrivnoteData(code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]" 
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - CONTENT: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]"
    +Fore.RESET)        

    time = datetime.datetime.now().strftime("%H:%M %p")  
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')
                
            headers = {'Authorization': token}
    
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', 
                headers=headers,
            ).text
        
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Success]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]"+Fore.RESET)
                NitroData(elapsed, code)
        else:
            return
            
    if 'Someone just dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]"+Fore.RESET)
                    SlotBotData()                     
                print(""
                f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]"+Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:    
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]"+Fore.RESET)
                    GiveawayData()            
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Sniped]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Crystal.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:    
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Won]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/'+code
            try:
                note_text = pn.read_note(link)
            except Exception as e:
                print(e)    
            with open(f'Privnote/{code}.txt', 'a+') as f:
                print(""
                f"\n{Fore.CYAN}[{time} - Privnote Sniped]"+Fore.RESET)
                PrivnoteData(code)
                f.write(note_text)
        else:
            return
    await Crystal.process_commands(message)

@Crystal.event
async def on_connect():
    Clear()

    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled"    
    
    startprint()
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Crystal Selfbot v{SELFBOT.__version__}] | Logged in as {Crystal.user.name}')

@Crystal.command(name="turbo")
async def turbo(ctx):
    await ctx.message.delete()
    await ctx.channel.send("Turbo is the coolest")

@Crystal.command(name="astrania")
async def astrania(ctx):
    await ctx.message.delete()
    await ctx.channel.send("https://discord.gg/QXmGDjTe9P")

@Crystal.command(name="killme")
async def killme(ctx):
    await ctx.message.delete()
    text = await ctx.channel.send("you are now dead")
    time.sleep(20)
    await text.delete()

@Crystal.command(name="yeet")
async def yeet(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Yeet", description="To discard an item at a high velocity", color=0x9F00FB)
    embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
    embed.set_footer(text="Crystal")
    text = await ctx.send(embed=embed)
    time.sleep(20)
    await text.delete()

@Crystal.command(name="why")
async def why(ctx):
    await ctx.message.delete()
    text = await ctx.channel.send("https://tenor.com/view/confused-white-persian-guardian-why-gif-11908780")
    time.sleep(20)
    await text.delete()

@Crystal.command(name="nom")
async def nom(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Nom", description="The sound made when eating something (or someone). Can be referred to as nomming as a verb, and is often pronounced in the sentence om nom nom.", color=0x9F00FB)
    embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
    embed.set_footer(text="Crystal")
    text = await ctx.send(embed=embed)
    time.sleep(20)
    await text.delete()

@Crystal.command(name="cringe")
async def cringe(ctx):
    await ctx.message.delete()
    await ctx.channel.send("https://cdn.discordapp.com/attachments/788185828559290418/821751009084309504/uamee_-_COMRADE_YOU_JUST_POSTED_CRINGE_HARDBASS.mp4")

@Crystal.command(name="about")
async def about(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Crystal Selfbot", description="Crystal SelfBot is an open source, easy to use, customizable selfbot. It was made by xxTurborocketxx#7955 and can be downloaded here https://github.com/xxTurborocketxx/Crystal-Selfbot", color=0x9F00FB)
    embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
    embed.set_footer(text="Crystal")
    text = await ctx.send(embed=embed)

@Crystal.command(name="frog")
async def frog(ctx):
    await ctx.message.delete()
    text = await ctx.channel.send("https://giphy.com/gifs/frog-mXnu6HiBvOckU")
    time.sleep(20)
    await text.delete()

@Crystal.command(name="skyline")
async def skyline(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Nissan Skyline", description="The Nissan Skyline (Japanese: 日産・スカイライン, Nissan Sukairain) is a brand of automobile originally produced by the Prince Motor Company starting in 1957, and then by Nissan after the two companies merged in 1967. After the merger, the Skyline and its larger counterpart, the Nissan Gloria, were sold in Japan at dealership sales channels called Nissan Prince Shop.", color=0x9F00FB)
    embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
    embed.set_footer(text="Crystal")
    text = await ctx.send(embed=embed)
    time.sleep(20)
    await text.delete()


@Crystal.command(name="s2000")
async def s2000(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Honda S2000",description="The Honda S2000 is an open top sports car that was manufactured by Japanese automobile manufacturer Honda, from 1999 to 2009. First shown as a concept car at the Tokyo Motor Show in 1995, the production version was launched on April 15, 1999 to celebrate the company's 50th anniversary. The S2000 is named for its engine displacement of two liters, carrying on in the tradition of the S500, S600, and S800 roadsters of the 1960s.",color=0x9F00FB)
    embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
    embed.set_footer(text="Crystal")
    text = await ctx.send(embed=embed)
    time.sleep(20)
    await text.delete()


@Crystal.command(name="chaser")
async def chaser(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Toyota Chaser",description="The Toyota Chaser is a mid-size car produced by Toyota in Japan. Most Chasers are four-door sedans and hardtop sedans; a two-door hardtop coupé was available on the first generation only. It was introduced on the 1976 Toyota Corona Mark II platform, and was sold new by Toyota at Toyota Vista Store dealerships only in Japan, together with the Toyota Cresta.",color=0x9F00FB)
    embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
    embed.set_footer(text="Crystal")
    text = await ctx.send(embed=embed)
    time.sleep(20)
    await text.delete()


@Crystal.command(name="jdm")
async def jdm(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="JDM",description="Japanese domestic market refers to Japan's home market for vehicles. For the importer, these terms refer to vehicles and parts designed to conform to Japanese regulations and to suit Japanese buyers. The term is abbreviated JDM.",color=0x9F00FB)
    embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
    embed.set_footer(text="Crystal")
    text = await ctx.send(embed=embed)
    time.sleep(20)
    await text.delete()

@Crystal.command(name="whoasked")
async def whoasked(ctx):
    await ctx.message.delete()
    await ctx.channel.send("https://cdn.discordapp.com/attachments/788185828559290418/834755269577277490/vsu9brkpb8t41.png")

@Crystal.command()
async def virus(ctx, user: discord.Member = None, *, virus: str = "trojan"):
        user = user or ctx.author
        list = (
            f"``[▓▓▓                    ] / {virus}-virus.exe Packing files.``",
            f"``[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..``",
            f"``Successfully downloaded {virus}-virus.exe``",
            "``Injecting virus.   |``",
            "``Injecting virus..  /``",
            "``Injecting virus... -``",
            f"``Successfully Injected {virus}-virus.exe into {user.name}``",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)

@Crystal.command(name="overload")
async def overload(ctx):
        list = (
            "`LOAD !! WARNING !! SYSTEM OVER`",
            "`OAD !! WARNING !! SYSTEM OVERL`",
            "`AD !! WARNING !! SYSTEM OVERLO`",
            "`D !! WARNING !! SYSTEM OVERLOA`",
            "`! WARNING !! SYSTEM OVERLOAD !`",
            "`WARNING !! SYSTEM OVERLOAD !!`",
            "`ARNING !! SYSTEM OVERLOAD !! W`",
            "`RNING !! SYSTEM OVERLOAD !! WA`",
            "`NING !! SYSTEM OVERLOAD !! WAR`",
            "`ING !! SYSTEM OVERLOAD !! WARN`",
            "`NG !! SYSTEM OVERLOAD !! WARNI`",
            "`G !! SYSTEM OVERLOAD !! WARNIN`",
            "`!! SYSTEM OVERLOAD !! WARNING`",
            "`! SYSTEM OVERLOAD !! WARNING !`",
            "`SYSTEM OVERLOAD !! WARNING !!`",
            "`IMMINENT SHUT-DOWN IN 0.5 SEC!`",
            "`WARNING !! SYSTEM OVERLOAD !!`",
            "`IMMINENT SHUT-DOWN IN 0.2 SEC!`",
            "`SYSTEM OVERLOAD !! WARNING !!`",
            "`IMMINENT SHUT-DOWN IN 0.01 SEC!`",
            "`SHUT-DOWN EXIT ERROR ¯\\(｡･益･)/¯`",
            "`CTRL + R FOR MANUAL OVERRIDE..`",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)

@Crystal.command()
async def typing(
        ctx, duration: int, channel: discord.TextChannel = None
    ):
        channel = channel or ctx.channel
        async with channel.typing():
            await asyncio.sleep(duration)

@Crystal.command()
async def hexcode(ctx, *, role: discord.Role):
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")

@Crystal.command()
async def cow(ctx):
        cnt = """```
 __________
 |        |
 |  Moo   |
 |        |
 ¯¯¯¯¯¯¯¯¯¯
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
```"""

        em = discord.Embed(color=random.randint(0, 0xFFFFFF))
        em.description = cnt
        text = await ctx.send(embed=em)
        await ctx.message.delete()
        time.sleep(20)
        await text.delete()

@Crystal.command()
async def nick(ctx, user: discord.Member, *, nickname: str = None):
        """change a user's nickname
        Parameter
        • user - the name or id of the user
        • nickname - the nickname to change to
        """
        prevnick = user.nick or user.name
        await user.edit(nick=nickname)
        newnick = nickname or user.name
        text = await ctx.send(f"Changed {prevnick}'s nickname to {newnick}")
        await ctx.message.delete()
        time.sleep(5)
        await text.delete()

@Crystal.command(name="fvd")
async def fvd(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="FVD", description="Stap in makker we breken het partij kartel", color=0x9F00FB)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/813786651310555207/820072051389497374/tenor.gif")
    embed.set_footer(text="Crystal")
    text = await ctx.send(embed=embed)
    time.sleep(20)
    await text.delete()

@Crystal.command(name="kkautist")
async def kkautist(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Ik zeg", description="je bent een kanker autist", color=0x9F00FB)
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/724718906933248052.gif?v=1")
    embed.set_footer(text="Crystal")
    text = await ctx.send(embed=embed)
    time.sleep(20)
    await text.delete()

@Crystal.command(name="sloppy")
async def sloppy(ctx, user):
    await ctx.message.delete()
    user = user
    embed = discord.Embed(title="I announce", description=(user +" will give you sloppy"), color=0x9F00FB)
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/724718906933248052.gif?v=1")
    embed.set_footer(text="Crystal")
    text = await ctx.send(embed=embed)
    time.sleep(20)
    await text.delete()

@Crystal.command()
async def pussy(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    text=await ctx.send(embed=em)
    time.sleep(20)
    await text.delete()

@Crystal.command()
async def neko(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/neko")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    text=await ctx.send(embed=em)
    time.sleep(20)
    await text.delete()

@Crystal.command()
async def notfunny(ctx):
        
        message1 = '''Not funny, didnt laugh. Your joke is so bad I would have preferred the joke went over my head and you gave up re-telling me the joke. To be honest this is a horrid attempt at trying to get a laugh out of me. Not a chuckle, not a hehe, not even a subtle burst of air out of my esophagus. Science says before you laugh your brain preps your face muscles but I didnt even feel the slightest twitch. 0/10 this joke is so bad I cannot believe anyone legally allowed you to be creative at all. The amount of brain power you must have put into that joke has the potential to power every house on Earth. Get a personality and learn how to make jokes, read a book. Im not saying this to be funny I genuinely mean it on how this is just bottom barrel embarrassment at comedy. Youve single handedly killed humor and every comedic act on the planet. Im so disappointed that society has failed as a whole in being able to teach you how to be funny.'''
        message2 = '''Honestly if I put in all my power and time to try and make your joke funny it would require Einstein himself to build a device to strap me into so I can be connected to the energy of a billion stars to do it, and even then all that joke would get from people is a subtle scuff. Youre lucky I still have the slightest of empathy for you after telling that joke otherwise I would have committed every war crime in the book just to prevent you from attempting any humor ever again. We should put that joke in text books so future generations can be wary of becoming such an absolute comedic failure. Im disappointed, hurt, and outright offended that my precious time has been wasted in my brain understanding that joke. In the time that took I was planning on helping kids who have been orphaned, but because of that youve wasted my time explaining the obscene integrity of your terrible attempt at comedy. Now those kids are suffering without meals and theres nobody to blame but you. I hope youre happy with what you have done and I truly hope you can move on and learn from this piss poor attempt.'''
        message3 = '''What you just actually posted basically has absolutely 0 sense of cohesion or comedy in a subtle way. It''s for all intents and purposes such a horrid attempt at communication I specifically am surprised you particularly are even able to basically exist in society, or so they for all intents and purposes thought. If it literally was a joke, it may really have been the for all intents and purposes worse joke i ever heard in my life, since it lacks any qualities actually your really normal joke would particularly have in a subtle way. If it particularly was supposed to for all intents and purposes be a particularly normal sentence, then it definitely fails as that too, as what you just really said literally makes absolutely no sense, which definitely shows that it's pretty such a horrid attempt at communication I actually am surprised you basically are even able to actually exist in society in a subtle way. It's so dumb, a cave man would really be able to really speak definitely more cleverly and for all intents and purposes more nuanced than you in a kind of big way. I for the most part am so ashamed of having to specifically see this, it's just sad, demonstrating how if it for all intents and purposes was supposed to generally be a really normal sentence, then it actually fails as that too, as what you just generally said for the most part makes absolutely no sense, which really shows that it's for all intents and purposes such a horrid attempt at communication I literally am surprised you mostly are even able to particularly exist in society in a for all intents and purposes big way.'''
        message4 = '''Your lack of brain cells doesn't definitely help you either, but if you generally wanna really try and mostly talk with me you mostly gotta kind of speak normally you idiotic piece of shit, particularly further showing how if it basically was a joke, it may particularly have been the much worse joke i ever heard in my life, since it lacks any qualities actually your basically normal joke would basically have, very contrary to popular belief. I honestly essentially think they should particularly put you in the mental hospital, but not for improving particularly your brain, but rather mostly keep you out of society so no one definitely has to kind of deal with particularly your crap, demonstrating how i kind of am so ashamed of having to actually see this, it's just sad, demonstrating how if it literally was supposed to specifically be a definitely normal sentence, then it specifically fails as that too, as what you just really said mostly makes absolutely no sense, which kind of shows that it's really such a horrid attempt at communication I kind of am surprised you particularly are even able to for the most part exist in society, for all intents and purposes contrary to popular belief. Your stupidity will kind of be essentially remembered forever as a very prime example of why humanity kind of is on a downwards spiral, generally further showing how it's generally such a horrid attempt at communication I for all intents and purposes am surprised you essentially are even able to literally exist in society, sort of contrary to popular belief'''
        await ctx.send(message1)
        await ctx.send(message2)
        await ctx.send(message3)
        await ctx.send(message4)

@Crystal.command()
async def beescript(ctx):
        await ctx.message.delete()
        await ctx.send("According to all known laws of aviation, there is no way a bee should be able to fly.")
        await ctx.send("Its wings are too small to get its fat little body off the ground.")
        await ctx.send("The bee, of course, flies anyway because bees don't care what humans think is impossible.")
        await ctx.send("Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little.")
        await ctx.send("Barry! Breakfast is ready!")
        await ctx.send("Coming!")
        await ctx.send("Hang on a second... Hello?")
        await ctx.send("- Barry?")
        await ctx.send("- Adam?")
        await ctx.send("- Can you believe this is happening?")
        await ctx.send("- I can't. I'll pick you up.")
        await ctx.send("Looking sharp.")
        await ctx.send("Use the stairs. Your father paid good money for those.")
        await ctx.send("Sorry, I'm excited.")
        await ctx.send("Here's the graduate. We're very proud of you, son.")
        await ctx.send("A perfect report card, all B's!")
        await ctx.send("Very proud.")
        await ctx.send("Ma! I got a think going here.")
        await ctx.send("- You got lint on your fuzz.")
        await ctx.send("- Ow! That's me!")
        await ctx.send("- Wave to us! We'll be in row 118,000!")
        await ctx.send("- Bye!")
        await ctx.send("Barry, I told you,")
        await ctx.send("stop flying in the house!")
        await ctx.send("- Hey, Adam.")
        await ctx.send("- Hey, Barry.")
        await ctx.send("- Is that fuzz gel?")
        await ctx.send("- A little. Special day, graduation.") 
        await ctx.send("Never thought I'd make it.")
        await ctx.send("Three days grade school,")
        await ctx.send("three days high school.")
        await ctx.send("Those were awkward.")
        await ctx.send("Three days college. I'm glad I took")
        await ctx.send("a day and hitchhiked around the hive.")
        await ctx.send("You did come back different.")
        await ctx.send("- Hi, Barry.")
        await ctx.send("- Artie, growing a mustache? Looks good.")
        await ctx.send("- Hear about Frankie?")
        await ctx.send("- Yeah.")
        await ctx.send("- You going to the funeral?")
        await ctx.send("- No, I'm not going.")
        await ctx.send("Everybody knows,")
        await ctx.send("sting someone, you die.")
        await ctx.send("Don't waste it on a squirrel.")
        await ctx.send("Such a hothead.")
        await ctx.send("I guess he could have")
        await ctx.send("just gotten out of the way.")
        await ctx.send("I love this incorporating")
        await ctx.send("an amusement park into our day.")
        await ctx.send("That's why we don't need vacations.")
        await ctx.send("Boy, quite a bit of pomp...")
        await ctx.send("under the circumstances.")
        await ctx.send("- Well, Adam, today we are men.")
        await ctx.send("- We are!")
        await ctx.send("- Bee-men.")
        await ctx.send("- Amen!")
        await ctx.send("Hallelujah!")
        await ctx.send("Students, faculty, distinguished bees,")
        await ctx.send("please welcome Dean Buzzwell.")
        await ctx.send("Welcome, New Hive Oity")
        await ctx.send("graduating class of...")
        await ctx.send("...9:15.")
        await ctx.send("That concludes our ceremonies.")
        await ctx.send("And begins your career")
        await ctx.send("at Honex Industries!")
        await ctx.send("Will we pick ourjob today?")
        await ctx.send("I heard it's just orientation.")
        await ctx.send("Heads up! Here we go.")
        await ctx.send("Keep your hands and antennas")
        await ctx.send("inside the tram at all times.")
        await ctx.send("- Wonder what it'll be like?")
        await ctx.send("- A little scary.")
        await ctx.send("Welcome to Honex,")
        await ctx.send("a division of Honesco")
        await ctx.send("and a part of the Hexagon Group.")
        await ctx.send("This is it!")
        await ctx.send("Wow.")
        await ctx.send("Wow.")
        await ctx.send("We know that you, as a bee,")
        await ctx.send("have worked your whole life")
        await ctx.send("to get to the point where you")
        await ctx.send("can work for your whole life.")
        await ctx.send("Honey begins when our valiant Pollen")
        await ctx.send("Jocks bring the nectar to the hive.")
        await ctx.send("Our top-secret formula")
        await ctx.send("is automatically color-corrected,")
        await ctx.send("scent-adjusted and bubble-contoured")
        await ctx.send("into this soothing sweet syrup")
        await ctx.send("with its distinctive")
        await ctx.send("golden glow you know as...")
        await ctx.send("Honey!")
        await ctx.send("- That girl was hot.")
        await ctx.send("- She's my cousin!")
        await ctx.send("- She is?")
        await ctx.send("- Yes, we're all cousins.")
        await ctx.send("- Right. You're right.")
        await ctx.send("- At Honex, we constantly strive")
        await ctx.send("to improve every aspect")
        await ctx.send("of bee existence.")
        await ctx.send("These bees are stress-testing")
        await ctx.send("a new helmet technology.")
        await ctx.send("- What do you think he makes?")
        await ctx.send("- Not enough.")
        await ctx.send("Here we have our latest advancement,")
        await ctx.send("the Krelman.")
        await ctx.send("- What does that do?")
        await ctx.send("- Oatches that little strand of honey")
        await ctx.send("that hangs after you pour it.")
        await ctx.send("Saves us millions.")
        await ctx.send("Oan anyone work on the Krelman?")
        await ctx.send("Of course. Most bee jobs are")
        await ctx.send("small ones. But bees know")
        await ctx.send("that every small job,")
        await ctx.send("if it's done well, means a lot.")
        await ctx.send("But choose carefully")
        await ctx.send("because you'll stay in the job")
        await ctx.send("you pick for the rest of your life.")
        await ctx.send("The same job the rest of your life?")
        await ctx.send("I didn't know that.")
        await ctx.send("What's the difference?")
        await ctx.send("You'll be happy to know that bees,")
        await ctx.send("as a species, haven't had one day off")
        await ctx.send("in 27 million years.")
        await ctx.send("So you'll just work us to death?")
        await ctx.send("We'll sure try.")
        await ctx.send("Wow! That blew my mind!")
        await ctx.send("What's the difference?")
        await ctx.send("How can you say that?")
        await ctx.send("One job forever?")
        await ctx.send("That's an insane choice to have to make.")
        await ctx.send("I'm relieved. Now we only have")
        await ctx.send("to make one decision in life.")
        await ctx.send("But, Adam, how could they")
        await ctx.send("never have told us that?")
        await ctx.send("Why would you question anything?")
        await ctx.send("We're bees.")
        await ctx.send("We're the most perfectly")
        await ctx.send("functioning society on Earth.")
        await ctx.send("You ever think maybe things")
        await ctx.send("work a little too well here?")
        await ctx.send("Like what? Give me one example.")
        await ctx.send("I don't know. But you know")
        await ctx.send("what I'm talking about.")
        await ctx.send("Please clear the gate.")
        await ctx.send("Royal Nectar Force on approach.")
        await ctx.send("Wait a second. Oheck it out.")
        await ctx.send("- Hey, those are Pollen Jocks!")
        await ctx.send("- Wow.")
        await ctx.send("I've never seen them this close.")
        await ctx.send("They know what it's like")
        await ctx.send("outside the hive.")
        await ctx.send("Yeah, but some don't come back.")
        await ctx.send("- Hey, Jocks!")
        await ctx.send("- Hi, Jocks!")
        await ctx.send("You guys did great!")
        await ctx.send("You're monsters!")
        await ctx.send("You're sky freaks! I love it! I love it!")
        await ctx.send("- I wonder where they were.")
        await ctx.send("- I don't know.")
        await ctx.send("Their day's not planned.")
        await ctx.send("Outside the hive, flying who knows")
        await ctx.send("where, doing who knows what.")
        await ctx.send("You can'tjust decide to be a Pollen")
        await ctx.send("Jock. You have to be bred for that.")
        await ctx.send("Right.")
        await ctx.send("Look. That's more pollen")
        await ctx.send("than you and I will see in a lifetime.")
        await ctx.send("It's just a status symbol.")
        await ctx.send("Bees make too much of it.")
        await ctx.send("Perhaps. Unless you're wearing it")
        await ctx.send("and the ladies see you wearing it.")
        await ctx.send("Those ladies?")
        await ctx.send("Aren't they our cousins too?")
        await ctx.send("Distant. Distant.")
        await ctx.send("Look at these two.")
        await ctx.send("- Oouple of Hive Harrys.")
        await ctx.send("- Let's have fun with them.")
        await ctx.send("It must be dangerous")
        await ctx.send("being a Pollen Jock.")
        await ctx.send("Yeah. Once a bear pinned me")
        await ctx.send("against a mushroom!")
        await ctx.send("He had a paw on my throat,")
        await ctx.send("and with the other, he was slapping me!")
        await ctx.send("- Oh, my!")
        await ctx.send("- I never thought I'd knock him out.")
        await ctx.send("What were you doing during this?")
        await ctx.send("Trying to alert the authorities.")
        await ctx.send("I can autograph that.")
        await ctx.send("A little gusty out there today,")
        await ctx.send("wasn't it, comrades?")
        await ctx.send("Yeah. Gusty.")
        await ctx.send("We're hitting a sunflower patch")
        await ctx.send("six miles from here tomorrow.")
        await ctx.send("- Six miles, huh?")
        await ctx.send("- Barry!")
        await ctx.send("A puddle jump for us,")
        await ctx.send("but maybe you're not up for it.")
        await ctx.send("- Maybe I am.")
        await ctx.send("- You are not!")
        await ctx.send("We're going 9 at J-Gate.")
        await ctx.send("What do you think, buzzy-boy?")
        await ctx.send("Are you bee enough?")
        await ctx.send("I might be. It all depends")
        await ctx.send("on what 9 means.")
        await ctx.send("Hey, Honex!")
        await ctx.send("Dad, you surprised me.")
        await ctx.send("You decide what you're interested in?")
        await ctx.send("- Well, there's a lot of choices.")
        await ctx.send("- But you only get one.")
        await ctx.send("Do you ever get bored")
        await ctx.send("doing the same job every day?")
        await ctx.send("Son, let me tell you about stirring.")
        await ctx.send("You grab that stick, and you just")
        await ctx.send("move it around, and you stir it around.")
        await ctx.send("You get yourself into a rhythm.")
        await ctx.send("It's a beautiful thing.")
        await ctx.send("You know, Dad,")
        await ctx.send("the more I think about it,")
        await ctx.send("maybe the honey field")
        await ctx.send("just isn't right for me.")
        await ctx.send("You were thinking of what,")
        await ctx.send("making balloon animals?")
        await ctx.send("That's a bad job")
        await ctx.send("for a guy with a stinger.")
        await ctx.send("Janet, your son's not sure")
        await ctx.send("he wants to go into honey!")
        await ctx.send("- Barry, you are so funny sometimes.")
        await ctx.send("- I'm not trying to be funny.")
        await ctx.send("You're not funny! You're going")
        await ctx.send("into honey. Our son, the stirrer!")
        await ctx.send("- You're gonna be a stirrer?")
        await ctx.send("- No one's listening to me!")
        await ctx.send("Wait till you see the sticks I have.")
        await ctx.send("I could say anything right now.")
        await ctx.send("I'm gonna get an ant tattoo!")
        await ctx.send("Let's open some honey and celebrate!")
        await ctx.send("Maybe I'll pierce my thorax.")
        await ctx.send("Shave my antennae.")
        await ctx.send("Shack up with a grasshopper. Get")
        await ctx.send("a gold tooth and call everybody 'dawg!'")
        await ctx.send("I'm so proud.")
        await ctx.send("- We're starting work today!")
        await ctx.send("- Today's the day.")
        await ctx.send("Oome on! All the good jobs")
        await ctx.send("will be gone.")
        await ctx.send("Yeah, right.")
        await ctx.send("Pollen counting, stunt bee, pouring,")
        await ctx.send("stirrer, front desk, hair removal...")
        await ctx.send("- Is it still available?")
        await ctx.send("- Hang on. Two left!")
        await ctx.send("One of them's yours! Oongratulations!")
        await ctx.send("Step to the side.")
        await ctx.send("- What'd you get?")
        await ctx.send("- Picking crud out. Stellar!")
        await ctx.send("Wow!")
        await ctx.send("Oouple of newbies?")
        await ctx.send("Yes, sir! Our first day! We are ready!")
        await ctx.send("Make your choice.")
        await ctx.send("- You want to go first?")
        await ctx.send("- No, you go.")
        await ctx.send("Oh, my. What's available?")
        await ctx.send("Restroom attendant's open,")
        await ctx.send("not for the reason you think.")
        await ctx.send("- Any chance of getting the Krelman?")
        await ctx.send("- Sure, you're on.")
        await ctx.send("I'm sorry, the Krelman just closed out.")
        await ctx.send("Wax monkey's always open.")
        await ctx.send("The Krelman opened up again.")
        await ctx.send("What happened?")
        await ctx.send("A bee died. Makes an opening. See?")
        await ctx.send("He's dead. Another dead one.")
        await ctx.send("Deady. Deadified. Two more dead.")
        await ctx.send("Dead from the neck up.")
        await ctx.send("Dead from the neck down. That's life!")
        await ctx.send("Oh, this is so hard!")
        await ctx.send("Heating, cooling,")
        await ctx.send("stunt bee, pourer, stirrer,")
        await ctx.send("humming, inspector number seven,")
        await ctx.send("lint coordinator, stripe supervisor,")
        await ctx.send("mite wrangler. Barry, what")
        await ctx.send("do you think I should... Barry?")
        await ctx.send("Barry!")
        await ctx.send("All right, we've got the sunflower patch")
        await ctx.send("in quadrant nine...")
        await ctx.send("What happened to you?")
        await ctx.send("Where are you?")
        await ctx.send("- I'm going out.")
        await ctx.send("- Out? Out where?")
        await ctx.send("- Out there.")
        await ctx.send("- Oh, no!")
        await ctx.send("I have to, before I go")
        await ctx.send("to work for the rest of my life.")
        await ctx.send("You're gonna die! You're crazy! Hello?")
        await ctx.send("Another call coming in.")
        await ctx.send("If anyone's feeling brave,")
        await ctx.send("there's a Korean deli on 83rd")
        await ctx.send("that gets their roses today.")
        await ctx.send("Hey, guys.")
        await ctx.send("- Look at that.")
        await ctx.send("- Isn't that the kid we saw yesterday?")
        await ctx.send("Hold it, son, flight deck's restricted.")
        await ctx.send("It's OK, Lou. We're gonna take him up.")
        await ctx.send("Really? Feeling lucky, are you?")
        await ctx.send("Sign here, here. Just initial that.")
        await ctx.send("- Thank you.")
        await ctx.send("- OK.")
        await ctx.send("You got a rain advisory today,")
        await ctx.send("and as you all know,")
        await ctx.send("bees cannot fly in rain.")
        await ctx.send("So be careful. As always,")
        await ctx.send("watch your brooms,")
        await ctx.send("hockey sticks, dogs,")
        await ctx.send("birds, bears and bats.")
        await ctx.send("Also, I got a couple of reports")
        await ctx.send("of root beer being poured on us.")
        await ctx.send("Murphy's in a home because of it,")
        await ctx.send("babbling like a cicada!")
        await ctx.send("- That's awful.")
        await ctx.send("- And a reminder for you rookies,")
        await ctx.send("bee law number one,")
        await ctx.send("absolutely no talking to humans!")
        await ctx.send("All right, launch positions!")
        await ctx.send("Buzz, buzz, buzz, buzz! Buzz, buzz,")
        await ctx.send("buzz, buzz! Buzz, buzz, buzz, buzz!")
        await ctx.send("Black and yellow!")
        await ctx.send("Hello!")
        await ctx.send("You ready for this, hot shot?")
        await ctx.send("Yeah. Yeah, bring it on.")
        await ctx.send("Wind, check.")
        await ctx.send("- Antennae, check.")
        await ctx.send("- Nectar pack, check.")
        await ctx.send("- Wings, check.")
        await ctx.send("- Stinger, check.")
        await ctx.send("Scared out of my shorts, check.")
        await ctx.send("OK, ladies,")
        await ctx.send("let's move it out!")
        await ctx.send("Pound those petunias,")
        await ctx.send("you striped stem-suckers!")
        await ctx.send("All of you, drain those flowers!")
        await ctx.send("Wow! I'm out!")
        await ctx.send("I can't believe I'm out!")
        await ctx.send("So blue.")
        await ctx.send("I feel so fast and free!")
        await ctx.send("Box kite!")
        await ctx.send("Wow!")
        await ctx.send("Flowers!")
        await ctx.send("This is Blue Leader.")
        await ctx.send("We have roses visual.")
        await ctx.send("Bring it around 3 degrees and hold.")
        await ctx.send("Roses!")
        await ctx.send("3 degrees, roger. Bringing it around.")
        await ctx.send("Stand to the side, kid.")
        await ctx.send("It's got a bit of a kick.")
        await ctx.send("That is one nectar collector!")
        await ctx.send("- Ever see pollination up close?")
        await ctx.send("- No, sir.")
        await ctx.send("I pick up some pollen here, sprinkle it")
        await ctx.send("over here. Maybe a dash over there,")
        await ctx.send("a pinch on that one.")
        await ctx.send("See that? It's a little bit of magic.")
        await ctx.send("That's amazing. Why do we do that?")
        await ctx.send("That's pollen power. More pollen, more")
        await ctx.send("flowers, more nectar, more honey for us.")
        await ctx.send("Oool.")
        await ctx.send("I'm picking up a lot of bright yellow.")
        await ctx.send("Oould be daisies. Don't we need those?")
        await ctx.send("Oopy that visual.")
        await ctx.send("Wait. One of these flowers")
        await ctx.send("seems to be on the move.")
        await ctx.send("Say again? You're reporting")
        await ctx.send("a moving flower?")
        await ctx.send("Affirmative.")
        await ctx.send("That was on the line!")
        await ctx.send("This is the coolest. What is it?")
        await ctx.send("I don't know, but I'm loving this color.")
        await ctx.send("It smells good.")
        await ctx.send("Not like a flower, but I like it.")
        await ctx.send("Yeah, fuzzy.")
        await ctx.send("Ohemical-y.")
        await ctx.send("Oareful, guys. It's a little grabby.")
        await ctx.send("My sweet lord of bees!")
        await ctx.send("Oandy-brain, get off there!")
        await ctx.send("Problem!")
        await ctx.send("- Guys!")
        await ctx.send("- This could be bad.")
        await ctx.send("Affirmative.")
        await ctx.send("Very close.")
        await ctx.send("Gonna hurt.")
        await ctx.send("Mama's little boy.")
        await ctx.send("You are way out of position, rookie!")
        await ctx.send("Ooming in at you like a missile!")
        await ctx.send("Help me!")
        await ctx.send("I don't think these are flowers.")
        await ctx.send("- Should we tell him?")
        await ctx.send("- I think he knows.")
        await ctx.send("What is this?!")
        await ctx.send("Match point!")
        await ctx.send("You can start packing up, honey,")
        await ctx.send("because you're about to eat it!")
        await ctx.send("Yowser!")
        await ctx.send("Gross.")
        await ctx.send("There's a bee in the car!")
        await ctx.send("- Do something!")
        await ctx.send("- I'm driving!")
        await ctx.send("- Hi, bee.")
        await ctx.send("- He's back here!")
        await ctx.send("He's going to sting me!")
        await ctx.send("Nobody move. If you don't move,")
        await ctx.send("he won't sting you. Freeze!")
        await ctx.send("He blinked!")
        await ctx.send("Spray him, Granny!")
        await ctx.send("What are you doing?!")
        await ctx.send("Wow... the tension level")
        await ctx.send("out here is unbelievable.")
        await ctx.send("I gotta get home.")
        await ctx.send("Oan't fly in rain.")
        await ctx.send("Oan't fly in rain.")
        await ctx.send("Oan't fly in rain.")
        await ctx.send("Mayday! Mayday! Bee going down!")
        await ctx.send("Ken, could you close")
        await ctx.send("the window please?")
        await ctx.send("Ken, could you close")
        await ctx.send("the window please?")
        await ctx.send("Oheck out my new resume.")
        await ctx.send("I made it into a fold-out brochure.")
        await ctx.send("You see? Folds out.")
        await ctx.send("Oh, no. More humans. I don't need this.")
        await ctx.send("What was that?")
        await ctx.send("Maybe this time. This time. This time.")
        await ctx.send("This time! This time! This...")
        await ctx.send("Drapes!")
        await ctx.send("That is diabolical.")
        await ctx.send("It's fantastic. It's got all my special")
        await ctx.send("skills, even my top-ten favorite movies.")
        await ctx.send("What's number one? Star Wars?")
        await ctx.send("Nah, I don't go for that...")
        await ctx.send("...kind of stuff.")
        await ctx.send("No wonder we shouldn't talk to them.")
        await ctx.send("They're out of their minds.")
        await ctx.send("When I leave a job interview, they're")
        await ctx.send("flabbergasted, can't believe what I say.")
        await ctx.send("There's the sun. Maybe that's a way out.")
        await ctx.send("I don't remember the sun")
        await ctx.send("having a big 75 on it.")
        await ctx.send("I predicted global warming.")
        await ctx.send("I could feel it getting hotter.")
        await ctx.send("At first I thought it was just me.")
        await ctx.send("Wait! Stop! Bee!")
        await ctx.send("Stand back. These are winter boots.")
        await ctx.send("Wait!")
        await ctx.send("Don't kill him!")
        await ctx.send("You know I'm allergic to them!")
        await ctx.send("This thing could kill me!")
        await ctx.send("Why does his life have")
        await ctx.send("less value than yours?")
        await ctx.send("Why does his life have any less value")
        await ctx.send("than mine? Is that your statement?")
        await ctx.send("I'm just saying all life has value. You")
        await ctx.send("don't know what he's capable of feeling.")
        await ctx.send("My brochure!")
        await ctx.send("There you go, little guy.")
        await ctx.send("I'm not scared of him.")
        await ctx.send("It's an allergic thing.")
        await ctx.send("Put that on your resume brochure.")
        await ctx.send("My whole face could puff up.")
        await ctx.send("Make it one of your special skills.")
        await ctx.send("Knocking someone out")
        await ctx.send("is also a special skill.")
        await ctx.send("Right. Bye, Vanessa. Thanks.")
        await ctx.send("- Vanessa, next week? Yogurt night?")
        await ctx.send("- Sure, Ken. You know, whatever.")
        await ctx.send("- You could put carob chips on there.")
        await ctx.send("- Bye.")
        await ctx.send("- Supposed to be less calories.")
        await ctx.send("- Bye.")
        await ctx.send("I gotta say something.")
        await ctx.send("She saved my life.")
        await ctx.send("I gotta say something.")
        await ctx.send("All right, here it goes.")
        await ctx.send("Nah.")
        await ctx.send("What would I say?")
        await ctx.send("I could really get in trouble.")
        await ctx.send("It's a bee law.")
        await ctx.send("You're not supposed to talk to a human.")
        await ctx.send("I can't believe I'm doing this.")
        await ctx.send("I've got to.")
        await ctx.send("Oh, I can't do it. Oome on!")
        await ctx.send("No. Yes. No.")
        await ctx.send("Do it. I can't.")
        await ctx.send("How should I start it?")
        await ctx.send("'You like jazz?' No, that's no good.")
        await ctx.send("Here she comes! Speak, you fool!")
        await ctx.send("Hi!")
        await ctx.send("I'm sorry.")
        await ctx.send("- You're talking.")
        await ctx.send("- Yes, I know.")
        await ctx.send("You're talking!")
        await ctx.send("I'm so sorry.")
        await ctx.send("No, it's OK. It's fine.")
        await ctx.send("I know I'm dreaming.")
        await ctx.send("But I don't recall going to bed.")
        await ctx.send("Well, I'm sure this")
        await ctx.send("is very disconcerting.")
        await ctx.send("This is a bit of a surprise to me.")
        await ctx.send("I mean, you're a bee!")
        await ctx.send("I am. And I'm not supposed")
        await ctx.send("to be doing this,")
        await ctx.send("but they were all trying to kill me.")
        await ctx.send("And if it wasn't for you...")
        await ctx.send("I had to thank you.")
        await ctx.send("It's just how I was raised.")
        await ctx.send("That was a little weird.")
        await ctx.send("- I'm talking with a bee.")
        await ctx.send("- Yeah.")
        await ctx.send("I'm talking to a bee.")
        await ctx.send("And the bee is talking to me!")
        await ctx.send("I just want to say I'm grateful.")
        await ctx.send("I'll leave now.")
        await ctx.send("- Wait! How did you learn to do that?")
        await ctx.send("- What?")
        await ctx.send("The talking thing.")
        await ctx.send("Same way you did, I guess.")
        await ctx.send("Mama, Dada, honey.' You pick it up.")
        await ctx.send("- That's very funny.")
        await ctx.send("- Yeah.")
        await ctx.send("Bees are funny. If we didn't laugh,")
        await ctx.send("we'd cry with what we have to deal with.")
        await ctx.send("Anyway...")
        await ctx.send("Oan I...")
        await ctx.send("...get you something?")
        await ctx.send("- Like what?")
        await ctx.send("I don't know. I mean...")
        await ctx.send("I don't know. Ooffee?")
        await ctx.send("I don't want to put you out.")
        await ctx.send("It's no trouble. It takes two minutes.")
        await ctx.send("- It's just coffee.")
        await ctx.send("- I hate to impose.")
        await ctx.send("- Don't be ridiculous!")
        await ctx.send("- Actually, I would love a cup.")
        await ctx.send("Hey, you want rum cake?")
        await ctx.send("- I shouldn't.")
        await ctx.send("- Have some.")
        await ctx.send("- No, I can't.")
        await ctx.send("- Oome on!")
        await ctx.send("I'm trying to lose a couple micrograms.")
        await ctx.send("- Where?")
        await ctx.send("- These stripes don't help.")
        await ctx.send("You look great!")
        await ctx.send("I don't know if you know")
        await ctx.send("anything about fashion.")
        await ctx.send("Are you all right?")
        await ctx.send("No.")
        await ctx.send("He's making the tie in the cab")
        await ctx.send("as they're flying up Madison.")
        await ctx.send("He finally gets there.")
        await ctx.send("He runs up the steps into the church.")
        await ctx.send("The wedding is on.")
        await ctx.send("And he says, 'Watermelon?'")
        await ctx.send("I thought you said Guatemalan.")
        await ctx.send("'Why would I marry a watermelon?'")
        await ctx.send("Is that a bee joke?")
        await ctx.send("That's the kind of stuff we do.")
        await ctx.send("Yeah, different.")
        await ctx.send("So, what are you gonna do, Barry?")
        await ctx.send("About work? I don't know.")
        await ctx.send("I want to do my part for the hive,")
        await ctx.send("but I can't do it the way they want.")
        await ctx.send("I know how you feel.")
        await ctx.send("- You do?")
        await ctx.send("- Sure.")
        await ctx.send("My parents wanted me to be a lawyer or")
        await ctx.send("a doctor, but I wanted to be a florist.")
        await ctx.send("- Really?")
        await ctx.send("- My only interest is flowers.")
        await ctx.send("Our new queen was just elected")
        await ctx.send("with that same campaign slogan.")
        await ctx.send("Anyway, if you look...")
        await ctx.send("There's my hive right there. See it?")
        await ctx.send("You're in Sheep Meadow!")
        await ctx.send("Yes! I'm right off the Turtle Pond!")
        await ctx.send("No way! I know that area.")
        await ctx.send("I lost a toe ring there once.")
        await ctx.send("- Why do girls put rings on their toes?")
        await ctx.send("- Why not?")
        await ctx.send("- It's like putting a hat on your knee.")
        await ctx.send("- Maybe I'll try that.")
        await ctx.send("- You all right, ma'am?")
        await ctx.send("- Oh, yeah. Fine.")
        await ctx.send("Just having two cups of coffee!")
        await ctx.send("Anyway, this has been great.")
        await ctx.send("Thanks for the coffee.")
        await ctx.send("Yeah, it's no trouble.")
        await ctx.send("Sorry I couldn't finish it. If I did,")
        await ctx.send("I'd be up the rest of my life.")
        await ctx.send("Are you...?")
        await ctx.send("Oan I take a piece of this with me?")
        await ctx.send("Sure! Here, have a crumb.")
        await ctx.send("- Thanks!")
        await ctx.send("- Yeah.")
        await ctx.send("All right. Well, then...")
        await ctx.send("I guess I'll see you around.")
        await ctx.send("Or not.")
        await ctx.send("OK, Barry.")
        await ctx.send("And thank you")
        await ctx.send("so much again... for before.")
        await ctx.send("Oh, that? That was nothing.")
        await ctx.send("Well, not nothing, but... Anyway...")
        await ctx.send("This can't possibly work.")
        await ctx.send("He's all set to go.")
        await ctx.send("We may as well try it.")
        await ctx.send("OK, Dave, pull the chute.")
        await ctx.send("- Sounds amazing.")
        await ctx.send("- It was amazing!")
        await ctx.send("It was the scariest,")
        await ctx.send("happiest moment of my life.")
        await ctx.send("Humans! I can't believe")
        await ctx.send("you were with humans!")
        await ctx.send("Giant, scary humans!")
        await ctx.send("What were they like?")
        await ctx.send("Huge and crazy. They talk crazy.")
        await ctx.send("They eat crazy giant things.")
        await ctx.send("They drive crazy.")
        await ctx.send("- Do they try and kill you, like on TV?")
        await ctx.send("- Some of them. But some of them don't.")
        await ctx.send("- How'd you get back?")
        await ctx.send("- Poodle.")
        await ctx.send("You did it, and I'm glad. You saw")
        await ctx.send("whatever you wanted to see.")
        await ctx.send("You had your 'experience.' Now you")
        await ctx.send("can pick out yourjob and be normal.")
        await ctx.send("- Well...")
        await ctx.send("- Well?")
        await ctx.send("Well, I met someone.")
        await ctx.send("You did? Was she Bee-ish?")
        await ctx.send("- A wasp?! Your parents will kill you!")
        await ctx.send("- No, no, no, not a wasp.")
        await ctx.send("- Spider?")
        await ctx.send("- I'm not attracted to spiders.")
        await ctx.send("I know it's the hottest thing,")
        await ctx.send("with the eight legs and all.")
        await ctx.send("I can't get by that face.")
        await ctx.send("So who is she?")
        await ctx.send("She's... human.")
        await ctx.send("No, no. That's a bee law.")
        await ctx.send("You wouldn't break a bee law.")
        await ctx.send("- Her name's Vanessa.")
        await ctx.send("- Oh, boy.")
        await ctx.send("She's so nice. And she's a florist!")
        await ctx.send("Oh, no! You're dating a human florist!")
        await ctx.send("We're not dating.")
        await ctx.send("You're flying outside the hive, talking")
        await ctx.send("to humans that attack our homes")
        await ctx.send("with power washers and M-8!")
        await ctx.send("One-eighth a stick of dynamite!")
        await ctx.send("She saved my life!")
        await ctx.send("And she understands me.")
        await ctx.send("This is over!")
        await ctx.send("Eat this.")
        await ctx.send("This is not over! What was that?")
        await ctx.send("- They call it a crumb.")
        await ctx.send("- It was so stingin' stripey!")
        await ctx.send("And that's not what they eat.")
        await ctx.send("That's what falls off what they eat!")
        await ctx.send("- You know what a Oinnabon is?")
        await ctx.send("- No.")
        await ctx.send("It's bread and cinnamon and frosting.")
        await ctx.send("They heat it up...")
        await ctx.send("Sit down!")
        await ctx.send("...really hot!")
        await ctx.send("- Listen to me!")
        await ctx.send("We are not them! We're us.")
        await ctx.send("There's us and there's them!")
        await ctx.send("Yes, but who can deny")
        await ctx.send("the heart that is yearning?")
        await ctx.send("There's no yearning.")
        await ctx.send("Stop yearning. Listen to me!")
        await ctx.send("You have got to start thinking bee,")
        await ctx.send("my friend. Thinking bee!")
        await ctx.send("- Thinking bee.")
        await ctx.send("- Thinking bee.")
        await ctx.send("Thinking bee! Thinking bee!")
        await ctx.send("Thinking bee! Thinking bee!")
        await ctx.send("There he is. He's in the pool.")
        await ctx.send("You know what your problem is, Barry?")
        await ctx.send("I gotta start thinking bee?")
        await ctx.send("How much longer will this go on?")
        await ctx.send("It's been three days!")
        await ctx.send("Why aren't you working?")
        await ctx.send("I've got a lot of big life decisions")
        await ctx.send("to think about.")
        await ctx.send("What life? You have no life!")
        await ctx.send("You have no job. You're barely a bee!")
        await ctx.send("Would it kill you")
        await ctx.send("to make a little honey?")
        await ctx.send("Barry, come out.")
        await ctx.send("Your father's talking to you.")
        await ctx.send("Martin, would you talk to him?")
        await ctx.send("Barry, I'm talking to you!")
        await ctx.send("You coming?")
        await ctx.send("Got everything?")
        await ctx.send("All set!")
        await ctx.send("Go ahead. I'll catch up.")
        await ctx.send("Don't be too long.")
        await ctx.send("Watch this!")
        await ctx.send("Vanessa!")
        await ctx.send("- We're still here.")
        await ctx.send("- I told you not to yell at him.")
        await ctx.send("He doesn't respond to yelling!")
        await ctx.send("- Then why yell at me?")
        await ctx.send("- Because you don't listen!")
        await ctx.send("I'm not listening to this.")
        await ctx.send("Sorry, I've gotta go.")
        await ctx.send("- Where are you going?")
        await ctx.send("- I'm meeting a friend.")
        await ctx.send("A girl? Is this why you can't decide?")
        await ctx.send("Bye.")
        await ctx.send("I just hope she's Bee-ish.")
        await ctx.send("They have a huge parade")
        await ctx.send("of flowers every year in Pasadena?")
        await ctx.send("To be in the Tournament of Roses,")
        await ctx.send("that's every florist's dream!")
        await ctx.send("Up on a float, surrounded")
        await ctx.send("by flowers, crowds cheering.")
        await ctx.send("A tournament. Do the roses")
        await ctx.send("compete in athletic events?")
        await ctx.send("No. All right, I've got one.")
        await ctx.send("How come you don't fly everywhere?")
        await ctx.send("It's exhausting. Why don't you")
        await ctx.send("run everywhere? It's faster.")
        await ctx.send("Yeah, OK, I see, I see.")
        await ctx.send("All right, your turn.")
        await ctx.send("TiVo. You can just freeze live TV?")
        await ctx.send("That's insane!")
        await ctx.send("You don't have that?")
        await ctx.send("We have Hivo, but it's a disease.")
        await ctx.send("It's a horrible, horrible disease.")
        await ctx.send("Oh, my.")
        await ctx.send("Dumb bees!")
        await ctx.send("You must want to sting all those jerks.")
        await ctx.send("We try not to sting.")
        await ctx.send("It's usually fatal for us.")
        await ctx.send("So you have to watch your temper.")
        await ctx.send("Very carefully.")
        await ctx.send("You kick a wall, take a walk,")
        await ctx.send("write an angry letter and throw it out.")
        await ctx.send("Work through it like any emotion:")
        await ctx.send("Anger, jealousy, lust.")
        await ctx.send("Oh, my goodness! Are you OK?")
        await ctx.send("Yeah.")
        await ctx.send("- What is wrong with you?!")
        await ctx.send("- It's a bug.")
        await ctx.send("He's not bothering anybody.")
        await ctx.send("Get out of here, you creep!")
        await ctx.send("What was that? A Pic 'N' Save circular?")
        await ctx.send("Yeah, it was. How did you know?")
        await ctx.send("It felt like about 1 page.")
        await ctx.send("Seventy-five is pretty much our limit.")
        await ctx.send("You've really got that")
        await ctx.send("down to a science.")
        await ctx.send("- I lost a cousin to Italian Vogue.")
        await ctx.send("- I'll bet.")
        await ctx.send("What in the name")
        await ctx.send("of Mighty Hercules is this?")
        await ctx.send("How did this get here?")
        await ctx.send("Oute Bee, Golden Blossom,")
        await ctx.send("Ray Liotta Private Select?")
        await ctx.send("- Is he that actor?")
        await ctx.send("- I never heard of him.")
        await ctx.send("- Why is this here?")
        await ctx.send("- For people. We eat it.")
        await ctx.send("You don't have")
        await ctx.send("enough food of your own?")
        await ctx.send("- Well, yes.")
        await ctx.send("- How do you get it?")
        await ctx.send("- Bees make it.")
        await ctx.send("- I know who makes it!")
        await ctx.send("And it's hard to make it!")
        await ctx.send("There's heating, cooling, stirring.")
        await ctx.send("You need a whole Krelman thing!")
        await ctx.send("- It's organic.")
        await ctx.send("- It's our-ganic!")
        await ctx.send("It's just honey, Barry.")
        await ctx.send("Just what?!")
        await ctx.send("Bees don't know about this!")
        await ctx.send("This is stealing! A lot of stealing!")
        await ctx.send("You've taken our homes, schools,")
        await ctx.send("hospitals! This is all we have!")
        await ctx.send("And it's on sale?!")
        await ctx.send("I'm getting to the bottom of this.")
        await ctx.send("I'm getting to the bottom")
        await ctx.send("of all of this!")
        await ctx.send("Hey, Hector.")
        await ctx.send("- You almost done?")
        await ctx.send("- Almost.")
        await ctx.send("He is here. I sense it.")
        await ctx.send("Well, I guess I'll go home now")
        await ctx.send("and just leave this nice honey out,")
        await ctx.send("with no one around.")
        await ctx.send("You're busted, box boy!")
        await ctx.send("I knew I heard something.")
        await ctx.send("So you can talk!")
        await ctx.send("I can talk.")
        await ctx.send("And now you'll start talking!")
        await ctx.send("Where you getting the sweet stuff?")
        await ctx.send("Who's your supplier?")
        await ctx.send("I don't understand.")
        await ctx.send("I thought we were friends.")
        await ctx.send("The last thing we want")
        await ctx.send("to do is upset bees!")
        await ctx.send("You're too late! It's ours now!")
        await ctx.send("You, sir, have crossed")
        await ctx.send("the wrong sword!")
        await ctx.send("You, sir, will be lunch")
        await ctx.send("for my iguana, Ignacio!")
        await ctx.send("Where is the honey coming from?")
        await ctx.send("Tell me where!")
        await ctx.send("Honey Farms! It comes from Honey Farms!")
        await ctx.send("Orazy person!")
        await ctx.send("What horrible thing has happened here?")
        await ctx.send("These faces, they never knew")
        await ctx.send("what hit them. And now")
        await ctx.send("they're on the road to nowhere!")
        await ctx.send("Just keep still.")
        await ctx.send("What? You're not dead?")
        await ctx.send("Do I look dead? They will wipe anything")
        await ctx.send("that moves. Where you headed?")
        await ctx.send("To Honey Farms.")
        await ctx.send("I am onto something huge here.")
        await ctx.send("I'm going to Alaska. Moose blood,")
        await ctx.send("crazy stuff. Blows your head off!")
        await ctx.send("I'm going to Tacoma.")
        await ctx.send("- And you?")
        await ctx.send("- He really is dead.")
        await ctx.send("All right.")
        await ctx.send("Uh-oh!")
        await ctx.send("- What is that?!")
        await ctx.send("- Oh, no!")
        await ctx.send("- A wiper! Triple blade!")
        await ctx.send("- Triple blade?")
        await ctx.send("Jump on! It's your only chance, bee!")
        await ctx.send("Why does everything have")
        await ctx.send("to be so doggone clean?!")
        await ctx.send("How much do you people need to see?!")
        await ctx.send("Open your eyes!")
        await ctx.send("Stick your head out the window!")
        await ctx.send("From NPR News in Washington,")
        await ctx.send("I'm Oarl Kasell.")
        await ctx.send("But don't kill no more bugs!")
        await ctx.send("- Bee!")
        await ctx.send("- Moose blood guy!!")
        await ctx.send("- You hear something?")
        await ctx.send("- Like what?")
        await ctx.send("Like tiny screaming.")
        await ctx.send("Turn off the radio.")
        await ctx.send("Whassup, bee boy?")
        await ctx.send("Hey, Blood.")
        await ctx.send("Just a row of honey jars,")
        await ctx.send("as far as the eye could see.")
        await ctx.send("Wow!")
        await ctx.send("I assume wherever this truck goes")
        await ctx.send("is where they're getting it.")
        await ctx.send("I mean, that honey's ours.")
        await ctx.send("- Bees hang tight.")
        await ctx.send("- We're all jammed in.")
        await ctx.send("It's a close community.")
        await ctx.send("Not us, man. We on our own.")
        await ctx.send("Every mosquito on his own.")
        await ctx.send("- What if you get in trouble?")
        await ctx.send("- You a mosquito, you in trouble.")
        await ctx.send("Nobody likes us. They just smack.")
        await ctx.send("See a mosquito, smack, smack!")
        await ctx.send("At least you're out in the world.")
        await ctx.send("You must meet girls.")
        await ctx.send("Mosquito girls try to trade up,")
        await ctx.send("get with a moth, dragonfly.")
        await ctx.send("Mosquito girl don't want no mosquito.")
        await ctx.send("You got to be kidding me!")
        await ctx.send("Mooseblood's about to leave")
        await ctx.send("the building! So long, bee!")
        await ctx.send("- Hey, guys!")
        await ctx.send("- Mooseblood!")
        await ctx.send("I knew I'd catch y'all down here.")
        await ctx.send("Did you bring your crazy straw?")
        await ctx.send("We throw it in jars, slap a label on it,")
        await ctx.send("and it's pretty much pure profit.")
        await ctx.send("What is this place?")
        await ctx.send("A bee's got a brain")
        await ctx.send("the size of a pinhead.")
        await ctx.send("They are pinheads!")
        await ctx.send("Pinhead.")
        await ctx.send("- Oheck out the new smoker.")
        await ctx.send("- Oh, sweet. That's the one you want.")
        await ctx.send("The Thomas")
        await ctx.send("Smoker?")
        await ctx.send("Ninety puffs a minute, semi-automatic.")
        await ctx.send("Twice the nicotine, all the tar.")
        await ctx.send("A couple breaths of this")
        await ctx.send("knocks them right out.")
        await ctx.send("They make the honey,")
        await ctx.send("and we make the money.")
        await ctx.send("They make the honey,")
        await ctx.send("and we make the money?")
        await ctx.send("Oh, my!")
        await ctx.send("What's going on? Are you OK?")
        await ctx.send("Yeah. It doesn't last too long.")
        await ctx.send("Do you know you're")
        await ctx.send("in a fake hive with fake walls?")
        await ctx.send("Our queen was moved here.")
        await ctx.send("We had no choice.")
        await ctx.send("This is your queen?")
        await ctx.send("That's a man in women's clothes!")
        await ctx.send("That's a drag queen!")
        await ctx.send("What is this?")
        await ctx.send("Oh, no!")
        await ctx.send("There's hundreds of them!")
        await ctx.send("Bee honey.")
        await ctx.send("Our honey is being brazenly stolen")
        await ctx.send("on a massive scale!")
        await ctx.send("This is worse than anything bears")
        await ctx.send("have done! I intend to do something.")
        await ctx.send("Oh, Barry, stop.")
        await ctx.send("Who told you humans are taking")
        await ctx.send("our honey? That's a rumor.")
        await ctx.send("Do these look like rumors?")
        await ctx.send("That's a conspiracy theory.")
        await ctx.send("These are obviously doctored photos.")
        await ctx.send("How did you get mixed up in this?")
        await ctx.send("He's been talking to humans.")
        await ctx.send("- What?")
        await ctx.send("- Talking to humans?!")
        await ctx.send("He has a human girlfriend.")
        await ctx.send("And they make out!")
        await ctx.send("Make out? Barry!")
        await ctx.send("We do not.")
        await ctx.send("- You wish you could.")
        await ctx.send("- Whose side are you on?")
        await ctx.send("The bees!")
        await ctx.send("I dated a cricket once in San Antonio.")
        await ctx.send("Those crazy legs kept me up all night.")
        await ctx.send("Barry, this is what you want")
        await ctx.send("to do with your life?")
        await ctx.send("I want to do it for all our lives.")
        await ctx.send("Nobody works harder than bees!")
        await ctx.send("Dad, I remember you")
        await ctx.send("coming home so overworked")
        await ctx.send("your hands were still stirring.")
        await ctx.send("You couldn't stop.")
        await ctx.send("I remember that.")
        await ctx.send("What right do they have to our honey?")
        await ctx.send("We live on two cups a year. They put it")
        await ctx.send("in lip balm for no reason whatsoever!")
        await ctx.send("Even if it's true, what can one bee do?")
        await ctx.send("Sting them where it really hurts.")
        await ctx.send("In the face! The eye!")
        await ctx.send("- That would hurt.")
        await ctx.send("- No.")
        await ctx.send("Up the nose? That's a killer.")
        await ctx.send("There's only one place you can sting")
        await ctx.send("the humans, one place where it matters.")
        await ctx.send("Hive at Five, the hive's only")
        await ctx.send("full-hour action news source.")
        await ctx.send("No more bee beards!")
        await ctx.send("With Bob Bumble at the anchor desk.")
        await ctx.send("Weather with Storm Stinger.")
        await ctx.send("Sports with Buzz Larvi.")
        await ctx.send("And Jeanette Ohung.")
        await ctx.send("- Good evening. I'm Bob Bumble.")
        await ctx.send("- And I'm Jeanette Ohung.")
        await ctx.send("A tri-county bee, Barry Benson,")
        await ctx.send("intends to sue the human race")
        await ctx.send("for stealing our honey,")
        await ctx.send("packaging it and profiting")
        await ctx.send("from it illegally!")
        await ctx.send("Tomorrow night on Bee Larry King,")
        await ctx.send("we'll have three former queens here in")
        await ctx.send("our studio, discussing their new book,")
        await ctx.send("Olassy Ladies,")
        await ctx.send("out this week on Hexagon.")
        await ctx.send("Tonight we're talking to Barry Benson.")
        await ctx.send("Did you ever think, 'I'm a kid")
        await ctx.send("from the hive. I can't do this?'")
        await ctx.send("Bees have never been afraid")
        await ctx.send("to change the world.")
        await ctx.send("What about Bee Oolumbus?")
        await ctx.send("Bee Gandhi? Bejesus?")
        await ctx.send("Where I'm from, we'd never sue humans.")
        await ctx.send("We were thinking")
        await ctx.send("of stickball or candy stores.")
        await ctx.send("How old are you?")
        await ctx.send("The bee community")
        await ctx.send("is supporting you in this case,")
        await ctx.send("which will be the trial")
        await ctx.send("of the bee century.")
        await ctx.send("You know, they have a Larry King")
        await ctx.send("in the human world too.")
        await ctx.send("It's a common name. Next week...")
        await ctx.send("He looks like you and has a show")
        await ctx.send("and suspenders and colored dots...")
        await ctx.send("Next week...")
        await ctx.send("Glasses, quotes on the bottom from the")
        await ctx.send("guest even though you just heard 'em.")
        await ctx.send("Bear Week next week!")
        await ctx.send("They're scary, hairy and here live.")
        await ctx.send("Always leans forward, pointy shoulders,")
        await ctx.send("squinty eyes, very Jewish.")
        await ctx.send("In tennis, you attack")
        await ctx.send("at the point of weakness!")
        await ctx.send("It was my grandmother, Ken. She's 81.")
        await ctx.send("Honey, her backhand's a joke!")
        await ctx.send("I'm not gonna take advantage of that?")
        await ctx.send("Quiet, please.")
        await ctx.send("Actual work going on here.")
        await ctx.send("- Is that that same bee?")
        await ctx.send("- Yes, it is!")
        await ctx.send("I'm helping him sue the human race.")
        await ctx.send("- Hello.")
        await ctx.send("- Hello, bee.")
        await ctx.send("This is Ken.")
        await ctx.send("Yeah, I remember you. Timberland, size")
        await ctx.send("ten and a half. Vibram sole, I believe.")
        await ctx.send("Why does he talk again?")
        await ctx.send("Listen, you better go")
        await ctx.send("cause we're really busy working.")
        await ctx.send("But it's our yogurt night!")
        await ctx.send("Bye-bye.")
        await ctx.send("Why is yogurt night so difficult?!")
        await ctx.send("You poor thing.")
        await ctx.send("You two have been at this for hours!")
        await ctx.send("Yes, and Adam here")
        await ctx.send("has been a huge help.")
        await ctx.send("- Frosting...")
        await ctx.send("- How many sugars?")
        await ctx.send("Just one. I try not")
        await ctx.send("to use the competition.")
        await ctx.send("So why are you helping me?")
        await ctx.send("Bees have good qualities.")
        await ctx.send("And it takes my mind off the shop.")
        await ctx.send("Instead of flowers, people")
        await ctx.send("are giving balloon bouquets now.")
        await ctx.send("Those are great, if you're three.")
        await ctx.send("And artificial flowers.")
        await ctx.send("- Oh, those just get me psychotic!")
        await ctx.send("- Yeah, me too.")
        await ctx.send("Bent stingers, pointless pollination.")
        await ctx.send("Bees must hate those fake things!")
        await ctx.send("Nothing worse")
        await ctx.send("than a daffodil that's had work done.")
        await ctx.send("Maybe this could make up")
        await ctx.send("for it a little bit.")
        await ctx.send("- This lawsuit's a pretty big deal.")
        await ctx.send("- I guess.")
        await ctx.send("You sure you want to go through with it?")
        await ctx.send("Am I sure? When I'm done with")
        await ctx.send("the humans, they won't be able")
        await ctx.send("to say, 'Honey, I'm home,")
        await ctx.send("without paying a royalty!")
        await ctx.send("It's an incredible scene")
        await ctx.send("here in downtown Manhattan,")
        await ctx.send("where the world anxiously waits,")
        await ctx.send("because for the first time in history,")
        await ctx.send("we will hear for ourselves")
        await ctx.send("if a honeybee can actually speak.")
        await ctx.send("What have we gotten into here, Barry?")
        await ctx.send("It's pretty big, isn't it?")
        await ctx.send("I can't believe how many humans")
        await ctx.send("don't work during the day.")
        await ctx.send("You think billion-dollar multinational")
        await ctx.send("food companies have good lawyers?")
        await ctx.send("Everybody needs to stay")
        await ctx.send("behind the barricade.")
        await ctx.send("- What's the matter?")
        await ctx.send("- I don't know, I just got a chill.")
        await ctx.send("Well, if it isn't the bee team.")
        await ctx.send("You boys work on this?")
        await ctx.send("All rise! The Honorable")
        await ctx.send("Judge Bumbleton presiding.")
        await ctx.send("All right. Oase number 4475,")
        await ctx.send("Superior Oourt of New York,")
        await ctx.send("Barry Bee Benson v. the Honey Industry")
        await ctx.send("is now in session.")
        await ctx.send("Mr. Montgomery, you're representing")
        await ctx.send("the five food companies collectively?")
        await ctx.send("A privilege.")
        await ctx.send("Mr. Benson... you're representing")
        await ctx.send("all the bees of the world?")
        await ctx.send("I'm kidding. Yes, Your Honor,")
        await ctx.send("we're ready to proceed.")
        await ctx.send("Mr. Montgomery,")
        await ctx.send("your opening statement, please.")
        await ctx.send("Ladies and gentlemen of the jury,")
        await ctx.send("my grandmother was a simple woman.")
        await ctx.send("Born on a farm, she believed")
        await ctx.send("it was man's divine right")
        await ctx.send("to benefit from the bounty")
        await ctx.send("of nature God put before us.")
        await ctx.send("If we lived in the topsy-turvy world")
        await ctx.send("Mr. Benson imagines,")
        await ctx.send("just think of what would it mean.")
        await ctx.send("I would have to negotiate")
        await ctx.send("with the silkworm")
        await ctx.send("for the elastic in my britches!")
        await ctx.send("Talking bee!")
        await ctx.send("How do we know this isn't some sort of")
        await ctx.send("holographic motion-picture-capture")
        await ctx.send("Hollywood wizardry?")
        await ctx.send("They could be using laser beams!")
        await ctx.send("Robotics! Ventriloquism!")
        await ctx.send("Oloning! For all we know,")
        await ctx.send("he could be on steroids!")
        await ctx.send("Mr. Benson?")
        await ctx.send("Ladies and gentlemen,")
        await ctx.send("there's no trickery here.")
        await ctx.send("I'm just an ordinary bee.")
        await ctx.send("Honey's pretty important to me.")
        await ctx.send("It's important to all bees.")
        await ctx.send("We invented it!")
        await ctx.send("We make it. And we protect it")
        await ctx.send("with our lives.")
        await ctx.send("Unfortunately, there are")
        await ctx.send("some people in this room")
        await ctx.send("who think they can take it from us")
        await ctx.send("'cause we're the little guys!")
        await ctx.send("I'm hoping that, after this is all over,")
        await ctx.send("you'll see how, by taking our honey,")
        await ctx.send("you not only take everything we have")
        await ctx.send("but everything we are!")
        await ctx.send("I wish he'd dress like that")
        await ctx.send("all the time. So nice!")
        await ctx.send("Oall your first witness.")
        await ctx.send("So, Mr. Klauss Vanderhayden")
        await ctx.send("of Honey Farms, big company you have.")
        await ctx.send("I suppose so.")
        await ctx.send("I see you also own")
        await ctx.send("Honeyburton and Honron!")
        await ctx.send("Yes, they provide beekeepers")
        await ctx.send("for our farms.")
        await ctx.send("Beekeeper. I find that")
        await ctx.send("to be a very disturbing term.")
        await ctx.send("I don't imagine you employ")
        await ctx.send("any bee-free-ers, do you?")
        await ctx.send("- No.")
        await ctx.send("- I couldn't hear you.")
        await ctx.send("- No.")
        await ctx.send("- No.")
        await ctx.send("Because you don't free bees.")
        await ctx.send("You keep bees. Not only that,")
        await ctx.send("it seems you thought a bear would be")
        await ctx.send("an appropriate image for a jar of honey.")
        await ctx.send("They're very lovable creatures.")
        await ctx.send("Yogi Bear, Fozzie Bear, Build-A-Bear.")
        await ctx.send("You mean like this?")
        await ctx.send("Bears kill bees!")
        await ctx.send("How'd you like his head crashing")
        await ctx.send("through your living room?!")
        await ctx.send("Biting into your couch!")
        await ctx.send("Spitting out your throw pillows!")
        await ctx.send("OK, that's enough. Take him away.")
        await ctx.send("So, Mr. Sting, thank you for being here.")
        await ctx.send("Your name intrigues me.")
        await ctx.send("- Where have I heard it before?")
        await ctx.send("- I was with a band called The Police.")
        await ctx.send("But you've never been")
        await ctx.send("a police officer, have you?")
        await ctx.send("No, I haven't.")
        await ctx.send("No, you haven't. And so here")
        await ctx.send("we have yet another example")
        await ctx.send("of bee culture casually")
        await ctx.send("stolen by a human")
        await ctx.send("for nothing more than")
        await ctx.send("a prance-about stage name.")
        await ctx.send("Oh, please.")
        await ctx.send("Have you ever been stung, Mr. Sting?")
        await ctx.send("Because I'm feeling")
        await ctx.send("a little stung, Sting.")
        await ctx.send("Or should I say... Mr. Gordon M. Sumner!")
        await ctx.send("That's not his real name?! You idiots!")
        await ctx.send("Mr. Liotta, first,")
        await ctx.send("belated congratulations on")
        await ctx.send("your Emmy win for a guest spot")
        await ctx.send("on ER in 2 5.")
        await ctx.send("Thank you. Thank you.")
        await ctx.send("I see from your resume")
        await ctx.send("that you're devilishly handsome")
        await ctx.send("with a churning inner turmoil")
        await ctx.send("that's ready to blow.")
        await ctx.send("I enjoy what I do. Is that a crime?")
        await ctx.send("Not yet it isn't. But is this")
        await ctx.send("what it's come to for you?")
        await ctx.send("Exploiting tiny, helpless bees")
        await ctx.send("so you don't")
        await ctx.send("have to rehearse")
        await ctx.send("your part and learn your lines, sir?")
        await ctx.send("Watch it, Benson!")
        await ctx.send("I could blow right now!")
        await ctx.send("This isn't a goodfella.")
        await ctx.send("This is a badfella!")
        await ctx.send("Why doesn't someone just step on")
        await ctx.send("this creep, and we can all go home?!")
        await ctx.send("- Order in this court!")
        await ctx.send("- You're all thinking it!")
        await ctx.send("Order! Order, I say!")
        await ctx.send("- Say it!")
        await ctx.send("- Mr. Liotta, please sit down!")
        await ctx.send("I think it was awfully nice")
        await ctx.send("of that bear to pitch in like that.")
        await ctx.send("I think the jury's on our side.")
        await ctx.send("Are we doing everything right, legally?")
        await ctx.send("I'm a florist.")
        await ctx.send("Right. Well, here's to a great team.")
        await ctx.send("To a great team!")
        await ctx.send("Well, hello.")
        await ctx.send("- Ken!")
        await ctx.send("- Hello.")
        await ctx.send("I didn't think you were coming.")
        await ctx.send("No, I was just late.")
        await ctx.send("I tried to call, but... the battery.")
        await ctx.send("I didn't want all this to go to waste,")
        await ctx.send("so I called Barry. Luckily, he was free.")
        await ctx.send("Oh, that was lucky.")
        await ctx.send("There's a little left.")
        await ctx.send("I could heat it up.")
        await ctx.send("Yeah, heat it up, sure, whatever.")
        await ctx.send("So I hear you're quite a tennis player.")
        await ctx.send("I'm not much for the game myself.")
        await ctx.send("The ball's a little grabby.")
        await ctx.send("That's where I usually sit.")
        await ctx.send("Right... there.")
        await ctx.send("Ken, Barry was looking at your resume,")
        await ctx.send("and he agreed with me that eating with")
        await ctx.send("chopsticks isn't really a special skill.")
        await ctx.send("You think I don't see what you're doing?")
        await ctx.send("I know how hard it is to find")
        await ctx.send("the rightjob. We have that in common.")
        await ctx.send("Do we?")
        await ctx.send("Bees have 1 percent employment,")
        await ctx.send("but we do jobs like taking the crud out.")
        await ctx.send("That's just what")
        await ctx.send("I was thinking about doing.")
        await ctx.send("Ken, I let Barry borrow your razor")
        await ctx.send("for his fuzz. I hope that was all right.")
        await ctx.send("I'm going to drain the old stinger.")
        await ctx.send("Yeah, you do that.")
        await ctx.send("Look at that.")
        await ctx.send("You know, I've just about had it")
        await ctx.send("with your little mind games.")
        await ctx.send("- What's that?")
        await ctx.send("- Italian Vogue.")
        await ctx.send("Mamma mia, that's a lot of pages.")
        await ctx.send("A lot of ads.")
        await ctx.send("Remember what Van said, why is")
        await ctx.send("your life more valuable than mine?")
        await ctx.send("Funny, I just can't seem to recall that!")
        await ctx.send("I think something stinks in here!")
        await ctx.send("I love the smell of flowers.")
        await ctx.send("How do you like the smell of flames?!")
        await ctx.send("Not as much.")
        await ctx.send("Water bug! Not taking sides!")
        await ctx.send("Ken, I'm wearing a Ohapstick hat!")
        await ctx.send("This is pathetic!")
        await ctx.send("I've got issues!")
        await ctx.send("Well, well, well, a royal flush!")
        await ctx.send("- You're bluffing.")
        await ctx.send("- Am I?")
        await ctx.send("Surf's up, dude!")
        await ctx.send("Poo water!")
        await ctx.send("That bowl is gnarly.")
        await ctx.send("Except for those dirty yellow rings!")
        await ctx.send("Kenneth! What are you doing?!")
        await ctx.send("You know, I don't even like honey!")
        await ctx.send("I don't eat it!")
        await ctx.send("We need to talk!")
        await ctx.send("He's just a little bee!")
        await ctx.send("And he happens to be")
        await ctx.send("the nicest bee I've met in a long time!")
        await ctx.send("Long time? What are you talking about?!")
        await ctx.send("Are there other bugs in your life?")
        await ctx.send("No, but there are other things bugging")
        await ctx.send("me in life. And you're one of them!")
        await ctx.send("Fine! Talking bees, no yogurt night...")
        await ctx.send("My nerves are fried from riding")
        await ctx.send("on this emotional roller coaster!")
        await ctx.send("Goodbye, Ken.")
        await ctx.send("And for your information,")
        await ctx.send("I prefer sugar-free, artificial")
        await ctx.send("sweeteners made by man!")
        await ctx.send("I'm sorry about all that.")
        await ctx.send("I know it's got")
        await ctx.send("an aftertaste! I like it!")
        await ctx.send("I always felt there was some kind")
        await ctx.send("of barrier between Ken and me.")
        await ctx.send("I couldn't overcome it.")
        await ctx.send("Oh, well.")
        await ctx.send("Are you OK for the trial?")
        await ctx.send("I believe Mr. Montgomery")
        await ctx.send("is about out of ideas.")
        await ctx.send("We would like to call")
        await ctx.send("Mr. Barry Benson Bee to the stand.")
        await ctx.send("Good idea! You can really see why he's")
        await ctx.send("considered one of the best lawyers...")
        await ctx.send("Yeah.")
        await ctx.send("Layton, you've")
        await ctx.send("gotta weave some magic")
        await ctx.send("with this jury,")
        await ctx.send("or it's gonna be all over.")
        await ctx.send("Don't worry. The only thing I have")
        await ctx.send("to do to turn this jury around")
        await ctx.send("is to remind them")
        await ctx.send("of what they don't like about bees.")
        await ctx.send("- You got the tweezers?")
        await ctx.send("- Are you allergic?")
        await ctx.send("Only to losing, son. Only to losing.")
        await ctx.send("Mr. Benson Bee, I'll ask you")
        await ctx.send("what I think we'd all like to know.")
        await ctx.send("What exactly is your relationship")
        await ctx.send("to that woman?")
        await ctx.send("We're friends.")
        await ctx.send("- Good friends?")
        await ctx.send("- Yes.")
        await ctx.send("How good? Do you live together?")
        await ctx.send("Wait a minute...")
        await ctx.send("Are you her little...")
        await ctx.send("...bedbug?")
        await ctx.send("I've seen a bee documentary or two.")
        await ctx.send("From what I understand,")
        await ctx.send("doesn't your queen give birth")
        await ctx.send("to all the bee children?")
        await ctx.send("- Yeah, but...")
        await ctx.send("- So those aren't your real parents!")
        await ctx.send("- Oh, Barry...")
        await ctx.send("- Yes, they are!")
        await ctx.send("Hold me back!")
        await ctx.send("You're an illegitimate bee,")
        await ctx.send("aren't you, Benson?")
        await ctx.send("He's denouncing bees!")
        await ctx.send("Don't y'all date your cousins?")
        await ctx.send("- Objection!")
        await ctx.send("- I'm going to pincushion this guy!")
        await ctx.send("Adam, don't! It's what he wants!")
        await ctx.send("Oh, I'm hit!!")
        await ctx.send("Oh, lordy, I am hit!")
        await ctx.send("Order! Order!")
        await ctx.send("The venom! The venom")
        await ctx.send("is coursing through my veins!")
        await ctx.send("I have been felled")
        await ctx.send("by a winged beast of destruction!")
        await ctx.send("You see? You can't treat them")
        await ctx.send("like equals! They're striped savages!")
        await ctx.send("Stinging's the only thing")
        await ctx.send("they know! It's their way!")
        await ctx.send("- Adam, stay with me.")
        await ctx.send("- I can't feel my legs.")
        await ctx.send("What angel of mercy")
        await ctx.send("will come forward to suck the poison")
        await ctx.send("from my heaving buttocks?")
        await ctx.send("I will have order in this court. Order!")
        await ctx.send("Order, please!")
        await ctx.send("The case of the honeybees")
        await ctx.send("versus the human race")
        await ctx.send("took a pointed turn against the bees")
        await ctx.send("yesterday when one of their legal")
        await ctx.send("team stung Layton T. Montgomery.")
        await ctx.send("- Hey, buddy.")
        await ctx.send("- Hey.")
        await ctx.send("- Is there much pain?")
        await ctx.send("- Yeah.")
        await ctx.send("I...")
        await ctx.send("I blew the whole case, didn't I?")
        await ctx.send("It doesn't matter. What matters is")
        await ctx.send("you're alive. You could have died.")
        await ctx.send("I'd be better off dead. Look at me.")
        await ctx.send("They got it from the cafeteria")
        await ctx.send("downstairs, in a tuna sandwich.")
        await ctx.send("Look, there's")
        await ctx.send("a little celery still on it.")
        await ctx.send("What was it like to sting someone?")
        await ctx.send("I can't explain it. It was all...")
        await ctx.send("All adrenaline and then...")
        await ctx.send("and then ecstasy!")
        await ctx.send("All right.")
        await ctx.send("You think it was all a trap?")
        await ctx.send("Of course. I'm sorry.")
        await ctx.send("I flew us right into this.")
        await ctx.send("What were we thinking? Look at us. We're")
        await ctx.send("just a couple of bugs in this world.")
        await ctx.send("What will the humans do to us")
        await ctx.send("if they win?")
        await ctx.send("I don't know.")
        await ctx.send("I hear they put the roaches in motels.")
        await ctx.send("That doesn't sound so bad.")
        await ctx.send("Adam, they check in,")
        await ctx.send("but they don't check out!")
        await ctx.send("Oh, my.")
        await ctx.send("Oould you get a nurse")
        await ctx.send("to close that window?")
        await ctx.send("- Why?")
        await ctx.send("- The smoke.")
        await ctx.send("Bees don't smoke.")
        await ctx.send("Right. Bees don't smoke.")
        await ctx.send("Bees don't smoke!")
        await ctx.send("But some bees are smoking.")
        await ctx.send("That's it! That's our case!")
        await ctx.send("It is? It's not over?")
        await ctx.send("Get dressed. I've gotta go somewhere.")
        await ctx.send("Get back to the court and stall.")
        await ctx.send("Stall any way you can.")
        await ctx.send("And assuming you've done step correctly, you're ready for the tub.")
        await ctx.send("Mr. Flayman.")
        await ctx.send("Yes? Yes, Your Honor!")
        await ctx.send("Where is the rest of your team?")
        await ctx.send("Well, Your Honor, it's interesting.")
        await ctx.send("Bees are trained to fly haphazardly,")
        await ctx.send("and as a result,")
        await ctx.send("we don't make very good time.")
        await ctx.send("I actually heard a funny story about...")
        await ctx.send("Your Honor,")
        await ctx.send("haven't these ridiculous bugs")
        await ctx.send("taken up enough")
        await ctx.send("of this court's valuable time?")
        await ctx.send("How much longer will we allow")
        await ctx.send("these absurd shenanigans to go on?")
        await ctx.send("They have presented no compelling")
        await ctx.send("evidence to support their charges")
        await ctx.send("against my clients,")
        await ctx.send("who run legitimate businesses.")
        await ctx.send("I move for a complete dismissal")
        await ctx.send("of this entire case!")
        await ctx.send("Mr. Flayman, I'm afraid I'm going")
        await ctx.send("to have to consider")
        await ctx.send("Mr. Montgomery's motion.")
        await ctx.send("But you can't! We have a terrific case.")
        await ctx.send("Where is your proof?")
        await ctx.send("Where is the evidence?")
        await ctx.send("Show me the smoking gun!")
        await ctx.send("Hold it, Your Honor!")
        await ctx.send("You want a smoking gun?")
        await ctx.send("Here is your smoking gun.")
        await ctx.send("What is that?")
        await ctx.send("It's a bee smoker!")
        await ctx.send("What, this?")
        await ctx.send("This harmless little contraption?")
        await ctx.send("This couldn't hurt a fly,")
        await ctx.send("let alone a bee.")
        await ctx.send("Look at what has happened")
        await ctx.send("to bees who have never been asked,")
        await ctx.send("Smoking or non?")
        await ctx.send("Is this what nature intended for us?")
        await ctx.send("To be forcibly addicted")
        await ctx.send("to smoke machines")
        await ctx.send("and man-made wooden slat work camps?")
        await ctx.send("Living out our lives as honey slaves")
        await ctx.send("to the white man?")
        await ctx.send("- What are we gonna do?")
        await ctx.send("- He's playing the species card.")
        await ctx.send("Ladies and gentlemen, please,")
        await ctx.send("free these bees!")
        await ctx.send("Free the bees! Free the bees!")
        await ctx.send("Free the bees!")
        await ctx.send("Free the bees! Free the bees!")
        await ctx.send("The court finds in favor of the bees!")
        await ctx.send("Vanessa, we won!")
        await ctx.send("I knew you could do it! High-five!")
        await ctx.send("Sorry.")
        await ctx.send("I'm OK! You know what this means?")
        await ctx.send("All the honey")
        await ctx.send("will finally belong to the bees.")
        await ctx.send("Now we won't have")
        await ctx.send("to work so hard all the time.")
        await ctx.send("This is an unholy perversion")
        await ctx.send("of the balance of nature, Benson.")
        await ctx.send("You'll regret this.")
        await ctx.send("Barry, how much honey is out there?")
        await ctx.send("All right. One at a time.")
        await ctx.send("Barry, who are you wearing?")
        await ctx.send("My sweater is Ralph Lauren,")
        await ctx.send("and I have no pants.")
        await ctx.send("- What if Montgomery's right?")
        await ctx.send("- What do you mean?")
        await ctx.send("We've been living the bee way")
        await ctx.send("a long time, 27 million years.")
        await ctx.send("Oongratulations on your victory.")
        await ctx.send("What will you demand as a settlement?")
        await ctx.send("First, we'll demand a complete shutdown")
        await ctx.send("of all bee work camps.")
        await ctx.send("Then we want back the honey")
        await ctx.send("that was ours to begin with,")
        await ctx.send("every last drop.")
        await ctx.send("We demand an end to the glorification")
        await ctx.send("of the bear as anything more")
        await ctx.send("than a filthy, smelly,")
        await ctx.send("bad-breath stink machine.")
        await ctx.send("We're all aware")
        await ctx.send("of what they do in the woods.")
        await ctx.send("Wait for my signal.")
        await ctx.send("Take him out.")
        await ctx.send("He'll have nauseous")
        await ctx.send("for a few hours, then he'll be fine.")
        await ctx.send("And we will no longer tolerate")
        await ctx.send("bee-negative nicknames...")
        await ctx.send("But it's just a prance-about stage name!")
        await ctx.send("...unnecessary inclusion of honey")
        await ctx.send("in bogus health products")
        await ctx.send("and la-dee-da human")
        await ctx.send("tea-time snack garnishments.")
        await ctx.send("Oan't breathe.")
        await ctx.send("Bring it in, boys!")
        await ctx.send("Hold it right there! Good.")
        await ctx.send("Tap it.")
        await ctx.send("Mr. Buzzwell, we just passed three cups,")
        await ctx.send("and there's gallons more coming!")
        await ctx.send("- I think we need to shut down!")
        await ctx.send("- Shut down? We've never shut down.")
        await ctx.send("Shut down honey production!")
        await ctx.send("Stop making honey!")
        await ctx.send("Turn your key, sir!")
        await ctx.send("What do we do now?")
        await ctx.send("Oannonball!")
        await ctx.send("We're shutting honey production!")
        await ctx.send("Mission abort.")
        await ctx.send("Aborting pollination and nectar detail.")
        await ctx.send("Returning to base.")
        await ctx.send("Adam, you wouldn't believe")
        await ctx.send("how much honey was out there.")
        await ctx.send("Oh, yeah?")
        await ctx.send("What's going on? Where is everybody?")
        await ctx.send("- Are they out celebrating?")
        await ctx.send("- They're home.")
        await ctx.send("They don't know what to do.")
        await ctx.send("Laying out, sleeping in.")
        await ctx.send("I heard your Uncle Oarl was on his way")
        await ctx.send("to San Antonio with a cricket.")
        await ctx.send("At least we got our honey back.")
        await ctx.send("Sometimes I think, so what if humans")
        await ctx.send("liked our honey? Who wouldn't?")
        await ctx.send("It's the greatest thing in the world!")
        await ctx.send("I was excited to be part of making it.")
        await ctx.send("This was my new desk. This was my")
        await ctx.send("new job. I wanted to do it really well.")
        await ctx.send("And now...")
        await ctx.send("Now I can't.")
        await ctx.send("I don't understand")
        await ctx.send("why they're not happy.")
        await ctx.send("I thought their lives would be better!")
        await ctx.send("They're doing nothing. It's amazing.")
        await ctx.send("Honey really changes people.")
        await ctx.send("You don't have any idea")
        await ctx.send("what's going on, do you?")
        await ctx.send("- What did you want to show me?")
        await ctx.send("- This.")
        await ctx.send("What happened here?")
        await ctx.send("That is not the half of it.")
        await ctx.send("Oh, no. Oh, my.")
        await ctx.send("They're all wilting.")
        await ctx.send("Doesn't look very good, does it?")
        await ctx.send("No.")
        await ctx.send("And whose fault do you think that is?")
        await ctx.send("You know, I'm gonna guess bees.")
        await ctx.send("Bees?")
        await ctx.send("Specifically, me.")
        await ctx.send("I didn't think bees not needing to make")
        await ctx.send("honey would affect all these things.")
        await ctx.send("It's notjust flowers.")
        await ctx.send("Fruits, vegetables, they all need bees.")
        await ctx.send("That's our whole SAT test right there.")
        await ctx.send("Take away produce, that affects")
        await ctx.send("the entire animal kingdom.")
        await ctx.send("And then, of course...")
        await ctx.send("The human species?")
        await ctx.send("So if there's no more pollination,")
        await ctx.send("it could all just go south here,")
        await ctx.send("couldn't it?")
        await ctx.send("I know this is also partly my fault.")
        await ctx.send("How about a suicide pact?")
        await ctx.send("How do we do it?")
        await ctx.send("- I'll sting you, you step on me.")
        await ctx.send("- Thatjust kills you twice.")
        await ctx.send("Right, right.")
        await ctx.send("Listen, Barry...")
        await ctx.send("sorry, but I gotta get going.")
        await ctx.send("I had to open my mouth and talk.")
        await ctx.send("Vanessa?")
        await ctx.send("Vanessa? Why are you leaving?")
        await ctx.send("Where are you going?")
        await ctx.send("To the final Tournament of Roses parade")
        await ctx.send("in Pasadena.")
        await ctx.send("They've moved it to this weekend")
        await ctx.send("because all the flowers are dying.")
        await ctx.send("It's the last chance")
        await ctx.send("I'll ever have to see it.")
        await ctx.send("Vanessa, I just wanna say I'm sorry.")
        await ctx.send("I never meant it to turn out like this.")
        await ctx.send("I know. Me neither.")
        await ctx.send("Tournament of Roses.")
        await ctx.send("Roses can't do sports.")
        await ctx.send("Wait a minute. Roses. Roses?")
        await ctx.send("Roses!")
        await ctx.send("Vanessa!")
        await ctx.send("Roses?!")
        await ctx.send("Barry?")
        await ctx.send("- Roses are flowers!")
        await ctx.send("- Yes, they are.")
        await ctx.send("Flowers, bees, pollen!")
        await ctx.send("I know.")
        await ctx.send("That's why this is the last parade.")
        await ctx.send("Maybe not.")
        await ctx.send("Oould you ask him to slow down?")
        await ctx.send("Oould you slow down?")
        await ctx.send("Barry!")
        await ctx.send("OK, I made a huge mistake.")
        await ctx.send("This is a total disaster, all my fault.")
        await ctx.send("Yes, it kind of is.")
        await ctx.send("I've ruined the planet.")
        await ctx.send("I wanted to help you")
        await ctx.send("with the flower shop.")
        await ctx.send("I've made it worse.")
        await ctx.send("Actually, it's completely closed down.")
        await ctx.send("I thought maybe you were remodeling.")
        await ctx.send("But I have another idea, and it's")
        await ctx.send("greater than my previous ideas combined.")
        await ctx.send("I don't want to hear it!")
        await ctx.send("All right, they have the roses,")
        await ctx.send("the roses have the pollen.")
        await ctx.send("I know every bee, plant")
        await ctx.send("and flower bud in this park.")
        await ctx.send("All we gotta do is get what they've got")
        await ctx.send("back here with what we've got.")
        await ctx.send("- Bees.")
        await ctx.send("- Park.")
        await ctx.send("- Pollen!")
        await ctx.send("- Flowers.")
        await ctx.send("- Repollination!")
        await ctx.send("- Across the nation!")
        await ctx.send("Tournament of Roses,")
        await ctx.send("Pasadena, Oalifornia.")
        await ctx.send("They've got nothing")
        await ctx.send("but flowers, floats and cotton candy.")
        await ctx.send("Security will be tight.")
        await ctx.send("I have an idea.")
        await ctx.send("Vanessa Bloome, FTD.")
        await ctx.send("Official floral business. It's real.")
        await ctx.send("Sorry, ma'am. Nice brooch.")
        await ctx.send("Thank you. It was a gift.")
        await ctx.send("Once inside,")
        await ctx.send("we just pick the right float.")
        await ctx.send("How about The Princess and the Pea?")
        await ctx.send("I could be the princess,")
        await ctx.send("and you could be the pea!")
        await ctx.send("Yes, I got it.")
        await ctx.send("- Where should I sit?")
        await ctx.send("- What are you?")
        await ctx.send("- I believe I'm the pea.")
        await ctx.send("- The pea?")
        await ctx.send("It goes under the mattresses.")
        await ctx.send("- Not in this fairy tale, sweetheart.")
        await ctx.send("- I'm getting the marshal.")
        await ctx.send("You do that!")
        await ctx.send("This whole parade is a fiasco!")
        await ctx.send("Let's see what this baby'll do.")
        await ctx.send("Hey, what are you doing?!")
        await ctx.send("Then all we do")
        await ctx.send("is blend in with traffic...")
        await ctx.send("...without arousing suspicion.")
        await ctx.send("Once at the airport,")
        await ctx.send("there's no stopping us.")
        await ctx.send("Stop! Security.")
        await ctx.send("- You and your insect pack your float?")
        await ctx.send("- Yes.")
        await ctx.send("Has it been")
        await ctx.send("in your possession the entire time?")
        await ctx.send("Would you remove your shoes?")
        await ctx.send("- Remove your stinger.")
        await ctx.send("- It's part of me.")
        await ctx.send("I know. Just having some fun.")
        await ctx.send("Enjoy your flight.")
        await ctx.send("Then if we're lucky, we'll have")
        await ctx.send("just enough pollen to do the job.")
        await ctx.send("Oan you believe how lucky we are? We")
        await ctx.send("have just enough pollen to do the job!")
        await ctx.send("I think this is gonna work.")
        await ctx.send("It's got to work.")
        await ctx.send("Attention, passengers,")
        await ctx.send("this is Oaptain Scott.")
        await ctx.send("We have a bit of bad weather")
        await ctx.send("in New York.")
        await ctx.send("It looks like we'll experience")
        await ctx.send("a couple hours delay.")
        await ctx.send("Barry, these are cut flowers")
        await ctx.send("with no water. They'll never make it.")
        await ctx.send("I gotta get up there")
        await ctx.send("and talk to them.")
        await ctx.send("Be careful.")
        await ctx.send("Oan I get help")
        await ctx.send("with the Sky Mall magazine?")
        await ctx.send("I'd like to order the talking")
        await ctx.send("inflatable nose and ear hair trimmer.")
        await ctx.send("Oaptain, I'm in a real situation.")
        await ctx.send("- What'd you say, Hal?")
        await ctx.send("- Nothing.")
        await ctx.send("Bee!")
        await ctx.send("Don't freak out! My entire species...")
        await ctx.send("What are you doing?")
        await ctx.send("- Wait a minute! I'm an attorney!")
        await ctx.send("- Who's an attorney?")
        await ctx.send("Don't move.")
        await ctx.send("Oh, Barry.")
        await ctx.send("Good afternoon, passengers.")
        await ctx.send("This is your captain.")
        await ctx.send("Would a Miss Vanessa Bloome in 24B")
        await ctx.send("please report to the cockpit?")
        await ctx.send("And please hurry!")
        await ctx.send("What happened here?")
        await ctx.send("There was a DustBuster,")
        await ctx.send("a toupee, a life raft exploded.")
        await ctx.send("One's bald, one's in a boat,")
        await ctx.send("they're both unconscious!")
        await ctx.send("- Is that another bee joke?")
        await ctx.send("- No!")
        await ctx.send("No one's flying the plane!")
        await ctx.send("This is JFK control tower, Flight 356.")
        await ctx.send("What's your status?")
        await ctx.send("This is Vanessa Bloome.")
        await ctx.send("I'm a florist from New York.")
        await ctx.send("Where's the pilot?")
        await ctx.send("He's unconscious,")
        await ctx.send("and so is the copilot.")
        await ctx.send("Not good. Does anyone onboard")
        await ctx.send("have flight experience?")
        await ctx.send("As a matter of fact, there is.")
        await ctx.send("- Who's that?")
        await ctx.send("- Barry Benson.")
        await ctx.send("From the honey trial?! Oh, great.")
        await ctx.send("Vanessa, this is nothing more")
        await ctx.send("than a big metal bee.")
        await ctx.send("It's got giant wings, huge engines.")
        await ctx.send("I can't fly a plane.")
        await ctx.send("- Why not? Isn't John Travolta a pilot?")
        await ctx.send("- Yes.")
        await ctx.send("How hard could it be?")
        await ctx.send("Wait, Barry!")
        await ctx.send("We're headed into some lightning.")
        await ctx.send("This is Bob Bumble. We have some")
        await ctx.send("late-breaking news from JFK Airport,")
        await ctx.send("where a suspenseful scene")
        await ctx.send("is developing.")
        await ctx.send("Barry Benson,")
        await ctx.send("fresh from his legal victory...")
        await ctx.send("That's Barry!")
        await ctx.send("...is attempting to land a plane,")
        await ctx.send("loaded with people, flowers")
        await ctx.send("and an incapacitated flight crew.")
        await ctx.send("Flowers?!")
        await ctx.send("We have a storm in the area")
        await ctx.send("and two individuals at the controls")
        await ctx.send("with absolutely no flight experience.")
        await ctx.send("Just a minute.")
        await ctx.send("There's a bee on that plane.")
        await ctx.send("I'm quite familiar with Mr. Benson")
        await ctx.send("and his no-account compadres.")
        await ctx.send("They've done enough damage.")
        await ctx.send("But isn't he your only hope?")
        await ctx.send("Technically, a bee")
        await ctx.send("shouldn't be able to fly at all.")
        await ctx.send("Their wings are too small...")
        await ctx.send("Haven't we heard this a million times?")
        await ctx.send("The surface area of the wings")
        await ctx.send("and body mass make no sense.")
        await ctx.send("- Get this on the air!")
        await ctx.send("- Got it.")
        await ctx.send("- Stand by.")
        await ctx.send("- We're going live.")
        await ctx.send("The way we work may be a mystery to you.")
        await ctx.send("Making honey takes a lot of bees")
        await ctx.send("doing a lot of small jobs.")
        await ctx.send("But let me tell you about a small job.")
        await ctx.send("If you do it well,")
        await ctx.send("it makes a big difference.")
        await ctx.send("More than we realized.")
        await ctx.send("To us, to everyone.")
        await ctx.send("That's why I want to get bees")
        await ctx.send("back to working together.")
        await ctx.send("That's the bee way!")
        await ctx.send("We're not made of Jell-O.")
        await ctx.send("We get behind a fellow.")
        await ctx.send("- Black and yellow!")
        await ctx.send("- Hello!")
        await ctx.send("Left, right, down, hover.")
        await ctx.send("- Hover?")
        await ctx.send("- Forget hover.")
        await ctx.send("This isn't so hard.")
        await ctx.send("Beep-beep! Beep-beep!")
        await ctx.send("Barry, what happened?!")
        await ctx.send("Wait, I think we were")
        await ctx.send("on autopilot the whole time.")
        await ctx.send("- That may have been helping me.")
        await ctx.send("- And now we're not!")
        await ctx.send("So it turns out I cannot fly a plane.")
        await ctx.send("All of you, let's get")
        await ctx.send("behind this fellow! Move it out!")
        await ctx.send("Move out!")
        await ctx.send("Our only chance is if I do what I'd do,")
        await ctx.send("you copy me with the wings of the plane!")
        await ctx.send("Don't have to yell.")
        await ctx.send("I'm not yelling!")
        await ctx.send("We're in a lot of trouble.")
        await ctx.send("It's very hard to concentrate")
        await ctx.send("with that panicky tone in your voice!")
        await ctx.send("It's not a tone. I'm panicking!")
        await ctx.send("I can't do this!")
        await ctx.send("Vanessa, pull yourself together.")
        await ctx.send("You have to snap out of it!")
        await ctx.send("You snap out of it.")
        await ctx.send("You snap out of it.")
        await ctx.send("- You snap out of it!")
        await ctx.send("- You snap out of it!")
        await ctx.send("- You snap out of it!")
        await ctx.send("- You snap out of it!")
        await ctx.send("- You snap out of it!")
        await ctx.send("- You snap out of it!")
        await ctx.send("- Hold it!")
        await ctx.send("- Why? Oome on, it's my turn.")
        await ctx.send("How is the plane flying?")
        await ctx.send("I don't know.")
        await ctx.send("Hello?")
        await ctx.send("Benson, got any flowers")
        await ctx.send("for a happy occasion in there?")
        await ctx.send("The Pollen Jocks!")
        await ctx.send("They do get behind a fellow.")
        await ctx.send("- Black and yellow.")
        await ctx.send("- Hello.")
        await ctx.send("All right, let's drop this tin can")
        await ctx.send("on the blacktop.")
        await ctx.send("Where? I can't see anything. Oan you?")
        await ctx.send("No, nothing. It's all cloudy.")
        await ctx.send("Oome on. You got to think bee, Barry.")
        await ctx.send("- Thinking bee.")
        await ctx.send("- Thinking bee.")
        await ctx.send("Thinking bee!")
        await ctx.send("Thinking bee! Thinking bee!")
        await ctx.send("Wait a minute.")
        await ctx.send("I think I'm feeling something.")
        await ctx.send("- What?")
        await ctx.send("- I don't know. It's strong, pulling me.")
        await ctx.send("Like a 27-million-year-old instinct.")
        await ctx.send("Bring the nose down.")
        await ctx.send("Thinking bee!")
        await ctx.send("Thinking bee! Thinking bee!")
        await ctx.send("- What in the world is on the tarmac?")
        await ctx.send("- Get some lights on that!")
        await ctx.send("Thinking bee!")
        await ctx.send("Thinking bee! Thinking bee!")
        await ctx.send("- Vanessa, aim for the flower.")
        await ctx.send("- OK.")
        await ctx.send("Out the engines. We're going in")
        await ctx.send("on bee power. Ready, boys?")
        await ctx.send("Affirmative!")
        await ctx.send("Good. Good. Easy, now. That's it.")
        await ctx.send("Land on that flower!")
        await ctx.send("Ready? Full reverse!")
        await ctx.send("Spin it around!")
        await ctx.send("- Not that flower! The other one!")
        await ctx.send("- Which one?")
        await ctx.send("- That flower.")
        await ctx.send("- I'm aiming at the flower!")
        await ctx.send("That's a fat guy in a flowered shirt.")
        await ctx.send("I mean the giant pulsating flower")
        await ctx.send("made of millions of bees!")
        await ctx.send("Pull forward. Nose down. Tail up.")
        await ctx.send("Rotate around it.")
        await ctx.send("- This is insane, Barry!")
        await ctx.send("- This's the only way I know how to fly.")
        await ctx.send("Am I koo-koo-kachoo, or is this plane")
        await ctx.send("flying in an insect-like pattern?")
        await ctx.send("Get your nose in there. Don't be afraid.")
        await ctx.send("Smell it. Full reverse!")
        await ctx.send("Just drop it. Be a part of it.")
        await ctx.send("Aim for the center!")
        await ctx.send("Now drop it in! Drop it in, woman!")
        await ctx.send("Oome on, already.")
        await ctx.send("Barry, we did it!")
        await ctx.send("You taught me how to fly!")
        await ctx.send("- Yes. No high-five!")
        await ctx.send("- Right.")
        await ctx.send("Barry, it worked!")
        await ctx.send("Did you see the giant flower?")
        await ctx.send("What giant flower? Where? Of course")
        await ctx.send("I saw the flower! That was genius!")
        await ctx.send("- Thank you.")
        await ctx.send("- But we're not done yet.")
        await ctx.send("Listen, everyone!")
        await ctx.send("This runway is covered")
        await ctx.send("with the last pollen")
        await ctx.send("from the last flowers")
        await ctx.send("available anywhere on Earth.")
        await ctx.send("That means this is our last chance.")
        await ctx.send("We're the only ones who make honey,")
        await ctx.send("pollinate flowers and dress like this.")
        await ctx.send("If we're gonna survive as a species,")
        await ctx.send("this is our moment! What do you say?")
        await ctx.send("Are we going to be bees, orjust")
        await ctx.send("Museum of Natural History keychains?")
        await ctx.send("We're bees!")
        await ctx.send("Keychain!")
        await ctx.send("Then follow me! Except Keychain.")
        await ctx.send("Hold on, Barry. Here.")
        await ctx.send("You've earned this.")
        await ctx.send("Yeah!")
        await ctx.send("I'm a Pollen Jock! And it's a perfect")
        await ctx.send("fit. All I gotta do are the sleeves.")
        await ctx.send("Oh, yeah.")
        await ctx.send("That's our Barry.")
        await ctx.send("Mom! The bees are back!")
        await ctx.send("If anybody needs")
        await ctx.send("to make a call, now's the time.")
        await ctx.send("I got a feeling we'll be")
        await ctx.send("working late tonight!")
        await ctx.send("Here's your change. Have a great")
        await ctx.send("afternoon! Oan I help who's next?")
        await ctx.send("Would you like some honey with that?")
        await ctx.send("It is bee-approved. Don't forget these.")
        await ctx.send("Milk, cream, cheese, it's all me.")
        await ctx.send("And I don't see a nickel!")
        await ctx.send("Sometimes I just feel")
        await ctx.send("like a piece of meat!")
        await ctx.send("I had no idea.")
        await ctx.send("Barry, I'm sorry.")
        await ctx.send("Have you got a moment?")
        await ctx.send("Would you excuse me?")
        await ctx.send("My mosquito associate will help you.")
        await ctx.send("Sorry I'm late.")
        await ctx.send("He's a lawyer too?")
        await ctx.send("I was already a blood-sucking parasite.")
        await ctx.send("All I needed was a briefcase.")
        await ctx.send("Have a great afternoon!")
        await ctx.send("Barry, I just got this huge tulip order,")
        await ctx.send("and I can't get them anywhere.")
        await ctx.send("No problem, Vannie.")
        await ctx.send("Just leave it to me.")
        await ctx.send("You're a lifesaver, Barry.")
        await ctx.send("Oan I help who's next?")
        await ctx.send("All right, scramble, jocks!")
        await ctx.send("It's time to fly.")
        await ctx.send("Thank you, Barry!")
        await ctx.send("That bee is living my life!")
        await ctx.send("Let it go, Kenny.")
        await ctx.send("- When will this nightmare end?!")
        await ctx.send("- Let it all go.")
        await ctx.send("- Beautiful day to fly.")
        await ctx.send("- Sure is.")
        await ctx.send("Between you and me,")
        await ctx.send("I was dying to get out of that office.")
        await ctx.send("You have got")
        await ctx.send("to start thinking bee, my friend.")
        await ctx.send("- Thinking bee!")
        await ctx.send("- Me?")
        await ctx.send("Hold it. Let's just stop")
        await ctx.send("for a second. Hold it.")
        await ctx.send("I'm sorry. I'm sorry, everyone.")
        await ctx.send("Oan we stop here?")
        await ctx.send("I'm not making a major life decision")
        await ctx.send("during a production number!")
        await ctx.send("All right. Take ten, everybody.")
        await ctx.send("Wrap it up, guys.")
        await ctx.send("I had virtually no rehearsal for that.")

@Crystal.command()
async def creeper(ctx):
    await ctx.message.delete()
    await ctx.send('https://cdn.discordapp.com/attachments/788185828559290418/835122311035879444/Creeper.webm')

@Crystal.command()
async def animate(ctx, *, text):
    await ctx.message.delete()
    try:
        message = f'{text[0]}'
        msg = await ctx.send(message)
        for c in text[1:]:
            message += c
            await msg.edit(content=message)
            await asyncio.sleep(0.5)
    except Exception:
        return

@Crystal.command()
async def strike(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f'~~{text}~~')

@Crystal.command()
async def spoil(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f'||{text}||')
        
@Crystal.command()
async def underline(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f'__{text}__')
        
@Crystal.command()
async def blockquote(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f'>>> {text} ')
        
@Crystal.command()
async def italic(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f'*{text}*')

@Crystal.command()
async def lspoil(ctx, *, text):
    await ctx.message.delete()
    message = ''
    for l in text:
        message += f'||{l}||'
    await ctx.send(message)
        
@Crystal.command()
async def lower(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(text.lower())

@Crystal.command()
async def calculator(ctx):
    await ctx.message.delete()
    os.system('calc')
        
@Crystal.command()
async def folder(ctx):
    await ctx.message.delete()
    os.system(f'explorer.exe {os.getcwd()}')
        
@Crystal.command()
async def winexplorer(ctx):
    await ctx.message.delete()
    os.system('explorer')

@Crystal.command()
async def noob(ctx):
    await ctx.message.delete()
    message1 = '''What the fuck did you just fucking say about my gear, you little n00b? I’ll have you know I am a lvl 90 Undead Arcane Mage, and I’ve won so many PVP matches, and I have done raids on every 10 man heroic dungeon. I also have a fuckton of macros and I have a GS of 10K. You are nothing to me but just a lvl 12 gnome hunter. I will pwn the fuck out of you with Arcane Missiles the likes of which has never been seen before on Azeroth AND Outland, mark my fucking words. You think you can get away with saying that shit to me over raid? Think again, fucker. As we speak I am contacting my guild of mages and shamans across The Eastern Kingdoms and your character is being targeted right now so you better prepare for the ownage, n00b. The Arcane Barrage that wipes out the pathetic little thing you call your character. You’re fucking pwn'd, n00b.'''
    message2 = '''I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my secondary talent tree. Not only am I extensively trained in Arcane magic, but I have access to the entire arsenal of Fire magic and I will use it to its full extent to wipe your miserable neckbeard off the face of Azeroth, you little faggot. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re getting debuffed, you goddamnn00b. I will shit Dragon's Breath all over you and you will burn in it. You’re fucking pwn'd, faggot.'''
    await ctx.send(message1)
    await ctx.send(message2)

@Crystal.command()
async def spamtillyouredead(ctx):
    await ctx.message.delete()
    lyrics = '''I see ya
Spam, spam, till your dead, dead dead dead dead
Spam, spam, till your dead dead dead dead dead
Spam spam till your dead dead dead dead dead
Spam spam till your dead dead dead dead dead
*Sonic ring noise*
Spam
(Dead)
S-S-Spam
(Dead)
Spam, Spam, Spam
(Dead)
Spam
(Dead)
Spam
(Dead)
Spam Spam Spam
Hey!
Heads will roll
Heads will roll
Heads will roll
I'm fine
Till your dead dead dead dead dead
Spam Spam till your dead dead dead dead
Spam Spam till your dead dead dead dead dead
Spam spam till your dead
Hey, Hey!
What?
Dead dead dead dead dead
Spam spam till your dead dead dead dead dead
Spam spam till your dead dead dead dead'''
    text = lyrics.split('\n')
    for line in text:
        await ctx.send(line)

@Crystal.command(name="fakenitro")
async def fakenitro(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Successfully Generated Nitro", description="**Gift Link**: http://alturl.com/p749b", color=0x9F00FB)
    embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
    embed.set_footer(text="Discord Administration Tool")
    text = await ctx.send(embed=embed)
    time.sleep(30)
    await text.delete()

@Crystal.command(name="fakenitro2")
async def fakenitro2(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Successfully Generated Nitro", description="**Gift Link**: http://alturl.com/o4grw", color=0x9F00FB)
    embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
    embed.set_footer(text="Discord Administration Tool")
    text = await ctx.send(embed=embed)
    time.sleep(30)
    await text.delete()

@Crystal.command()
async def spurge(ctx, amount: int):
    await ctx.message.delete()
    try:
        await ctx.channel.purge(limit=amount, before=ctx.message, check=lambda e: e.author == Crystal.user)
    except Exception:
        pass

@Crystal.command()
async def bulkreact(ctx, amount: int, emoji: str):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount + 1):
        try:
            await message.add_reaction(emoji)
        except:
            pass

@Crystal.command()
async def count(ctx, _from: int, _to: int):
    await ctx.message.delete()
    try:
        first = _from
        msg = await ctx.send(first)
        for i in range((first + 1), (_to + 1)):
            await msg.edit(content=i)
            await asyncio.sleep(0.5)
    except Exception:
        pass
            
@Crystal.command()
async def countdown(ctx, _from: int, _to: int):
    await ctx.message.delete()
    try:
        first = _from
        msg = await ctx.send(first)
        for i in range((first - 1), (_to - 1), -1):
            await msg.edit(content=i)
            await asyncio.sleep(0.5)
    except Exception:
        pass

@Crystal.command(aliases=["guildinfo"])
async def serverinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=f"Server Info of {ctx.guild.name}:",
                        description=f"{len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                        timestamp=datetime.datetime.utcnow(), color=0x0000)
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)

@Crystal.command(name="stoptalking")
async def stoptalking(ctx):
    await ctx.message.delete()
    await ctx.channel.send("https://cdn.discordapp.com/attachments/781140293410881546/802967926881386496/yes.mov")

@Crystal.command(name="rx7rr")
async def rx7rr(ctx):
    await ctx.message.delete()
    await ctx.channel.send("https://cdn.discordapp.com/attachments/769632571092762684/835222749994811451/Rx7-2step.mp4")

@Crystal.command(name="flip", aliases=["coinflip"])
async def coin_flip(ctx):
    """ Toss a coin """
    result = random.randint(0, 1)

    msg = "http://researchmaniacs.com/Random/Images/Quarter-Tails.png" if result else "http://researchmaniacs.com/Random/Images/Quarter-Heads.png"
    await ctx.message.edit(content=msg)

@Crystal.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in Crystal.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)

@Crystal.command(name="bread")
async def bread(ctx):
    await ctx.message.delete()
    await ctx.channel.send("https://cdn.discordapp.com/attachments/769632571092762684/835265002406936626/bread.mp4")

@Crystal.command(name="sus")
async def sus(ctx):
    await ctx.message.delete()
    await ctx.channel.send("https://cdn.discordapp.com/attachments/781140293410881546/835269177065340948/Among_Us_Eurobeat_Remix.mp4")

@Crystal.command()
async def stream(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await Crystal.change_presence(activity=stream)    

@Crystal.command()
async def game(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Crystal.change_presence(activity=game)

@Crystal.command()
async def listening(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await Crystal.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))

@Crystal.command()
async def watching(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await Crystal.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))

@Crystal.command()
async def uptime(ctx): # b'\xfc'
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')

@Crystal.command()
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Crystal.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@Crystal.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in Crystal.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

@Crystal.command(aliases=['markasread', 'ack'])
async def read(ctx): # b'\xfc'
    await ctx.message.delete()
    for guild in Crystal.guilds:
        await guild.ack()

@Crystal.command()
async def reverse(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)

@Crystal.command()
async def shrug(ctx): # b'\xfc'
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)

@Crystal.command()
async def lenny(ctx): # b'\xfc'
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)

@Crystal.command()
async def tableflip(ctx): # b'\xfc'
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)

@Crystal.command()
async def unflip(ctx): # b'\xfc'
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

@Crystal.command()
async def bold(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('**'+message+'**')

@Crystal.command()
async def secret(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('||'+message+'||')

@Crystal.command()
async def topic(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)

@Crystal.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text
    em = discord.Embed(description=f'{qa}\n{qor}\n{qb}')
    await ctx.send(embed=em)

@Crystal.command()
async def hastebin(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

@Crystal.command()
async def ascii(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@Crystal.command()
async def abc(ctx): # b'\xfc'
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

@Crystal.command(aliases=['bitcoin'])
async def btc(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    text=await ctx.send(embed=em)
    time.sleep(20)
    await text.delete()

@Crystal.command(aliases=['ethereum'])
async def eth(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    text=await ctx.send(embed=em)
    time.sleep(20)
    await text.delete()

@Crystal.command()
async def tinyurl(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed()
    em.add_field(name='Shortened link', value=r, inline=False )
    await ctx.send(embed=em)

@Crystal.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role): # b'\xfc'
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(10)
        except:
            break

@Crystal.command(name='8ball')
async def _ball(ctx, *, question): # b'\xfc'
    await ctx.message.delete()
    responses = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
      'Maybe',
      'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

@Crystal.command(aliases=['slots', 'bet'])
async def slot(ctx): # b'\xfc'
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))

@Crystal.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx, channelid): # b'\xfc'
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1 
            channel = Crystal.get_channel(int(channelid))
            await channel.send('!d bump')           
            print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent'+Fore.RESET)
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Crystal.command()
async def tts(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))

@Crystal.command()
async def upper(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message.upper()
    await ctx.send(message)

@Crystal.command(aliases=['guildpfp'])
async def guildicon(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)

@Crystal.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@Crystal.command()
async def copy(ctx): # b'\xfc'
    await ctx.message.delete()
    await Crystal.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Crystal.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:                
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@Crystal.command()
async def destroy(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="https://Crystal.wtf",
            reason="https://Crystal-selfbot.github.io",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(250):
        await ctx.guild.create_text_channel(name=RandString())
    for _i in range(250):
        await ctx.guild.create_role(name=RandString(), color=RandomColor())

@Crystal.command()
async def dmall(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)    
            await user.send(message)
        except:
            pass

@Crystal.command()
async def massban(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@Crystal.command()
async def masskick(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    

@Crystal.command()
async def massrole(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return    

@Crystal.command()
async def masschannel(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=RandString())
        except:
            return

@Crystal.command()
async def delchannels(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@Crystal.command() 
async def delroles(ctx): # b'\xfc'
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@Crystal.command()
async def massunban(ctx): # b'\xfc'
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@Crystal.command()
async def spam(ctx, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

@Crystal.command()
async def dm(ctx, user : discord.Member, *, message): # b'\xfc'
    await ctx.message.delete()
    user = Crystal.get_user(user.id)
    if ctx.author.id == Crystal.user.id:
        return
    else:
        try:
            await user.send(message) 
        except:
            pass

@Crystal.command()
async def whois(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    em = discord.Embed(description=user.mention)
    em.set_author(name=str(user), icon_url=user.avatar_url)
    em.set_thumbnail(url=user.avatar_url)
    em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    em.add_field(name="Join position", value=str(members.index(user)+1))
    em.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    em.add_field(name="Guild permissions", value=perm_string, inline=False)
    em.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=em)

@Crystal.command()
async def minesweeper(ctx, size: int = 5): # b'\xfc'
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)

@Crystal.command()
async def combine(ctx, name1, name2): # b'\xfc'
    await ctx.message.delete()
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = "".join([name1letters, name2letters])
    emb = (discord.Embed(description=f"{ship}"))
    emb.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=emb)       

@Crystal.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')

@Crystal.command(aliases=['dvwl'])
async def devowel(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    dvl = text.replace('a', '').replace('A', '').replace('e', '')\
            .replace('E', '').replace('i', '').replace('I', '')\
            .replace('o', '').replace('O', '').replace('u', '').replace('U', '')
    await ctx.send(dvl)

@Crystal.command()
async def blank(ctx): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:  
        password = config.get('password')
        with open('Images/Avatars/Transparent.png', 'rb') as f:
          try:      
             await Crystal.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
          except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Crystal.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
          r = requests.get(user.avatar_url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
              await Crystal.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Crystal.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
async def _set_pfp(ctx, *, url): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
          r = requests.get(url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png'   ).convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await Crystal.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Crystal.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x0000)
    await ctx.send(embed=em)

@Crystal.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house): # b'\xfc'
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }    
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Crystal.command(aliases=['tokenfucker', 'disable', 'crash']) 
async def tokenfuck(ctx, _token): # b'\xfc' 
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "Crystal Selfbot",
        'region': "europe"
    } 
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
            else:
                break   

@Crystal.command()
async def masslogin(ctx, choice = None): # b'\xfc'
    await ctx.message.delete()
    _masslogin(choice)

@Crystal.command()
async def masscon(ctx, _type, amount: int, *, name=None): # b'\xfc'
    await ctx.message.delete()
    payload = {
        'name': name,
        'visibility': 1 
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json', 
    }
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        print(f'Avaliable connections: {avaliable}')
    for _i in range(amount):
        try:
            ID = random.randint(10000000, 90000000)
            time.sleep(5) 
            r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
            if r.status_code == 200:
                print(f"[{Fore.GREEN}+{Fore.RESET}] New connection added!")
            else:
                print(f"[{Fore.RED}-{Fore.RESET}] Couldnt add connection!");break
        except (Exception, ValueError) as e:
            print(e);break
    print(f"[{Fore.GREEN}+{Fore.RESET}] Finished adding connections!")

@Crystal.command(aliases=['fakeconnection', 'spoofconnection'])
async def fakenet(ctx, _type, *, name = None): # b'\xfc'
    await ctx.message.delete()
    ID  = random.randrange(10000000, 90000000)
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    payload = {
        'name': name,
        'visibility': 1
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json', 
    }
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after = 3)
    r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
    if r.status_code == 200:            
        await ctx.send(f"Added connection: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after = 3)
    else:
        await ctx.send('Some error has happened with the endpoint', delete_after = 3)

#@Crystal.command()
#async def clear(ctx): # b'\xfc'
#    await ctx.message.delete()
#    await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')

@Crystal.command()
async def genname(ctx): # b'\xfc'
    await ctx.message.delete()
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))

@Crystal.command()
async def login(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }   
            """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("{_token}")')    

@Crystal.command()
async def botlogin(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
    function login(token) {
      ((i) => {
        window.webpackJsonp.push([  
          [i], {
            [i]: (n, b, d) => {
              let dispatcher;
              for (let key in d.c) {
                if (d.c[key].exports) {
                  const module = d.c[key].exports.default || d.c[key].exports;
                  if (typeof(module) === 'object') {
                    if ('setToken' in module) {
                      module.setToken(token);
                      module.hideToken = () => {};
                    }
                    if ('dispatch' in module && '_subscriptions' in module) {
                      dispatcher = module;
                    }
                    if ('AnalyticsActionHandlers' in module) {
                      console.log('AnalyticsActionHandlers', module);
                      module.AnalyticsActionHandlers.handleTrack = (track) => {};
                    }
                  } else if (typeof(module) === 'function' && 'prototype' in module) {
                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);
                    if ('_discoveryFailed' in descriptors) {
                      const connect = module.prototype._connect;
                      module.prototype._connect = function(url) {
                        console.log('connect', url);
                        const oldHandleIdentify = this.handleIdentify;
                        this.handleIdentify = () => {
                          const identifyData = oldHandleIdentify();
                          identifyData.token = identifyData.token.split(' ').pop();
                          return identifyData;
                        };
                        const oldHandleDispatch = this._handleDispatch;
                        this._handleDispatch = function(data, type) {
                          if (type === 'READY') {
                            console.log(data);
                            data.user.bot = false;
                            data.user.email = 'Crystal-Was-Here@Fuckyou.com';
                            data.analytics_tokens = [];
                            data.connected_accounts = [];
                            data.consents = [];
                            data.experiments = [];
                            data.guild_experiments = [];
                            data.relationships = [];
                            data.user_guild_settings = [];
                          }
                          return oldHandleDispatch.call(this, data, type);
                        }
                        return connect.call(this, url);
                      };
                    }
                  }
                }
              }
              console.log(dispatcher);
              if (dispatcher) {
                dispatcher.dispatch({
                  type: 'LOGIN_SUCCESS',
                  token
                });
              }
            },
          },
          [
            [i],
          ],
        ]);
      })(Math.random());
    }
    """ 
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("Bot {_token}")')

@Crystal.command()
async def address(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    addy = ' '.join(text)
    address_array = []
    i = 0
    while i < 10:
        address_array.append(GenAddress(addy))
        i+=1
    final_str = "\n".join(address_array)
    em = discord.Embed(description=final_str)
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(final_str)    

@Crystal.command()
async def weather(ctx, *, city): # b'\xfc'
    await ctx.message.delete()
    if weather_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Weather API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}')
            r = req.json()
            temperature = round(float(r["main"]["temp"]) - 273.15, 1)
            lowest = round(float(r["main"]["temp_min"]) - 273.15, 1)
            highest = round(float(r["main"]["temp_max"]) - 273.15, 1)
            weather = r["weather"][0]["main"]
            humidity = round(float(r["main"]["humidity"]), 1)
            wind_speed = round(float(r["wind"]["speed"]), 1)
            em = discord.Embed(description=f'''
            Temperature: `{temperature}`
            Lowest: `{lowest}`
            Highest: `{highest}`
            Weather: `{weather}`
            Humidity: `{humidity}`
            Wind Speed: `{wind_speed}`
            ''')
            em.add_field(name='City', value=city.capitalize())
            em.set_thumbnail(url='https://ak0.picdn.net/shutterstock/videos/1019313310/thumb/1.jpg')
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(f'''
                Temperature: {temperature}
                Lowest: {lowest}
                Highest: {highest}
                Weather: {weather}
                Humidity: {humidity}
                Wind Speed: {wind_speed}
                City: {city.capitalize()}
                ''')    
        except KeyError:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{city} Is not a real city"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Crystal.command(aliases=['shorteen'])
async def bitly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if bitly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Bitly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}') as req:
                    r = await req.read()
                    r = json.loads(r) 
            new = r['data']['url']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            await ctx.send(embed=em)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Crystal.command()
async def cuttly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if cuttly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cutt.ly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'https://cutt.ly/api/api.php?key={cuttly_key}&short={link}')
            r = req.json()
            new = r['url']['shortLink']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(new)    
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Crystal.command() 
async def cat(ctx): # b'\xfc'
    await ctx.message.delete()
    if cat_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cat API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f"https://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}")
            r = req.json()
            em = discord.Embed()
            em.set_image(url=str(r[0]["url"]))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r[0]["url"]))
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Crystal.command()
async def dog(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))    

@Crystal.command()
async def fox(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Random fox image", color=16202876)
    em.set_image(url=r["image"])
    try:
        text = await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])   

@Crystal.command()
async def encode(ctx, string): # b'\xfc'
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff) 

@Crystal.command()
async def decode(ctx, string): # b'\xfc'+
    await ctx.message.delete()  
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)

@Crystal.command(name='ebay-view', aliases=['ebay-view-bot', 'ebayviewbot', 'ebayview'])
async def _ebay_view(ctx, url, views: int): # b'\xfc'
    await ctx.message.delete()
    start_time = datetime.datetime.now()
    def EbayViewer(url, views):
        headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }        
        for _i in range(views):
            requests.get(url, headers=headers)
    EbayViewer(url, views)
    elapsed_time = datetime.datetime.now() - start_time
    em = discord.Embed(title='Ebay View Bot')
    em.add_field(name='Views sent', value=views, inline=False)
    em.add_field(name='Elapsed time', value=elapsed_time, inline=False)
    await ctx.send(embed=em)

@Crystal.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

@Crystal.command()
async def pingweb(ctx, website = None): # b'\xfc'
    await ctx.message.delete()
    if website is None: 
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        if r == 404:
            await ctx.send(f'Site is down, responded with a status code of {r}', delete_after=3)
        else:
            await ctx.send(f'Site is up, responded with a status code of {r}', delete_after=3)       

@Crystal.command()
async def tweet(ctx, username: str, *, message: str): # b'\xfc'
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.set_image(url=res["message"])
            await ctx.send(embed=em)

@Crystal.command()
async def revav(ctx, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Crystal.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}"))      

@Crystal.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)

@Crystal.command()
async def massping(ctx):
    await ctx.message.delete()
    try:
        members = ctx.channel.members
            
        await ctx.send(" ".join([member.mention for member in members[:40]]))
    except Exception:
        pass
        
@Crystal.command()
async def massgping(ctx):
    await ctx.message.delete()
    try:
        members = sctx.channel.members
            
        le_msg = await ctx.send(" ".join([member.mention for member in members[:40]]))
        await le_msg.delete()
    except Exception:
        pass

@Crystal.command()
async def cloneserver(ctx, server_id: int=None):
        await ctx.message.delete()
        
        if server_id is None:
            server = ctx.guild
        else: 
            server = discord.utils.get(ctx.bot.guilds, id=server_id)
        channels = server.channels
        roles = server.roles
        try:
            async with httpx.AsyncClient() as client:
                originguild = ctx.guild
                result = await client.post('https://canary.discordapp.com/api/v8/guilds', json={'name': f'{originguild.name} clone', 'guild_template_code': '2TffvPucqHkN'}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                cloneserverid = result.json()['id']
        except Exception:
            pass
        
        defaultchannels = requests.get(f'https://canary.discordapp.com/api/v8/guilds/{cloneserverid}/channels', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}).json()
        
        for defaultchannel in defaultchannels:
            try:
                defaultchannel_id = defaultchannel['id']
                requests.delete(f'https://canary.discordapp.com/api/v8/channels/{defaultchannel_id}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
            except Exception:
                pass
        
        for channel in channels:
            try:
                if channel.type == discord.ChannelType.category:
                    category = requests.post(f'https://canary.discordapp.com/api/v8/guilds/{cloneserverid}/channels', json={'name': channel.name, 'permission_overwrites': [], 'type': 4}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                    categoryid = category.json()['id']
                    subchannels = channel.channels
                    for subchannel in subchannels:
                        if subchannel.type == discord.ChannelType.text:
                            requests.post(f'https://canary.discordapp.com/api/v8/guilds/{cloneserverid}/channels', json={'name': subchannel.name, 'permission_overwrites': [], 'type': 0, 'parent_id': f'{categoryid}'}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                        elif subchannel.type == discord.ChannelType.voice:
                            requests.post(f'https://canary.discordapp.com/api/v8/guilds/{cloneserverid}/channels', json={'name': subchannel.name, 'permission_overwrites': [], 'type': 2, 'parent_id': f'{categoryid}'}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                
                
                if channel.type == discord.ChannelType.text and channel.category_id == None:
                    requests.post(f'https://canary.discordapp.com/api/v8/guilds/{cloneserverid}/channels', json={'name': channel.name, 'permission_overwrites': [], 'type': 0}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                elif channel.type == discord.ChannelType.voice and channel.category_id == None:
                    requests.post(f'https://canary.discordapp.com/api/v8/guilds/{cloneserverid}/channels', json={'name': channel.name, 'permission_overwrites': [], 'type': 2}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
            except Exception:
                pass
            
        for role in reversed(roles):
            try:
                if role.name != '@everyone':
                    role_color = int(f"{role.color}".replace("#", "0x"), 0)
                    requests.post(f'https://canary.discordapp.com/api/v8/guilds/{cloneserverid}/roles', json={'name': role.name, 'color': role_color}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
            except Exception:
                pass
            
@Crystal.command()
async def cloneservertoserver(ctx, old_server_id: int, server_id: int=None):
        await ctx.message.delete()
        
        if server_id is None:
            server = ctx.guild
        else: 
            server = discord.utils.get(ctx.bot.guilds, id=server_id)
        channels = server.channels
        roles = server.roles
        
        cloneserverid = old_server_id
        
        defaultchannels = requests.get(f'https://canary.discordapp.com/api/v8/guilds/{cloneserverid}/channels', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}).json()
        
        for defaultchannel in defaultchannels:
            try:
                defaultchannel_id = defaultchannel['id']
                requests.delete(f'https://canary.discordapp.com/api/v8/channels/{defaultchannel_id}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
            except Exception:
                pass
        
        for channel in channels:
            try:
                if channel.type == discord.ChannelType.category:
                    category = requests.post(f'https://canary.discordapp.com/api/v8/guilds/{cloneserverid}/channels', json={'name': channel.name, 'permission_overwrites': [], 'type': 4}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                    categoryid = category.json()['id']
                    subchannels = channel.channels
                    for subchannel in subchannels:
                        if subchannel.type == discord.ChannelType.text:
                            requests.post(f'https://canary.discordapp.com/api/v8/guilds/{cloneserverid}/channels', json={'name': subchannel.name, 'permission_overwrites': [], 'type': 0, 'parent_id': f'{categoryid}'}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                        elif subchannel.type == discord.ChannelType.voice:
                            requests.post(f'https://canary.discordapp.com/api/v8/guilds/{cloneserverid}/channels', json={'name': subchannel.name, 'permission_overwrites': [], 'type': 2, 'parent_id': f'{categoryid}'}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                
                
                if channel.type == discord.ChannelType.text and channel.category_id == None:
                    requests.post(f'https://canary.discordapp.com/api/v8/guilds/{cloneserverid}/channels', json={'name': channel.name, 'permission_overwrites': [], 'type': 0}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                elif channel.type == discord.ChannelType.voice and channel.category_id == None:
                    requests.post(f'https://canary.discordapp.com/api/v8/guilds/{cloneserverid}/channels', json={'name': channel.name, 'permission_overwrites': [], 'type': 2}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
            except Exception:
                pass
            
        for role in reversed(roles):
            try:
                if role.name != '@everyone':
                    role_color = int(f"{role.color}".replace("#", "0x"), 0)
                    requests.post(f'https://canary.discordapp.com/api/v8/guilds/{cloneserverid}/roles', json={'name': role.name, 'color': role_color}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
            except Exception:
                pass

@Crystal.command()
async def impersonate(ctx, user: discord.User, *, message: str):
    await ctx.message.delete()
    webhook = await ctx.channel.create_webhook(name=user.name)
    await webhook.send(message, username=user.name, avatar_url=user.avatar_url)
    await webhook.delete()

@Crystal.command(aliases=["firstmsg"])
async def firstmessage(ctx):
    await ctx.message.delete()
    try:
        channel = ctx.channel
            
        first_message = (await channel.history(limit = 1, oldest_first = True).flatten())[0]
        try:                                        
            embed = discord.Embed(title="First message", description="The first message of the channel is:", color=0x9F00FB)
            try:
                embed.add_field(name = "Content", value = f"{first_message.content}", inline=True)
            except:
                pass
            try:
                embed.add_field(name = "Channel", value = f"{first_message.channel.mention}", inline=True)
            except:
                    pass
            embed.add_field(name = "Jump URL", value = f"{first_message.jump_url}", inline=False)
            embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
            embed.set_footer(text="Crystal")
            await ctx.send(embed=embed)


        except:
                pass
            
    except Exception:
        pass

@Crystal.command()
async def roles(ctx, server_id: int=None):
        await ctx.message.delete()
        try:             
            if server_id is None:
                server = discord.utils.get(ctx.bot.guilds, id=ctx.guild.id)
            else: 
                server = discord.utils.get(ctx.bot.guilds, id=server_id)
                
            roles = server.roles
                
            le_roles = []   
            
            for role in roles:
                le_roles.append(role)
            try:
                embed = discord.Embed(title=f'Server Roles', description='\n'.join([f"{g.name}" for g in reversed(le_roles)]), color=0x9F00FB)              
                embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
                embed.set_footer(text="Crystal")
                await ctx.send(embed=embed)
            except:
                pass
            
        except Exception:
            pass

@Crystal.command()
async def channels(ctx, server_id: int=None):
        await ctx.message.delete()
        try:             
            if server_id is None:
                server = discord.utils.get(ctx.bot.guilds, id=ctx.guild.id)
            else: 
                server = discord.utils.get(ctx.bot.guilds, id=server_id)
                
            channels = server.channels
                
            le_channels = []   
            
            for channel in channels:
                le_channels.append(channel)
            try:                                        
                if True:
                    embed = discord.Embed(title=f'Server Channels', description='\n'.join([f"{g.name}" for g in le_channels]) or 'None', color=0x9F00FB)
                    embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
                    embed.set_footer(text="Crystal")
                    await ctx.send(embed=embed)


                else:
                    await ctx.send(f'`Server Channels:`' + '\n'.join([f"{g.name}" for g in le_channels]) or 'None', color=0x9F00FB)
            except:
                pass
            
        except Exception:
            pass

@Crystal.command()
async def truthordare(ctx, truth_or_dare: str='truth'):
    await ctx.message.delete()
    try:
        if truth_or_dare.lower() not in ['truth', 'dare']:
            truth_or_dare = 'truth' 
        resp = requests.get("https://raw.githubusercontent.com/sylhare/Truth-or-Dare/master/src/output.json").json()
        available_values = len(resp)
        def go_deep() -> int:
            random_value = random.randint(0, available_values)
            if resp[random_value]['type'].lower() == truth_or_dare:
                return random_value
            else:
                return go_deep()

        value_id = go_deep()

        embed = discord.Embed(title='Truth or Dare', color=0x9F00FB)
        embed.add_field(name=f'__🎨 Type__', value=f"{resp[value_id]['type']}", inline=False)
        embed.add_field(name=f'__🥽 Summary__', value=f"{resp[value_id]['summary']}", inline=False)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

    except Exception:
        pass

@Crystal.command()
async def addrole(ctx, member: discord.Member, role: discord.Role):
        await ctx.message.delete()
        try:
            if role not in member.roles:
                roles = member.roles
                roles.append(role)
                asyncio.sleep(0.5)
                await member.edit(roles=roles)

            embed = discord.Embed(title='Member Roles', color=0x9F00FB)
            embed.add_field(name='__🧑 Member__', value=f"{member.mention}", inline=True)
            embed.add_field(name='__🌈 Added Role__', value=f"{role.mention}", inline=False)
            embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
            embed.set_footer(text="Crystal")
            await ctx.send(embed=embed)
        except Exception:
            pass

@Crystal.command()
async def removerole(ctx, member: discord.Member, role: discord.Role):
        await ctx.message.delete()
        try:
            if role in member.roles:
                roles = member.roles
                roles.remove(role)
                asyncio.sleep(0.5)
                await member.edit(roles=roles)

            embed = discord.Embed(title='Member Roles', color=0x9F00FB)
            embed.add_field(name='__🧑 Member__', value=f"{member.mention}", inline=True)
            embed.add_field(name='__🌈 Removed Role__', value=f"{role.mention}", inline=False)
            embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
            embed.set_footer(text="Crystal")
            await ctx.send(embed=embed)
        except Exception:
            pass

@Crystal.command()
async def lockchannel(ctx, channel: discord.channel.TextChannel=None):
        await ctx.message.delete()
        try:
            if channel is None:
                channel = ctx.channel
            if channel:
                if channel in ctx.guild.text_channels:
                    perms = channel.overwrites_for(ctx.guild.default_role)
                    perms.send_messages = False
                    await channel.set_permissions(ctx.guild.default_role, overwrite=perms)
                    embed = discord.Embed(title='Channel Lock', color=0x9F00FB)
                    embed.add_field(name='__🔐 Locked Channel__', value=f"{channel.mention}", inline=True)
                    embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
                    embed.set_footer(text="Crystal")
                    await ctx.send(embed=embed)
        except Exception:
            pass

@Crystal.command()
async def unlockchannel(ctx, channel: discord.channel.TextChannel=None):
        await ctx.message.delete()
        try:
            if channel is None:
                channel = ctx.channel
            if channel:
                if channel in ctx.guild.text_channels:
                    perms = channel.overwrites_for(ctx.guild.default_role)
                    perms.send_messages = True
                    await channel.set_permissions(ctx.guild.default_role, overwrite=perms)
                    embed = discord.Embed(title='Channel Lock', color=0x9F00FB)
                    embed.add_field(name='__🔐 Unlocked Channel__', value=f"{channel.mention}", inline=True)
                    embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
                    embed.set_footer(text="Crystal")
                    await ctx.send(embed=embed)
        except Exception:
            pass

@Crystal.command()
async def rule34(ctx, tag=None):
        await ctx.message.delete()
        if tag is None:
            try:
                request = requests.get(f'https://rule34.xxx/index.php?page=post&s=random')
                soup = BeautifulSoup(request.content, 'html.parser')
                link = soup.find(id="image").get("src")
                embed= discord.Embed(title=f'Rule34', color=0x9F00FB)
                embed.set_image(url=link)
                embed.set_footer(text="Crystal")
                await ctx.send(embed=embed)


            except Exception:
                return
        else:
            try:
                request = requests.get(f'https://rule34.xxx/index.php?page=post&s=list&tags={urllib.parse.quote(tag)}')
                soup = BeautifulSoup(request.content, 'html.parser')
                link = soup.find(id="image").get("src")
                embed= discord.Embed(title=f'Rule34', color=0x9F00FB)
                embed.set_image(url=link)
                embed.set_footer(text="Crystal")
                await ctx.send(embed=embed)


            except Exception:
                return

@Crystal.command()
async def aag(ctx, text1: str="", text2: str=""):
        await ctx.message.delete()
        embed= discord.Embed(title=f"""Ancient Aliens Guy""", color=0x9F00FB)
        embed.set_image(url=f"""https://api.memegen.link/images/aag/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png""")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def ackbar(ctx, text1: str="", text2: str=""):
        await ctx.message.delete()
        embed= discord.Embed(title=f"""It's A Trap!""", color=0x9F00FB)
        embed.set_image(url=f"""https://api.memegen.link/images/ackbar/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png""")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def afraid(ctx, text1: str="", text2: str=""):
        await ctx.message.delete()
        embed= discord.Embed(title=f"""Afraid to Ask Andy""", color=0x9F00FB)
        embed.set_image(url=f"""https://api.memegen.link/images/afraid/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png""")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def agnes(ctx, text1: str="", text2: str=""):
        await ctx.message.delete()
        embed= discord.Embed(title=f"""Agnes Harkness Winking""", color=0x9F00FB)
        embed.set_image(url=f"""https://api.memegen.link/images/agnes/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png""")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def aintgottime(ctx, text1: str="", text2: str=""):
        await ctx.message.delete()
        embed= discord.Embed(title=f"""Sweet Brown / Ain't Nobody Got Time For That""", color=0x9F00FB)
        embed.set_image(url=f"""https://api.memegen.link/images/aint-got-time/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png""")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def ams(ctx, text1: str="", text2: str=""):
        await ctx.message.delete()
        embed= discord.Embed(title=f"""Awkward Moment Seal""", color=0x9F00FB)
        embed.set_image(url=f"""https://api.memegen.link/images/ams/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png""")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def ants(ctx, text1: str="", text2: str=""):
        await ctx.message.delete()
        embed= discord.Embed(title=f"""Do You Want Ants?""", color=0x9F00FB)
        embed.set_image(url=f"""https://api.memegen.link/images/ants/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png""")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def apcr(ctx, text1: str="", text2: str=""):
        await ctx.message.delete()
        embed= discord.Embed(title=f"""Almost Politically Correct Redneck""", color=0x9F00FB)
        embed.set_image(url=f"""https://api.memegen.link/images/apcr/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png""")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def atis(ctx, text1: str="", text2: str=""):
        await ctx.message.delete()
        embed= discord.Embed(title=f"""And Then I Said""", color=0x9F00FB)
        embed.set_image(url=f"""https://api.memegen.link/images/atis/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png""")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def away(ctx, text1: str="", text2: str=""):
        await ctx.message.delete()
        embed= discord.Embed(title=f"""Life... Finds a Way""", color=0x9F00FB)
        embed.set_image(url=f"""https://api.memegen.link/images/away/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png""")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def awesome(ctx, text1: str="", text2: str=""):
        await ctx.message.delete()
        embed= discord.Embed(title=f"""Socially Awesome Penguin""", color=0x9F00FB)
        embed.set_image(url=f"""https://api.memegen.link/images/awesome/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png""")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def awesomeawkward(ctx, text1: str="", text2: str=""):
        await ctx.message.delete()
        embed= discord.Embed(title=f"""Socially Awesome Awkward Penguin""", color=0x9F00FB)
        embed.set_image(url=f"""https://api.memegen.link/images/awesome-awkward/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png""")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def awkward(ctx, text1: str="", text2: str=""):
        await ctx.message.delete()
        embed= discord.Embed(title=f"""Socially Awkward Penguin""", color=0x9F00FB)
        embed.set_image(url=f"""https://api.memegen.link/images/awkward/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png""")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def awkwardawesome(ctx, text1: str="", text2: str=""):
        await ctx.message.delete()
        embed= discord.Embed(title=f"""Socially Awkward Awesome Penguin""", color=0x9F00FB)
        embed.set_image(url=f"""https://api.memegen.link/images/awkward-awesome/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png""")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def bad(ctx, text1: str="", text2: str=""):
        await ctx.message.delete()
        embed= discord.Embed(title=f"""You Should Feel Bad""", color=0x9F00FB)
        embed.set_image(url=f"""https://api.memegen.link/images/bad/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png""")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def badchoice(ctx, text1: str="", text2: str=""):
        await ctx.message.delete()
        embed= discord.Embed(title=f"""Milk Was a Bad Choice""", color=0x9F00FB)
        embed.set_image(url=f"""https://api.memegen.link/images/badchoice/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png""")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def poll(ctx, *, poll: str):
        await ctx.message.delete()
        embed= discord.Embed(title=f'Poll', description=poll, color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')

@Crystal.command()
async def suggestion(ctx, *, suggestion: str):
        await ctx.message.delete()
        embed= discord.Embed(title=f'Suggestion', description=suggestion, color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        msg= await ctx.send(embed=embed)
        await msg.add_reaction('✅')
        await msg.add_reaction('❌')

@Crystal.command()
async def car(ctx):
        await ctx.message.delete()
        request = requests.get('https://no-api-key.com/api/v1/car')
        data = request.json()
        image_url = data['image']
        embed= discord.Embed(title=f'Car', color=0x9F00FB)
        embed.set_image(url=image_url)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def userstats(ctx):
        await ctx.message.delete()
        try:
            nitro_type = None
            try:
                Crystal.user.premium_type
            except Exception:
                nitro_type ="None"
            else:
                if Crystal.user.premium_type == discord.PremiumType.nitro_classic:
                    nitro_type ="Nitro Classic"

                elif Crystal.user.premium_type == discord.PremiumType.nitro:
                    nitro_type ="Nitro"
            
            embed = discord.Embed(title='User Statistics', color=0x9F00FB)
            embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
            embed.set_footer(text="Crystal")
            embed.add_field(name='__🧯 Guilds__', value=f'`{len(Crystal.guilds)}`')
            embed.add_field(name='__😎 Emojis__', value=f'`{len(Crystal.emojis)}`')
            embed.add_field(name='__🔑 2FA Enabled__', value=f'`{bool(Crystal.user.mfa_enabled)}`')
            embed.add_field(name='__💎 Nitro__', value=f'`{bool(Crystal.user.premium)}`')
            embed.add_field(name='__🔮 Nitro Type__', value=f'`{nitro_type}`')
            embed.add_field(name='__🎎 Relationships__', value=f'`{len(Crystal.user.relationships)}`')
            embed.add_field(name='__🧁 Verified__', value=f'`{bool(Crystal.user.verified)}`')
            await ctx.send(embed=embed)


        except Exception:
            pass

@Crystal.command()
async def rockstargamesstatus(ctx):
        await ctx.message.delete()
        resp = requests.get(f'https://support.rockstargames.com/services/status.json')
        data = resp.json()
        information = data['services']
        
        if True:
            embed= discord.Embed(title=f'Current Rockstar Games Status', color=0x9F00FB)
            embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
            embed.add_field(name=f'General', value="🟢 Online" if information[0]['status'] else "🔴 Offline", inline=True)
            embed.add_field(name=f'Red Dead Online', value="🟢 Online" if information[1]['status'] else "🔴 Offline", inline=True)
            embed.add_field(name=f'Grand Theft Auto Online', value="🟢 Online" if information[2]['status'] else "🔴 Offline", inline=True)
            embed.add_field(name=f'Social Club', value="🟢 Online" if information[3]['status'] else "🔴 Offline", inline=True)
            embed.add_field(name=f'Support', value="🟢 Online" if information[4]['status'] else "🔴 Offline", inline=True)
            embed.add_field(name=f'Rockstar Games Launcher', value="🟢 Online" if information[5]['status'] else "🔴 Offline", inline=True)
            embed.set_footer(text="Crystal")
            await ctx.send(embed=embed)


        else:
            msg = f'''```yaml
Rockstar Games Status:
General: {"🟢 Online" if information[0]['status'] else "🔴 Offline"}
Red Dead Online: {"🟢 Online" if information[1]['status'] else "🔴 Offline"}
Grand Theft Auto Online: {"🟢 Online" if information[2]['status'] else "🔴 Offline"}
Social Club: {"🟢 Online" if information[3]['status'] else "🔴 Offline"}
Support: {"🟢 Online" if information[4]['status'] else "🔴 Offline"}
Voice: {"🟢 Online" if information[5]['status'] else "🔴 Offline"}
Rockstar Games Launcher: {"🟢 Online" if information[6]['status'] else "🔴 Offline"}
```'''
            await ctx.send(msg)

@Crystal.command()
async def discordstatus(ctx):
        await ctx.message.delete()
        resp = requests.get(f'https://srhpyqt94yxb.statuspage.io/api/v2/summary.json')
        data = resp.json()
        information = data['components']
        
        if True:
            embed= discord.Embed(title=f'Current Discord Status', color=0x9F00FB)
            embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
            embed.add_field(name=f'Cloudflare', value=information[0]['status'].capitalize(), inline=True)
            embed.add_field(name=f'API', value=information[2]['status'].capitalize(), inline=True)
            embed.add_field(name=f'Tax Calculation', value=information[4]['status'].capitalize(), inline=True)
            embed.add_field(name=f'Media Proxy', value=information[5]['status'].capitalize(), inline=True)
            embed.add_field(name=f'Push Notifications', value=information[8]['status'].capitalize(), inline=True)
            embed.add_field(name=f'Voice', value=information[9]['status'].capitalize(), inline=True)
            embed.add_field(name=f'Third Party', value=information[12]['status'].capitalize(), inline=True)
            embed.add_field(name=f'Overall Status', value=f"{data['status']['description'].capitalize()}", inline=True)
            embed.set_footer(text="Crystal")
            await ctx.send(embed=embed)


        else:
            msg = f'''```yaml
Discord Status:
Cloudflare: {information[0]['status'].capitalize()}
API: {information[2]['status'].capitalize()}
Tax Calculation: {information[4]['status'].capitalize()}
Media Proxy: {information[5]['status'].capitalize()}
Push Notifications: {information[8]['status'].capitalize()}
Voice: {information[9]['status'].capitalize()}
Third Party: {information[12]['status'].capitalize()}
Overall Status: {data['status']['description'].capitalize()}
```'''
            await ctx.send(msg)

@Crystal.command()
async def userinfotest(ctx, user: discord.Member=None):
        await ctx.message.delete()
        try:
            if ctx.guild is not None:
                server = ctx.guild
                if user is None:
                    member = ctx.author
                else:
                    member = ctx.guild.get_member(user.id)
                avi = member.avatar_url
                roles = sorted(member.roles, key=lambda c: c.position / -1)

                rolenames = ' '.join([r.mention for r in roles if r.name != '@everyone']) or 'None'
                member_number = sorted(server.members, key=lambda m: m.joined_at).index(member) + 1
                permissions = ', '.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])

                resp = requests.get(f'https://canary.discordapp.com/api/v8/users/{member.id}/profile', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                j = resp.json()
                premium_since = j['premium_since']

                channel = None
                streaming = False
                if member.voice is not None:
                    channel = member.voice.channel
                    streaming = member.voice.self_stream
                if True:
                    embed = discord.Embed(title=f'Userinfo', color=0x9F00FB)
                    embed.add_field(name='Nickname', value=member.nick, inline=True)
                    embed.add_field(name='Member Number', value=str(member_number), inline = True)
                    embed.add_field(name='Account Created', value=member.created_at.__format__('%A, %d. %B %Y'), inline=True)
                    embed.add_field(name='User ID', value=str(member.id), inline=True)
                    embed.add_field(name='Join Date', value=member.joined_at.__format__('%A, %d. %B %Y'))
                    embed.add_field(name='Roles', value=rolenames, inline=True)
                    embed.add_field(name='Top Role', value=member.top_role.mention, inline=True)
                    embed.add_field(name='Nitro Subscription Since', value=premium_since, inline=True)
                    embed.add_field(name='Is On Mobile', value=member.is_on_mobile(), inline=True)
                    embed.add_field(name='Is In Voice Channel', value=channel, inline=True)
                    embed.add_field(name='Is Streaming', value=streaming, inline=True)
                    embed.add_field(name='Guild permissions', value=permissions, inline=True)
                    embed.set_footer(text="Crystal")
                    embed.set_thumbnail(url=avi)
                    embed.set_author(name=member, icon_url=server.icon_url)

                    await ctx.send(embed=embed)


                else:
                    msg = f'''```yaml
User Information about {member}:
Nickname: {member.nick}
Member Number: {member_number}
Account Created: {member.created_at.__format__('%A, %d. %B %Y')}
User ID: {str(member.id)}
Join Date: {member.joined_at.__format__('%A, %d. %B %Y')}
Roles: {rolenames}
Top Role: {member.top_role.mention}
Nitro Subscription Since: {premium_since}
Is On Mobile: {member.is_on_mobile()}
Is In Voice Channel: {channel}
Is Streaming: {streaming}
Guild permissions: {permissions}
```'''
                    await ctx.send(msg)
                    await ctx.send(avi)
            else:
                if user is None:
                    member = ctx.author
                else:
                    member = user
                avi = member.avatar_url
                resp = requests.get(f'https://canary.discordapp.com/api/v8/users/{member.id}/profile', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
                j = resp.json()
                premium_since = j['premium_since']

                if True:
                    embed = discord.Embed(color=int(json.load(open(f'./Themes/{json.load(open("""config.json""", encoding="""utf-8"""))["""theme"""]}.json'))['embed_color'].replace('#', '0x'), 0), url=json.load(open(f'./Themes/{json.load(open("""config.json""", encoding="""utf-8"""))["""theme"""]}.json'))['embed_title_url'])
                    embed.add_field(name='Account Created', value=member.created_at.__format__('%A, %d. %B %Y'))
                    embed.add_field(name='Is On Mobile', value=member.is_on_mobile(), inline=True)
                    embed.add_field(name='User ID', value=str(member.id), inline=True)
                    embed.add_field(name='Nitro Subscription Since', value=premium_since, inline=True)
                    embed.set_footer(text="Crystal")
                    embed.set_thumbnail(url=avi)
                    embed.set_author(name=member, icon_url=avi)
                else:
                    msg = f'''```yaml
User Information about {member}:
Account Created: {member.created_at.__format__('%A, %d. %B %Y')}
Is On Mobile: {member.is_on_mobile()}
User ID: {str(member.id)}
Nitro Subscription Since: {premium_since}
```'''
                    await ctx.send(msg)
                    await ctx.send(avi)

                await ctx.send(embed=embed)


        except Exception:
            return

@Crystal.command()
async def rickroll(ctx):
    await ctx.message.delete()
    lyrics2 = '''We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching, but
You're too shy to say it
Inside, we both know what's been going on
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
(Ooh, give you up)
(Ooh, give you up)
Never gonna give, never gonna give
(Give you up)
Never gonna give, never gonna give
(Give you up)
We've known each other for so long
Your heart's been aching, but
You're too shy to say it
Inside, we both know what's been going on
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you'''
    text = lyrics2.split('\n')
    for line in text:
        await ctx.send(line)

@Crystal.command()
async def shrekscript(ctx):
    await ctx.message.delete()
    script = '''Shrek: "Once upon a time, there was a lovely princess. But she had an enchantment upon her of a fearful sort, which could only be broken by love's first kiss. She was locked away in a castle, guarded by a terrible fire-breathing dragon. Many brave knights had attempted to free her from the dreadful prison, but none prevailed. She waited in the dragon's keep, in the highest room of the tallest tower, for her true love and true love's first kiss." [Laughing] Like that's ever gonna happen.
[Paper Rustling, Toilet Flushes]
Shrek: What a load of--
[Toilet Door slams]
Shrek hops out his outhouse and his routine like taking a mud shower and farting in his pool.
[♪ All-Star By Smash Mouth Playing]
Steve Harwell: ♪ Somebody once told me the world is gonna roll me, I ain't the sharpest tool in the shed. She was lookin' kind of dumb with her finger and her thumb in the shape of an "L" on her forehead. The years start comin', and they don't stop comin', fed to the rules and I hit the ground runnin', didn't make sense not to live for fun. Your brain gets smart but your head gets dumb. So much to do, so much to see, so what's wrong with takin' the backstreets. You'll never know if you don't go, you'll never shine if you don't glow. Hey, now, you're an all-star. Get your game on, go play. Hey, now, you're a rock star. Get the show on, get paid. And all that glitters is gold, only shootin' stars break the mold. It's a cool place, and they say it gets colder, you're bundled up now, but wait till you get older. But the meteor men beg to differ judging by the hole in the satellite picture. The ice we skate is gettin' pretty thin, the water's getting warm so you might as well swim. My world's on fire, how 'bout yours? That's the way I like it and I'll never get bored. Hey, now, you're an all-star. ♪
[Shouting]
Steve Harwell: ♪ Get your game on, go play. Hey, now, you're a rock star. Get the show on, get paid. And all that glitters is gold, only shootin' stars break the mold. ♪
[Belches]
Villagers: Go! Go!
[Record Scrating]
Steve Harwell: ♪ Go. Go. Go. Hey, now, you're an all-star. Get your game on, go play. Hey, now, you're a rock star, get the show on, get paid. And all that glitters is gold, only shootin' stars break the mold. ♪
Villagers: Think it's in there? All right! Let's get it!
Villager 1: Whoa. Hold on. Do you know what that thing could do to you?
Villager 2: Yeah, it'll grind your bones for its bread.
Shrek: [Laughs] Yes, well, actually, that would be a giant. Now, ogres-- they're much worse. They'll make a suit from your freshly peeled skin.
Villager 3: No!
Shrek: They'll shave your liver. Squeeze the jelly from your eyes! Actually, it's quite good on toast.
Villager 3: Back! Back, beast! Back! I warn ya!
[Gasping]
Villager 3: Right.
[Roaring]
[Shouting]
[Roaring]
[Roaring Continues]
[Shouting Continues]
Shrek: [Whispers] This is the part where you run away.
[Gasping]
Shrek: [Laughs] [Laughing] And stay out! "Wanted. Fairy tale creatures." [Sighs]
Guard 1: All right. This one's full. Take it away!
[Gasps]
Guard 2: Move it along. Come on. Get up!
Captain of the Guards: Next!
Guard 3: Give me that! Your flying days are over.
Captain of the Guards: That's 20 pieces of silver for the witch. Next.
Guard 4: Get up!
Captain of the Guards: Twenty pieces.
Guard 5: Come on!
[Thudding]
Guard 6: Sit down there! Keep quiet!
Bear: [Crying] This cage is too small.
Donkey: Please, don't turn me in. I'll never be stubborn again. I can change. Please! Give me another chance!
Old Lady: Oh, shut up!
Donkey: Oh!
Captain of the Guards: Next! What have you got?
Geppetto: This little wooden puppet.
Pinocchio: I'm not a puppet. I'm a real boy.
Captain of the Guards: Five shillings for the possessed toy. Take it away.
Pinocchio: Father, please! Don't let them do this!
Captain of the Guards: Next.
Pinocchio: Help me!
Captain of the Guards: What have you got?
Old Lady: Well, I've got a talking donkey.
[Grunts]
Captain of the Guards: Right. Well, that's good for ten shillings, if you can prove it.
Old Lady: Oh, go ahead, little fella.
Captain of the Guards: Well?
Old Lady: Oh, oh, he's just-- He's just a little nervous. He's really quite a chatterbox. Talk, you boneheaded dolt--
Captain of the Guards: That's it. I've heard enough. Guards!
Old Lady: No, no, he talks! He does. [Moves Donkey’s lips] I can talk. I love to talk. I'm the talkingest damn thing you ever saw.
Captain of the Guards: Get her out of my sight.
Old Lady: No, no! I swear. Oh! He can talk!
Donkey: [Gasps] Hey, I can fly!
Peter Pan: He can fly!
Pigs: He can fly!
Captain of the Guards: He can talk!
Donkey: Ha, ha! That's right, fool! Now I'm a flying, talking, donkey. You might have seen a housefly, maybe even a superfly, but I bet you ain't never seen a donkey fly. Ha, ha! Uh-oh.
Captain of the Guards: Seize him!
Guard 7: After him! He's getting away!
[Grunts, Gasps]
Guard 8: Get him! This way! Turn!
Captain of the Guards: You there. Ogre!
Shrek: Aye?
Captain of the Guards: By the order of Lord Farquaad, I am authorized to place you both under arrest, and transport you to a designated, resettlement facility.
Shrek: Oh, really? You and what army?
[Gasps, Whimpering]
Donkey: [Chuckles] Can I say somethin' to you? Listen, you was really, really somethin' back there. Incredible!
Shrek: Are you talkin' to-- me? Whoa!
Donkey: Yes, I was talkin' to you. Can I tell you that you was great back there? Those guards! They thought they was all of that. Then you showed up, then bam! They was trippin' over themselves like babies in the woods. That really made me feel good to see that.
Shrek: Oh, that's great. Really.
Donkey: Man, it's good to be free.
Shrek: Now, why don't you go celebrate your freedom with your own friends? Hmm?
Donkey: But, uh, I don't have any friends. And I'm not goin' out there by myself. Hey, wait a minute! I got a great idea! I'll stick with you. You're a mean, green, fightin' machine. Together we'll scare the spit out of anybody that crosses us.
[Roaring]
Donkey: Oh, wow! That was really scary. If you don't mind me sayin', if that don't work, your breath certainly will get the job done, 'cause you definitely need some Tic Tacs or something, 'cause your breath stinks! Man, you almost burned the hair outta my nose, just like the time-- [Mumbling] Then I ate some rotten berries. I had strong gases eking out of my butt that day.
Shrek: Why are you following me?
Donkey: I'll tell you why. ♪ 'Cause I'm all alone. There's no one here beside me. My problems have all gone, there's no one to deride me. But you gotta have friends-- ♪
Shrek: Stop singing! It's no wonder you don't have any friends.
Donkey: Wow. Only a true friend would be that cruelly honest.
Shrek: Listen, little donkey. Take a look at me. What am I?
Donkey: Uh-- Really tall?
Shrek: No! I'm an ogre. You know. "Grab your torch and pitchforks." Doesn't that bother you?
Donkey: Nope.
Shrek: Really?
Donkey: Really, really.
Shrek: Oh.
Donkey: Man, I like you. What's your name?
Shrek: Uh, Shrek.
Donkey: Shrek? Well, you know what I like about you, Shrek? You got that kind of I-don't-care-what-nobody-thinks-of-me thing. I like that. I respect that, Shrek. You all right. Whoo! Look at that. Who'd want to live in a place like that?
Shrek: That would be my home.
Donkey: Oh! And it is lovely! Just beautiful. You are quite a decorator. It's amazing what you've done with such a modest budget. I like that boulder. That is a nice boulder. I guess you don't entertain much, do you?
Shrek: I like my privacy.
Donkey: You know, I do too. That's another thing we have in common. Like, I hate it when you got somebody in your face. You're trying to give them a hint, and they won't leave. There's that awkward silence. You know? Can I stay with you?
Shrek: Uh, what?
Donkey: Can I stay with you? Please?
Shrek: Of course!
Donkey: Really?
Shrek: No.
Donkey: Please! I don't wanna go back there! You don't know what it's like to be considered a freak. Well, maybe you do. But, that's why we gotta stick together. You gotta let me stay! Please! Please!
Shrek: Okay! Okay! But one night only.
Donkey: Ah! Thank you!
Shrek: What are you-- No. No.
Donkey: This is gonna be fun. We can stay up late, swappin' manly stories, and in the mornin', I'm makin' waffles.
Shrek: Oh!
Donkey: Where do, uh, I sleep?
Shrek: Outside!
Donkey: Oh, well, I guess that's cool. I mean, I don't know you, and you don't know me, I guess outside is best. [Sniffles] Here I go. Good night. [Sighs] I mean, I do like the outdoors. I'm a donkey. I was born outside. I'll just be sitting by myself. Outside, I guess. You know. By myself. Outside. ♪ I'm all alone, there's no one here beside me. ♪
[Bubbling]
[Sighs]
[Creaking]
Shrek: [Sighs] I thought I told you to stay outside?
Donkey: I am outside.
[Clattering]
[Clattering]
Mouse 1: Well, gents, it's a far cry from the farm, but what choice do we have?
Mouse 2: It's not home, but it'll do just fine.
Gorder: What a lovely bed.
Shrek: Got ya.
Gorder: [Sniffs] I found some cheese.
Shrek: Ow! [Grunts]
Gorder: Blah! Awful stuff.
Mouse 1: Is that you, Gorder?
Gorder: How did you know?
Shrek: Enough! What are you doing in my house? [Grunts] Hey!
[Snickers]
Shrek: Oh, no, no, no. Dead broad off the table.
Dwarf: Where are we supposed to put her? The bed's taken.
Shrek: Huh? [Gasps]
Wolf: What?
Shrek: I live in a swamp. I put up signs. I'm a terrifying ogre! What do I have to do to get a little privacy?
Wolf: Aah!
Shrek: Oh, no. No! No! Oh, no.
[Cackling]
[Cackling Continues]
Shrek: What?
Girl: Quit it. Don't push.
[Squeaking]
[Lows]
Shrek: What are you doing in my swamp? [Echoing] Swamp? Swamp? Swamp?
[Gasping]
Fairies: Oh, dear!
Dwarf: Whoa!
Shrek: All right, get out of here. All of you, move it. Come on. Let's go! Hapaya! Hapaya! Hey!
Dwarf: Quickly. Come on!
Shrek: No, no! No, no. Not there. Not there.
Dwarf: Oh!
[Sighs]
Donkey: Hey, don’t look at me. I didn't invite them.
Pinocchio: Oh, gosh, no one invited us.
Shrek: What?
Pinocchio: We were forced to come here.
Shrek: By who?
Pig: Lord Farquaad. He huffed und he puffed und he... singed an eviction notice.
Shrek: [Sighs] All right. Who knows where this Farquaad guy is.
[Murmuring]
Donkey: Oh, I do. I know where he is.
Shrek: Does anyone else know where to find him? Anyone at all?
Donkey: Me! Me!
Shrek: Anyone?
Donkey: Oh! Oh, pick me! Oh, I know! I know! Me, me!
Shrek: Okay, fine. Attention, all fairy tale things. Do not get comfortable. Your welcome is officially worn out. In fact, I'm gonna see this guy Farquaad right now, and get you all off my land and back where you came from!
[Cheering]
[Twittering]
[Cheering Continues]
Shrek: Oh! You! You're comin' with me.
Donkey: All right, that's what I like to hear, man. Shrek and Donkey, two stalwart friends, off on a whirlwind big-city adventure. I love it! ♪ On the road again. ♪ Sing it with me, Shrek.
Dwarf: Hey. Oh, oh!
Donkey: ♪ I can't wait to get in the road again. ♪
Shrek: What did I say about singing?
Donkey: Can I whistle?
Shrek: No.
Donkey: Can I hum it?
Shrek: All right, hum it.
♪♪ [Humming]
[Gurgling]
[Coughing]
Farquaad: That's enough! He's ready to talk.
[Coughing]
Farquaad: [Laughing] [Clears Throat] Run, run, run, as fast as you can. You can't catch me. I'm the gingerbread man!
Gingy: You're a monster.
Farquaad: I'm not the monster here, you are! You and the rest of that fairy tale trash, poisoning my perfect world. Now tell me, where are the others!?
Gingy: Eat me!
[Spits]
Farquaad: I've tried to be fair to you creatures. Now my patience has reached its end! Tell me, or I'll--
Gingy: No! Not the buttons! Not my gumdrop buttons!
Farquaad: All right, then. Who's hiding them?
Gingy: Okay. I'll tell you. Do you know the muffin man?
Farquaad: The muffin man?
Gingy: The muffin man.
Farquaad: Yes. I know the muffin man. Who lives on Drury Lane?
Gingy: Well, she's married to the muffin man.
Farquaad: The muffin man?
Gingy: The muffin man!
Farquaad: She's married to the muffin man.
[Door Opens]
Captain of the Guards: My lord! We found it.
Farquaad: Then what are you waiting for? Bring it in.
[Man Grunting]
[Gasping]
Gingy: Oh!
Farquaad: Magic Mirror.
Gingy: Don't tell him anything! No!
Farquaad: Evening. Mirror, mirror, on the wall. Is this not the most perfect kingdom of all?
Mirror: Well, technically you're not a king.
Farquaad: Uh, Thelonius. You were saying?
Mirror: What I mean is, you're not a king yet. But you can become one. All you have to do is marry a princess.
Farquaad: Go on.
Mirror: [Chuckles] So, just sit back and relax, my lord, because it's time for you to meet today's eligible bachelorettes. And here they are! Bachelorette number one is a mentally abused shut-in from a kingdom far, far away. She likes sushi and hot tubbing anytime. Her hobbies include cooking and cleaning for her two evil sisters. Please welcome Cinderella. Bachelorette number two is a cape-wearing girl from the land of fancy. Although she lives with seven other men, she's not easy. Just kiss her dead, frozen lips and find out what a live wire she is. Come on. Give it up for Snow White! And last, but certainly not the least, bachelorette number three is a fiery redhead, from a dragon-guarded castle surrounded by hot boiling lava! But, don't let that cool you off. She's a loaded pistol who likes piña coladas and getting caught in the rain. Yours for the rescuing, Princess Fiona! So will it be, bachelorette number one, bachelorette number two or bachelorette number three?
Guards: Two! Two! Three! Three! Two! Two! Three!
Farquaad: Three? One? [Shudders] Three?
Thelonius: Three! Pick number three, my lord!
Farquaad: Okay, okay, uh, number three!
Mirror: Lord Farquaad, you've chosen Princess Fiona.
[♪ Escape By Rupert Holmes Playing]
Rupert Holmes: ♪ If you like piña coladas. And getting caught in the rain. ♪
Farquaad: Princess Fiona.
Rupert Holmes: ♪ If you're not into yoga. ♪
Farquaad: She's perfect. All I have to do is just find someone who can go--
Mirror: But I probably should mention the little thing that happens at night.
Farquaad: I'll do it.
Mirror: Yes, but after sunset.
Farquaad: Silence! I will make this Princess Fiona my queen, and Duloc will finally have the perfect king! Captain, assemble your finest men. We're going to have a tournament.
Donkey: But that's it. That's it right there. That's Duloc. I told ya I'd find it.
Shrek: So, that must be Lord Farquaad's castle.
Donkey: Uh-huh. That's the place.
Shrek: Do you think maybe he's compensating for something? [Laughs]
Donkey: [Groans] Hey, wait. Wait up, Shrek.
Man: Hurry, darling. We're late. Hurry.
Shrek: Hey, you!
[Screams]
Shrek: Wait a second. Look, I'm not gonna eat ya. I just-- I just--
[Whimpering]
[Sighs]
[Whimpering, Groans]
[Turnstile Clatters]
[Chuckles]
[Sighs]
♪♪ [Instrumental Music]
Shrek: It's quiet. Too quiet.
[Creaking]
Shrek: Where is everybody?
Donkey: Hey, look at this!
[Clattering, Whirring, Clicking]
[Clicking]
[Clicking Quickens]
Clockwork Chorus: ♪ Welcome to Duloc such a perfect town. Here was have some rules, let us lay them down. Don't make waves, stay in line and we'll get along fine, Duloc is a perfect place. Please keep off of the grass, shine your shoes, wipe your... face. Duloc is, Duloc is, Duloc is a perfect place! ♪
[Camera Shutter Clicks]
[Whirring]
Donkey: Wow! Let's do that again!
Shrek: No. No. No, no, no! No.
[Trumpet Fanfare]
[Crowd Cheering]
Farquaad: Brave knights. You are the best and brightest in all the land.
[Donkey Humming]
Farquaad: Today one of you shall prove himself--
Shrek: All right. You're going the right way for a smacked bottom.
Donkey: Sorry about that.
[Cheering]
Farquaad: That champion shall have the honor-- no, no-- the privilege, to go forth and rescue the lovely Princess Fiona, from the fiery keep of the dragon. If for any reason the winner is unsuccessful, the first runner-up will take his place, and so on and so forth. Some of you may die, but it's a sacrifice I am willing to make.
[Cheering]
Farquaad: Let the tournament begin!
[Gasps]
Knight 1: Oh!
Farquaad: What is that?
[Gasping]
Farquaad: It's hideous!
Shrek: Ah, that's not very nice. It's just a donkey.
Donkey: Huh?
Farquaad: Indeed. Knights, new plan! The one who kills the ogre will be named champion! Have at him!
Knight 2: Get him!
Shrek: Oh, hey! Now come on! Hang on now.
Woman: Go ahead! Get him!
Shrek: Can't we just settle this over a pint?
Knight 3: Kill the beast!
Shrek: No? All right then. Come on!
[♪ Bad Reputation By Joan Jett Playing]
Halfcocked: ♪ I don't give a damn about my reputation. You're living in the past, it's a new generation. ♪
Knight 4: Damn!
[Whinnying]
Halfcocked: ♪ A girl can do what she wants to do, and that's what I'm gonna do. And I don't give a damn about my bad reputation. Oh, no, no, no, no, no. Not me. Me, me, me. ♪
Donkey: Hey, Shrek, tag me! Tag me!
Halfcocked: ♪ And I don't give a damn about my reputation. Never said I wanted to improve my station. ♪
Shrek: Ah! [Laughs]
Halfcocked: ♪ And I'm always feelin' good when I'm having fun. ♪
Shrek: Yeah!
Halfcocked: ♪ And I don't have to please no one. ♪
Wrestling Fan: The chair! Give him the chair!
Halfcocked: ♪ And I don't give a damn about my reputation. Oh, no, no, no, no, no. Not me. Me, me, me. Oh, no, no, no, no. Not me, not me. Not me. ♪
[Bell Dings]
[Cheering]
Shrek: [Laughs] Oh, yeah! Ah! Ah! Thank you! Thank you very much! I'm here till Thursday. Try the veal! Ha, ha!
[Shrek Laughs]
[Crowd Gasping, Murmuring]
Guard 9: Shall I give the order, sir?
Farquaad: No, I have a better idea. People of Duloc! I give you our champion!
Shrek: What?
Farquaad: Congratulations, ogre. You're won the honor of embarking on a great and noble quest.
Shrek: Quest? I'm already on a quest. A quest to get my swamp back.
Farquaad: Your swamp?
Shrek: Yeah, my swamp! Where you dumped those fairy tale creatures!
[Crowd Murmuring]
Farquaad: Indeed. All right, ogre. I'll make you a deal. Go on this quest for me, and I'll give you your swamp back.
Shrek: Exactly the way it was?
Farquaad: Down to the last slime-covered toadstool.
Shrek: And the squatters?
Farquaad: As good as gone.
Shrek: What kind of quest?
Donkey: Let me get this straight. You're gonna go fight a dragon, and rescue a princess just so Farquaad will give you back a swamp, which you only don't have because he filled it full of freaks in the first place. Is that about right?
Shrek: You know what? Maybe there's a good reason donkeys shouldn't talk.
Donkey: I don't get it, Shrek. Why don't you just pull some of that ogre stuff on him? Throttle him, lay siege to his fortress, grind his bones to make your bread, the whole ogre trip.
Shrek: Oh, I know what. Maybe I could have decapitated an entire village, and put their heads on a pike, gotten a knife, cut open their spleen and drink their fluids. Does that sound good to you?
Donkey: Uh, no, not really, no.
Shrek: For your information, there's a lot more to ogres than people think.
Donkey: Example?
Shrek: Example? Okay, um, ogres are like onions.
Donkey: [Sniffs] They stink?
Shrek: Yes-- No!
Donkey: They make you cry?
Shrek: No!
Donkey: You leave them out in the sun, they get all brown, start sproutin' little white hairs.
Shrek: No! Layers! Onions have layers. Ogres have layers! Onions have layers. You get it? We both have layers. [Sighs]
Donkey: Oh, you both have layers. Oh. [Sniffs] You know, not everybody likes onions. Cakes! Everybody loves cakes! Cakes have layers.
Shrek: I don't care what everyone likes. Ogres. Are not. Like cakes.
Donkey: You know what else everybody likes? Parfaits. Have you ever met a person, you say, "Hey, let's get some parfait," they say, "Hell no, I don't like no parfait"? Parfaits are delicious.
Shrek: No! You dense, irritating, miniature beast of burden! Ogres are like onions! And of story. Bye-bye. See ya later.
Donkey: Parfaits may be the most delicious thing on the whole damn planet.
Shrek: You know, I think preferred your humming.
Donkey: Do you have a tissue or something? I'm making a mess. Just the word parfait makes me start slobbering.
[♪ I'm On My Way By The Proclaimers Playing]
The Proclaimers: ♪ I'm on my way from misery to happiness today. Uh-huh, uh-huh, uh-huh, uh-huh. I'm on my way from misery to happiness today. Uh-huh, uh-huh, uh-huh, uh-huh. And everything that you receive up yonder is what you give to me the day I wander, I'm on my way. I'm on my way. I'm on my way. ♪
Donkey: Ooh! Shrek! Did you do that? You gotta warn somebody before you just crack one off. My mouth was open and everything.
Shrek: Believe me, Donkey, if it was me, you'd be dead. [Sniffs] It's brimstone. We must be getting close.
Donkey: Yeah, right, brimstone. Don't be talking about it's the brimstone. I know what I smell. It wasn't no brimstone. It didn't come off no stone either.
[Rumbling]
Shrek: Sure, it's big enough, but look at the location. [Laughing]
Donkey: Shrek? Remember when you said ogres have layers?
Shrek: Oh, aye.
Donkey: Well, I have a bit of a confession to make. Donkeys don't have layers. We wear our fear right out there on our sleeves.
Shrek: Wait a second. Donkeys don't have sleeves.
Donkey: You know what I mean.
Shrek: You can't tell me you're afraid of heights?
Donkey: No, I'm just a little uncomfortable being on a rickety over a boiling lake of lava!
Shrek: Come on, Donkey. I'm right here beside ya, okay. For emotional support. We'll just tackle this thing together one little baby step at a time.
Donkey: Really?
Shrek: Really, really.
Donkey: Okay, that makes me feel so much better.
Shrek: Just keep moving. And don't look down.
Donkey: Okay, don't look down. Don't look down. Don't look down. Keep on moving. Don't look down. [Gasps] Shrek! I'm lookin' down! God, I can't do this! Just let me off right now. Please.
Shrek: But you're already halfway.
Donkey: But I know that half is safe!
Shrek: Okay, fine. I don't have time for this. You go back.
Donkey: Shrek, no! Wait!
Shrek: Donkey-- Let's have a dance then, shall we?
Donkey: Don't do that!
Shrek: Oh, I'm sorry. Do what? Oh, this?
Donkey: Yes, that!
Shrek: This? This, do it. Okay.
Donkey: [Screams] No, Shrek! No! Stop it!
Shrek: You said do it. I'm doin' it.
Donkey: I'm gonna die. I'm gonna die. Shrek, I'm gonna die. Oh!
Shrek: That'll do, Donkey. That'll do.
Donkey: Cool. So, where is this fire-breathing pain-in-the-neck anyway?
Shrek: Inside, waiting for us to rescue her.
Donkey: [Chuckles] I was talkin' about the dragon, Shrek.
[Water Dripping]
[Wind Howling]
Donkey: [Donkey Whispering] You afraid?
Shrek: No, but-- Shh.
Donkey: Oh, good. Me neither. [Gasps] 'Cause there's nothin' wrong with bein' afraid. Fear's a sensible response to an unfamiliar situation. Unfamiliar dangerous situation, I might add. With a dragon that breathes fire and eats knights and breathes fire, it sure doesn't mean you're a coward if you're a little scared, you know what I mean. I sure as heck ain't no coward. I know that. [Gasps]
Shrek: Donkey, two things, okay? Shut... up. Now go over there and see if you can find any stairs.
Donkey: Stairs? I thought I was lookin' for the princess.
Shrek: The princess will be up the stairs in the highest room in the tallest tower.
Donkey: What makes it you think she'll be there?
Shrek: I read it in a book once.
Donkey: Cool. You handle the dragon. I'll handle the stairs. I'll find those stairs. I'll whip their butt too. Those stairs won't know which way they're goin'.
[Creaking]
Donkey: I'm gonna take drastic steps. Kick it to the curb. Don't mess with me. I'm the stair master. I've mastered the stairs. I wish I had a step right here, right here. I'd step all over it.
Shrek: Well, at least we know where the princess is, but where's the--?
Donkey: Dragon! [Screams] [Gasps]
[Roars]
Shrek: Donkey, look out! [Screams]
[Screams]
[Whimpering]
Shrek: Got ya!
[Roars]
[Gasps]
Shrek: [Shouts] Whoa! Whoa! Whoa! [Screaming]
Donkey: [Gasps] Oh! Aah! Aah! [Gasping]
[Growls]
Donkey: No. Oh, no. No! [Screams] Oh, what large teeth you have.
[Growls]
Donkey: I mean, I mean, white sparkling teeth. I know you probably hear this all the time from your food, but you must bleach, 'cause that is one dazzling smile you got there. Do I detect a hint of minty freshness? And you know what else? You're-- You're a girl dragon! Oh, sure! I mean, of course you're a girl dragon. 'Cause, you're just reeking a feminine beauty. What's the matter with you? You got something in your eye? Ooh. Oh. Oh. Man, I'd really love to stay, but, you know, I'm, uh-- [Coughs] I'm an asthmatic, and I don't know if it'd work out if you're gonna blow smoke rings and stuff. Shrek! [Gasps] [Whimpering] No! Shrek! Shrek! Shrek!
[Groans, Sighs]
♪♪ [Chorus Vocalizing]
♪♪ [Vocalizing Continues]
♪♪ [Vocalizing Continues]
Fiona: Oh! Oh!
Shrek in Armor: Wake up!
Fiona: What?
Shrek in Armor: Are you Princess Fiona?
Fiona: I am, awaiting a knight so bold as to rescue me.
Shrek in Armor: Oh, that's nice. Now let's go!
Fiona: But wait, Sir Knight. This be-ith our first meeting. Should it not be a wonderful, romantic moment?
Shrek in Amror: Yeah, sorry, lady. There's no time.
Fiona: Hey, wait. What are you doing? You know, you should sweep me off my feet, out yonder window and down a rope onto your valiant steed.
Shrek in Armor: You've had a lot of time to plan this, haven't you?
Fiona: Mm-hmm. [Screams, Grunts] But we have to savor this moment! You could recite an epic poem for me. A ballad? A sonnet! A limerick? Or something!
Shrek in Armor: I don't think so.
Fiona: Can I at least know the name of my champion?
Shrek: Um, Shrek.
Fiona: Sir Shrek. [Clears Throat] I pray that you take this favor as a token of my gratitude.
Shrek in Armor: Thanks!
[Roaring]
Fiona: You didn't slay the dragon?
Shrek in Armor: It's on my to-do list. Now, come on!
Fiona: [Screams] But this isn't right! You’re meant to charge in, sword drawn, banner flying! That's what all the other knights did!
Shrek in Armor: Yeah, right before they burst into flame!
(they pass a skeleton of one of the unfortunate victims)
Fiona: You know, that's not the point! Oh! Wait. Where are you going? The exit's over there.
Shrek in Armor: Well, I have to save my ass.
Fiona: What kind of knight are you?
Shrek in Armor: One of a kind.
Donkey: Slow down. Slow down, baby, please. I believe it's healthy to get to know someone over a long period of time. Just call me old-fashioned, you know. [Laughs] I don't to rush into a physical relationship. I'm not emotionally ready for a commitment of, uh, this-- Magnitude really is the word I'm looking for. Magnitude-- Hey, that is unwanted physical contact. Hey, what are you doing? Okay, okay. Let's just back up a little and take this one step at a time. I mean, we really should get to know each other first as friends or maybe his pen pals. 'Cause I'm the road a lot, but I just love receiving cards, and-- I'd really love to stay, but-- Hey, hey, hey! Don't do that! That's my tail! That's my personal tail. You're gonna tear it off. I don't give permission to-- Wait. What are you gonna do with that? Hey, now. No way. No! No! No, no! No. No, no, no! No! Oh!
[Growls]
[Roars]
[Roaring]
[Gasps]
Donkey: Hi, Princess!
Fiona: It talks!
Shrek in Armor: Yeah, it's getting him to shut up that's the trick!
Donkey: Shrek! [Screams] [Screaming]
Shrek: Oh!
[Thuds]
[Groans]
[Shrek Groans]
[Roars]
[Roars]
[Roaring]
[Roars]
Shrek in Armor: Okay, you two! Head for the exit! I'll take care of the dragon. [Echoing] Run!
[Gasping]
[Screaming]
[Screams]
[Roars]
[Panting, Sighs]
[Whimpers]
[Roars]
[Roars, Whimpers]
[Dragon Growling In The Distance]
Fiona: You did it! You rescued me! You're amazing. You're-- You're wonderful. You're... A little unorthodox, I'll admit. But thy deed is great, and thine heart is pure. I am eternally in your debt.
[Clears Throat]
Fiona: And where would be a brave knight be without his noble steed?
Donkey: All right, I hope you heard that. She called me a noble steed. She think I'm a noble steed.
Fiona: [Fiona Laughs] The battle is won. You may remove your helmet, good Sir Knight.
Shrek in Armor: Uh, no.
Fiona: Why not?
Shrek: I have helmet hair.
Fiona: Please. I would'st look upon the face of my rescuer.
Shrek in Armor: No, no, you wouldn't'st.
Fiona: But, how will you kiss me?
Shrek in Armor: What? That job wasn't in the job description.
Donkey: Maybe it's a perk.
Fiona: No, it's destiny. Oh, you must know how it goes. A princess locked in a tower and beset by a dragon, is rescued by a brave knight, and then they share true love's first kiss.
Donkey: Hmm? With Shrek? You think-- Wait. Wait. You think that Shrek is your true love?
Fiona: Well, yes.
[Laughing]
[Laughing]
Donkey: You think Shrek is your true love!
Fiona: What is so funny?
Shrek in Armor: Let's just say I'm not your type, okay?
Fiona: Of course, you are. You're my rescuer. Now-- Now remove your helmet.
Shrek in Amror: Look. I really don't think this is a good idea.
Fiona: Just take off the helmet.
Shrek in Amror: I'm not going to.
Fiona: Take it off.
Shrek in Amror: No!
Fiona: Now!
Shrek in Armor: Okay! Easy. As you command, Your Highness.
Fiona: You-- You're-- an ogre.
Shrek: Oh, you were expecting Prince Charming.
Fiona: Well, yes, actually. Oh, no. This is all wrong. You're not supposed to be an ogre.
Shrek: Princess, I was sent to rescue you by Lord Farquaad, okay. He's the one who wants to marry you.
Fiona: Then why didn't he come to rescue me?
Shrek: Good question. You should ask him that when we get there.
Fiona: But I have to be rescued by my true love. Not by some ogre and his pet.
Donkey: So much for noble steed.
Shrek: You're not making my job any easier.
Fiona: I'm sorry, but your job is not my problem. You can tell Lord Farquaad that if he wants to rescue me properly, I'll be waiting for him right here.
Shrek: Hey! I'm no one's messenger boy, all right? I'm a delivery boy.
Fiona: You wouldn't dare. Put me down!
Shrek: Ya comin', Donkey?
Donkey: I'm right behind ya.
Fiona: Put me down, or you will suffer the consequences! This is not dignified! Put me down! [Screams]
Donkey: Okay, so here's another question. Say there's a woman that digs you, right? But you don't really like her that way. How do you let her down real easy so her feelings aren't hurt, but you don't get burned to a crisp and eaten?
Fiona: You just tell her she's not your true love. Everyone knowest what happens when you find your-- Hey? [Sighs] The sooner we get to Duloc the better.
Donkey: Oh, yeah. You're gonna love it there, Princess? It's beautiful!
Fiona: And my groom-to-be? Lord Farquaad? What's he like?
Shrek: Well, let me put this way, Princess. Men of Farquaad's standards are in short supply. [Laughs]
Donkey: I don't know, Shrek. There are those who think little of him.
[Both Laughing]
Fiona: Stop it. Stop it, both of you. You're just jealous that you can never measure up to a great ruler like Lord Farquaad.
Shrek: Maybe. But I'll let you do the "measuring" when you see him tomorrow.
Fiona: Tomorrow? It'll take that long? Shouldn't we stop to make camp?
Shrek: No, that'll take longer.
Fiona: But there's robbers in the woods.
Donkey: Whoa! Time out, Shrek! Camping is definitely startin' to sound good.
Shrek: Hey, come on. I'm scarier than anything we're going to see in this forest.
Fiona: I need to find somewhere to camp right now!
[Bird Wings Fluttering]
Shrek: [Grunting] Hey! Over here.
Donkey: Shrek, we can do better than that. I don't think this is fit for a princess.
Fiona: No, no, it's perfect. It just needs a few homey touches.
Shrek: Homey touches? Like what?
[Crashing]
Fiona: A door. Well, gentlemen, I bid thee good night.
Donkey: You want me to read you a bedtime story? I will.
Fiona: I said, good night!
Donkey: Shrek, what are you doing?
Shrek: [Laughs] I just-- You know-- Oh, come on. I was just kidding.
[Fire Crackling]
Shrek: And, uh, that one, that's Throwback, the only ogre to ever spit over three wheat fields.
Donkey: Right. Yeah. Hey, can you tell my future from these stars?
Shrek: The stars don't tell the future, Donkey. They tell stories. Look, there's Bloodnut, the Flatulent. You can guess what he's famous for.
Donkey: I know you're making this up.
Shrek: No, look. There he is, and there's the group of hunters running away from his stench.
Donkey: Man, that ain't nothin' but a bunch of little dots.
Shrek: Sometimes things are more than they appear. Hmm? Forget it.
Donkey: [Sighs] Hey, Shrek, what we gonna do when we get our swamp anyway?
Shrek: Our swamp?
Donkey: You know, when we're through rescuing the princess.
Shrek: We? Donkey, there is no "we." There's no "our." There's just me and my swamp. The first thing I'm gonna do is build a ten-foot wall around my land.
Donkey: You cut me deep, Shrek. You cut me real deep just now. You know what I think? I think this whole wall thing is just a way to keep somebody out.
Shrek: No. Do ya think?
Donkey: Are you hidin' something?
Shrek: Never mind, Donkey.
Donkey: Oh! This is another one of those onion things, isn't it?
Shrek: No, this is one of those drop-it and leave-it-alone things.
Donkey: Why don't you want to talk about it?
Shrek: Why do you always want to?
Donkey: Why are you blocking?
Shrek: I'm not blocking.
Donkey: Yes, you are.
Shrek: Donkey, I'm warning you.
Donkey: Who you trying to keep out?
Shrek: Everyone! Okay?
Donkey: Now we're gettin' somewhere.
Shrek: Oh! For the love of Pete!
Donkey: What's your problem? What you got against the whole world?
Shrek: Look, I'm not the one with the problem, okay? It's the world that seems to have a problem with me. People take one look at me and go, "Aah! Help! Run! A big, stupid, ugly ogre!" [Sighs] They judge me before they even know me. That's why I'm better off alone.
Donkey: You know what? When we met, I didn't think you was just a big, stupid, ugly ogre.
Shrek: Yeah, I know.
Donkey: So, uh, are there any donkeys up there?
Shrek: Well, there's, um, Gabby, the Small and Annoying.
Donkey: Okay, I see it now. The big shiny one, right there. That one there?
Shrek: That's the moon.
Donkey: Oh, okay.
♪♪ [Orchestra]
♪♪ [Dulcimer]
Farquaad: Again. Show me again.
[Music Stops, Rewinds]
Farquaad: Mirror, mirror, show her to me. Show me the princess.
Mirror: Hmph.
[Rewinds, Resumes]
Farquaad: Ah. Perfect. [Inhales]
[Snoring]
♪♪ [Vocalizing]
♪♪ [Vocalizing Continues]
♪♪ [Whistling]
♪♪ [Whistling Continues]
♪♪ [Vocalizes]
♪♪ [Whistles]
♪♪ [Vocalizes]
♪♪ [Whistles]
♪♪ [Vocalizing]
♪♪ [Whistling]
♪♪ [Vocalizing, High-pitched]
♪♪ [Whistling, High-pitched]
♪♪ [Continues]
[Sizzling]
[Sniffs, Yawns]
Shrek: Mmm, yeah, you know I like it like that.
Donkey: Come on, baby. I said I like it.
Shrek: Donkey, wake up.
Donkey: Huh? What?
Shrek: Wake up.
Donkey: What?
Fiona: Good morning. How do you like your eggs?
Donkey: Good morning, Princess!
Shrek: What's all this about?
Fiona: We kind of got off to a bad start yesterday. I wanted to make it up to you. After all, you did rescue me.
Shrek: Uh, thanks.
[Sniffs]
Fiona: Well, eat up. We've got a big day ahead of us.
[Belches]
Donkey: Shrek!
Shrek: What? It's a compliment. Better out than in, I always say. [Laughs]
Donkey: Well, it's no way to behave in front of a princess.
[Belches]
Fiona: Thanks.
Donkey: She's as nasty as you are.
Shrek: [Laughs] You know, you're not exactly what I expected.
Fiona: Maybe you shouldn't judge people before you get to know them. [Vocalizing]
Monsieur Hood: La liberte! Hey!
Shrek: Princess?
[Laughs]
Fiona: What are you doing?
Monsieur Hood: Be still, cherie, for I am your savior! And I am rescuing you from this green [Kissing Sounds] beast.
Shrek: Hey! That's my princess. Go find your own!
Monsieur Hood: Please, monsters! Can't you see I'm a little busy here?
Fiona: Look, pal. I don't know who you think you are!
Monsieur Hood: Oh! Of course! How rude. Please let me introduce myself. Oh, Merry Men! [Laughs]
♪♪ [Accordion]
Merry Men: ♪ Ta, dah, dah, dah, whoo! ♪
Monsieur Hood: ♪ I steal from the rich and give to the needy. ♪
Man: ♪ He takes a wee percentage. ♪
Monsieur Hood: ♪ But I'm not greedy. I rescue pretty damsels. Man, I'm good. ♪
Merry Men: ♪ What a guy, Monsieur Hood! ♪
Monsieur Hood: ♪ Break it down. I like an honest fight and a saucy little maid. ♪
Merry Men: ♪ What he's basically saying is he likes to get-- ♪
Monsieur Hood: ♪ Paid. ♪
Merry Men: ♪ So. ♪
Monsieur Hood: ♪ When an ogre in the bush grabs a lady by the tush, that's bad. ♪
Merry Men: ♪ That's bad. ♪
Monsieur Hood: ♪ When a beauty's with a beast it makes me awfully mad. ♪
Merry Men: ♪ He's mad. He's really, really mad. ♪
Monsieur Hood: ♪ I'll take my blade and ram it through your heart. Keep your eyes on me, boys 'cause I'm about to start! ♪
[Tarzan Yell]
[Grunts, Groans]
[Karate Yell]
[Merry Men Gasping]
Fiona: [Panting] Man, that was annoying!
Man: Oh, you little--
[Karate Yell]
♪♪ [Accordion]
[Tarzan woman yell]
[Shouting, Groaning]
[Tarzan woman yells about 3 times]
[Groaning]
Fiona: [Chuckles] Um, shall we?
Shrek: Hold the phone.
[Grunts]
Shrek: Oh! Whoa, whoa, whoa. Hold on now. Where did that come from?
Fiona: What?
Shrek: That! Back there. That was amazing! Where did you learn that?
Fiona: Well-- [Chuckles] When one lives alone, uh, one has to learn these things in case there's a-- There's an arrow in your butt!
Shrek: What? Oh, would you look at that?
Fiona: Oh, no. This is all my fault. I'm so sorry.
Donkey: Why? What's wrong?
Fiona: Shrek's hurt.
Donkey: Shrek's hurt. Shrek's hurt? Oh, no, Shrek's gonna die.
Shrek: Donkey, I'm okay.
Donkey: Oh, you can't do this to me. I'm too young for you to die. Keep your legs elevated. Turn your head and cough. Does anyone know the Heimlich?
Fiona: Donkey! Calm down. If you want to help Shrek, run into the woods and find me a blue flower with red thorns.
Donkey: Blue flower, red thorns. Okay. I'm on it. Blue flower, red thorns. Blue flower, red thorns. Don't die, Shrek. If you see a long tunnel, stay away from the light!
Shrek: Donkey!
Donkey: Okay, okay. Blue flower, red thorns. Blue flower, red thorns.
Shrek: What are the flowers for?
Fiona: For getting rid of Donkey.
Shrek: Ah.
Fiona: Now you hold still, and I'll yank this thing out.
Shrek: Ow! Hey! Easy with the yankin'.
Fiona: I'm sorry, but it has to come out.
Shrek: No, it's tender. Now, hold on. What you're doing is the opposite of help.
Fiona: Don't move.
Shrek: Look, time out.
Fiona: Would you-- [Grunts] Okay. What do you propose we do?
Donkey: Blue flower, red thorns. Blue flower, red thorns. Blue flower, red thorns. This would be so much easier if I wasn't color-blind! Blue flower, red thorns.
Shrek: Ow!
Donkey: Hold on, Shrek! I'm comin'!
Shrek: Ow! Not good.
Fiona: Okay. Okay, I can nearly see the head.
[Grunts]
Fiona: It's just about--
Shrek: Ow! Ohh!
Donkey: Ahem.
Shrek: Nothing happened. We were just, uh--
Donkey: Look, if you wanted to be alone, all you had to do was as, okay.
Shrek: Oh, come on! That's the last thing on my mind! The princess here was just-- Ugh! Ow!
Donkey: Hey, what's that? [Nervous Chuckle] That's-- Is that blood? [Sighs]
[Bird Chirping]
[♪ My Beloved Monster By Eels Playing]
[Grunts]
Eels: ♪ My beloved monster and me. We go everywhere together. Wearin' a raincoat that has four sleeves, gets us through all kinds of weather. ♪
Donkey: Aah!
Eels: ♪ She will always be the only thing. That comes between me and the awful sting. That comes from living in the world that's so damn mean. ♪
[Croaks]
Eels: ♪ Oh, oh-oh-oh-oh. ♪
Fiona: Hey!
Eels: ♪ La-la, la-la, la-la-la-la. ♪
[Both Laughing]
Eels: La-la, la-la, la-la.
Shrek: There it is, Princess. Your future awaits you.
Fiona: That's Duloc?
Donkey: Yeah, I know. You know, Shrek thinks Lord Farquaad's compensating for something, which I think means he has a really-- Ow!
Shrek: Um, I, uh-- I guess we better move one.
Fiona: Sure. But, Shrek? I'm-- I'm worried about Donkey.
[Blubbering]
Shrek: What?
Fiona: I mean, look at him. He doesn't look so good.
Donkey: What are you talking about? I'm fine.
Fiona: That's what they always say, and then next thing you know, you're on your back. Dead.
Shrek: You know, she's right. You look awful. Do you want to sit down?
Fiona: I'll make you some tea.
Donkey: I didn't want to say nothin', but I got this twinge in my neck, and when I turn my head like this, look. [Bones Crunch] Ow! See?
Shrek: Who's hungry? I'll find us some dinner.
Fiona: I'll get the firewood.
Donkey: Hey, where you goin'? Oh, man, I can't feel my toes! I don't have any toes! I think I need a hug.
Fiona: Mmm. Mmm. This is good. This is really good. What is this?
Shrek: Uh, weedrat. Rotisserie style.
Fiona: No kidding.
Shrek: Well, this is delicious. Well, they're also great in stews. Now, I don't mean to brag, but I make a mean weedrat stew. [Chuckling]
Donkey: [Sighs] I guess I'll be dining a little differently tomorrow night.
Shrek: [Gulps] Maybe you can come visit me in the swamp sometime. I'll cook all kinds of stuff for you. Swamp toad soup, fish eye tartare-- you name it.
Fiona: [Chuckles] I'd like that.
[Slurps, Laughs]
Donkey: ♪ See the pyramids along the Nile. ♪
Shrek: Um, Princess?
Donkey: ♪ Watch the sunrise from a tropical isle. ♪
Fiona: Yes, Shrek?
Shrek: I, um, I was wondering.
Donkey: ♪ Just remember, darling all the while. ♪
Shrek: Are you--
Donkey: You belong to me.
Shrek: [Sighs] Are you gonna eat that?
[Chuckles]
Donkey: Man, isn't this romantic? Just look at that sunset.
Fiona: Sunset? Oh, no! I mean, it's late. I-It's very late.
Shrek: What?
Donkey: Wait a minute. I see what's goin' on here. You're afraid of the dark, aren't you?
Fiona: Yes! Yes, that's it. I'm terrified. You know, I'd better go inside.
Donkey: Don't feel bad, Princess. I used to be afraid of the dark, too, until-- Hey, no, wait. I'm still afraid of the dark.
[Shrek Sighs]
Fiona: Good night.
Shrek: Good night.
[Door Creaks]
Donkey: Ohh! Now I really see what's goin' on here.
Shrek: Oh, what are you talkin' about?
Donkey: I don't even wanna hear it. Look, I'm an animal, and I got instincts. I know two were diggin' in each other. I could feel it.
Shrek: You're crazy. I'm just bringing her back to Farquaad.
Donkey: Oh, come on, Shrek. Wake up and smell the pheromones. Just go on in and tell her how you feel.
Shrek: I-- There's nothing to tell. Besides, even if I did tell her that, well, you know-- and I'm not sayin' I do 'cause I don't-- she's a princess, and I'm--
Donkey: An ogre?
Shrek: Yeah. An ogre.
Donkey: Hey, where you goin'?
Shrek: To get... more firewood. [Sighs]
Donkey: Princess? Princess Fiona? Princess, where are you?
[Wings Fluttering]
Donkey: Princess?
[Creaking]
Donkey: [Gasps] It's very spooky in here. I ain't playing no games.
[Screams]
Donkey: Aah!
Fiona: Oh, no!
Donkey: No, help!
Fiona: Shh!
Donkey: Shrek! Shrek! Shrek!
Fiona: No, it's okay. It's okay.
Donkey: What did you do with the princess?
Fiona: Donkey, I'm the princess.
Donkey: Aah!
Fiona: It's me, in this body.
Donkey: Oh, my God! You ate the princess! Can you hear me?
Fiona: Donkey!
Donkey: Listen, keep breathing! I'll get you out of there!
Fiona: No!
Donkey: Shrek! Shrek! Shrek!
Fiona: Shh.
Donkey: Shrek!
Fiona: This is me.
Donkey: [Muffled Mumbling] Princess? What happened to you? You're, uh, uh, uh, different.
Fiona I'm ugly, okay?
Donkey: Well, yeah! Was it something you ate? 'Cause I told Shrek those rats was a bad idea. You are what you eat, I said. Now--
Fiona: No. I-- I've been this way as long as I can remember.
Donkey: What do you mean? Look, I ain't never seen you like this before.
Fiona: It only happens when the sun goes down. "By night one way, by day another. This shall be the norm, until you find true love's first kiss, and then take love's true form."
Donkey: Ah, that's beautiful. I didn't know you wrote poetry.
Fiona: It's a spell. [Sighs] When I was a little girl, a witch cast a spell on me. Every night I become this. This horrible, ugly beast! I was placed in a tower to await the day my true love would rescue me. That's why I have to marry Lord Farquaad tomorrow, before the sun sets and he sees me, like this. [Sobs]
Donkey: All right, all right. Calm down. Look, it's not that bad. You're not that ugly. Well, I ain't gonna lie. You are ugly. But you only look like this at night. Shrek's ugly 24-7.
Fiona: But, Donkey, I'm a princess, and this is not how a princess is meant to look.
Donkey: Princess, how 'bout if you don't marry Farquaad?
Fiona: I have to. Only my true love's kiss can break the spell.
Donkey: But, you know, um, you're kind of an ogre, and Shrek-- well, you got a lot in common.
Fiona: Shrek?
Shrek: Princess, I-- Uh, how's going, first of all? Good? Um, good for me too. I'm okay. I saw this flower and thought of you because it's pretty and-- well, I don't really like it, but I thought you might like it 'cause you're pretty. But I like you anyway. I'd-- uh, uh-- [Sighs] I'm in trouble. Okay, here we go.
Fiona: I can't just marry whoever I want. Take a good look at me, Donkey. I mean, really, who could ever love a beast so hideous and ugly? "Princess" and "ugly" don't go together. That's why I can't stay here with Shrek. My only chance to live happily ever after is to marry my true love.
[Deep Sigh]
Fiona: Don't you see, Donkey? That's just how it has to be. It's the only way to break the spell.
Donkey: You at least gotta tell Shrek the truth.
Fiona: No! You can't breathe a word. No one must ever know.
Donkey: What's the point of being able to talk if you gotta keep secrets?
Fiona: Promise you won't tell. Promise!
Donkey: All right, all right. I won't tell him. But you should. I just know before this is over, I'm gonna need a whole lot of serious therapy. Look at my eye twitchin'.
[Door Opens]
[Snoring]
Fiona: I tell him, I tell him not. I tell him, I tell him not. I tell him. Shrek! Shrek, there's something I want--
[Snoring]
Fiona: Shrek. Are you all right?
Shrek: Perfect! Never been better.
Fiona: I-- I don't-- There's something I have to tell you.
Shrek: You don't have to tell me anything, Princess. I heard enough last night.
Fiona: You heard what I said?
Shrek: Every word.
Fiona: I thought you'd understand.
Shrek: Oh, I understand. Like you said, "Who could love a hideous, ugly beast?"
Fiona: But I thought that wouldn't matter to you.
Shrek: Yeah? Well, it does.
[Gasps, Sighs]
Shrek: Ah, right on time.
[Horse Whinnies]
Shrek: Princess, I've brought you a little something.
♪♪ [Fanfare]
Donkey: [Yawns] What'd I miss? What'd I miss? [Muffled] Who said that? Couldn't have been a donkey.
Farquaad: Princess Fiona.
Shrek: As promised. Now hand it over.
Farquaad: Very well, ogre. The deed to your swamp, cleared out, ad agreed. Take it and go before I change my mind. Forgive me, Princess, for startling you, but you startled me, for I have ever seen such a radiant beauty before. I am Lord Farquaad.
Fiona: Forgive me, my lord, for I was just saying, a short, farewell.
Farquaad: That's so sweet. You don't have to waste good manners on the ogre. It's not like it has feelings.
Fiona: No, you're right. It doesn't.
Farquaad: Princess Fiona, beautiful, fair, flawless Fiona. I ask your hand in marriage.
[Gasps]
Farquaad: Will you be the perfect bride for the perfect groom?
Fiona: Lord Farquaad, I accept. Nothing would make.
Farquaad: Excellent! I'll start the plans, for tomorrow we wed!
Fiona: No! I mean, uh, why wait? Let's get married today before the sun sets.
Farquaad: Oh, anxious, are we? You're right. The sooner, the better. There's so much to do! There's the caterer, the cake, the band, the guest list. Captain, round up some guests!
Fiona: Fare-thee-well, ogre.
Donkey: Shrek, what are you doing? You're letting her get away.
Shrek: Yeah? So what?
Donkey: Shrek, there's something about her you don't know. Look, I talked to her last night. She's--
Shrek: I know you talked to her last night. You're great pals, aren't ya? Now, if you two are such good friends, why don't you follow her home?
Donkey: Shrek, I-- I wanna go with you.
Shrek: I told you, didn't I? You're not coming home with me. I live alone! My swamp! Me! Nobody else! Understand? Nobody! Especially useless, pathetic, annoying, talking donkeys!
Donkey: But I thought--
Shrek: Yeah. You know what? You thought wrong!
Donkey: Shrek.
[♪ Hallelujah By John Cale Playing]
John Cale: ♪ I heard there was a secret chord, that David played, and it pleased the Lord. But you don't really care for music, do ya? It goes like this the fourth, the fifth, the minor fall the major lift. The baffled king composing hallelujah. Hallelujah, hallelujah, hallelujah, hallelujah. Baby, I've been here before, I know this room I've walked this floor, I used to live alone before I knew you. I've seen your flag on the marble arch, but love is not a victory march. It's a cold and it's broken hallelujah. Hallelujah, hallelujah, hallelujah, hallelujah. And all I ever learned from love is how to shoot at someone who outdrew you. ♪
[Moaning]
John Cale: ♪ And it's not a cry you can hear at night, it's not somebody who's seen the light. It's a cold and it's a broken hallelujah. ♪
[Moaning]
John Cale: ♪ Hallelujah, hallelujah, hallelujah, hallelujah. ♪
[Thumping Sound]
Shrek: Donkey?
[Grunts]
Shrek: What are you doing?
Donkey: I would think, of all people, you would recognize a wall when you see one.
Shrek: Well, yeah. But the wall's supposed to go around my swamp, not through it.
Donkey: It is. Around your half. See, that's your half, and this is my half.
Shrek: Oh! Your half. Hmm.
Donkey: Yes, my half. I helped rescue the princess. I did half the work. I get half the booty. Now hand me that big old rock, the one that looks like your head.
Shrek: Back off!
Donkey: No, you back off.
Shrek: This is my swamp!
Donkey: Our swamp.
Shrek: Let go, Donkey!
Donkey: You let go.
Shrek: Stubborn jackass!
Donkey: Smelly ogre.
Shrek: Fine!
Donkey: Hey, come back here. I'm not through with you yet.
Shrek: Well, I'm through with you.
Donkey: Uh-uh. You know, with you it's always, "Me, me, me!" Well, guess what! Now it's my turn! So you just shut up and pay attention! You are mean to me. You insult me and you don't appreciate anything that I do! You're always pushing me around or pushing me away.
Shrek: Oh, yeah? Well, if I treated you so bad, how come you came back?
Donkey: Because that's what friends do! They forgive each other!
Shrek: Oh, yeah. You're right, Donkey. I forgive you, for stabbin' me in the back!
Donkey: Ohh! You're so wrapped up in layers, onion boy, you're afraid of your own feelings.
Shrek: Go away!
Donkey: There you are, doing it again just like you did to Fiona. All she ever do was like you, maybe even love you.
Shrek: Love me? She said I was ugly, a hideous creature. I heard the two of you talking.
Donkey: She wasn't talkin' about you. She was talkin' about, uh, somebody else.
Shrek: She wasn't talking about me? Well, then who was she talking about?
Donkey: Uh-uh, no way. I ain't saying anything. You don't wanna listen to me. Right? Right?
Shrek: Donkey!
Donkey: No!
Shrek: Okay, look. I'm sorry, all right?
Donkey: Hmph.
Shrek: [Sighs] I'm sorry. I guess I am just a big, stupid, ugly ogre. Can you forgive me?
Donkey: Hey, that's what friends are for, right?
Shrek: Right. Friends?
Donkey: Friends.
Shrek: So, um, what did Fiona say about me?
Donkey: What are you asking me for? Why don't you just go ask her?
Shrek: The wedding! We'll never make it in time.
Donkey: Ha-ha-ha! Never fear, for where there's a will, there's a way, and I have a way. [Whistles]
Shrek: Donkey?
[Donkey Laughing]
Donkey: I guess it's just an animal magnetism.
Shrek: [Laughing] Aw, come here, you.
Donkey: All right, all right. Don't get all slobbery. No one likes a kiss ass. All right, hop on and hold on tight. I haven't had a chance to install the seat belts yet. [Donkey Laughing] Whoo!
[Bells Tolling]
[All Gasping]
Bishop: People of Duloc, we gather here today, to bear witness, to the union...
Fiona: Um-- of our now king--
Bishop: Excuse me.
Fiona: Could we just skip ahead to the "I do's"?
Farquaad: [Chuckling] Go on.
Donkey: Go ahead, have some fun. If we need you, I'll whistle. How about that? Shrek, wait, wait! Wait a minute! You wanna do this right, don't you?
Shrek: What are you talking about?
Donkey: There's a line you gotta wait for. The preacher's gonna say, "Speak now or forever hold your peace." That's when you say, "I object!"
Shrek: I don't have time for this!
Donkey: Wait. What are you doing? Listen to me! Look, you love this woman, don't you?
Shrek: Yes.
Donkey: You wanna hold her?
Shrek: Yes.
Donkey: Please her?
Shrek: Yes!
Donkey: ♪ Then you got to, got to try a little tenderness. ♪ The chicks love that romantic crap!
Shrek: All right! Cut it out. When does this guy say the line?
Donkey: We gotta check it out.
[Donkey Grunting]
Bishop: And so, by the power vested in me...
Shrek: What do you see?
Donkey: The whole town's in there.
Bishop: ...I now pronounce you husband and wife...
Donkey: They're at the altar.
Bishop: ...king and queen.
Donkey: Mother Fletcher! He already said it.
Shrek: Oh, for the love of Pete!
[Grunts]
Shrek: I object!
Fiona: Shrek?
[Gasps]
Farquaad: Oh, now what does he want?
[Crowd Clamoring]
Shrek: Hi, everyone. Havin' a good time, are ya? I love Duloc, first of all. Very clean.
Fiona: What are you doing here?
Farquaad: Really, it's rude enough being alive when no one wants you, but showing up uninvited to a wedding--
Shrek: Fiona! I need to talk to you.
Fiona: Oh, now you wanna talk? It's a little late for that, so if you'll excuse me--
Shrek: But you can't marry him.
Fiona: And why not?
Shrek: Because-- Because he's just marrying you so he can be king.
Farquaad: Outrageous! Fiona, don't listen to him.
Shrek: He's not your true love.
Fiona: And what do you know about true love?
Shrek: Well, I-- Uh-- I mean--
Farquaad: Oh, this is precious. [Chuckling] The ogre has fallen in love with the princess! Oh, good Lord.
[Crowd Laughing]
Farquaad: An ogre and a princess! [Laughing Continues]
Fiona: Shrek, is this true?
Farquaad: Who cares? It's preposterous! Fiona, my love, we're but a kiss away from our "happily ever after." Now kiss me! Mmmm!
Fiona: "By night one way, by day another." I wanted to show you before.
[Whimpers]
[Crowd Gasping]
Shrek: Well, uh, that explains a lot.
Farquaad: Ugh! It's disgusting! Guards! Guards! I order you to get that out of my sight now! Get them! Get them both!
Fiona: No, no! Shrek!
Farquaad: This hocus-pocus alters nothing. This marriage is binding, and that makes me king! See? See?
Fiona: No, let go of me, Shrek!
Shrek: No!
Farquaad: Don't just stand there, you morons.
Shrek: Get out of my way! Fiona! Arrgh!
Farquaad: I'll make you regret the day we met. I'll see you drawn and quartered! You'll beg for death to save you!
Fiona: No! Shrek!
Farquaad: And as for you, my wife,
Shrek: Fiona!
Farquaad: I'll have you locked back in that tower for the rest of your days! I am king!
[Whistles]
Farquaad: I will have order! I will have perfection! I will have-- Aaah! Aah!
Donkey: All right. Nobody move. I got a dragon here, and I'm not afraid to use it.
[Dragon Roars]
Donkey: I'm a donkey on the edge!
[Belches]
Donkey: [Donkey Laughs] Celebrity marriages. They never last, do they?
[Cheering]
Donkey: Go ahead, Shrek.
Shrek: Uh, Fiona?
Fiona: Yes, Shrek?
Shrek: I-- I love you.
Fiona: Really?
Shrek: Really, really.
Fiona: I love you too.
All: Aawww!
Fiona: "Until you find true love's first kiss, and then take love's true form." [Echoing] [Echoing Continues] "Take love's true from. Take love's true form."
Shrek: Fiona? Fiona. Are you all right?
Fiona: Well, yes. But I don't understand. I'm supposed to be beautiful.
Shrek: But you are beautiful.
[Chuckles]
Donkey: I was hoping would be a happy ending.
[♪ I'm A Believer By Smash Mouth Playing]
Steve Harwell: ♪ I thought love was only true in fairy tales. ♪
All: Oy!
Steve Harwell: ♪ Meant for someone else but not for me. Love was out to get me, that's the way it seemed, disappointment haunted all my dreams. And then I saw her face. Now I'm a believer. And not a trace. Of doubt in my mind. I'm in love. ♪
Choir: ♪ Ohh-ahh. ♪
Steve Harwell: ♪ I'm a believer I couldn't leaver her if I tried. ♪
Gingy: God bless us, every one.
Donkey: Come on, y'all! ♪ Then I saw her face. ♪ Ha-ha! ♪ Now I'm a believer. ♪ Listen! Not a trace. ♪ Of doubt in my mind. I'm in love. Ooh-ahh. I'm a believer I couldn't leave her if I tried. ♪
Mice: Ooh! Uh!
Donkey: ♪ Then I saw her face! Now I'm a believer! Hey! Not a trace. Uhh! Yeah. Of doubt in my mind. One more time! I'm in love. I'm a believer. Come on! I believe, I believe, I believe, I believe, I believe, I believe, I believe, I believe, I believe, hey! Y'all sing it with me! I believe! I believe! People in the back! I believe! ♪
Smash Mouth: ♪ I'm a believer. ♪
Donkey: ♪ I believe. I believe. I believe! ♪ [Hysterical Laughing] Oh, that's funny. Oh. Oh. I can't breathe. I can't breathe.'''
    text = script.split('\n')
    for line in text:
        await ctx.send(line)

@Crystal.command(name="chikachika")
async def chikachika(ctx):
    await ctx.message.delete()
    await ctx.channel.send("https://cdn.discordapp.com/attachments/769632571092762684/836362078150852644/Chika_dance.mp4")

@Crystal.command()
async def hentaipussy(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/pussy')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Hentai Pussy', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def hentaikuni(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/kuni')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Hentai Kuni', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def hentaitits(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/tits')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Hentai Tits', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def hentaiketa(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/keta')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Hentai Keta', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def hentaikemonomimi(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/kemonomimi')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Hentai Kemonomimi', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def hentaigasm(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/gasm')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Hentai Gasm', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def goose(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/goose')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Goose', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def slap(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/slap')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Slap', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def pat(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/pat')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Pat', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def poke(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/poke')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Poke', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def tickle(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/tickle')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Tickle', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def cuddle(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/cuddle')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Cuddle', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def smug(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/smug')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Smug', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def baka(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/baka')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Baka', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def futanari(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/futanari')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Futanari', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def kiss(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/kiss')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Kiss', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


    
@Crystal.command()
async def cum(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/cum')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Cum', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def trap(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekos.life/api/v2/img/trap')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Trap', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)




@Crystal.command()
async def hentai(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=hentai')
        data = request.json()
        link = data['message']
        embed= discord.Embed(title=f'Hentai', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)



@Crystal.command()
async def hentaianal(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=hanal')
        data = request.json()
        link = data['message']
        embed= discord.Embed(title=f'Hentai Anal', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)



@Crystal.command()
async def hentaiboobs(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=hboobs')
        data = request.json()
        link = data['message']
        embed= discord.Embed(title=f'Hentai Boobs', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


    
@Crystal.command()
async def hentaitentacle(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=tentacle')
        data = request.json()
        link = data['message']
        embed= discord.Embed(title=f'Hentai Tentacle', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def porngif(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=pgif')
        data = request.json()
        link = data['message']
        embed= discord.Embed(title=f'Porn Gif', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)



@Crystal.command()
async def meme(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://meme-api.herokuapp.com/gimme')
        data = request.json()
        link = data['url']
        title = data['title']
        embed= discord.Embed(title=title, color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)



@Crystal.command()
async def uselessfact(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://uselessfacts.jsph.pl/random.json?language=en')
        data = request.json()
        fact = data['text']
        embed= discord.Embed(title='Useless Fact', description=f'> {fact}', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)



@Crystal.command()
async def dogfact(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://some-random-api.ml/facts/dog')
        data = request.json()
        fact = data['fact']
        embed= discord.Embed(title='Dog Fact', description=f'{fact}', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)



@Crystal.command()
async def catfact(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://catfact.ninja/fact')
        data = request.json()
        fact = data['fact']
        embed= discord.Embed(title='Cat Fact', description=f'{fact}', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)



@Crystal.command()
async def dadjoke(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
        data = request.json()
        joke = data['joke']
        embed= discord.Embed(title='Dad Joke', description=f'{joke}', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)



@Crystal.command()
async def joke(ctx):
        await ctx.message.delete()
        request = requests.get(f'http://www.official-joke-api.appspot.com/random_joke')
        data = request.json()
        setup = data['setup']
        punchline = data['punchline']
        embed= discord.Embed(title='Joke', description=f'{setup}\n||{punchline}||', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def lyrics(ctx, *, title: str):
        await ctx.message.delete()
        try:
            request = requests.get(f'https://some-random-api.ml/lyrics?title={urllib.parse.quote(title)}')
            data = request.json()
            lyrics = data['lyrics']
            if len(lyrics) < 1950:
                embed= discord.Embed(title=f"{data['author']} - {data['title']}", description=lyrics, color=0x9F00FB)
                embed.set_footer(text="Crystal")
                embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
                await ctx.send(embed=embed)


            else:
                embed= discord.Embed(title=f"{data['author']} - {data['title']}", description=lyrics[:1950], color=0x9F00FB)
                embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
                embed.set_footer(text="Crystal")
                await ctx.send(embed=embed)


                
                embed2= discord.Embed(description=lyrics[1950:3900], color=0x9F00FB)
                embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
                embed.set_footer(text="Crystal")
                await ctx.send(embed=embed2)


        except Exception:
            return

@Crystal.command()
async def cocksize(ctx, *users: discord.User):
        await ctx.message.delete()
        try:
            if not users:
                users = [ctx.author]

            dongs = {}
            msg = ""
            state = random.getstate()

            for user in users:
                random.seed(user.id)
                dongs[user] = "8{}D".format("=" * random.randint(0, 30))

            random.setstate(state)
            dongs = sorted(dongs.items(), key=lambda x: x[1])

            for user, dong in dongs:
                msg += "**{}'s size:**\n{}\n".format(user.display_name, dong)

            embed = discord.Embed(title='Cock Size', description=msg, color=0x9F00FB)
            embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
            embed.set_footer(text="Crystal")
            await ctx.send(embed=embed)


        except Exception:
            return
            
@Crystal.command()
async def dice(ctx, sides: int=6):
        await ctx.message.delete()
        result = str(random.randint(1, sides))
        embed = discord.Embed(title='Dice', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        embed.add_field(name=f'Sides', value=f'{sides}', inline=False)
        embed.add_field(name=f'Result', value=f'{result}', inline=False)
        await ctx.send(embed=embed)

@Crystal.command()
async def spamwebhook(ctx, webhook):  
        await ctx.message.delete()  
        embed = discord.Embed(title='Spam Webhook', color=0x9F00FB)
        embed.add_field(name=f'__🔗 Spamming Webhook__', value=f'{webhook}', inline=True)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

    
        payload = json.dumps({
        "content": "@everyone",
        "embeds": [
            {
            "title": "Crystal Webhook Spammer",
            "color": 0x9F00FB,
            "thumbnail": {
                "url": "https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif"
            },
            "footer": {
                "text": "Crystal Selfbot"
            }
            }
        ]

        })
        try:
            for i in range(0, 300):
                async with httpx.AsyncClient() as client:
                    await client.post(webhook, data=payload.encode(), headers={'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'})
        except Exception:
            pass

@Crystal.command()
async def howgay(ctx, *, user: discord.User=None):
        await ctx.message.delete()
        if user is None:
            member = ctx.author
        else:
            member = user

        random.seed(member.id)
        embed = discord.Embed(title=f'How Gay is {member}', description=f'{member} is { random.randint(0, 100) }% Gay!', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def howcorona(ctx, *, user: discord.User=None):
        await ctx.message.delete()
        if user is None:
            member = ctx.author
        else:
            member = user

        random.seed((member.id * 6) / 2)
        percent = random.randint(0, 100)
        embed = discord.Embed(title=f'Corona Test', description=f'{member} is {percent}% Corona positive!\n\nOverall: {"**Positive**" if (percent > 50) else "**Negative**"}', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
        
@Crystal.command()
async def howcap(ctx, *, user: discord.User=None):
        await ctx.message.delete()
        if user is None:
            member = ctx.author
        else:
            member = user

        random.seed((member.id * 4.5) / 2)
        percent = random.randint(0, 100)
        embed = discord.Embed(title=f'How Cap', description=f'{member} is {percent}% capping!', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def lovecalc(ctx, user1: discord.User, user2: discord.User):
        await ctx.message.delete()
        random.seed((user1.id + user2.id) / 2)
        embed = discord.Embed(title=f'Love Calculator', description=f'{user1} and {user2} are { random.randint(0, 100) }% compatible!', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def iq(ctx, *, user: discord.User=None):
        await ctx.message.delete()
        if user is None:
            member = ctx.author
        else:
            member = user

        random.seed(member.id * 3)
        embed = discord.Embed(title=f'IQ Test', description=f'{member}\'s IQ is { random.randint(30, 140) }!', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def insult(ctx, *, user: discord.User=None):
        await ctx.message.delete()
        if user is None:
            member = ctx.author
        else:
            member = user

        insult = requests.get(f'https://insult.mattbas.org/api/insult')    
        
        embed = discord.Embed(title=f'Insult for {member}', description=f'> {member}, {insult.content.decode("ascii")}', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def kanyequote(ctx):
        await ctx.message.delete()
        info = requests.get(f'https://api.kanye.rest/')    
        quote = info.json()['quote']
        embed = discord.Embed(title=f'Kanye West Quote', description=f'> {quote}', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)



@Crystal.command()
async def chucknorrisjoke(ctx):
        await ctx.message.delete()
        info = requests.get(f'https://api.chucknorris.io/jokes/random')    
        joke = info.json()['value']
        embed = discord.Embed(title=f'Chuck Norris Joke', description=f'{joke}', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def trumpquote(ctx):
        await ctx.message.delete()
        info = requests.get(f'https://tronalddump.io/random/quote')    
        quote = info.json()['value']
        
        embed = discord.Embed(title=f'Donald Trump Quote', description=f'> {quote}', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def texttobinary(ctx, *, text):
        await ctx.message.delete()
        info = requests.get(f'https://no-api-key.com/api/v1/binary?text={urllib.parse.quote(text)}')    
        binary_text = info.json()['binary']
        
        embed = discord.Embed(title=f'Text to Binary', color=0x9F00FB)
        embed.add_field(name = "Text", value = f"{text}")
        embed.add_field(name = "Binary", value = f"{binary_text}")
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def binarytotext(ctx, *, binary):
        await ctx.message.delete()
        info = requests.get(f'https://no-api-key.com/api/v1/binary-text?binary={urllib.parse.quote(binary)}')    
        text = info.json()['text']
        
        embed = discord.Embed(title=f'Binary to Text', color=0x9F00FB)
        embed.add_field(name = "Binary", value = f"{binary}")
        embed.add_field(name = "Text", value = f"{text}")
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def amazonsearch(ctx, *, product: str):
        await ctx.message.delete()
        embed = discord.Embed(title='Amazon Search Results', description=f'Here are your search results for [{product}](https://amazon.com/s?k={urllib.parse.quote(product)})', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command()
async def revavatar(ctx, *, user: discord.User):
        await ctx.message.delete()
        try:
            embed = discord.Embed(title='Reverse Avatar', description=f'Here are the [results](https://images.google.com/searchbyimage?image_url={urllib.parse.quote(str(user.avatar_url))}) for {user.mention}\'s avatar.', color=0x9F00FB)
            embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
            embed.set_footer(text="Crystal")
            await ctx.send(embed=embed)
        except Exception:
            pass

@Crystal.command()
async def revimage(ctx, *, url: str):
        await ctx.message.delete()
        try:
            embed = discord.Embed(title='Reverse Image Search', description=f'Here are the [results](https://images.google.com/searchbyimage?image_url={urllib.parse.quote(url)}) for the image.', color=0x9F00FB)
            embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
            embed.set_footer(text="Crystal")
            await ctx.send(embed=embed)
        except Exception:
            pass

@Crystal.command()
async def pornsearch(ctx, *, query: str):
        await ctx.message.delete()
        try:
            embed = discord.Embed(title='Porn Search', description=f'Here are the [results](https://just-tit.com/{urllib.parse.quote(query)}.html) for **{query}**.', color=0x9F00FB)
            embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
            embed.set_footer(text="Crystal")
            await ctx.send(embed=embed)
        except Exception:
            pass

@Crystal.command()
async def youtubesearch(ctx, *, search: str):
        await ctx.message.delete()    
        embed = discord.Embed(title='YouTube Search Results', description=f'Here are your search results for [{search}](https://www.youtube.com/results?search_query={urllib.parse.quote(search)})', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def googlesearch(ctx, *, search: str):
        await ctx.message.delete()    
        embed = discord.Embed(title='Google Search Results', description=f'Here are your search results for [{search}](https://www.google.com/search?q={urllib.parse.quote(search)})', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


    
@Crystal.command()
async def pornhubsearch(ctx, *, search: str):
        await ctx.message.delete()   
        embed = discord.Embed(title='PornHub Search Results', description=f'Here are your search results for [{search}](https://www.pornhub.com/video/search?search={urllib.parse.quote(search)})', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def steamsearch(ctx, *, search: str):
        await ctx.message.delete()    
        embed = discord.Embed(title='Steam Search Results', description=f'Here are your search results for [{search}](https://store.steampowered.com/search/?term={urllib.parse.quote(search)})', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def githubsearch(ctx, *, search: str):
        await ctx.message.delete()   
        embed = discord.Embed(title='GitHub Search Results', description=f'Here are your search results for [{search}](https://github.com/search?q={urllib.parse.quote(search)})', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def stackoverflowsearch(ctx, *, search: str):
        await ctx.message.delete()
        embed = discord.Embed(title='StackOverflow Search Results', description=f'Here are your search results for [{search}](https://stackoverflow.com/search?q={urllib.parse.quote(search)})', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def wikisearch(ctx, *, search: str):
        await ctx.message.delete()
        embed = discord.Embed(title='Wikipedia Search Results', description=f'Here are your search results for [{search}](https://wikipedia.org/w/index.php?search={urllib.parse.quote(search)})', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)



@Crystal.command()
async def lmgtfy(ctx, *, search: str):
        await ctx.message.delete()
        embed = discord.Embed(title='I\'ve Googled that for you', description=f'Click [here](https://lmgtfy.com/?q={urllib.parse.quote(search)}&iie=1) to find out **{search}**', color=0x9F00FB)
        embed.set_thumbnail(url="https://media.giphy.com/media/Q5w2ItO7cdzFe/giphy.gif")
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

@Crystal.command(name='911')
async def _911(ctx):
        await ctx.message.delete()
        
        first = r'''                     ,-------------------.
                ,'                    ;
                ,'                    .'|
            ,'                    .'# |
            ,'                    .'# # |
            :-------------------.'# # # | 
            | # # # # # # # # # | # # # |
            | # # # # # # # # # | # # # |
            | # # # # # # # # # | # # # |
            | # # # # # # # # # | # # # |
            | # # # # # # # # # | # # # |
            | # # # # # # # # # | # # # |
            | #,-'. # # # # # # | # # # |
            |_/'  / # # # # # # | # # # |
    _.--""     /_ # # # # # # | # # #  
    '__.--,       `-.# # # # # | # #    
        /  /''`--.__; # # # # | #      
    _,|\ ,'  # # # # # # # # #|       
    `--|._`.                            '''
        second = r'''                        ,-------------------.
                    ,'                    ;
                ,'                    .'|
                ,'                    .'# |
            ,'                    .'# # |888
            :-------------------.'# # # |)(888)
            | # # # # # # # # # | # # # |8888)(8)
            | # # # # # # # # # | # # # |88)(88) 
            '  | # # # # # # # # # | # # # |8)(88)  
        |  / - , # ####### # # # # | # # # |(8)
    -   / , .   ############# # # | # # # |   
    \  -  ,  '#################  | # # # |
    -  .  /  \ /############## #  | # # # |
            .  - / # # # # # # # | # # # |
            | # # # # # # # # # | # # # |
            | # # # # # # # # # | # # # |
            | # # # # # # # # # | # # #
            | # # # # # # # # # | # #  
            | # # # # # # # # # | # 
            | # # # # # # # # # |      '''

        third = r'''                    ,-------------------.     
                ,'                    ;  '::
            ,'                    .'|'::::
        ::.: ,'                    .'# |::::':
    ':':.: ,'                    .'# # |::':::'
    :'. : :-------------------.'# # # |':::'::
    :::.:| # # # # # # # # # | # # # |:::::'
    ::.:..| # # # # # # # # # | # # # |::'
    `:;.::'| # # # # # # # # # | # # # |
    '::..:'| #.:::.. # # # # # | # # # |
    :::::|.,:.:::::::..::# # | # # # |
    `:::::::::::.::..:#::::.# | # # # |
    `:':::`::'.::::. :: # # | # # # |
    ,`::::::::::'::'::' # # | # # # |
    `:;.::'| # # # # # # # # # | # # # |
        | # # # # # # # # # | # # # |
        | # # # # # # # # # | # # # 
        | # # # # # # # # # | # #   
        | # # # # # # # # # | #     
        | # # # # # # # # # |       '''
        embed = discord.Embed(description=f"```{first}```", color=0x9F00FB)
        embed.set_footer(text="Crystal")
        firstsent = await ctx.send(embed=embed, delete_after=5)


        await asyncio.sleep(1)
        embed2 = discord.Embed(description=f"```{second}```", color=0x9F00FB)
        embed2.set_footer(text="Crystal")
        await firstsent.edit(embed=embed2)

        await asyncio.sleep(1)
        embed3 = discord.Embed(description=f"```{third}```", color=0x9F00FB)
        embed3.set_footer(text="Crystal")
        await firstsent.edit(embed=embed3)

@Crystal.command()
async def boobs(ctx):
        await ctx.message.delete()        
        request = requests.get(f'http://api.oboobs.ru/noise')
        data = request.json()
        path = data[0]['preview']
        link = f'http://media.oboobs.ru/{path}'
        embed= discord.Embed(title=f'Boobs', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)



@Crystal.command()
async def yaoi(ctx):
        await ctx.message.delete()    
        request = requests.get(f'https://nekobot.xyz/api/image?type=yaoi')
        data = request.json()
        link = data['message']
        embed= discord.Embed(title=f'Yaoi', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)



@Crystal.command()
async def ass(ctx):
        await ctx.message.delete()    
        request = requests.get(f'https://nekobot.xyz/api/image?type=ass')
        data = request.json()
        link = data['message']
        embed= discord.Embed(title=f'Ass', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)



@Crystal.command()
async def hentaiass(ctx):
        await ctx.message.delete()    
        request = requests.get(f'https://nekobot.xyz/api/image?type=hass')
        data = request.json()
        link = data['message']
        embed= discord.Embed(title=f'Hentai Ass', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)



@Crystal.command()
async def food(ctx):
        await ctx.message.delete()    
        request = requests.get(f'https://nekobot.xyz/api/image?type=food')
        data = request.json()
        link = data['message']
        embed= discord.Embed(title=f'Food', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)



@Crystal.command()
async def anal(ctx):
        await ctx.message.delete()    
        request = requests.get(f'https://nekobot.xyz/api/image?type=anal')
        data = request.json()
        link = data['message']
        embed= discord.Embed(title=f'Anal', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


            
@Crystal.command()
async def blowjob(ctx):
        await ctx.message.delete()    
        request = requests.get(f'https://nekos.life/api/v2/img/blowjob')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Blowjob', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def feet(ctx):
        await ctx.message.delete()    
        request = requests.get(f'https://nekos.life/api/v2/img/feet')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Feet', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


        
@Crystal.command()
async def waifu(ctx):
        await ctx.message.delete()    
        request = requests.get(f'https://nekos.life/api/v2/img/waifu')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Waifu', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)


    
@Crystal.command()
async def wallpaper(ctx):
        await ctx.message.delete()    
        request = requests.get(f'https://nekos.life/api/v2/img/wallpaper')
        data = request.json()
        link = data['url']
        embed= discord.Embed(title=f'Wallpaper', color=0x9F00FB)
        embed.set_image(url=link)
        embed.set_footer(text="Crystal")
        await ctx.send(embed=embed)

if __name__ == '__main__':
    Init()
