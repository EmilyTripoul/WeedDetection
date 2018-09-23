# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 2018

@author: Emily
"""

import http.server as https
import logging
import json

import api_token


def apiHandleCeleryScript(httpHandler):
    requestContent = httpHandler.getRequestContent()
    logging.getLogger('celery_scripts').info('Celery script request from %s'%(httpHandler.address_string()))
    if requestContent=='':
        httpHandler.send_error(https.HTTPStatus.BAD_REQUEST, "Bad request")
        return None
    if api_token.apiCheckToken(httpHandler)== False:
        return None

    contentDict=json.loads(requestContent)

    print(contentDict)
    httpHandler.sendResponse()