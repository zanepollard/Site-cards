import wx
import files
import card
import re

class info():
	def __init__(self):
		self.cardList = {}

class EditDialog(wx.Dialog):
	def __init__(self,parent,id,title):
		wx.Dialog.__init__(self,parent,id,title)
		v = parent.inf.cardList
		print(v)
		self.InitUI()
		self.SetSize((350,420))
		self.SetTitle('Edit')
	
	def InitUI(self):
		pnl = wx.Panel(self)
		vbox = wx.BoxSizer(wx.VERTICAL)
		sb = wx.StaticBox(pnl, label="Add")
		sbs = wx.StaticBoxSizer(sb,orient=wx.VERTICAL)

		font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(4)

		#CARD SPACER
		self.cSpacer = wx.StaticText(pnl, label='')
		self.cSpacer.SetFont(font)
		self.cSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.cSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#CARD
		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		cLabel = wx.StaticText(pnl,label="Card:")
		self.cEntry = wx.TextCtrl(pnl)
		self.cEntry.SetMaxLength(12)

		hbox1.Add(cLabel,proportion=1,flag=wx.LEFT,border=10)
		hbox1.Add(self.cEntry,proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		sbs.Add(hbox1,flag=wx.EXPAND)

		#ACCOUNT SPACER
		self.aSpacer = wx.StaticText(pnl, label='')
		self.aSpacer.SetFont(font)
		self.aSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.aSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#ACCOUNT
		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		aLabel = wx.StaticText(pnl,label="Account:")
		self.aEntry = wx.TextCtrl(pnl)
		self.aEntry.SetMaxLength(12)

		hbox2.Add(aLabel,proportion=1,flag=wx.LEFT,border=10)
		hbox2.Add(self.aEntry,proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		sbs.Add(hbox2,flag=wx.EXPAND,border=10)

		#DESCRIPTION SPACER
		self.dSpacer = wx.StaticText(pnl, label='')
		self.dSpacer.SetFont(font)
		self.dSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.dSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#DESCRIPTION
		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		dLabel = wx.StaticText(pnl,label="Name:")
		self.dEntry = wx.TextCtrl(pnl)
		self.dEntry.SetMaxLength(30)

		hbox3.Add(dLabel,proportion=1,flag=wx.LEFT,border=10)
		hbox3.Add(self.dEntry,proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		sbs.Add(hbox3,flag=wx.EXPAND,border=10)

		#PIN SPACER
		self.pSpacer = wx.StaticText(pnl, label='')
		self.pSpacer.SetFont(font)
		self.pSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.pSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#PIN
		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
		pLabel = wx.StaticText(pnl,label="PIN:")
		self.pEntry = wx.TextCtrl(pnl)
		self.pEntry.SetMaxLength(30)

		hbox4.Add(pLabel,proportion=1,flag=wx.LEFT,border=10)
		hbox4.Add(self.pEntry,proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		sbs.Add(hbox4,flag=wx.EXPAND,border=10)

		#SEQUENCE SPACER
		self.sSpacer = wx.StaticText(pnl, label='')
		self.sSpacer.SetFont(font)
		self.sSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.sSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#SEQUENCE
		hbox5 = wx.BoxSizer(wx.HORIZONTAL)
		sLabel = wx.StaticText(pnl,label="Prompts:")
		self.sEntry = wx.TextCtrl(pnl)
		self.sEntry.SetMaxLength(30)

		hbox5.Add(sLabel,proportion=1,flag=wx.LEFT,border=10)
		hbox5.Add(self.sEntry,proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		sbs.Add(hbox5,flag=wx.EXPAND,border=10)

		#AUTHORIZATION SPACER
		self.dSpacer = wx.StaticText(pnl, label='')
		self.dSpacer.SetFont(font)
		self.dSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.dSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#AUTHORIZATION
		hbox6 = wx.BoxSizer(wx.HORIZONTAL)
		authLabel = wx.StaticText(pnl,label="Restrictions:")
		self.authEntry = wx.TextCtrl(pnl)
		self.authEntry.SetMaxLength(30)

		hbox6.Add(authLabel,proportion=1,flag=wx.LEFT,border=10)
		hbox6.Add(self.authEntry,proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		sbs.Add(hbox6,flag=wx.EXPAND,border=10)

		#BUTTON SPACER
		self.bSpacer = wx.StaticText(pnl, label='')
		self.bSpacer.SetFont(font)
		self.bSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.bSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#BUTTONS
		hbox7 = wx.BoxSizer(wx.HORIZONTAL)
		aButt = wx.Button(pnl,label='ADD')
		hbox7.Add(aButt,flag=wx.EXPAND,proportion=1)

		cButt = wx.Button(pnl,label="CANCEL")
		#cButt.Bind(wx.EVT_BUTTON,self.OnExit)
		hbox7.Add(cButt,flag=wx.EXPAND,proportion=1)

		#SPACER
		self.cbSpacer = wx.StaticText(pnl, label='')
		self.cbSpacer.SetFont(font)
		self.cbSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.cbSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		sbs.Add(hbox7,flag=wx.EXPAND,proportion=1)

		pnl.SetSizer(sbs)

class SearchDialog(wx.Dialog):
	def __init__(self,information):
		super(AddDialog,self).__init__(*args,**kw)

		self.InitUI()
		self.SetSize((200,200))
		self.SetTitle('Search')
	
	def InitUI(self):
		pnl = wx.Panel(self)
		vBox = wx.BoxSizer(wx.VERTICAL)


class Confirmation(wx.Dialog):
	def __init__(self,information):
		super(AddDialog,self).__init__(*args,**kw)

		self.InitUI()
		self.SetSize((200,200))
		self.SetTitle('Confirm')
	
	def InitUI(self):
		pnl = wx.Panel(self)
		vBox = wx.BoxSizer(wx.VERTICAL)

		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		conf = wx.StaticText(pnl, label='Are you sure?')
		hbox1.Add(conf,flag=wx.EXPAND,border=10)

		hbox2=wx.BoxSizer(wx.HORIZONTAL)
		yBut = wx.Button(pnl, label='YES')
		hbox2.Add(yBut,flag=wx.EXPAND)
		nBut = wx.Button(pnl,label='NO')
		hbox2.Add(nBut,flag=wx.EXPAND)

		vBox.Add(hbox1)
		vBox.Add(hbox2)

class AddDialog(wx.Dialog):
	def __init__(self,*args,**kw):
		super(AddDialog,self).__init__(*args,**kw)
		self.InitUI()
		self.SetSize((350,420))
		self.SetTitle('Add Card')

	def InitUI(self):
		pnl = wx.Panel(self)
		vbox = wx.BoxSizer(wx.VERTICAL)
		sb = wx.StaticBox(pnl, label="Add")
		sbs = wx.StaticBoxSizer(sb,orient=wx.VERTICAL)

		font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(4)

		#CARD SPACER
		self.cSpacer = wx.StaticText(pnl, label='')
		self.cSpacer.SetFont(font)
		self.cSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.cSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#CARD
		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		cLabel = wx.StaticText(pnl,label="Card:")
		self.cEntry = wx.TextCtrl(pnl)
		self.cEntry.SetMaxLength(12)

		hbox1.Add(cLabel,proportion=1,flag=wx.LEFT,border=10)
		hbox1.Add(self.cEntry,proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		sbs.Add(hbox1,flag=wx.EXPAND)

		#ACCOUNT SPACER
		self.aSpacer = wx.StaticText(pnl, label='')
		self.aSpacer.SetFont(font)
		self.aSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.aSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#ACCOUNT
		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		aLabel = wx.StaticText(pnl,label="Account:")
		self.aEntry = wx.TextCtrl(pnl)
		self.aEntry.SetMaxLength(12)

		hbox2.Add(aLabel,proportion=1,flag=wx.LEFT,border=10)
		hbox2.Add(self.aEntry,proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		sbs.Add(hbox2,flag=wx.EXPAND,border=10)

		#DESCRIPTION SPACER
		self.dSpacer = wx.StaticText(pnl, label='')
		self.dSpacer.SetFont(font)
		self.dSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.dSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#DESCRIPTION
		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		dLabel = wx.StaticText(pnl,label="Name:")
		self.dEntry = wx.TextCtrl(pnl)
		self.dEntry.SetMaxLength(30)

		hbox3.Add(dLabel,proportion=1,flag=wx.LEFT,border=10)
		hbox3.Add(self.dEntry,proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		sbs.Add(hbox3,flag=wx.EXPAND,border=10)

		#PIN SPACER
		self.pSpacer = wx.StaticText(pnl, label='')
		self.pSpacer.SetFont(font)
		self.pSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.pSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#PIN
		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
		pLabel = wx.StaticText(pnl,label="PIN:")
		self.pEntry = wx.TextCtrl(pnl)
		self.pEntry.SetMaxLength(30)

		hbox4.Add(pLabel,proportion=1,flag=wx.LEFT,border=10)
		hbox4.Add(self.pEntry,proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		sbs.Add(hbox4,flag=wx.EXPAND,border=10)

		#SEQUENCE SPACER
		self.sSpacer = wx.StaticText(pnl, label='')
		self.sSpacer.SetFont(font)
		self.sSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.sSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#SEQUENCE
		hbox5 = wx.BoxSizer(wx.HORIZONTAL)
		sLabel = wx.StaticText(pnl,label="Prompts:")
		self.sEntry = wx.TextCtrl(pnl)
		self.sEntry.SetMaxLength(30)

		hbox5.Add(sLabel,proportion=1,flag=wx.LEFT,border=10)
		hbox5.Add(self.sEntry,proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		sbs.Add(hbox5,flag=wx.EXPAND,border=10)

		#AUTHORIZATION SPACER
		self.dSpacer = wx.StaticText(pnl, label='')
		self.dSpacer.SetFont(font)
		self.dSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.dSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#AUTHORIZATION
		hbox6 = wx.BoxSizer(wx.HORIZONTAL)
		authLabel = wx.StaticText(pnl,label="Restrictions:")
		self.authEntry = wx.TextCtrl(pnl)
		self.authEntry.SetMaxLength(30)

		hbox6.Add(authLabel,proportion=1,flag=wx.LEFT,border=10)
		hbox6.Add(self.authEntry,proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		sbs.Add(hbox6,flag=wx.EXPAND,border=10)

		#BUTTON SPACER
		self.bSpacer = wx.StaticText(pnl, label='')
		self.bSpacer.SetFont(font)
		self.bSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.bSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#BUTTONS
		hbox7 = wx.BoxSizer(wx.HORIZONTAL)
		aButt = wx.Button(pnl,label='ADD')
		aButt.Bind(wx.EVT_BUTTON,self.GetValues)
		hbox7.Add(aButt,flag=wx.EXPAND,proportion=1)

		cButt = wx.Button(pnl,label="CANCEL")
		cButt.Bind(wx.EVT_BUTTON,self.OnExit)
		hbox7.Add(cButt,flag=wx.EXPAND,proportion=1)

		#SPACER
		self.cbSpacer = wx.StaticText(pnl, label='')
		self.cbSpacer.SetFont(font)
		self.cbSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.cbSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		sbs.Add(hbox7,flag=wx.EXPAND,proportion=1)

		pnl.SetSizer(sbs)

	def GetValues(self, e):
		validEntry=True
		'''
		print("card " + self.cEntry.GetValue())
		print("acc " + self.aEntry.GetValue())
		print("det " + self.dEntry.GetValue())
		print("pin " + self.pEntry.GetValue())
		print("seq " + self.sEntry.GetValue())
		'''
		if(files.numCheck(self.cEntry.GetValue())[1] == False or self.cEntry.GetValue() == ""):
			self.cSpacer.SetLabel("Card Value can only contain numbers (0-9)")
			validEntry = False
		else:
			self.cSpacer.SetLabel("")
		if(files.numCheck(self.aEntry.GetValue())[1] == False or self.cEntry.GetValue() == ""):
			self.aSpacer.SetLabel("Account Value can only contain numbers (0-9)")
			validEntry = False
		else:
			self.aSpacer.SetLabel("")
		if(files.numCheck(self.pEntry.GetValue())[1] == False and self.pEntry.GetValue() != ""):
			self.pSpacer.SetLabel("PIN Value can only contain numbers (0-9)")
			validEntry = False
		else:
			self.pSpacer.SetLabel("")
		if(files.numCheck(self.sEntry.GetValue())[1] == False):
			self.sSpacer.SetLabel("Sequence Value can only contain numbers (0-9)")
			validEntry = False
		else:
			self.sSpacer.SetLabel("")
		
		if validEntry:
			self.completeCard = card.card(self.cEntry.GetValue(),self.aEntry.GetValue(),self.dEntry.GetValue(),self.pEntry.GetValue(),self.sEntry.GetValue(),self.authEntry.GetValue(),True)
			self.EndModal(1)

	def OnExit(self, e):
		self.EndModal(0)


class Main_Window(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Main_Window, self).__init__(*args, **kwargs)
		icon = wx.Icon("tsc.ico", wx.BITMAP_TYPE_ANY)
		self.currentEdit = ""
		self.inf = info()
		self.SetIcon(icon)
		self.InitUI()
		self.Centre()
		self.SetTitle('TSC Card Manager')
	def InitUI(self):


		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		searchMenu = wx.Menu()

		menuNew = fileMenu.Append(wx.ID_NEW,'&New')
		menuSave = fileMenu.Append(wx.ID_SAVE,'&Save')
		fileMenu.AppendSeparator()

		imp = wx.Menu()
		imCard = imp.Append(wx.ID_ANY,'Import Cards.txt...')
		fileMenu.Append(wx.ID_ANY, 'I&mport',imp)
		fileMenu.AppendSeparator()
		menuQuit = fileMenu.Append(wx.ID_EXIT,'&Quit')
		menubar.Append(fileMenu, '&File')

		byCard = searchMenu.Append(wx.ID_ANY, '&By Card Number')
		byAcct = searchMenu.Append(wx.ID_ANY, '&By Account Number')
		menubar.Append(searchMenu, '&Search')

		self.SetMenuBar(menubar)
		self.Bind(wx.EVT_MENU, self.OnQuit, menuQuit)
		self.Bind(wx.EVT_MENU, self.OnNew, menuNew)
		self.Bind(wx.EVT_MENU, self.OnImportCards, imCard)
		self.SetSize((880, 340))
		
		panel = wx.Panel(self)

		font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(9)

		vbox = wx.BoxSizer(wx.VERTICAL)

		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		hbox3 = wx.BoxSizer(wx.VERTICAL)
		hbox4 = wx.BoxSizer(wx.VERTICAL)
		fill1 = wx.BoxSizer(wx.HORIZONTAL)
		fill2 = wx.BoxSizer(wx.HORIZONTAL)
		hbox6 = wx.BoxSizer(wx.HORIZONTAL)
		

		st1 = wx.StaticText(panel, label='Select a card below:')
		st1.SetFont(font)
		hbox1.Add(st1)
		vbox.Add(hbox1,flag=wx.LEFT|wx.TOP,border=4)
		vbox.Add((-1, 10))

		
		self.listbox = wx.ListBox(panel)
		hbox2.Add(self.listbox, proportion=1, flag=wx.EXPAND)
		vbox.Add(hbox2, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=10)

		b1 = wx.Button(panel,label='ADD CARD')
		b1.SetFont(font)
		hbox3.Add(b1,flag=wx.EXPAND, border=10)

		fill1.Add(wx.StaticText(panel,label=""),flag=wx.EXPAND,border=10)
		hbox3.Add(fill1,flag=wx.EXPAND,border=10)

		eBut = wx.Button(panel,label='EDIT CARD')
		eBut.SetFont(font)
		hbox3.Add(eBut,flag=wx.EXPAND, border=10)

		eBut.Bind(wx.EVT_BUTTON,self.OnEdit)

		adBox = wx.BoxSizer(wx.HORIZONTAL)
		bON = wx.Button(panel,label='ACTIVATE CARD')
		bON.SetFont(font)
		adBox.Add(bON,flag=wx.EXPAND, border=10,proportion=1)

		bOFF = wx.Button(panel,label='DEACTIVATE CARD')
		bOFF.SetFont(font)
		adBox.Add(bOFF,flag=wx.EXPAND, border=10,proportion=1)
		hbox3.Add(adBox,flag=wx.EXPAND)

		bON.Bind(wx.EVT_BUTTON,self.OnToggleOn)
		bOFF.Bind(wx.EVT_BUTTON,self.OnToggleOff)

		b2 = wx.Button(panel,label='DELETE CARD')
		b2.SetFont(font)
		hbox4.Add(b2,flag=wx.EXPAND, border=10, proportion =1)
		hbox3.Add(hbox4,flag=wx.EXPAND)

		fill2.Add(wx.StaticText(panel,label=""),flag=wx.EXPAND,border=10)
		hbox3.Add(fill2,flag=wx.EXPAND,border=10)

		b5 = wx.Button(panel,label="SAVE TO CARDS.TXT")
		b5.SetFont(font)
		hbox3.Add(b5,flag=wx.EXPAND)


		hbox2.Add(hbox3,flag=wx.LEFT,border=10)
		

		vbox.Add((-1, 25))

		b1.Bind(wx.EVT_BUTTON,self.OnAdd)
		self.Bind(wx.EVT_BUTTON,self.OnDelete, id=b2.GetId())
		panel.SetSizer(vbox)

	def OnEdit(self,e):
		sel = self.listbox.GetSelection()
		if sel != -1:
			ed = EditDialog(self, -1, 'Edit')
			result = ed.ShowModal()
			ed.Destroy()

	def Refresh(self):
		self.listbox.Clear()
		tgl = ""
		for i in self.inf.cardList:
			if self.inf.cardList[i].getActive() == True:
				tgl = "ACTIVE     "
			else:
				tgl = "INACTIVE "
			space = ""
			for __ in range(18 - len(self.inf.cardList[i].card)):
				space = space + " "
			self.listbox.Append(tgl + " CARD #: " + self.inf.cardList[i].card + space + self.inf.cardList[i].description)

	def OnNew(self, e):
		addDialog = Confirmation(None, title='Confirm')
		addDialog.ShowModal()
		addDialog.Destroy()
		self.listbox.Clear()
	
	def OnToggleOn(self, e):
		sel = self.listbox.GetSelection()
		if sel != -1:
			if self.inf.cardList[self.listbox.GetString(sel).split()[3]].getActive() is not True:
				print(self.listbox.GetString(sel).split()[3] + " Turned On")
				self.inf.cardList[self.listbox.GetString(sel).split()[3]].setActive(True)
				self.Refresh()
	
	def OnToggleOff(self, e):
		sel = self.listbox.GetSelection()
		if sel != -1:	
			if self.inf.cardList[self.listbox.GetString(sel).split()[3]].getActive() is True:
				print(self.listbox.GetString(sel).split()[3] + " Turned Off")
				self.inf.cardList[self.listbox.GetString(sel).split()[3]].setActive(False)
				self.Refresh()

	def OnDelete(self, e):
		sel = self.listbox.GetSelection()
		if sel != -1:
			print(self.listbox.GetString(sel).split()[3] + " Deleted")
			self.listbox.Delete(sel)
			print(self.inf.cardList.pop(self.listbox.GetString(sel).split()[3]))

	def OnAdd(self, e):
		addDialog = AddDialog(None)
		result = addDialog.ShowModal()
		if result == 1:
			self.AddCard(addDialog.completeCard)
		addDialog.Destroy()

	def OnQuit(self, e):
		self.Close()

	def OnImportCards(self, e):
		self.listbox.Clear()
		self.inf.cardList = files.importCards()
		self.Refresh()
	
	def AddCard(self,card):
		if card.card not in self.inf.cardList:
			self.inf.cardList[card.card] = card
			self.Refresh()
		else:
			print("card already in deck")


def main():

	app = wx.App()
	ex = Main_Window(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()