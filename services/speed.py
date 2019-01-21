#!/usr/bin/env python3
"""
test module
"""
import wx
import time


__author__ = "Triktron"
__version__ = "0.1.0"
__license__ = "MIT"

menu=None

def start(app):
    global menu
    menu = app
    app.speed = wx.Timer(app)
    app.Bind(wx.EVT_TIMER, p, app.speed)
    app.speed.Start(1)

def p(event):
    global menu
    for f in menu.apps:
        if f.NAME == "speed":
            f.messg(float(time.time() * 10) % 20)
