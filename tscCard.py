import wx
import files
import card
import re

class info():
	def __init__(self): 
		self.cardList = {}

class DoneDialog(wx.Dialog):
	def __init__(self,*args,**kw):
		super(DoneDialog,self).__init__(*args,**kw)

		self.InitUI()
		self.SetSize((150,150))
		self.SetTitle('Done!')
	
	def InitUI(self):	
		font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(12)
		bfont = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		bfont.SetPointSize(4)

		pnl = wx.Panel(self)
		vbox = wx.BoxSizer(wx.VERTICAL)
		sb = wx.StaticBox(pnl, label="")
		sb.SetFont(font)
		sbs = wx.StaticBoxSizer(sb,orient=wx.VERTICAL)

		#spacer
		spacer=wx.BoxSizer(wx.HORIZONTAL)
		spaceText=wx.StaticText(pnl,label="  File saved!")
		spaceText.SetFont(font)
		spacer.Add(spaceText)
		sbs.Add(spacer)
		#spacer2
		spacer2=wx.BoxSizer(wx.HORIZONTAL)
		spacer2.Add(wx.StaticText(pnl,label=""))
		sbs.Add(spacer2)

		hbox = wx.BoxSizer(wx.HORIZONTAL)
		bOK = wx.Button(pnl,label='OK')
		bOK.Bind(wx.EVT_BUTTON,self.OnOK)
		hbox.Add(bOK)

		sbs.Add(hbox,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,proportion=1,border=10)

		pnl.SetSizer(sbs)

	def OnOK(self,e):
		self.EndModal(1)

class EditDialog(wx.Dialog):
	def __init__(self,parent,id,title):
		wx.Dialog.__init__(self,parent,id,title)
		self.p = parent
		self.InitUI()
		self.SetSize((450,380))
		self.SetTitle('Edit')
	
	def InitUI(self):
		pnl = wx.Panel(self)
		vbox = wx.BoxSizer(wx.VERTICAL)
		subTitle = "Editing Card " + self.p.currentEdit
		sb = wx.StaticBox(pnl, label=subTitle)
		sbs = wx.StaticBoxSizer(sb,orient=wx.VERTICAL)
		font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(4)

		#ACCOUNT SPACER
		self.aSpacer = wx.StaticText(pnl, label='')
		self.aSpacer.SetFont(font)
		self.aSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.aSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#ACCOUNT
		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		aLabel = wx.StaticText(pnl,label="Account:")
		oldAccText = self.p.inf.cardList[self.p.currentEdit].getAccount()
		self.aEntry = wx.TextCtrl(pnl)
		self.aEntry.SetMaxLength(12)
		self.aEntry.write(oldAccText)

		hbox2.Add(aLabel,proportion=1,flag=wx.LEFT,border=10)
		hbox2.Add(self.aEntry,proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		sbs.Add(hbox2,flag=wx.EXPAND,border=10)

		#DESCRIPTION SPACER
		self.dSpacer = wx.StaticText(pnl, label='')
		self.dSpacer.SetFont(font)
		self.dSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.dSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#DESCRIPTION
		oldDesc = self.p.inf.cardList[self.p.currentEdit].getDescription()
		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		dLabel = wx.StaticText(pnl,label="Name:")
		self.dEntry = wx.TextCtrl(pnl)
		self.dEntry.SetMaxLength(30)
		self.dEntry.write(oldDesc)

		hbox3.Add(dLabel,proportion=1,flag=wx.LEFT,border=10)
		hbox3.Add(self.dEntry,proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		sbs.Add(hbox3,flag=wx.EXPAND,border=10)

		#PIN SPACER
		self.pSpacer = wx.StaticText(pnl, label='')
		self.pSpacer.SetFont(font)
		self.pSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.pSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#PIN
		oldPin = self.p.inf.cardList[self.p.currentEdit].getPin()
		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
		pLabel = wx.StaticText(pnl,label="PIN:")
		self.pEntry = wx.TextCtrl(pnl)
		self.pEntry.SetMaxLength(30)
		self.pEntry.write(oldPin)

		hbox4.Add(pLabel,proportion=1,flag=wx.LEFT,border=10)
		hbox4.Add(self.pEntry,proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		sbs.Add(hbox4,flag=wx.EXPAND,border=10)

		#SEQUENCE SPACER
		self.sSpacer = wx.StaticText(pnl, label='')
		self.sSpacer.SetFont(font)
		self.sSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.sSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#SEQUENCE
		oldSeq = self.p.inf.cardList[self.p.currentEdit].getSeq()
		hbox5 = wx.BoxSizer(wx.HORIZONTAL)
		sLabel = wx.StaticText(pnl,label="Prompts:")
		self.sEntry = wx.TextCtrl(pnl)
		self.sEntry.SetMaxLength(30)
		self.sEntry.write(oldSeq)

		hbox5.Add(sLabel,proportion=1,flag=wx.LEFT,border=10)
		hbox5.Add(self.sEntry,proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		sbs.Add(hbox5,flag=wx.EXPAND,border=10)

		#AUTHORIZATION SPACER
		self.dSpacer = wx.StaticText(pnl, label='')
		self.dSpacer.SetFont(font)
		self.dSpacer.SetForegroundColour('#ff0000')
		sbs.Add(self.dSpacer,flag=wx.EXPAND|wx.LEFT|wx.RIGHT)

		#AUTHORIZATION
		oldAuth = self.p.inf.cardList[self.p.currentEdit].getAuth()
		hbox6 = wx.BoxSizer(wx.HORIZONTAL)
		authLabel = wx.StaticText(pnl,label="Restrictions:")
		self.authEntry = wx.TextCtrl(pnl)
		self.authEntry.SetMaxLength(30)
		self.authEntry.write(oldAuth)

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
		aButt = wx.Button(pnl,label='SAVE')
		aButt.Bind(wx.EVT_BUTTON,self.OnSave)
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

	def OnSave(self, e):
		validEntry=True
		if(files.numCheck(self.aEntry.GetValue())[1] == False or self.aEntry.GetValue() == ""):
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
			self.completeCard = card.card(self.p.currentEdit,self.aEntry.GetValue(),self.dEntry.GetValue(),self.pEntry.GetValue(),self.sEntry.GetValue(),self.authEntry.GetValue(),True)
			
			self.p.inf.cardList[self.p.currentEdit] = self.completeCard
			self.EndModal(1)
	
	def OnExit(self, e):
		self.EndModal(0)

class ExistsError(wx.Dialog):
	def __init__(self,*args,**kw):
		super(ExistsError,self).__init__(*args,**kw)

		self.InitUI()
		self.SetSize((220,150))
		self.SetTitle('Oops')
	
	def InitUI(self):	
		font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(12)
		bfont = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		bfont.SetPointSize(4)

		pnl = wx.Panel(self)
		vbox = wx.BoxSizer(wx.VERTICAL)
		sb = wx.StaticBox(pnl, label="")
		sb.SetFont(font)
		sbs = wx.StaticBoxSizer(sb,orient=wx.VERTICAL)

		#spacer
		spacer=wx.BoxSizer(wx.HORIZONTAL)
		spaceText=wx.StaticText(pnl,label="An entry with that card \nnumber already exists!")
		spaceText.SetFont(font)
		spacer.Add(spaceText)
		sbs.Add(spacer)
		#spacer2
		spacer2=wx.BoxSizer(wx.HORIZONTAL)
		spacer2.Add(wx.StaticText(pnl,label=""))
		sbs.Add(spacer2)

		hbox = wx.BoxSizer(wx.HORIZONTAL)
		bOK = wx.Button(pnl,label='OK')
		bOK.Bind(wx.EVT_BUTTON,self.OnOK)
		hbox.Add(bOK)

		sbs.Add(hbox,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,proportion=1,border=10)

		pnl.SetSizer(sbs)

	def OnOK(self,e):
		self.EndModal(1)

class Confirmation(wx.Dialog):
	def __init__(self,*args,**kw):
		super(Confirmation,self).__init__(*args,**kw)

		self.InitUI()
		self.SetSize((200,150))
		self.SetTitle('Confirm')
	
	def InitUI(self):	
		font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(24)
		bfont = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
		bfont.SetPointSize(4)

		pnl = wx.Panel(self)
		vbox = wx.BoxSizer(wx.VERTICAL)
		sb = wx.StaticBox(pnl)
		sb.SetFont(font)
		sbs = wx.StaticBoxSizer(sb,orient=wx.VERTICAL)

		#spacer
		spacer=wx.BoxSizer(wx.HORIZONTAL)
		confText = wx.StaticText(pnl,label="       Are you sure?")
		confText.SetFont(font)
		spacer.Add(confText)
		sbs.Add(spacer)
		#spacer2
		spacer2=wx.BoxSizer(wx.HORIZONTAL)
		spacer2.Add(wx.StaticText(pnl,label=""))
		sbs.Add(spacer2)

		hbox = wx.BoxSizer(wx.HORIZONTAL)
		bYes = wx.Button(pnl,label='YES')
		bNo = wx.Button(pnl,label='NO')
		bYes.Bind(wx.EVT_BUTTON,self.OnYes)
		bNo.Bind(wx.EVT_BUTTON,self.OnNo)
		hbox.Add(bYes,flag=wx.EXPAND,proportion=1,border=10)
		hbox.Add(bNo,flag=wx.EXPAND,proportion=1,border=10)

		sbs.Add(hbox)

		pnl.SetSizer(sbs)

	def OnYes(self,e):
		self.EndModal(1)

	def OnNo(self,e):
		self.EndModal(0)

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
		self.contentNotSaved = False
		self.searchType = ""
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
		imData = imp.Append(wx.ID_ANY,'Import from tsv...')
		fileMenu.Append(wx.ID_ANY, 'I&mport',imp)
		fileMenu.AppendSeparator()
		menuQuit = fileMenu.Append(wx.ID_EXIT,'&Quit')
		menubar.Append(fileMenu, '&File')

		self.SetMenuBar(menubar)
		self.Bind(wx.EVT_MENU, self.OnQuit, menuQuit)
		self.Bind(wx.EVT_MENU, self.OnNew, menuNew)
		self.Bind(wx.EVT_MENU, self.OnImportCards, imCard)
		self.Bind(wx.EVT_MENU, self.OnOpenCSV, imData)
		self.SetSize((880, 600))
		
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
		hbox3.Add(b1,flag=wx.EXPAND, border=10)

		fill1.Add(wx.StaticText(panel,label=""),flag=wx.EXPAND,border=10)
		hbox3.Add(fill1,flag=wx.EXPAND,border=10)

		eBut = wx.Button(panel,label='EDIT CARD')
		hbox3.Add(eBut,flag=wx.EXPAND, border=10)

		eBut.Bind(wx.EVT_BUTTON,self.OnEdit)

		adBox = wx.BoxSizer(wx.HORIZONTAL)
		bON = wx.Button(panel,label='ACTIVATE CARD')
		adBox.Add(bON,flag=wx.EXPAND, border=10,proportion=1)

		bOFF = wx.Button(panel,label='DEACTIVATE CARD')
		adBox.Add(bOFF,flag=wx.EXPAND, border=10,proportion=1)
		hbox3.Add(adBox,flag=wx.EXPAND)

		bON.Bind(wx.EVT_BUTTON,self.OnToggleOn)
		bOFF.Bind(wx.EVT_BUTTON,self.OnToggleOff)

		b2 = wx.Button(panel,label='DELETE CARD')
		hbox4.Add(b2,flag=wx.EXPAND, border=10, proportion =1)
		hbox3.Add(hbox4,flag=wx.EXPAND)

		#SPACER
		hbox3.Add(wx.StaticLine(panel,wx.LI_HORIZONTAL),flag=wx.ALL|wx.EXPAND,border=20)

		saveToData = wx.Button(panel,label='SAVE TO MASTER .TSV FILE')
		saveToData.Bind(wx.EVT_BUTTON,self.OnExport)
		b5 = wx.Button(panel,label="SAVE TO CARDS.TXT")
		b5.Bind(wx.EVT_BUTTON,self.OnSave)
		hbox3.Add(saveToData,flag=wx.EXPAND)
		hbox3.Add(b5,flag=wx.EXPAND)

		#SEARCH SPACER
		hbox3.Add(wx.StaticLine(panel,wx.LI_HORIZONTAL),flag=wx.ALL|wx.EXPAND,border=20)
		

		#SEARCH
		sHBox = wx.BoxSizer(wx.HORIZONTAL)
		sLabel = wx.StaticText(panel,label="Search:")
		self.sEntry = wx.TextCtrl(panel)
		sHBox.Add(sLabel, proportion=1,flag=wx.LEFT,border=10)
		sHBox.Add(self.sEntry, proportion=2,flag=wx.LEFT|wx.EXPAND|wx.RIGHT, border=10)
		hbox3.Add(sHBox, border = 10, flag=wx.EXPAND)
		
		#RADIO BUTTON SPACER
		self.rSpacer = wx.StaticText(panel, label='')
		self.rSpacer.SetFont(font)
		self.rSpacer.SetForegroundColour('#ff0000')
		hbox3.Add(self.rSpacer)

		rBBox = wx.BoxSizer(wx.HORIZONTAL)
		self.cRButton = wx.RadioButton(panel, label="CARD # SEARCH")
		rBBox.Add(self.cRButton, border=10, flag=wx.LEFT|wx.EXPAND|wx.RIGHT)
		self.cRButton.SetValue(True)
		self.cRButton2 = wx.RadioButton(panel, label="ACCT # SEARCH")
		rBBox.Add(self.cRButton2, border=10, flag=wx.LEFT|wx.EXPAND|wx.RIGHT)
		hbox3.Add(rBBox,border=10)
		
		#SEARCH SPACER
		hbox3.Add(wx.StaticLine(panel,wx.LI_HORIZONTAL),flag=wx.ALL,border=10)

		#SEARCH BUTTONS
		schBut = wx.Button(panel, label="SEARCH")
		hbox3.Add(schBut, flag=wx.EXPAND)
		schBut.Bind(wx.EVT_BUTTON,self.OnSearch)
		rfsBut = wx.Button(panel, label="CLEAR SEARCH")
		hbox3.Add(rfsBut, flag=wx.EXPAND)
		rfsBut.Bind(wx.EVT_BUTTON,self.OnRefresh)

		


		hbox2.Add(hbox3,flag=wx.LEFT,border=10)
		

		vbox.Add((-1, 25))

		b1.Bind(wx.EVT_BUTTON,self.OnAdd)
		self.Bind(wx.EVT_BUTTON,self.OnDelete, id=b2.GetId())
		panel.SetSizer(vbox)

	def OnRefresh(self, e):
		self.Refresh()

	def OnExport(self,e):
		with wx.FileDialog(self, "Save .tsv file", defaultDir='c:\\ICS',wildcard=".tsv files (*.tsv)|*.tsv",style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return     # the user changed their mind
			
			# save the current contents in the file
			pathname = fileDialog.GetPath()
			try:
				files.dataExport(self.inf.cardList, pathname)
			except IOError:
				wx.LogError("Cannot save current data in file '%s'." % pathname)
			
		self.contentNotSaved = False

	def OnSearch(self, e):
		if self.sEntry.GetValue() != "":
			if self.cRButton.GetValue() == True:
				self.listbox.Clear()
				for i in self.inf.cardList:
					space = ""
					tgl = ""
					if self.inf.cardList[i].card == self.sEntry.GetValue():
						if self.inf.cardList[i].getActive() == True:
							tgl = "ACTIVE     "
						else:
							tgl = "INACTIVE "
						for __ in range(8 - len(self.inf.cardList[i].card)):
							space = space + "  "
						self.listbox.Append(tgl + "   CARD #: " + self.inf.cardList[i].card + space + self.inf.cardList[i].description)
			else:
				self.listbox.Clear()
				temp = self.inf.cardList
				for i in self.inf.cardList:
					space = ""
					tgl = ""
					if self.inf.cardList[i].getAccount() == self.sEntry.GetValue():
						if self.inf.cardList[i].getActive() == True:
							tgl = "ACTIVE     "
						else:
							tgl = "INACTIVE "
						for __ in range(8 - len(self.inf.cardList[i].card)):
							space = space + "  "
						self.listbox.Append(tgl + "   CARD #: " + self.inf.cardList[i].card + space + self.inf.cardList[i].description)

	def OnEdit(self,e):
		sel = self.listbox.GetSelection()
		if sel != -1:
			self.currentEdit = self.inf.cardList[self.listbox.GetString(sel).split()[3]].getCard()
			ed = EditDialog(self, -1, 'Edit')
			result = ed.ShowModal()
			if result == 1:
				self.Refresh()
			ed.Destroy()
		self.contentNotSaved = True

	def Refresh(self):
		self.listbox.Clear()
		tgl = ""
		for i in self.inf.cardList:
			if self.inf.cardList[i].getActive() == True:
				tgl = "ACTIVE     "
			else:
				tgl = "INACTIVE "
			space = ""
			for __ in range(8 - len(self.inf.cardList[i].card)):
				space = space + "  "
			self.listbox.Append(tgl + "   CARD #: " + self.inf.cardList[i].card + space + self.inf.cardList[i].description)

	def OnNew(self, e):
		if not self.contentNotSaved:
			addDialog = Confirmation(None)
			result = addDialog.ShowModal()
			if result == 1:
				self.inf.cardList.clear()
				self.listbox.Clear()	
			addDialog.Destroy()

	def OnSave(self,e):
		if self.listbox.GetCount() > 0:
			with wx.FileDialog(self, "Save cards.txt", defaultDir='c:\\ICS',wildcard="Card files (*.txt)|*.txt",style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
				if fileDialog.ShowModal() == wx.ID_CANCEL:
					return     # the user changed their mind

				# save the current contents in the file
				pathname = fileDialog.GetPath()
				try:
					files.cardsOutput(self.inf.cardList, pathname)
				except IOError:
					wx.LogError("Cannot save current data in file '%s'." % pathname)
		
	def OnToggleOn(self, e):
		sel = self.listbox.GetSelection()
		if sel != -1:
			if self.inf.cardList[self.listbox.GetString(sel).split()[3]].getActive() is not True:
				self.inf.cardList[self.listbox.GetString(sel).split()[3]].setActive(True)
				self.Refresh()
	
	def OnToggleOff(self, e):
		sel = self.listbox.GetSelection()
		if sel != -1:	
			if self.inf.cardList[self.listbox.GetString(sel).split()[3]].getActive() is True:
				self.inf.cardList[self.listbox.GetString(sel).split()[3]].setActive(False)
				self.Refresh()

	def OnDelete(self, e):
		sel = self.listbox.GetSelection()
		if sel != -1:
			addDialog = Confirmation(None)
			result = addDialog.ShowModal()
			if result == 1:
				self.listbox.Delete(sel)
				self.inf.cardList.pop(self.listbox.GetString(sel).split()[3])
			addDialog.Destroy()
		self.contentNotSaved = True
			
	def OnAdd(self, e):
		addDialog = AddDialog(None)
		result = addDialog.ShowModal()
		if result == 1:
			self.AddCard(addDialog.completeCard)
		addDialog.Destroy()
		self.contentNotSaved = True

	def OnQuit(self, e):
		self.Close()

	def OnImportCards(self, e):
		if self.contentNotSaved:
			if wx.MessageBox("Data has not been saved to primary CSV. Proceed?", "Please confirm",wx.ICON_QUESTION | wx.YES_NO, self) == wx.NO:
				return
    # otherwise ask the user what new file to open
		with wx.FileDialog(self, "Open cards.txt file", defaultDir='c:\\ICS',wildcard="cards files (*.txt)|*.txt",style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return     # the user changed their mind

			# Proceed loading the file chosen by the user
			pathname = fileDialog.GetPath()
			try:
				self.inf.cardList = files.importCards(pathname)
			except IOError:
				wx.LogError("Cannot open file '%s'." % newfile)
		self.listbox.Clear()
		self.Refresh()
		self.contentNotSaved = True
	
	def AddCard(self,card):
		if card.card not in self.inf.cardList:
			print("adding card")
			self.inf.cardList[card.card] = card
			self.Refresh()
		self.contentNotSaved = True

	def OnOpenCSV(self, e):
		if self.contentNotSaved:
			if wx.MessageBox("Data has not been saved to a .tsv File. Proceed?", "Please confirm",wx.ICON_QUESTION | wx.YES_NO, self) == wx.NO:
				return

    # otherwise ask the user what new file to open
		with wx.FileDialog(self, "Open .tsv file", defaultDir='c:\\ICS',wildcard=".tsv files (*.tsv)|*.tsv",style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return     # the user changed their mind

			pathname = fileDialog.GetPath()
			try:
				self.inf.cardList = files.importData(pathname)
			except IOError:
				wx.LogError("Cannot open file '%s'." % newfile)
		self.listbox.Clear()
		self.Refresh()
		self.contentNotSaved = True

def main():

	app = wx.App()
	ex = Main_Window(None)
	ex.Show()
	app.MainLoop()


if __name__ == '__main__':
	main()