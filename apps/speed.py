#!/usr/bin/env python3
"""
test module

replace buttons with BitmapToggleButton
"""

__author__ = "Triktron"
__version__ = "0.1.0"
__license__ = "MIT"

import wx
import math
import wx.lib.agw.speedmeter as SM
# import libs.speedmeter as SM

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
        frame.speed.SetSpeedValue(msg)

class MainFrame(wx.Frame):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        # speed_panel = wx.Panel(self, wx.ID_ANY, size=(100,100))
        # speed_panel.SetBackgroundColour("#4a3172")

        # m_button3 = wx.Button( self, wx.ID_ANY, u"MyButton", pos=(50,50))

        self.speed = SM.SpeedMeter(self, agwStyle=SM.SM_DRAW_HAND|SM.SM_DRAW_SECTORS|SM.SM_DRAW_MIDDLE_TEXT|SM.SM_DRAW_SECONDARY_TICKS)
        self.speed.SetSpeedBackground( wx.Colour( 56, 44, 104 ) )
        self.speed.SetAngleRange(-math.pi/6, 7*math.pi/6)
        intervals = range(0, 21, 2)
        self.speed.SetIntervals(intervals)
        colours = [wx.BLACK]*10
        self.speed.SetIntervalColours(colours)
        ticks = [str(interval) for interval in intervals]
        self.speed.SetTicks(ticks)
        self.speed.SetTicksColour(wx.WHITE)
        self.speed.SetNumberOfSecondaryTicks(5)
        self.speed.SetTicksFont(wx.Font(7, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.speed.SetMiddleText("Km/h")
        self.speed.SetMiddleTextColour(wx.WHITE)
        self.speed.SetMiddleTextFont(wx.Font(8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.speed.SetHandColour(wx.Colour(255, 50, 0))
        self.speed.DrawExternalArc(False)
        self.speed.SetSpeedValue(0)
