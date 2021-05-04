import discord
import dotenv
import os
import requests
from random import randint

client = discord.Client()
api_key = os.environ['API_TOKEN']
kanye = "https://api.kanye.rest/"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('$hello'):
        await message.channel.send('Hello {.author.display_name}!'.format(message))

    if '$goodbot' in message.content.lower() or 'good bot' in message.content.lower():
        await message.channel.send(file=discord.File("popcat.png"))

    if '$badbot' in message.content.lower() or 'bad bot' in message.content.lower():
        await message.channel.send(':c')

    if '$mood' in message.content.lower() and message.content.split('$mood')[1] is None:
        await message.channel.send(file=discord.File("moods/{num}.png".format(num = randint(1, 34))))

    if '$mood' in message.content.lower() and message.content.split('$mood')[1] not None:
        await message.channel.send('```{}```'.format(message.content.split('$mood')[1]),file=discord.File("moods/{num}.png".format(num = randint(1, 34))))

    if '$kanye' in message.content.lower():
        await message.channel.send("```"+requests.get(url = kanye).json()['quote']+"``` - Kanye")

    if '$help' in message.content.lower():
        await message.channel.send('`$goodbot` - Returns a cat smiling png file (will also return this file if a message contains good bot\n'+
                                    '`$badbot` - Returns a sad face will also return this file if a message contains bad bot\n'+
                                    '`$mood {optional:caption}` - Returns a random png with Felix\'s possible mood at the time \n'+
                                    '`$kanye` - Returns a random Kanye West quote \n'+
                                    '`$hello` - Returns a Hello {Your Name}!')

client.run(api_key)
