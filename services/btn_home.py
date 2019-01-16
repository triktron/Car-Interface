#!/usr/bin/env python3
"""
test module
"""

import wx

__author__ = "Triktron"
__version__ = "0.1.0"
__license__ = "MIT"

app = None

def start(app):
    frame = wx.Frame(None, wx.ID_ANY, 'homeButton', style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, size=(100,100), pos=(0,500))
    panel = wx.Panel(frame, wx.ID_ANY)
    button = wx.Button(panel, id=wx.ID_ANY, label="home")
    buttonexit = wx.Button(panel, id=wx.ID_ANY, label="close", pos=(0,30))

    button.Bind(wx.EVT_BUTTON, lambda click: app.toggleHome())
    buttonexit.Bind(wx.EVT_BUTTON, lambda click: app.Close())
    frame.Show()
