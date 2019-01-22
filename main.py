#!/usr/bin/python

import wx
from menu import Menu

def main():
    app = wx.App()
    menu = Menu()

    app.MainLoop()


if __name__ == "__main__":
    """ start the app """

    import sys, os
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
    else:
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    print( 'bundle dir is', bundle_dir )

    main()
