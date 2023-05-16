
import discord
from discord.ext import commands
import asyncio
import logging

import bingobot_admin


# Settings

with open("Token.txt", 'r') as fp:
    gTOKEN = fp.readline()

gPREFIX = "¬"


# Bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

description = '''Discord osrs bot'''
bot = commands.Bot(intents=intents, command_prefix=gPREFIX, description='Bingo time',  case_insensitive=True)



@bot.command()
async def bingo(ctx: discord.ext.commands.Context, *args):
    """ Administer the Bingo """

    await bingobot_admin.command(ctx, args) 



logging.basicConfig(level=logging.ERROR)

bot.run(gTOKEN)
