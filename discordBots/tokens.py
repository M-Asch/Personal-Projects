#Imports
######################################################
import os
import sys
import importlib
import requests
from lxml import etree
import urllib

#
url = 'https://www.giantbomb.com/destiny-2/3030-52647/characters/'
r = requests.get(url)

htmlparser = etree.HTMLParser()
indroot = etree.fromstring(r.content, parser=htmlparser)

path = (indroot.xpath("""//*[@class="editorial"]/li/a/div"""))
path2 = (indroot.xpath("""//*[@class="editorial"]/li/a/div/img"""))
for character in path2:
    print(character.xpath('./@src'))
