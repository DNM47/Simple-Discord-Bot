from imaplib import Commands
import discord
import requests
import json
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

salute = ['hello', 'hi', 'hey', 'whats up']

salute_anwser = [
    'Hello there!',
    'Hey!',
    'How can I help you?',
    'Hola'
]


def get_quote():
    response = requests.get('https://api.breakingbadquotes.xyz/v1/quotes')
    json_data = json.loads(response.text)
    quote = json_data[0]["quote"] + ' -' + json_data[0]["author"]
    return quote


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    if msg.startswith('$bb'):
        quote = get_quote()
        await message.channel.send(quote)

    if any (w in msg for w in salute):
        await message.channel.send(random.choice(salute_anwser))

token = '' #token goes here
client.run(token)