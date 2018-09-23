# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 2018

@author: Emily
"""

serverIp='127.0.0.1'
serverPort=3333

import http.server as https
import socketserver
from datetime import datetime
import os
import logging
import io


def apiHandleCeleryScript(httpHandler):
    pass

def apiHandleBotState(httpHandler):
    pass

def apiHandleToken(httpHandler):
    requestContent = httpHandler.getRequestContent()


    httpHandler.sendResponse()
    print(requestContent)

apiEndpointGet={
    '/api/bot_state':apiHandleBotState
    }
apiEndpointPost={
    '/api/celery_script':apiHandleCeleryScript,
    '/api/tokens':apiHandleToken
    }

class HTTPHandler(https.SimpleHTTPRequestHandler):
    """This handler uses server.base_path instead of always using os.getcwd()"""
    def translate_path(self, path):
        path = https.SimpleHTTPRequestHandler.translate_path(self, path)
        relpath = os.path.relpath(path, os.getcwd())
        fullpath = os.path.join(self.server.base_path, relpath)
        return fullpath
    
    def do_GET(self):        
        try:
            print(self.path)
            handler=apiEndpointGet[self.path]
            handler(self)
        except KeyError:
            https.SimpleHTTPRequestHandler.do_GET(self)

    
    def do_POST(self):
        try:
            handler=apiEndpointPost[self.path]
            handler(self)
        except KeyError:
            # Doesn't do anything with posted data
            https.SimpleHTTPRequestHandler.do_GET(self)

    def getRequestContent(self):
        content = self.rfile.read(int(self.headers.get('content-length')))
        return content.decode('utf-8')

            
    def sendResponse(self, content='', contentType='application/json'):
        # Header 
        self.send_response(https.HTTPStatus.OK)
        self.send_header("Content-type", contentType)
        self.send_header("Content-Length", str(len(content.encode('utf-8'))))
        self.send_header("Last-Modified", self.date_time_string())
        self.end_headers()
        # Body
        if content!='':       
            f = io.StringIO(content)     
            length=1024*16
            while 1:
                buf = f.read(length)
                if not buf:
                    break
                self.wfile.write(buf)


class HTTPServer(https.HTTPServer):
    """The main server, you pass in base_path which is the path you want to serve requests from"""
    def __init__(self, base_path, server_address, RequestHandlerClass=HTTPHandler):
        self.base_path = base_path
        https.HTTPServer.__init__(self, server_address, RequestHandlerClass)

def log(message):
    print(message)
    timeString=datetime.now().isoformat(timespec='minutes') 
    with open('server.log','a') as file:
        file.write('[%s] %s \n'%(timeString, message))

def runServer():
    serverAddress = (serverIp, serverPort)
    serverDirectory = os.path.join(os.path.dirname(__file__), 'web-server/')

    httpd = HTTPServer(serverDirectory ,serverAddress, HTTPHandler)
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
    runServer()
