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

client.run('NDE1NjU5NzAwNzU2MDIxMjY4.DW6ujw.X83tKLyPJ3MJ51XIMTD1jDhzFec')
