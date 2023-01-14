import discord
from discord.ext import commands, tasks
import random
import numpy as np
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = 1063700026620117004 #Test Server General

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    Quote.start()

file = "LukeQuoteList.txt"

@tasks.loop(hours=24)
async def Quote():
    channel = client.get_channel(CHANNEL)
    f = open(file,'r',encoding='utf8')
    lines = f.readlines()
    await channel.send(random.choice(lines))
    
client.run(TOKEN)