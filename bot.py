import discord
import dotenv
import os
from random import randint

client = discord.Client()
dotenv.load_dotenv()
api_key = os.getenv('API_KEY')

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

    if '$mood' in message.content.lower():
        await message.channel.send(file=discord.File("moods/{num}.png".format(num = randint(1, 34))))

    if '$help' in message.content.lower():
        await message.channel.send('$good bot - Returns a cat smiling png file (will also return this file if a message contains good bot')
        await message.channel.send('$bad bot - Returns a sad face will also return this file if a message contains bad bot')
        await message.channel.send("$mood - Returns a random png with Felix's possible mood at the time")
        await message.channel.send("$hello - Returns a Hello {Your Name}!")
        await messgea.channel.send("$kanye - Returns a random quote by accessing the kanye.rest API.")


client.run(api_key)
