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
from threading import Timer
import time

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
menuSidebar = None
currentApp = None

bgColor = "#211535"
bgColorSidebar = "#4a3172"

def toggleHome():
    global menu
    global currentApp

    if currentApp == None:
        return

    """ switch between the app and the menu """
    if currentApp.panel.IsShown():
        currentApp.panel.Hide()
        menu.Show()
        menuSidebar.Show()
    else:
        currentApp.panel.Show()
        menu.Hide()
        menuSidebar.Hide()

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

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

timeElement = None
timerThread = None
def setupSidebar(panel, frame):
    global timeElement
    global timerThread
    timeElement = wx.StaticText(panel, id=wx.ID_ANY, label=time.strftime('%H:%M'), pos=(9,400))
    font = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
    timeElement.SetFont(font)
    timeElement.SetForegroundColour((255,255,255))
    timerThread = RepeatedTimer(1, updateTime)
    frame.Bind(wx.EVT_CLOSE, OnClose)

def OnClose(evnt):
    global timerThread
    timerThread.stop()
    print("exit")
    wx.GetApp().ExitMainLoop()

def updateTime():
    global timeElement
    timeElement.SetLabel(time.strftime('%H:%M'))

def init(frame):
    global menu
    global menuSidebar
    menu = wx.Panel(frame, wx.ID_ANY, size=(720,480), pos=(80,0))
    menu.SetBackgroundColour(bgColor)
    menuSidebar = wx.Panel(frame, wx.ID_ANY, size=(80,480))
    menuSidebar.SetBackgroundColour(bgColorSidebar)
    setupSidebar(menuSidebar, frame)
    menu.Show()
    menuSidebar.Show()
    frame.Bind(wx.EVT_CHAR_HOOK, onKeyPress)
    modules = load_plugins()
    for f in modules:
        if hasattr(f, 'init'):
            panel = wx.Panel(frame, wx.ID_ANY, size=(800,480))
            panel.Hide()
            app = f.init(panel)
            addApp(f, menu)

    frame.Layout()
