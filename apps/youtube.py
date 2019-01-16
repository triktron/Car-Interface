#!/usr/bin/env python3
"""
https://wxpython.org/Phoenix/docs/html/wx.CallLater.html
"""

__author__ = "Triktron"
__version__ = "0.1.0"
__license__ = "MIT"

import wx
from cefpython3 import cefpython as cef
import platform
import sys
import os

# Platforms
WINDOWS = (platform.system() == "Windows")
LINUX = (platform.system() == "Linux")

NAME="youtube"
ICON="icons/youtube.png"

app = None

frame = None

def start(app):
    global frame
    frame = MainFrame()
    frame.Center()
    frame.Show()

    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    settings = {'user_agent':"Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0"}
    if WINDOWS:
        # noinspection PyUnresolvedReferences, PyArgumentList
        cef.DpiAware.EnableHighDpiSupport()
    cef.Initialize(settings=settings)


def stop():
    global frame
    frame.Close()

class MainFrame(wx.Frame):

    def __init__(self):
        self.browser = None

        # Must ignore X11 errors like 'BadWindow' and others by
        # installing X11 error handlers. This must be done after
        # wx was intialized.
        if LINUX:
            cef.WindowUtils.InstallX11ErrorHandlers()

        wx.Frame.__init__(self, parent=None, id=wx.ID_ANY,
                          title='wxPython example', size=(800,480), style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP)
        # wxPython will set a smaller size when it is bigger
        # than desktop size.
        print("[webbrowser.py] MainFrame actual size: %s" % self.GetSize())

        self.Bind(wx.EVT_CLOSE, self.OnClose)

        # Set wx.WANTS_CHARS style for the keyboard to work.
        # This style also needs to be set for all parent controls.
        self.browser_panel = wx.Panel(self, style=wx.WANTS_CHARS)
        self.browser_panel.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        self.timer.Start(10)

        if LINUX:
            # On Linux must show before embedding browser, so that handle
            # is available (Issue #347).
            self.Show()
            # In wxPython 3.0 and wxPython 4.0 on Linux handle is
            # still not yet available, so must delay embedding browser
            # (Issue #349).
            if wx.version().startswith("3.") or wx.version().startswith("4."):
                wx.CallLater(100, self.embed_browser)
            else:
                # This works fine in wxPython 2.8 on Linux
                wx.CallLater(1, self.embed_browser)
        else:
            wx.CallLater(1, self.embed_browser)
            self.Show()

    def on_timer(self, _):
        # pass
        cef.MessageLoopWork()

    def embed_browser(self):
        window_info = cef.WindowInfo()
        (width, height) = self.browser_panel.GetClientSize().Get()
        assert self.browser_panel.GetHandle(), "Window handle not available"
        window_info.SetAsChild(self.browser_panel.GetHandle(),
                               [0, 0, width, height])
        self.browser = cef.CreateBrowserSync(window_info,
                                             url="http://www.youtube.com/tv")
        self.browser.SetClientHandler(FocusHandler())

    def OnSetFocus(self, _):
        if not self.browser:
            return
        if WINDOWS:
            cef.WindowUtils.OnSetFocus(self.browser_panel.GetHandle(),
                                       0, 0, 0)
        self.browser.SetFocus(True)

    def OnSize(self, _):
        if not self.browser:
            return
        if WINDOWS:
            cef.WindowUtils.OnSize(self.browser_panel.GetHandle(),
                                   0, 0, 0)
        elif LINUX:
            (x, y) = (0, 0)
            (width, height) = self.browser_panel.GetSize().Get()
            self.browser.SetBounds(x, y, width, height)
        self.browser.NotifyMoveOrResizeStarted()

    def OnClose(self, event):
        if not self.browser:
            print("[webbrowser.py] browser not found!")
            return
        else:
            # Calling browser.CloseBrowser() and/or self.Destroy()
            # in OnClose may cause app crash on some paltforms in
            # some use cases, details in Issue #107.
            self.browser.ParentWindowWillClose()
            self.clear_browser_references()
            self.timer.Stop()
            event.Skip()

    def clear_browser_references(self):
        # Clear browser references that you keep anywhere in your
        # code. All references must be cleared for CEF to shutdown cleanly.
        self.browser = None

class FocusHandler(object):
    def OnGotFocus(self, browser, **_):
        # Temporary fix for focus issues on Linux (Issue #284).
        if LINUX:
            print("[webbrowser.py] FocusHandler.OnGotFocus:"
                  " keyboard focus fix (Issue #284)")
            browser.SetFocus(True)
