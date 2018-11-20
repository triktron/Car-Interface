#!/usr/bin/python

import wx
import menu

def main():
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, 'CAR Interface', style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, size=(800,480))

    menu.init(frame);

    frame.Show()
    frame.Centre()
    app.MainLoop()


if __name__ == "__main__":
    """ start the app """
    main()
