import discord

client = discord.Client()

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
        await message.channel.send('c:')

    if 'bad bot' in message.content.lower():
        await message.channel.send(':c')



client.run('ODMyMjk3OTU1NjQ1MDYzMTg4.YHhv3w.vY8Zk0G3qpzZDT9p7Kwm_S_2ngI')
