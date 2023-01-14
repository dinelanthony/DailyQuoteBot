import discord
from discord.ext import commands, tasks
import random
import numpy as np

client = commands.Bot(command_prefix='.')
token = "MTA2MzcwMDQyNzk3MzA3NDk4NQ.G1yUvQ.shO1-K4uaz1tIwyjb-IlvZZgpYOpgDb_1WefcE"

@tasks.loop(seconds=10)
async def Luke():
    channel = client.get_channel("1063700026620117004")
    qList = np.loadtxt("LukeQuoteList.txt")
    await channel.send(random.choice(qList))