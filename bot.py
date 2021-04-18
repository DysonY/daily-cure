import os
import random


from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='!')


@bot.command(name='cure', help='Display info on a random cure')
async def cure(ctx):
    with open('cure_names.txt') as f:
        cures = f.read().splitlines()
        response = random.choice(cures)
        await ctx.send(response)


bot.run(TOKEN)
