import discord
from discord import embeds
from discord.client import Client
from discord.ext import commands
from discord.utils import valid_icon_size
from discord_ui.components import Button, Component
import youtube_dl
from os import replace
import urllib.request
import json
from pytube import YouTube
from bs4 import BeautifulSoup
import os
from bs4 import BeautifulSoup
import requests
import datetime
import os
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
import discord.ext.commands as commands
import time
import wikipedia
import random
import wolframalpha
import giphy_client
from giphy_client.rest import ApiException
import DiscordUtils
from discord.ext.commands import has_permissions, MissingPermissions
from discord_buttons_plugin import*
import asyncio
from discord.utils import get

user="Night Wolf#6328"

Role="Sillaki'S"



server_id=913073298940776508

newMemberMessage = "New Member Joined"
given_name= "vanakamu-ley"

FFMPEG_OPTIONS = {
	'before_options':
	'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
	'options': '-vn'
}

YDL_OPTIONS = {'format': "bestaudio"}

def get_prefix(client,message):
    with open('prefix.json','r')as f:
        prefixes=json.load(f)
    return prefixes[str(message.guild.id)]

intents = discord.Intents.default()

intents.members = True

client=commands.Bot(command_prefix=get_prefix,intents=intents)#Beats
client.remove_command("help")

@client.event
async def on_ready():
    print("Logged in as", client.user.name)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="bthelp"))
    


@client.event
async def on_member_join(member):
    with open("Wel_Role_ID.json", 'r') as f:
        data = json.load(f)
    Member_Joined_Role=data['Name']
    role = get(member.guild.roles,name=Member_Joined_Role)
    await member.add_roles(role)
    guild = client.guilds[0]
    
    Channel_Name="vanakamu-ley"
    try:
        given_name= Channel_Name
        for channel in member.guild.channels:
            if channel.name == given_name:
                wanted_channel_id = channel.id
        try:
            channel = client.get_channel(wanted_channel_id)
            try:
                embed = discord.Embed(colour=discord.Colour.green())
                embed.set_author(name=member.name, icon_url=member.avatar_url)
                embed.add_field(name="Welcome" ,value=f"**Hey,{member.mention}! Welcome to {member.guild.name}\nThanks for joining**", inline=False)
                embed.set_thumbnail(url=member.guild.icon_url)
                await channel.send(embed=embed)
                
            except Exception as e:
                raise e
        except Exception as e:
            raise e
    except Exception:
            
        channel = await guild.create_text_channel(Channel_Name)
        given_name= Channel_Name
        for channel in member.guild.channels:
            if channel.name == given_name:
                wanted_channel_id = channel.id
        try:
            channel = client.get_channel(wanted_channel_id)
            try:
                embed = discord.Embed(colour=discord.Colour.green())
                embed.set_author(name=member.name, icon_url=member.avatar_url)
                embed.add_field(name="Welcome" ,value=f"**Hey,{member.mention}! Welcome to {member.guild.name}\nThanks for joining**", inline=False)
                embed.set_thumbnail(url=member.guild.icon_url)
                await channel.send(embed=embed)
                member : discord.Member 

            except Exception as e:
                raise e
        except Exception as e:
            raise e

@client.event
async def on_member_remove(member):
    guild = client.guilds[0]
    if(guild.id==server_id):
        Channel_Name="bye-bye"
        try:
            given_name= Channel_Name
            for channel in member.guild.channels:
                if channel.name == given_name:
                    wanted_channel_id = channel.id
            try:
                channel = client.get_channel(wanted_channel_id)
                try:
                    embed = discord.Embed(colour=discord.Colour.red())
                    embed.set_author(name=member.name, icon_url=member.avatar_url)
                    embed.add_field(name="Bye-Bye", value=f"**{member.mention} just left The Server.**", inline=False)
                    embed.set_thumbnail(url=member.guild.icon_url)
                    await channel.send(embed=embed)
                except Exception as e:
                    raise e
            except Exception as e:
                raise e

        except Exception:
            guild = client.guilds[0]
            channel = await guild.create_text_channel(Channel_Name)
            given_name= Channel_Name
            for channel in member.guild.channels:
                if channel.name == given_name:
                    wanted_channel_id = channel.id
            try:
                channel = client.get_channel(wanted_channel_id)
                try:
                    embed = discord.Embed(colour=discord.Colour.red())
                    embed.set_author(name=member.name, icon_url=member.avatar_url)
                    embed.add_field(name="Bye-Bye", value=f"**{member.mention} just left The Server.**", inline=False)
                    embed.set_thumbnail(url=member.guild.icon_url)
                    await channel.send(embed=embed)
                except Exception as e:
                    raise e
            except Exception as e:
                raise e




@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if message.content.startswith('bthelp'):
        with open('prefix.json','r')as f:
            prefixes=json.load(f)
        p=prefixes[str(message.guild.id)]
        author=message.author


        embed=discord.Embed(colour=discord.Colour.random())
        
        embed.set_author(name='Help')
        embed.add_field(name='Changing Prefix Command',value='ChangePrefix',inline=False)
        embed.add_field(name='Joining Voice Channel Command',value='join',inline=False)
        embed.add_field(name='Leaving Voice Channel Command',value='leave',inline=False)
        embed.add_field(name='Playing Audio Command',value='p,pl,pla,P,Pl,Pla,PLAY,play',inline=False)
        embed.add_field(name='Pausing Audio Command',value='pause,pe,pa,pu',inline=False)
        embed.add_field(name='Resuming Audio Command',value='resume,re',inline=False)
        embed.add_field(name= 'Stoping Audio Command',value='stop,st,stp',inline=False)
        embed.add_field(name= 'Loop Audio Command',value='loop',inline=False)
        embed.add_field(name= 'Playlist For YouTube',value='ytpl',inline=False)
        embed.add_field(name= 'Skip Audio Command',value='skip',inline=False)
        embed.add_field(name= 'Volume Command',value='volume,vol',inline=False)
        embed.add_field(name= 'Remove Audio Command',value='remove,rem,rv',inline=False)
        embed.add_field(name= 'Weather Command',value='Weather',inline=False)
        embed.add_field(name= 'Calculator Command',value='calc',inline=False)
        embed.add_field(name= 'Time Command',value='Time',inline=False)
        embed.add_field(name= 'Gif Command',value='gif',inline=False)
        embed.add_field(name= 'Clear Text In Text Channel Command',value='clear',inline=False)
        embed.add_field(name= 'Syncing Music',value='sync',inline=False)
        embed.add_field(name= message.guild.name+' Server Prefix Is: ',value=p,inline=False)
        
        await message.channel.send(author,embed=embed)
        #await message.channel.send("Your Prefix Is: "+p)
    if message.content.startswith('Paithiyakar'or'Comalicon'):
        a="Paithiyakar","Comalicon"
        c=random.choice(a)
        await message.channel.send("You: "+c) 
    #await client.process_commands(message)
    elif message.content.startswith("Srijith"or"srijith"or"nightwolf"or"NightWolf"):
        a="He is the best","He is the best person ever"
        b=random.choice(a)
        await message.channel.send(b)
    elif message.content.startswith("Donop"):
        a="Ultra Pro Noob"
        
        await message.channel.send(a)
    elif message.content.startswith("Toss"):
        a="Head","Tails"
        b=random.choice(a)
        await message.channel.send(b)
    elif message.content.startswith("Sathish" or"SAToxic"):
        a="He Is The Worst","He is an Paithiyakar","He is an Comalicon"
        b=random.choice(a)
        await message.channel.send(b)  
    await client.process_commands(message)

@client.event
async def on_guild_join(guild):
    with open('prefix.json','r')as f:
        prefixes=json.load(f)
    prefixes[str(guild.id)]='.'
    
    with open('prefix.json','w')as f:
        json.dump(prefixes,f,indent=4)
    



@client.event
async def on_guild_remove(guild):
    with open('prefix.json','r')as f:
        prefixes=json.load(f)
    prefixes.pop(str(guild.id))
    with open('prefix.json','w')as f:
        json.dump(prefixes,f,indent=4)




@client.group(invoke_without_command=True)
async def help(ctx):

    author=ctx.message.author

    embed=discord.Embed(colour=discord.Colour.random())
    embed.set_author(name='Help')
    embed.add_field(name='Changing Prefix Command',value='ChangePrefix',inline=False)
    embed.add_field(name='Joining Voice Channel Command',value='join',inline=False)
    embed.add_field(name='Leaving Voice Channel Command',value='leave',inline=False)
    embed.add_field(name='Playing Audio Command',value='p,pl,pla,P,Pl,Pla,PLAY,play',inline=False)
    embed.add_field(name='Pausing Audio Command',value='pause,pe,pa,pu',inline=False)
    embed.add_field(name='Resuming Audio Command',value='resume,re',inline=False)
    embed.add_field(name= 'Stoping Audio Command',value='stop,st,stp',inline=False)
    embed.add_field(name= 'Loop Audio Command',value='loop',inline=False)
    embed.add_field(name= 'Playlist For YouTube',value='ytpl',inline=False)
    embed.add_field(name= 'Skip Audio Command',value='skip',inline=False)
    embed.add_field(name= 'Volume Command',value='volume,vol',inline=False)
    embed.add_field(name= 'Remove Audio Command',value='remove,rem,rv',inline=False)
    embed.add_field(name= 'Weather Command',value='Weather',inline=False)
    embed.add_field(name= 'Calculator Command',value='calc',inline=False)
    embed.add_field(name= 'Time Command',value='Time',inline=False)
    embed.add_field(name= 'Gif Command',value='gif',inline=False)
    embed.add_field(name= 'Clear Text In Text Channel Command',value='clear',inline=False)
    embed.add_field(name= 'Syncing Music',value='sync',inline=False)
    await ctx.send(author,embed=embed)

@client.command()
@commands.has_role(Role)
async def ChangePrefix(ctx,prefix):
    with open('prefix.json','r')as f:
        prefixes=json.load(f)
    prefixes[str(ctx.guild.id)]=prefix

    

    with open('prefix.json','w')as f:
        json.dump(prefixes,f,indent=4)
    author=ctx.author
    await ctx.send(author)
    await ctx.send(f"Prefix Changed to: {prefix}")
    print(prefixes)



@client.command()
@commands.has_role(Role)
async def calc(ctx,*,calc):
    try:
        author=ctx.author
        await ctx.send(author)
        loctime=calc
        loctime=loctime.replace("+","%2B")
        URL = "https://www.google.com/search?q="+loctime

        headers = {
                        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
                        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
                        
        where = soup.find(class_='qv3Wpe').get_text()

        
        await ctx.send(calc+" = "+where)
        #(resultinC+" °C"+" And "+resultinF[2:]+" °F")

                            
        
    except Exception:
        await ctx.send("data not available")


    
@client.command()
@commands.has_role(Role)
async def Weather(ctx,*,loc):

    
    try:
        URL = "https://www.google.com/search?q=weather+in"+loc.lower()

        headers = {
                        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
                        }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
                        
        resultinC = soup.find(class_='wob_t q8U8x').get_text()
        resultinF = soup.find(class_='vk_bk TylWce SGNhVe').get_text()
        author=ctx.author
        await ctx.send(author)
        await ctx.send(resultinC+" °C"+" And "+resultinF[2:]+" °F")
        #(resultinC+" °C"+" And "+resultinF[2:]+" °F")

                            
        resultPHW=soup.find(class_='wtsRwe').get_text()
        await ctx.send(resultPHW[:18])
        #(resultPHW[:17])

        await ctx.send(resultPHW[18:][:13])
        #(resultPHW[17:][:13])

        await ctx.send(resultPHW[31:])
        #(resultPHW[30:])

        location= soup.find(class_='wob_loc q8U8x').get_text()
        DateAndTime= soup.find(class_='wob_dts').get_text()
        weather= soup.find(class_='wob_dcp').get_text()
        await ctx.send(location)
        #(location)
        await ctx.send(DateAndTime)
        #(DateAndTime)
        await ctx.send(weather)
        #(weather)
        inp_str = DateAndTime
        num = ""
        for c in inp_str:
            if c.isdigit():
                num = num + c
        time=datetime.datetime.now().strftime("%M")
        databaseNumber=num[1:]
        timeAgo=(int(time)+int(databaseNumber))
        URL = "https://www.google.com/search?q="+loc+"+time"
        headers = {
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
                }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        alltime = soup.find(class_='vk_gy vk_sh card-section sL6Rbf').get_text()
        time=(alltime[:9][1:])
        
        await ctx.send("Time "+loc+" "+time)
        time2=(alltime[3:][:2])
        time2=(int(time2))
        if (time2 <=60):
            #(timeAgo,"Minutes Ago")
            Time=str(time2)
            if (Time==0):
                await ctx.send("Few Seconds Ago")
            else:
                await ctx.send(Time+" Minutes Ago")
        
        loc=(alltime[48:])
    except Exception:
        author=ctx.author
        await ctx.send(author)
        await ctx.send("data not available")
        #("data not available")
    
@client.command()
@commands.has_role(Role)
async def Time(ctx,*,loc):
        URL = "https://www.google.com/search?q="+loc+"+time"
        headers = {
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
                }

        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        alltime = soup.find(class_='vk_gy vk_sh card-section sL6Rbf').get_text()
        time=(alltime[:9][1:])
        author=ctx.author
        await ctx.send(author)
        await ctx.send("Time "+loc+": "+time)
@client.command()
@commands.has_role(Role)
async def Wiki(ctx,*,Wikki):
    results=wikipedia.summary(Wikki,sentences=2)
    author=ctx.author
    
    await ctx.send(results)



@client.command()
@commands.has_role(Role)
async def gif(ctx,*,gifq):
    author=ctx.author
    api_key='naGVckoc4UK7zixVoqBEYdPWaI0NYTsZ'
    api_instance=giphy_client.DefaultApi()
    try:
        api_response=api_instance.gifs_search_get(api_key,gifq,limit=5,rating='g')
        lst=list(api_response.data)
        gif=random.choice(lst)
        await ctx.send(author)
        await ctx.send(gif.embed_url)
    except Exception:
        await ctx.send("No Gif")

@client.command()
@commands.has_role(Role)
async def whereAmI(ctx):
    author=ctx.author
    await ctx.send(author)
    await ctx.send(ctx.message.guild.name)

@client.command()
@commands.has_role(Role)
async def clear(ctx,CA=1):
    CA=(int(CA))
    await ctx.channel.purge(limit=CA)
    author=ctx.author
    #await ctx.send(author)
    CA=(str(CA))
    #print(author.id)
    """if("Night Wolf" in author):
        print("You Have Clear Chat")
    else:
        await ctx.send(author)
        await ctx.send("As Been Clear Chat: "+CA)"""

@client.command()
@commands.has_role(Role)
async def countmember(ctx):
    guild = ctx.guild
    await ctx.send(f"Member count: {guild.member_count}") 

music = DiscordUtils.Music()
@client.command(aliases=["p","pl","pla","P","Pl","Pla","PLAY"])
@commands.has_role(Role)
async def play(ctx, *, search_keyword):
    
    voice_channel=ctx.author.voice.channel
    if ctx.author.voice is None:
        author=ctx.author
        await ctx.send("You Are Not In A Voice Channel")
    

    if ctx.voice_client is None:
        await voice_channel.connect()
        Channel=ctx.author.voice.channel.name
        author=ctx.author
        await ctx.send("Joined: "+Channel) 

    import re
    #KeyWord To YT URL 
    search_keyword1=search_keyword.replace(" ","+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword1)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url="https://www.youtube.com/watch?v=" + video_ids[0]
    video = YouTube(url) 

    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await player.queue(url, search=True)
        song = await player.play()
        author=ctx.author
        embed=discord.Embed(colour=discord.Colour.random())
        embed.set_author(name=ctx.author)
        embed.add_field(name= 'Now Playing: ',value=f"{song.name}",inline=False)
        await ctx.send(embed=embed)
        
    else:
        song = await player.queue(url, search=True)
        
        embed=discord.Embed(colour=discord.Colour.random())
        embed.set_author(name=ctx.author)
        embed.add_field(name= 'Queued: ',value=f"{song.name}",inline=False)
        await ctx.send(embed=embed)



@client.command()
@commands.has_role(Role)
async def ytpl(ctx,*,plurl):
    voice_channel=ctx.author.voice.channel
    if ctx.author.voice is None:
        author=ctx.author
        await ctx.send("You Are Not In A Voice Channel")
    

    if ctx.voice_client is None:
        await voice_channel.connect()
        Channel=ctx.author.voice.channel.name
        author=ctx.author
        await ctx.send("Joined: "+Channel) 

    player = music.get_player(guild_id=ctx.guild.id)
    import re
    from pytube import Playlist

    playlist = Playlist(plurl)

    # this fixes the empty playlist.videos list
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

   
    embed=discord.Embed(colour=discord.Colour.random())
    embed.set_author(name=ctx.author)
    embed.add_field(name= 'Number Of Tracks: ',value=len(playlist.video_urls),inline=False)
    await ctx.send(embed=embed)
    for url in playlist.video_urls:
        if not player:
            player = music.create_player(ctx, ffmpeg_error_betterfix=True)
        if not ctx.voice_client.is_playing():
            await player.queue(url, search=True)
            song = await player.play()
            author=ctx.author
            embed=discord.Embed(colour=discord.Colour.random())
            embed.set_author(name=ctx.author)
            embed.add_field(name= 'Now Playing: ',value=f"{song.name}",inline=False)
            await ctx.send(embed=embed)
            
        else:
            song = await player.queue(url, search=True)
            


@client.command(aliases=["pe","pa","pu"])
@commands.has_role(Role)
async def pause(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.pause()
    
    embed=discord.Embed(colour=discord.Colour.random())
    embed.set_author(name=ctx.author)
    embed.add_field(name= 'Paused: ',value=f"{song.name}",inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=["re"])
@commands.has_role(Role)
async def resume(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()
    
    embed=discord.Embed(colour=discord.Colour.random())
    embed.set_author(name=ctx.author)
    embed.add_field(name= 'Resumed: ',value=f"{song.name}",inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=["st","stp"])
@commands.has_role(Role)
async def stop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await player.stop()
    await ctx.send("Stopped")

@client.command()
@commands.has_role(Role)
async def loop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
        await ctx.send("Enabled loop")
    else:
        await ctx.send("Disabled loop")

@client.command()
@commands.has_role(Role)
async def queue(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await ctx.send(f"{', '.join([song.name for song in player.current_queue()])}")

@client.command()
@commands.has_role(Role)
async def np(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    embed=discord.Embed(colour=discord.Colour.random())
    embed.set_author(name=ctx.author)
    embed.add_field(name= 'Now Playing: ',value=f"{song.name}",inline=False)
    await ctx.send(embed=embed)

@client.command()
@commands.has_role(Role)
async def skip(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
        embed=discord.Embed(colour=discord.Colour.random())
        embed.set_author(name=ctx.author)
        embed.add_field(name= 'Skipped: ',value=f"{data[0].name}",inline=False)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(colour=discord.Colour.random())
        embed.set_author(name=ctx.author)
        embed.add_field(name= 'Skipped: ',value=f"{data[0].name}",inline=False)
        await ctx.send(embed=embed)

@client.command(aliases=["vol"])
@commands.has_role(Role)
async def volume(ctx, vol):
    player = music.get_player(guild_id=ctx.guild.id)
    song, volume = await player.change_volume(float(vol) / 100) # volume should be a float between 0 to 1
    await ctx.send(f"Changed volume to {volume*100}%")

@client.command(aliases=["rem","rv"])
@commands.has_role(Role)
async def remove(ctx, index):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))
    embed=discord.Embed(colour=discord.Colour.random())
    embed.set_author(name=ctx.author)
    embed.add_field(name= 'Removed: ',value=f"{song.name}",inline=False)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
@commands.has_role(Role)
async def join(ctx):
    if ctx.author.voice is None:
        author=ctx.author
        await ctx.send("You Are Not In A Voice Channel")
    voice_channel=ctx.author.voice.channel

    if ctx.voice_client is None:
        await voice_channel.connect()
        Channel=ctx.author.voice.channel.name
        author=ctx.author
        await ctx.send("Joined: "+Channel) 

    else:
        await ctx.voice_client.move_to(voice_channel)
        Channel=ctx.author.voice.channel.name
        author=ctx.author
        
        await ctx.send("Joined: "+Channel)

@client.command(pass_context = True)
@commands.has_role(Role)
async def leave(ctx):
    if(ctx.voice_client):
        Channel=ctx.author.voice.channel.name
        await ctx.voice_client.disconnect()
        author=ctx.author
        await ctx.send(author)
        await ctx.send("Leaving: "+Channel)
        
    else:
        await ctx.send("I Am Not In A Voice Channel To Leave")


@client.command()
@commands.has_role(Role)
async def sync(ctx):
    try:
        ctx.voice_client.pause()
        time.sleep(2)
        ctx.voice_client.resume()
        await ctx.send("Done Syncing")
    except Exception:
        await ctx.send("No Audio Playing To Syncing")

@client.command()
async def addrole(ctx):
    from discord.utils import get
    member = ctx.author
    var = discord.utils.get(ctx.guild.roles, name = "Visitor")
    member.add_role(var)

@client.command()
async def chRoleName(ctx,name):
    author=ctx.author
    author=str(author)
    if(author==user):
        dictionary ={
            "Name" : name,
        }
        with open("Wel_Role_ID.json", "w") as outfile:
            json.dump(dictionary, outfile)
        await ctx.send(f"Welcome Role Changed To: {name}")
    else:
        await ctx.send("You Can't Change Welcome Role")

    
TOKEN = 'OTU4NzQ4MjkwMjM5ODQ0NDIy.Gw8Uqg.ps0vdrazlvSY9xLbXk-w5666TN4tac'

client.run(TOKEN)


