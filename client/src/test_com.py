# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 2018

@author: Emily
"""

import os
import com_server
import com_farmbot

if __name__=="__main__":    
    serverIp='127.0.0.1'
    serverPort=3333
    serverUrl='http://%s:%d'%(serverIp, serverPort)

    response=com_server.getToken(serverUrl, {'email':'test@email.com', 'password':'abc'})
    token = response['token']

    com_farmbot.initCommunication(serverUrl, token)

    com_farmbot.move_relative(50, 50, 50, 80)


    print(response)