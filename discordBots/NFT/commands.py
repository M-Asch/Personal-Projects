#Imports
######################################################
import os
import sys
import importlib
from classDef import *
from datetime import datetime

############################################
#
#       Global Variables
#
############################################

#listN and listW are lists filled with NFT objects

def createNFT(name, link, rarity = 1):
    createToken()
    listN.append(NFT(name, link, rarity, createToken()))S

#def create_Wallet():

#def rollNFT():

#def currentCredit():

#def tradeNFT():

#def sellNFT():

def createToken():
    string = (str(datetime.now())).strip('-')
    return(string[:10] + string[11:])

createNFT("Omaha_Thomas", "ur mom", 10)
