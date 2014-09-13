#!/usr/bin/python

import json
import requests
from ConfigParser import SafeConfigParser
import time

def _refresh_token():

    cp = SafeConfigParser()
    cp.read('.imgur_token')
    refresh_token = cp.get('tokens','refresh_token').strip()
    client_id = cp.get('tokens','client_id').strip()
    client_secret = cp.get('tokens','client_secret').strip()

    url = 'https://api.imgur.com/oauth2/token'
    refresh_data = {'grant_type':'refresh_token','refresh_token':refresh_token,'client_id':client_id,'client_secret':client_secret}

    api_key = requests.post(url,data=refresh_data)
    api_token = json.loads(api_key.text)

    access_token = api_token['access_token']
    refresh_token = api_token['refresh_token']
    expires_in = api_token['expires_in']

    curr_time = time.strftime('%s',time.gmtime())
    expire_time = int(curr_time) + int(expires_in)

    cp.set('tokens','access_token',access_token)
    cp.set('tokens','expire_time',str(expire_time))
    cp.set('tokens','refresh_token',refresh_token)
    fp = open('.imgur_token','w+')
    cp.write(fp)
    fp.close()

    return access_token

if __name__ == "__main__":
    tokeny_thingy=_refresh_token()
    print tokeny_thingy 

