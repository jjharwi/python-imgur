#!/usr/bin/python

import os
import json
import requests
import urllib
from Imgur_Refresh import _refresh_token

print 'Getting an access token...'
access_token = _refresh_token()
headers = {"Authorization": "Bearer " + access_token}

gallery = raw_input('Enter the gallery name you wish to download : ')

images = []
page = 1
while page < 3:
    print page
    url = '%s%s' % ('https://api.imgur.com/3/gallery/r/' + gallery +'?page=',page)
    gall_list = requests.get(url,headers=headers).json()
    if not gall_list:
        break
    images.extend(gall_list['data'])
    page+=1

for picture in images:
    dl_link = picture['link']
    dl_name = picture['id']
    dl_name = dl_name + '.jpg'
    if not os.path.isfile('./images/' + dl_name):
        print 'Downloading ' + dl_link
        urllib.urlretrieve(dl_link, './images/' + dl_name)
