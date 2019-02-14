#!/usr/bin/env python3
"""
test module

replace buttons with BitmapToggleButton
"""

__author__ = "Triktron"
__version__ = "0.1.0"
__license__ = "MIT"

import wx
import os
import sys

NAME="settings"
ICON="icons/settings.png"

app = None
frame = None

if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

def start(app):
    global frame
    frame = MainFrame(app)
    frame.Center()
    frame.Show()

def stop():
    global frame
    if frame:
        frame.Close()

class MainFrame(wx.Frame):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 238, 238, 238 ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow1.SetScrollRate( 5, 5 )
        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"settings" ), wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )


        bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_bpButton1 = wx.BitmapToggleButton( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

        self.m_bpButton1.SetBitmap( wx.Bitmap( os.path.join(bundle_dir, "../icons/btn_off.png"), wx.BITMAP_TYPE_ANY ) )
        self.m_bpButton1.SetBitmapPressed( wx.Bitmap( os.path.join(bundle_dir, "../icons/btn_on.png"), wx.BITMAP_TYPE_ANY ) )
        bSizer2.Add( self.m_bpButton1, 0, wx.ALL, 5 )


        sbSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

        bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText11 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        bSizer21.Add( self.m_staticText11, 0, wx.ALL, 5 )


        bSizer21.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_bpButton11 = wx.BitmapToggleButton( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.BORDER_NONE )

        self.m_bpButton11.SetBitmap( wx.Bitmap( os.path.join(bundle_dir, "../icons/btn_off.png"), wx.BITMAP_TYPE_ANY ) )
        self.m_bpButton11.SetBitmapPressed( wx.Bitmap( os.path.join(bundle_dir, "../icons/btn_on.png"), wx.BITMAP_TYPE_ANY ) )
        bSizer21.Add( self.m_bpButton11, 0, wx.ALL, 5 )


        sbSizer1.Add( bSizer21, 1, wx.EXPAND, 5 )


        self.m_scrolledWindow1.SetSizer( sbSizer1 )
        self.m_scrolledWindow1.Layout()
        sbSizer1.Fit( self.m_scrolledWindow1 )
        bSizer1.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )
