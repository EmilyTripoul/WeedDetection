# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 2018

@author: Emily
"""

import http.server as https
import logging
import json

import api_token


def parseCeleryScript(contentDict):

    return None

def apiHandleCeleryScript(httpHandler):
    requestContent = httpHandler.getRequestContent()
    logging.getLogger('celery_scripts').info('Celery script request from %s'%(httpHandler.address_string()))
    if requestContent=='':
        httpHandler.send_error(https.HTTPStatus.BAD_REQUEST, "Bad request")
        return None
    if api_token.apiCheckToken(httpHandler)== False:
        return None
    logging.getLogger('celery_scripts').info('Celery script request from %s : %s'%(httpHandler.address_string(), requestContent))

    contentDict=json.loads(requestContent)
    
    response=parseCeleryScript(contentDict)

    httpHandler.sendResponse()