import os
import sys
import importlib
import requests
from lxml import etree
import urllib



module_path = os.path.abspath('../../../Aschm/Desktop/ZavalaBot/Modules')

if not module_path in sys.path:
    sys.path.append(module_path)

import util
importlib.reload(util)


def weeklyReset():
    location = 'warframe.today'
    resource = '/destiny-2-weekly-reset-time/'
    
    url = util.buildURL(resource, location)
    r = requests.get(url)
    
    htmlparser = etree.HTMLParser()
    indroot = etree.fromstring(r.content, parser=htmlparser)
    
    #chartKey = (indroot.xpath("""/html/body/div[1]/div/article/div/div/div[1]/div/div/ul[2]/li/strong/text()"""))
    #chartResult = (indroot.xpath("""/html/body/div[1]/div/article/div/div/div[1]/div/div/ul[2]/li/text()"""))
    
    #print(chartKey[2], chartResult[2])
    
    image = (indroot.xpath("""//*[@id="post-2013"]/div[1]/div/div/figure[1]/img"""))
    dic = (image[0].attrib)
    url = dic['src']
    return(url)


weeklyReset()

