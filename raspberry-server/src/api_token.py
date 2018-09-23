# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 2018

@author: Emily
"""

import http.server as https
import csv
import json
import logging

_credentials=[]

def loadCredentials():
    global _credentials
    num=0
    with open('./data/credential.csv') as csvfile:
        csvreader=csv.DictReader(csvfile, delimiter=';', quotechar='"')
        for row in csvreader:
            _credentials.append(row)
            num+=1
    
    logging.getLogger('Token').info('Loading %d credentials from the database'%(num))


def getCredentialToken(email, password):
    for credential in _credentials:
        if(credential['email']==email and credential['password']==password):
            return credential['token']
    return None

def isTokenValid(token):
    for credential in _credentials:
        if(credential['token']==token):
            return True
    return False


def apiCheckToken(httpHandler):
    requestHeader = httpHandler.headers.get('Authorization')
    token=requestHeader.split(' ')[1:][0]
    if not isTokenValid(token):
        httpHandler.send_error(https.HTTPStatus.UNAUTHORIZED, "Unauthorized Token")
        return False
    
    return True

def apiHandleToken(httpHandler):
    requestContent = httpHandler.getRequestContent()
    logging.getLogger('Token').info('Token request from %s'%(httpHandler.address_string()))
    if requestContent=='':
        httpHandler.send_error(https.HTTPStatus.BAD_REQUEST, "Bad request")
        return None
    contentDict=json.loads(requestContent)
    if not ('user' in contentDict and 'email' in contentDict['user'] and 'password' in contentDict['user']):
        httpHandler.send_error(https.HTTPStatus.BAD_REQUEST, "Bad request")
        return None

    token = getCredentialToken(contentDict['user']['email'], contentDict['user']['password'])
    if token == None:
        httpHandler.send_error(https.HTTPStatus.UNAUTHORIZED, "Unauthorized user")
        return None

    response={'token':token}
    httpHandler.sendResponse(json.dumps(response))