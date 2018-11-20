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
menu = None
currentApp = None

bgColor = "#211535"

def toggleHome():
    global menu
    global currentApp

    if currentApp == None:
        return

    """ switch between the app and the menu """
    if currentApp.panel.IsShown():
        currentApp.panel.Hide()
        menu.Show()
    else:
        currentApp.panel.Show()
        menu.Hide()

def addApp(app, panel):
    global lastAppId
    bmp = wx.Bitmap(app.ICON, wx.BITMAP_TYPE_ANY)
    button = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp,
                              size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
    button.SetBackgroundColour(bgColor)
    button.SetWindowStyleFlag(wx.NO_BORDER)


    button.Bind(wx.EVT_BUTTON, lambda click: startApp(app))
    button.SetPosition((10 + 140*lastAppId,10))
    lastAppId = lastAppId + 1

def startApp(app):
    global currentApp
    if hasattr(app, 'start'):
        currentApp = app
        toggleHome()

def onKeyPress(event):
    global currentApp
    keycode = event.GetKeyCode()
    if keycode == wx.WXK_TAB:
        event.Skip()
        toggleHome()

def OnPaint(event):
        global menu
        dc = wx.PaintDC(menu)
        dc.Clear()
        dc.SetPen(wx.Pen('#d4d4d4'))
        dc.SetBrush(wx.Brush('#c56c00'))
        dc.DrawRectangle(0, 0, 480, 80)

def init(frame):
    global menu
    menu = wx.Panel(frame, wx.ID_ANY, size=(800,480))
    menu.SetBackgroundColour(bgColor)
    menu.Show()
    frame.Bind(wx.EVT_CHAR_HOOK, onKeyPress)
    # menu.Bind(wx.EVT_PAINT, OnPaint)
    modules = load_plugins()
    for f in modules:
        if hasattr(f, 'init'):
            panel = wx.Panel(frame, wx.ID_ANY, size=(800,480))
            panel.Hide()
            app = f.init(panel)
            addApp(f, menu)

    frame.Layout()
