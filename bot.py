import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTE0NDc3ODYyMzU1NjAwOTk4NA.GPpR3N.DA5JPFoj9KKf1bzUgtV240goBir1T6mHT9QKu4')

