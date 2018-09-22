# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 2018

@author: Emily
"""
import logging

# Make root
import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from cefpython3 import cefpython as cef
import platform
import sys
import threading
from functools import wraps

import gui_interface
import gui_utils


import http.server as https
import socketserver

g_ressourceServer=None

class HTTPHandler(https.SimpleHTTPRequestHandler):
    """This handler uses server.base_path instead of always using os.getcwd()"""
    def translate_path(self, path):
        path = https.SimpleHTTPRequestHandler.translate_path(self, path)
        relpath = os.path.relpath(path, os.getcwd())
        fullpath = os.path.join(self.server.base_path, relpath)
        return fullpath
        
    def log_request(self, code='-', size='-'):
        pass

class HTTPServer(https.HTTPServer):
    """The main server, you pass in base_path which is the path you want to serve requests from"""
    def __init__(self, base_path, server_address, RequestHandlerClass=HTTPHandler):
        self.base_path = base_path
        https.HTTPServer.__init__(self, server_address, RequestHandlerClass)

def stopLovalRessourceServer():
    global g_ressourceServer
    logging.getLogger('Ressource').info('Stopping server')
    if g_ressourceServer!=None:
        g_ressourceServer.shutdown()
        g_ressourceServer=None

def startLocalRessourceServer(ressourceServerIp, ressourceServerPort):
    global g_ressourceServer
    logging.getLogger('Ressource').info('Starting server on %s:%d'%(ressourceServerIp, ressourceServerPort))

    serverAddress = (ressourceServerIp, ressourceServerPort)
    serverDirectory = os.path.join(os.path.dirname(__file__), 'web-app/')
    logging.getLogger('Ressource').info('Serving directory %s'%(serverDirectory))

    g_ressourceServer = HTTPServer(serverDirectory, serverAddress, HTTPHandler)
    
    thread = threading.Thread(target = g_ressourceServer.serve_forever)    
    thread.daemon = True
    try:
        thread.start()
    except KeyboardInterrupt:
        stopLovalRessourceServer()

def startInterface(ressourceServerIp, ressourceServerPort):
    checkVersion()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    settings = {
    }
    cef.Initialize(settings=settings)

    browser = cef.CreateBrowserSync(url='http://%s:%d/'%(ressourceServerIp, ressourceServerPort),
                                    window_title="WeedDetectionBot")
    gui_utils.setJavascriptBindings(browser)
    cef.MessageLoop()
    cef.Shutdown()

def main():
    ressourceServerIp='127.0.0.1'
    ressourceServerPort=9999
    startLocalRessourceServer(ressourceServerIp, ressourceServerPort)
    startInterface(ressourceServerIp, ressourceServerPort)
    stopLovalRessourceServer()

def checkVersion():
    ver = cef.GetVersion()
    logging.getLogger('Main').info("CEF Python {ver}".format(ver=ver["version"]))
    logging.getLogger('Main').info("Chromium {ver}".format(ver=ver["chrome_version"]))
    logging.getLogger('Main').info("CEF {ver}".format(ver=ver["cef_version"]))
    logging.getLogger('Main').info("Python {ver} {arch}".format(
           ver=platform.python_version(),
           arch=platform.architecture()[0]))
    assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"


if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s] %(levelname)s - %(name)s - %(message)s', level=logging.DEBUG,
    handlers=[
        logging.FileHandler("{0}/{1}.log".format(os.getcwd(), 'client')),
        logging.StreamHandler()
    ])
    main()
