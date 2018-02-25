import discord
import asyncio
import random

quotes=[
    '”Appear weak when you are strong, and strong when you are weak.” ― Sun Tzu, The Art of War',
    '“The supreme art of war is to subdue the enemy without fighting.” ― Sun Tzu, The Art of War',
    '“Let your plans be dark and impenetrable as night, and when you move, fall like a thunderbolt.”',
    '“Supreme excellence consists of breaking the enemys resistance without fighting.”',
    '“All warfare is based on deception. Hence, when we are able to attack, we must seem unable; when using our forces, we must appear inactive; when we are near, we must make the enemy believe we are far away; when far away, we must make him believe we are near.” ― Sun Tzu, The Art of War',
    '“In the midst of chaos, there is also opportunity” ― Sun Tzu, A Arte da Guerra',
]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()

@client.event
async def on_message(message):
  if message.content.startswith('!quote'):
     await client.send_message(message.channel, random.choice(quotes))

client.run('NDE1NjU5NzAwNzU2MDIxMjY4.DXOOGw.AOV9qfSSGQGVbEapQ-h62Fvh2lU')
