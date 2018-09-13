# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 2018

@author: Emily
"""

import requests
import json
import utils

def getToken(credentialFile):
    with open(credentialFile) as file:
        credential=json.loads(file.read())

    # Get your FarmBot Web App token.
    headers = {'content-type': 'application/json'}
    user = {'user': {'email': credential['email'], 'password': credential['password']}}
    response = requests.post('https://my.farmbot.io/api/tokens',
                            headers=headers, json=user)
    return response.json()