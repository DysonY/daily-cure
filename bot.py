import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='!')


@bot.command(name='cure', help='Display info on a random cure')
async def cure(ctx):
    with open('cure_names.txt') as f1, open('civilian_names.txt') as f2:
        cure_names = f1.read().splitlines()
        civilian_names = f2.read().splitlines()

        index = random.randint(0, 69)
        cure = cure_names[index]
        civilian = civilian_names[index]

        url_ext = civilian.replace(' ', '_')

        response = discord.Embed(
            title = cure + '/' + civilian,
            url = 'https://prettycure.fandom.com/wiki/' + url_ext
        )
        await ctx.send(embed=response)


bot.run(TOKEN)
