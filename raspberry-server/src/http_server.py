# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 2018

@author: Emily
"""

import http.server as https
import os
import io

class HTTPHandler(https.SimpleHTTPRequestHandler):
    """This handler uses server.base_path instead of always using os.getcwd()"""
    def translate_path(self, path):
        path = https.SimpleHTTPRequestHandler.translate_path(self, path)
        relpath = os.path.relpath(path, os.getcwd())
        fullpath = os.path.join(self.server.base_path, relpath)
        return fullpath
    
    def do_GET(self):        
        if self.path in self.server.apiEndpointGet:
            handler=self.server.apiEndpointGet[self.path]
            handler(self)
        else:
            https.SimpleHTTPRequestHandler.do_GET(self)

    
    def do_POST(self):
        if self.path in self.server.apiEndpointPost:
            handler=self.server.apiEndpointPost[self.path]
            handler(self)
        else:
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
            f = io.BytesIO(content.encode('utf-8'))     
            length=1024*16
            while 1:
                buf = f.read(length)
                if not buf:
                    break
                self.wfile.write(buf)


class HTTPServer(https.HTTPServer):
    """The main server, you pass in base_path which is the path you want to serve requests from"""
    def __init__(self, base_path, server_address, apiEndpointGet={}, apiEndpointPost={}, RequestHandlerClass=HTTPHandler):
        self.base_path = base_path
        self.apiEndpointGet = apiEndpointGet
        self.apiEndpointPost = apiEndpointPost
        https.HTTPServer.__init__(self, server_address, RequestHandlerClass)