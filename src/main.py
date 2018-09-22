# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 2018

@author: Emily
"""


# Make root
import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from cefpython3 import cefpython as cef
import base64
import platform
import sys
import threading
import json
from functools import wraps

# HTML code. Browser will navigate to a Data uri created
# from this html code.


def main():
    check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    settings = {
    }
    cef.Initialize(settings=settings)
    #set_global_handler()
    browser = cef.CreateBrowserSync(url=os.path.dirname(os.path.realpath(__file__))+'/web-app/index.html',
                                    window_title="WeedDetectionBot")
    #set_client_handlers(browser)
    set_javascript_bindings(browser)
    cef.MessageLoop()
    cef.Shutdown()


def check_versions():
    ver = cef.GetVersion()
    print("[WeedDetectionBot.py] CEF Python {ver}".format(ver=ver["version"]))
    print("[WeedDetectionBot.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[WeedDetectionBot.py] CEF {ver}".format(ver=ver["cef_version"]))
    print("[WeedDetectionBot.py] Python {ver} {arch}".format(
           ver=platform.python_version(),
           arch=platform.architecture()[0]))
    assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"

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
        

def html_to_data_uri(html, js_callback=None):
    # This function is called in two ways:
    # 1. From Python: in this case value is returned
    # 2. From Javascript: in this case value cannot be returned because
    #    inter-process messaging is asynchronous, so must return value
    #    by calling js_callback.
    html = html.encode("utf-8", "replace")
    b64 = base64.b64encode(html).decode("utf-8", "replace")
    ret = "data:text/html;base64,{data}".format(data=b64)
    if js_callback:
        js_print(js_callback.GetFrame().GetBrowser(),
                 "Python", "html_to_data_uri",
                 "Called from Javascript. Will call Javascript callback now.")
        js_callback.Call(ret)
    else:
        return ret


def set_global_handler():
    # A global handler is a special handler for callbacks that
    # must be set before Browser is created using
    # SetGlobalClientCallback() method.
    global_handler = GlobalHandler()
    cef.SetGlobalClientCallback("OnAfterCreated",
                                global_handler.OnAfterCreated)


def set_client_handlers(browser):
    client_handlers = [LoadHandler(), DisplayHandler()]
    for handler in client_handlers:
        browser.SetClientHandler(handler)

def set_javascript_bindings(browser):
    external = External(browser)
    bindings = cef.JavascriptBindings(
            bindToFrames=False, bindToPopups=False)
    bindings.SetProperty("py_cefpython_version", cef.GetVersion())
    for functionName in _py_expose_list:
        bindings.SetFunction(functionName, _py_expose_list[functionName])
    #bindings.SetObject("external", external)
    browser.SetJavascriptBindings(bindings)


def js_print(browser, lang, event, msg):
    # Execute Javascript function "js_print"
    browser.ExecuteFunction("js_print", lang, event, msg)


class GlobalHandler(object):
    def OnAfterCreated(self, browser, **_):
        """Called after a new browser is created."""
        # DOM is not yet loaded. Using js_print at this moment will
        # throw an error: "Uncaught ReferenceError: js_print is not defined".
        # We make this error on purpose. This error will be intercepted
        # in DisplayHandler.OnConsoleMessage.
        js_print(browser, "Python", "OnAfterCreated",
                 "This will probably never display as DOM is not yet loaded")
        # Delay print by 0.5 sec, because js_print is not available yet
        args = [browser, "Python", "OnAfterCreated",
                "(Delayed) Browser id="+str(browser.GetIdentifier())]
        threading.Timer(0.5, js_print, args).start()


class LoadHandler(object):
    def OnLoadingStateChange(self, browser, is_loading, **_):
        """Called when the loading state has changed."""
        if not is_loading:
            # Loading is complete. DOM is ready.
            js_print(browser, "Python", "OnLoadingStateChange",
                     "Loading is complete")


class DisplayHandler(object):
    def OnConsoleMessage(self, browser, message, **_):
        """Called to display a console message."""
        # This will intercept js errors, see comments in OnAfterCreated
        if "error" in message.lower() or "uncaught" in message.lower():
            # Prevent infinite recurrence in case something went wrong
            if "js_print is not defined" in message.lower():
                if hasattr(self, "js_print_is_not_defined"):
                    print("Python: OnConsoleMessage: "
                          "Intercepted Javascript error: "+message)
                    return
                else:
                    self.js_print_is_not_defined = True
            # Delay print by 0.5 sec, because js_print may not be
            # available yet due to DOM not ready.
            args = [browser, "Python", "OnConsoleMessage",
                    "(Delayed) Intercepted Javascript error: <i>{error}</i>"
                    .format(error=message)]
            threading.Timer(0.5, js_print, args).start()


class External(object):
    def __init__(self, browser):
        self.browser = browser

    def test_multiple_callbacks(self, js_callback):
        """Test both javascript and python callbacks."""
        js_print(self.browser, "Python", "test_multiple_callbacks",
                 "Called from Javascript. Will call Javascript callback now.")

        def py_callback(msg_from_js):
            js_print(self.browser, "Python", "py_callback", msg_from_js)
        js_callback.Call("String sent from Python", py_callback)


if __name__ == '__main__':
    main()
