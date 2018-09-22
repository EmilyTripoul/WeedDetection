# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 2018

@author: Emily
"""
from cefpython3 import cefpython as cef
from functools import wraps

_py_expose_list={}
def py_expose(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        'Expose the function for the browser'
        jsCallback=None
        try:
            jsCallback = kwargs.pop('jsCallback')
        except KeyError:
            if len(args)>0:
                jsCallback=args[-1]

        if jsCallback!=None:
            newArgs=args[0:-1]
            command = jsCallback.Call(function(*newArgs, **kwargs))
        else:            
            command = function(*args, **kwargs)
        
        if type(command)==object:
            return json.dumps(command)
        else:
            return command
        
    if function.__name__ not in _py_expose_list:
        _py_expose_list[function.__name__] = wrapper
    return wrapper


def setJavascriptBindings(browser):
    bindings = cef.JavascriptBindings(bindToFrames=False, bindToPopups=False)
    bindings.SetProperty("py_cefpython_version", cef.GetVersion())
    for functionName in _py_expose_list:
        bindings.SetFunction(functionName, _py_expose_list[functionName])
    browser.SetJavascriptBindings(bindings)