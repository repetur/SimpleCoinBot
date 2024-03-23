# Simple Coin Bot by eXmansa, 2020-2024. GitHub: https://github.com/repetur
# Distributed under the WTFPL License.

import discord
from discord import app_commands
import random
## imports

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
## variables

@client.event
async def on_ready():
    await tree.sync() # syncing the command tree on discord server
    print("We're online!")

# a command name and its description which will display on discord server

@tree.command(
    name="coin",
    description="Drop a Coin",
)

# the command itself

async def coin(interaction):
    choices = [ '🌝','🌚' ]
    winresult = random.choice(choices)
    await interaction.response.send_message(winresult)

client.run('paste-your-token-here')