#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import files
"""
ZetCode wxPython tutorial

This example shows a simple menu.

author: Jan Bodnar
website: www.zetcode.com
last modified: April 2018
"""

import wx


class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		self.InitUI()
		self.Centre()
		self.SetTitle('TSC Card Manager')
	def InitUI(self):

		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		menuNew = fileMenu.Append(wx.ID_NEW,'&New')
		menuSave = fileMenu.Append(wx.ID_SAVE,'&Save')
		fileMenu.AppendSeparator()

		imp = wx.Menu()
		imCard = imp.Append(wx.ID_ANY,'Import Cards.txt...')
		fileMenu.Append(wx.ID_ANY, 'I&mport',imp)
		menubar.Append(fileMenu, '&File')
		self.SetMenuBar(menubar)
		self.Bind(wx.EVT_MENU, self.listing, imCard)
		self.SetSize((300, 400))
		
		panel = wx.Panel(self)
		font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

		font.SetPointSize(9)

		vbox = wx.BoxSizer(wx.VERTICAL)

		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		st1 = wx.StaticText(panel, label='Select a card below:')
		st1.SetFont(font)
		hbox1.Add(st1)
		vbox.Add(hbox1,flag=wx.LEFT|wx.TOP,border=4)
		vbox.Add((-1, 20))

		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
		hbox2.Add(tc2, proportion=1, flag=wx.EXPAND)
		vbox.Add(hbox2, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=10)

		vbox.Add((-1, 25))

		panel.SetSizer(vbox)
		

	def OnQuit(self, e):
		self.Close()

	def listing(self, e):
		print(files.importCards())

def main():

	app = wx.App()
	ex = Example(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()