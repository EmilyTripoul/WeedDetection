# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 2018

@author: Emily
"""

import requests
import json

def getToken(serverBaseUrl, credential):
    headers = {'content-type': 'application/json'}
    user = {'user': {'email': credential['email'], 'password': credential['password']}}
    response = requests.post(serverBaseUrl+'/api/tokens',
                            headers=headers, json=user)
    return response.json()

if __name__ =="__main__":
    getToken('http://127.0.0.1:3333', {'email':'test@email.com', 'password':'abc'})