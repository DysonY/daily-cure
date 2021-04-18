import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='!')
colors = {
    'pink' : discord.Color.from_rgb(235, 71, 242),
    'yellow' : discord.Color.from_rgb(247, 253, 14),
    'blue' : discord.Color.from_rgb(0, 0, 255),
    'red' : discord.Color.from_rgb(255, 0, 0),
    'purple' : discord.Color.from_rgb(165, 57, 254),
    'green'  : discord.Color.from_rgb(0, 255, 0),
    'white' : discord.Color.from_rgb(255, 255, 255)
}

@bot.command(name='cure', help='Display info on a random cure')
async def cure(ctx):
    with open('cure_names.txt') as f1, open('civilian_names.txt') as f2:
        cure_names = f1.read().splitlines()

        civilian_names = f2.read().splitlines()

        index = random.randint(0, 69)
        cure = cure_names[index].split(',')[0]
        color = colors[cure_names[index].split(',')[1]]
        civilian = civilian_names[index]

        url_ext = civilian.replace(' ', '_')

        response = discord.Embed(
            title = cure + '/' + civilian,
            url = 'https://prettycure.fandom.com/wiki/' + url_ext,
            color = color
        )
        await ctx.send(embed=response)


bot.run(TOKEN)
