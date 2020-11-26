#!/usr/bin/env python

import wx

class HelloFrame(wx.Frame):

	def __init__(self, *args, **kw):
		super(HelloFrame, self).__init__(*args, **kw)

		panel = wx.Panel(self)

		text = wx.StaticText(panel, label="Hello World!")
		font = text.GetFont()
		font.PointSize += 10
		font = font.Bold()
		text.SetFont(font)

		sizer = wx.BoxSizer(orient=wx.VERTICAL)
		sizer.Add(text, flag=wx.TOP|wx.LEFT, border=25)
		panel.SetSizer(sizer)

		self.makeMenuBar()

		self.CreateStatusBar()
		self.SetStatusText("Welcome to wxPython")

	def makeMenuBar(self):
		fileMenu = wx.Menu()
		# \t defines a keybind for the event
		helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
			"Help string in status bar")
		fileMenu.AppendSeparator()

		# wx.ID_EXIT is a stock menu item
		exitItem = fileMenu.Append(wx.ID_EXIT)

		helpMenu = wx.Menu()
		aboutItem = helpMenu.Append(wx.ID_ABOUT)

		menuBar = wx.MenuBar()
		menuBar.Append(fileMenu, "&File")
		menuBar.Append(helpMenu, "&Help")

		self.SetMenuBar(menuBar)

		# associate handler functions
		self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
		self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
		self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

	def OnExit(self, event):
		self.Close(True)

	def OnHello(self, event):
		wx.MessageBox("Hello again from wxPython")

	def OnAbout(self, event):
		wx.MessageBox("This is a wxPython Hello World", "About Hello World 2", wx.OK|wx.ICON_INFORMATION)

if __name__ == '__main__':
	app = wx.App()
	frame = HelloFrame(None, title='Hello World 2')
	frame.Show()
	app.MainLoop()
