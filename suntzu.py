import discord
import asyncio
import random
from config import *

quotes=[
    '”Appear weak when you are strong, and strong when you are weak.” ― Sun Tzu, The Art of War',
    '“The supreme art of war is to subdue the enemy without fighting.” ― Sun Tzu, The Art of War',
    '“Let your plans be dark and impenetrable as night, and when you move, fall like a thunderbolt.” ― Sun Tzu, The Art of War',
    '“Supreme excellence consists of breaking the enemy\'s resistance without fighting.”',
    '“All warfare is based on deception. Hence, when we are able to attack, we must seem unable; when using our forces, we must appear inactive; when we are near, we must make the enemy believe we are far away; when far away, we must make him believe we are near.” ― Sun Tzu, The Art of War',
    '“In the midst of chaos, there is also opportunity” ― Sun Tzu, A Arte da Guerra',
    '“The greatest victory is that which requires no battle.” ― Sun Tzu, The Art of War',
    '“Engage people with what they expect; it is what they are able to discern and confirms their projections. It settles them into predictable patterns of response, occupying their minds while you wait for the extraordinary moment — that which they cannot anticipate.” ― Sun Tzu, The Art of War',
    '“Move swift as the Wind and closely-formed as the Wood. Attack like the Fire and be still as the Mountain.” ― Sun Tzu, The Art of War',
    '“Treat your men as you would your own beloved sons. And they will follow you into the deepest valley.” ― Sun Tzu, The Art of War',
    '“When you surround an army, leave an outlet free. Do not press a desperate foe too hard.” ― Sun Tzu, The Art of War',
    '“When the enemy is relaxed, make them toil. When full, starve them. When settled, make them move.” ― Sun Tzu, The Art of War',
    '“So in war, the way is to avoid what is strong, and strike at what is weak.” ― Sun Tzu, The Art of War',
    '“To win one hundred victories in one hundred battles is not the acme of skill. To subdue the enemy without fighting is the acme of skill.” ― Sun Tzu, The Art of War',
    '“Be extremely subtle even to the point of formlessness. Be extremely mysterious even to the point of soundlessness. Thereby you can be the director of the opponent\'s fate.” ― Sun Tzu, The Art of War',
    '“One may know how to conquer without being able to do it. ” ― Sun Tzu, The Art of War',
    '“He who is prudent and lies in wait for an enemy who is not, will be victorious.” ― Sun Tzu, The Art of War',
    '“Anthony has a big head” ― Sun Tzu, The Art of War',
    '“Here lies Omar\'s hair” ― Sun Tzu, The Art of War',
    '“Oliver is a midget” ― Sun Tzu, The Art of War',
    '“Classical music is trash” ― Sun Tzu, The Art of War',
    '“Wanna hear a joke? Nabil & Joe-anna” ― Sun Tzu, The Art of War'
]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

client = MyClient()

@client.event
async def on_message(self, message):
    print('Message from {0.author}: {0.content}'.format(message))

@client.event
async def on_message(message):
  if message.content.startswith('!quote'):
     await client.send_message(message.channel, random.choice(quotes))

client.run(token)
