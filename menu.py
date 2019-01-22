#!/usr/bin/env python3
"""
Main SYSTEM_MENU

this launches other modules
"""

__author__ = "Triktron"
__version__ = "0.1.0"
__license__ = "MIT"

import wx
import time
from os.path import dirname, basename, isfile
import glob
import os
import sys
import re
import importlib

if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

class Menu(wx.Frame):
    bgColor = "#211535"
    bgColorSidebar = "#4a3172"

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Car Interface", style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, size=(800,480))

        menu = wx.Panel(self, wx.ID_ANY, size=(720,480), pos=(80,0))
        menu.SetBackgroundColour(self.bgColor)
        menuSidebar = wx.Panel(self, wx.ID_ANY, size=(80,480))
        menuSidebar.SetBackgroundColour(self.bgColorSidebar)

        self.setupSidebar(menuSidebar)

        modules = self.load("apps")
        for f in modules:
            if hasattr(f, 'start'):
                self.addApp(f, menu)

        modules = self.load("services")
        for f in modules:
            if hasattr(f, 'start'):
                f.start(self)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        self.timer.Start(1000)

        self.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.Center()
        self.Show()

    def OnClose(self, event):
        print("OnClose called")
        if self.currentApp >= 0 and hasattr(self.apps[self.currentApp], 'stop'):
            self.apps[self.currentApp].stop()
        event.Skip()

    def setupSidebar(self, panel):
        self.clockElement = wx.StaticText(panel, id=wx.ID_ANY, label=time.strftime('%H:%M'), pos=(9,400))
        font = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.clockElement.SetFont(font)
        self.clockElement.SetForegroundColour((255,255,255))

    def load(self, path):
        pysearchre = re.compile('.py$', re.IGNORECASE)
        pluginfiles = filter(pysearchre.search, os.listdir(os.path.join(bundle_dir, path)))
        form_module = lambda fp: '.' + os.path.splitext(fp)[0]
        plugins = map(form_module, pluginfiles)
        # import parent module / namespace
        importlib.import_module(path)
        modules = []
        for plugin in plugins:
                 if not plugin.startswith('__'):
                     modules.append(importlib.import_module(plugin, package=path))

        return modules

    def onKeyPress(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_TAB:
            event.Skip()
            self.toggleHome()

    apps = []
    currentApp = -1
    isMenuOpen = True

    def addApp(self, app, panel):
        print(app.NAME)
        bmp = wx.Bitmap(os.path.join(bundle_dir, app.ICON), wx.BITMAP_TYPE_ANY) # "/" + os.path.dirname(sys.argv[0]) +
        button = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=bmp, size=(bmp.GetWidth()+10, bmp.GetHeight()+10))
        button.SetBackgroundColour(self.bgColor)
        button.SetWindowStyleFlag(wx.NO_BORDER)

        button.Bind(wx.EVT_BUTTON, lambda click: self.startApp(app))

        button.SetPosition((10 + 140*(len(self.apps) % 5),10 + (len(self.apps) - len(self.apps) % 5) / 5 * 140))
        self.apps.append(app)

    def startApp(self, app):
        if hasattr(app, 'start'):
            if self.currentApp >= 0 and hasattr(self.apps[self.currentApp], 'stop'):
                self.apps[self.currentApp].stop()
            app.start(self)
            app.frame.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)
            self.currentApp = self.apps.index(app)

    def toggleHome(self):
        if self.currentApp < 0:
            return
        if self.isMenuOpen:
            # self.Show()
            self.apps[self.currentApp].frame.Hide()
        else:
            # self.Hide()
            self.apps[self.currentApp].frame.Show()
        self.isMenuOpen = not self.isMenuOpen

    def update(self, event):
        self.clockElement.SetLabel(time.strftime('%H:%M'))
