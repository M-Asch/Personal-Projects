#Imports
######################################################
import os
import sys
import importlib
import requests
from lxml import etree
import urllib
import json

############################################
#
#       NFT Class
#
############################################
class NFT:
    #base class for NFT to hold basic info

    def __init__(self, nm, fl, ra = 1, tk = '', cr = '', ow = []):
        information = {}
        information['name'] = nm
        information['file_location'] = fl
        information['token'] = tk
        information['owner'] = cr
        information['owners'] = ow
        information['rarity'] = ra
        self.information = information

    def __str__(self):
        string = ''
        for item in self.information:
            string = string + item + ':' + str(self.information[item]) + '\n'
        return(string)

    def get_full_Info(self):
        list = {}
        for item in self.information:
            list[item] = self.information[item]
        return(list)

    def get_Info(self):
        return(self.information['name'], self.information['owner'])

    def set_tk(self, tk):
        self.information['token'] = tk

    def set_cr(self, cr):
        self.information['owner'] = cr
        self.add_owner(cr)

    def add_owner(self, ow):
        self.information['owners'].append(ow)

    def set_rarity(self, ra):
        self.information['rarity'] = ra

############################################
#
#       Wallet Class
#
############################################

class Wallet:

    def __init__(self, name, id, count = 100, wallet = []):
        credentials = {}
        credentials['Name'] = name
        credentials['ThomasTokens'] = count
        credentials['id'] = id
        credentials['Wallet'] = wallet
        self.credentials = credentials

    def get_current(self):
        return(self.credentials['wallet'])

    def get_wallet_info(self):
        list = {}
        for item in self.credentials:
            list[item] = self.credentials[item]
        return(list)

############################################
#
#       Saving/Updating File Functions
#
############################################

def update_NFT(nfts, wallets):
    fullInfo = []
    wall = []
    f = open("NFT_information.json", 'w')
    wa = open("WALLET_information.json", 'w')
    for nft in nfts:
        fullInfo.append(nft.get_full_Info())
    for w in wallets:
        wall.append(w.get_full_Info())
    json.dump(fullInfo, f)
    f.close()
    json.dump(wall, wa)
    wa.close()

def remake_NFT(nftI):
    listN = []
    for N in nftI:
        listN.append(NFT(N['name'],N['file_location'],N['token'],N['owner'],N['owners'],N['rarity']))
    return(listN)

def remake_Wallet(walI):
    listW = []
    for W in walI:
        listW.append(Wallet(W['name'], W['ThomasTokens'], W['id'], W['Wallet']))
    return listW

def pull_files(f1, f2):
    f = open(f1, "r")
    w = open(f2, "r")
    try:
        listN = json.load(f)
        listW = json.load(w)
        return(listN, listW)
    except:
        return([], [])

def setup():
    try:
        c = open("config.json", "x")
        n = open("NFT_information.json", "x")
        w = open("WALLET_information.json", "x")

        files = ['c', 'n', 'w']

        #json.dump({'token':'', 'setup':True}, c)
        json.dump([], n)
        json.dump([], w)

        for f in files:
            f.close()
        print('Files have been Created')
    except:
        c = open("config.json")
        config = json.load(c)
        nftI, walI = pull_files("NFT_information.json", "WALLET_information.json")
        listN = remake_NFT(nftI)
        listW = remake_Wallet(walI)
        return(config, listN, listW)

############################################
#
#       Global Variables
#
############################################

config = {}
listN = [1]
listW = [2]
config, listN, listW = setup()
