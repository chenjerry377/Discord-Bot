import discord
import json
import requests
import random

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents = intents)

key_words = ["inspire", "sad", "pressured", "despressed", "encouragement", "encourage", "inspirebot", "inspirationalbot"]

start_quotes = [ 
    "You can do it",
    "Keep fighting",
    "Believe in yourself"
]

def get_inspiration_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " " + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!quote'):
        quote = get_inspiration_quote()
        await message.channel.send(quote)

    if any(word in message.content for word in key_words):
        await message.channel.send(random.choice(start_quotes))

client.run('MTE0NDc3ODYyMzU1NjAwOTk4NA.GPpR3N.DA5JPFoj9KKf1bzUgtV240goBir1T6mHT9QKu4')
