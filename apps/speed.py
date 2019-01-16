#!/usr/bin/env python3
"""
test module

replace buttons with BitmapToggleButton
"""

__author__ = "Triktron"
__version__ = "0.1.0"
__license__ = "MIT"

import wx

NAME="speed"
ICON="icons/speed.png"

app = None
frame = None

def start(app):
    global frame
    frame = MainFrame(app)
    frame.Center()
    frame.Show()

def stop():
    global frame
    if frame:
        frame.Close()

def messg(msg):
    global Frame

    if frame:
        frame.m_gauge1.SetValue( msg )

class MainFrame(wx.Frame):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 800,-1 ), wx.GA_HORIZONTAL )
        self.m_gauge1.SetValue( 0 )
        bSizer6.Add( self.m_gauge1, 0, wx.ALL, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()

        self.Centre( wx.BOTH )
