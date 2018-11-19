#!/usr/bin/python

import wx
import menu

def main():
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, 'CAR Interface', style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
    frame.SetDimensions(0,0,800,480)
    panel = wx.Panel(frame, wx.ID_ANY)

    menu.init(panel);

    frame.Show()
    frame.Centre()
    app.MainLoop()


if __name__ == "__main__":
    """ start the app """
    main()
