#!/usr/bin/env python3
"""
Main SYSTEM_MENU

this launches other modules
"""

__author__ = "Triktron"
__version__ = "0.1.0"
__license__ = "MIT"

import wx
from os.path import dirname, basename, isfile
import glob
import os
import sys
import re
import importlib

def load_plugins():
    pysearchre = re.compile('.py$', re.IGNORECASE)
    pluginfiles = filter(pysearchre.search,
                           os.listdir(os.path.join(os.path.dirname(__file__),
                                                 'apps')))
    form_module = lambda fp: '.' + os.path.splitext(fp)[0]
    plugins = map(form_module, pluginfiles)
    # import parent module / namespace
    importlib.import_module('apps')
    modules = []
    for plugin in plugins:
             if not plugin.startswith('__'):
                 modules.append(importlib.import_module(plugin, package="apps"))

    return modules

lastAppId = 0

def addApp(name, icon, panel):
    global lastAppId
    id = lastAppId
    bmp = wx.Bitmap(icon, wx.BITMAP_TYPE_ANY)
    button = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp,
                              size=(bmp.GetWidth()+10, bmp.GetHeight()+10))

    button.Bind(wx.EVT_BUTTON, lambda click: print(id))
    button.SetPosition((10 + 58*lastAppId,10))
    lastAppId = lastAppId + 1

def init(panel):
    modules = load_plugins()
    for f in modules:
        if hasattr(f, 'init'):
            app = f.init(panel)
            addApp(app["name"], app["icon"], panel)
