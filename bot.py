import discord
import dotenv
import os
import requests
from random import randint
from flask import Flask, redirect
from threading import Thread

app = Flask(__name__)
client = discord.Client()
api_key = os.environ['API_TOKEN']
kanye = "https://api.kanye.rest/"

@app.route('/')
def invite():
    return redirect("https://discord.com/oauth2/authorize?client_id=832297955645063188&permissions=247808&scope=bot", code=302)

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

    if '$kanye' in message.content.lower():
        await message.channel.send("```"+requests.get(url = kanye).json()['quote']+"``` - Kanye")

    if '$help' in message.content.lower():
        await message.channel.send('`$goodbot` - Returns a cat smiling png file (will also return this file if a message contains good bot\n'+
                                    '`$badbot` - Returns a sad face will also return this file if a message contains bad bot\n'+
                                    '`$mood` - Returns a random png with Felix\'s possible mood at the time \n'+
                                    '`$kanye` - Returns a random Kanye West quote \n'+
                                    '`$hello` - Returns a Hello {Your Name}!')

if __name__ == '__main__':
    #thread_one = Thread(target = client.run(api_key)).start()
    Thread(target = app.run, args = ('0.0.0.0', port)).start()
    app.run(threaded=True, port = 5000)
    # thread_one.start()
    # thread_two.start()
