import wx
import wx.lib.agw.shapedbutton as SB

class MyFrame(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, -1, "ShapedButton Demo")

        panel = wx.Panel(self)

        # Create 2 bitmaps for the button
        upbmp = wx.Bitmap("play.png", wx.BITMAP_TYPE_PNG)
        disbmp = wx.Bitmap("playdisabled.png", wx.BITMAP_TYPE_PNG)

        play = SB.SBitmapToggleButton(panel, -1, upbmp, (100, 50))
        play.SetUseFocusIndicator(False)
        play.SetBitmapDisabled(disbmp)


# our normal wxApp-derived class, as usual

app = wx.App(0)

frame = MyFrame(None)
app.SetTopWindow(frame)
frame.Show()

app.MainLoop()
