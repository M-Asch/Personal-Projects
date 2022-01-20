#Imports
######################################################
import os
import sys
import importlib
import requests
from lxml import etree
import urllib
import json

#class definition
class NFT:
    #base class for NFT to hold basic info

    def __init__(self, nm, fl, tk = '', cr = '', ow = [], ra = 1):
        information = {}
        information['name'] = nm
        information['file_location'] = fl
        information['token'] = tk
        information['owner'] = cr
        information['owners'] = ow
        information['rarity'] = ra
        self.information = information

    def get_full_Info(self):
        list = {}
        for item in self.information:
            list[item] = self.information[item]
        return(list)

    def get_Info(self):
        return(self.information['name'], self.information['owner'])

def update_Files(nfts):
    fullInfo = []
    for nft in nfts:
        fullInfo.append(nft.get_full_Info())
    f = open("NFT_information.json", 'w')
    json.dump(fullInfo, f)
    f.close()

def test():
    nfts = []
    for i in range(10):
        nfts.append(NFT('thomas', 'mom'))
    update_Files(nfts)
test()
