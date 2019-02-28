#!/usr/bin/env python3
"""
test module
"""
import wx
import time

import serial

__author__ = "Triktron"
__version__ = "0.1.0"
__license__ = "MIT"

menu=None
ser=None

def start(app):
    global menu
    global ser
    menu = app
    app.speed = wx.Timer(app)
    app.Bind(wx.EVT_TIMER, p, app.speed)
    app.speed.Start(10)
    ser = serial.Serial('COM4', 115200)

def p(event):
    global menu
    for f in menu.apps:
        if f.NAME == "speed":
            if (ser.inWaiting()>0):
                data_str = ser.read(ser.inWaiting()).decode()
                if (data_str[0] == "S" and not "S" in data_str[1:]):
                    try:
                        f.messg(float(data_str[1:]))
                    except:
                        pass

            ser.write(b'S')
