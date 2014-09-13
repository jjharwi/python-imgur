#!/usr/bin/python

import requests
import json
import urllib
import string
import os

reddits = ['pics']

for reddit in reddits:

  if not os.path.exists(reddit):
    os.makedirs(reddit)

  list = requests.get('http://api.reddit.com/r/' + reddit).json()

  for item in list['data']['children']:
    img_url = item['data']['url']
    img_name = item['data']['name'] + ".jpg"
    if "i.imgur" not in img_url:
      img_url = string.replace(img_url,'imgur.com','i.imgur.com')
      img_url = img_url + ".jpg"
      print img_url
      if not os.path.isfile("./" + reddit + "/" + img_name):
        urllib.urlretrieve(img_url,"./" + reddit + "/" + img_name)
    else:
      print img_url
      if not os.path.isfile("./" + reddit + "/" + img_name):
        urllib.urlretrieve(img_url,"./" + reddit +"/" + img_name)
