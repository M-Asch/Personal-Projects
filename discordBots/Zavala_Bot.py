#Imports
######################################################
import discord
import nest_asyncio
import random
import os
import sys
import importlib
import urllib
######################################################



#Import the Util Module
######################################################
module_path = os.path.abspath('../../../Aschm/Desktop/ZavalaBot/Modules')

if not module_path in sys.path:
    sys.path.append(module_path)

import util
importlib.reload(util)

import WeeklyReset
importlib.reload(WeeklyReset)
######################################################



#Activating Clients
######################################################
nest_asyncio.apply()
client = discord.Client()
######################################################



#Client Events
######################################################
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
    
@client.event
async def on_message(message):
    messageF = message.content.lower()
    if message.author == client.user:
        return

    elif messageF == ('hey zavala'):
        await message.channel.send('Hello Guardian, lets see what we are working with!')
    
    elif messageF == ('!update status'):
        gameChoice = update_status()
        print(gameChoice)
        game = discord.Game(gameChoice)
        await client.change_presence(status=discord.Status.idle, activity=game)
    
    elif messageF == ("what's going on with the cabal on mars?"):
        author = (message.author.id)
        #if (author.voice.channel):
         #   print('yes')
        #else:
         #   print('no')            
    elif messageF == ('!update weekly'):
        url = WeeklyReset.weeklyReset()
        path = '../ZavalaBot/Images/reset.jpg'
        urllib.request.urlretrieve(url, path)
    elif messageF == ('!weekly'):
        await message.channel.send(file=discord.File('../ZavalaBot/Images/reset.jpg'))
######################################################



#Commands
######################################################
def update_status():
    gameList = ['Starting a war with the Cabal on Mars!', 'Not avenging Cayde...', 'Rallying the Troops!']
    game = random.choice(gameList)
    return game
    
    



client.run('Nzk1MzU2NjgzMjQ5MTIzMzQ4.X_ILog.dFVdo8BJWB94lYYsceRO3XZaDiY')
