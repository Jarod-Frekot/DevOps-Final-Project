import discord
import dotenv
import os

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
        await message.channel.send('Hello {.author}!'.format(message))

    if 'good bot' in message.content.lower():
        await message.channel.send(file=discord.File("popcat.png"))

    if 'bad bot' in message.content.lower():
        await message.channel.send(':c')



client.run(api_key)
