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
    'white' : discord.Color.from_rgb(254, 254, 254)
}

@bot.command(name='cure', help='Display info on a random cure')
async def cure(ctx):
    with open('cure_names.txt') as f1, open('civilian_names.txt') as f2:
        # Read from file
        cure_names = f1.read().splitlines()
        civilian_names = f2.read().splitlines()
        index = random.randrange(0, len(cure_names))
        data = cure_names[index].split(';')

        # Get text to display
        cure = data[0]
        color = colors[data[1]]
        phrase = data[2]
        team = data[3]
        age = data[4]
        img_url = data[5]
        civilian = civilian_names[index]

        # TODO: images
        # formatting tutoral: https://python.plainenglish.io/python-discord-bots-formatting-text-efca0c5dc64a

        url_ext = civilian.replace(' ', '_')

        response = discord.Embed(
            title = cure + '/' + civilian,
            url = 'https://prettycure.fandom.com/wiki/' + url_ext,
            description = phrase,
            color = color
        )
        response.set_image(url=img_url)
        response.add_field(name='Team: ', value=team)
        response.add_field(name='Age: ', value=age)

        await ctx.send(embed=response)

bot.run(TOKEN)
