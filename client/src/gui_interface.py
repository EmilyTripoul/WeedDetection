# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 2018

@author: Emily
"""

import json

from gui_utils import py_expose

@py_expose
def py_getLoginInfo():
    try:
        with open('./data/credential.json') as file:
            data=json.loads(file.read())
    except FileNotFoundError:
        data={}
    return data

@py_expose
def py_validateLogin(data):
    
    print(data)
    return True

