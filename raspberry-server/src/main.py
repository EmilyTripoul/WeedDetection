# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 2018

@author: Emily
"""

serverIp='127.0.0.1'
serverPort=3333

from datetime import datetime
import os
import logging

import http_server
import api_token
import api_celery_scripts


def apiHandleBotState(httpHandler):
    pass


apiEndpointGet={
    '/api/bot_state':apiHandleBotState
    }
apiEndpointPost={
    '/api/celery_script':api_celery_scripts.apiHandleCeleryScript,
    '/api/tokens':api_token.apiHandleToken
    }


def runServer():
    serverAddress = (serverIp, serverPort)
    serverDirectory = os.path.join(os.path.dirname(__file__), 'web-server/')

    httpd = http_server.HTTPServer(serverDirectory ,serverAddress, \
                                    apiEndpointGet, apiEndpointPost, \
                                    http_server.HTTPHandler)
    logging.getLogger('Server').info('Start serving at %s:%d'%(serverAddress[0], serverAddress[1]))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

    logging.getLogger('Server').info('Stopped server')


if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s] %(levelname)s - %(name)s - %(message)s', level=logging.DEBUG,
    handlers=[
        logging.FileHandler("{0}/{1}.log".format(os.getcwd(), 'server')),
        logging.StreamHandler()
    ])
    api_token.loadCredentials()
    runServer()
