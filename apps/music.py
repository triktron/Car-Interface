#!/usr/bin/env python3
"""
test module
"""

__author__ = "Triktron"
__version__ = "0.1.0"
__license__ = "MIT"

import wx

NAME="music"
ICON="icons/music.png"

panel = None

def start(panel):
    panel.Hide()

def init(p):
    """ Main entry point of the app """
    global panel
    panel = p

    wx.StaticText(panel, id=wx.ID_ANY, label="music")
