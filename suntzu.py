import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('---')

@client.event
async def on_message(message):
  if message.content.startswith('!quote'):
     await client.send_message(message.channel, 'The Art of War')

client.run('token')
