from tkinter import *
from tkinter import font
from tkinter import ttk
import os
import csv
import files

class tscCards(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        #iconbitmap(self,"PATH TO ICON HERE") #TODO

        container = Frame(self)
        container.pack(side="top", fill="both",expand="true")
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.title("TSC Card Manager")

        self.frames = {}

        for F in (StartPage, AddCard):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")
 
        self.show_frame(StartPage)
        self.init_menu()

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

    def init_menu(self):
        menu = Menu(self)
        self.config(menu=menu)
        f = Menu(menu)

        f.add_command(label='Import Cards.txt')
        f.add_command(label='Export Cards.txt',command=self.client_exit)
        f.add_command(label='Exit',command=self.client_exit)
        menu.add_cascade(label='File',menu=f)

        edit = Menu(menu)
        edit.add_command(label='Add Card')
        edit.add_command(label='Remove Card')
        menu.add_cascade(label='Edit',menu=edit)
    def client_exit(self):
        exit()

class StartPage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        
        self.f1 = Frame(self)
        self.f2 = Frame(self)
        self.f1.grid(row=0, column=0, columnspan=3,padx =15,pady=15)
        self.f2.grid(row=0, column=3,padx =15,pady=15, sticky=(N, S, E, W))
        self.helv14 = font.Font(family='Helvetica',size=14)
        self.helv14B = font.Font(family='Helvetica',size=14,weight='bold')
        self.helv12 = font.Font(family='Helvetica',size=12)
        self.grid()
        self.grid(sticky=N+S+E+W) 
        #self.pack(fill = BOTH, expand = 1)
        self.yScroll = ttk.Scrollbar(self.f1,orient=VERTICAL)
        self.yScroll.grid(row=1,column=1,rowspan=5,sticky=N+S)
        self.label =Label(self.f1,text="Select card below:",font=self.helv12)
        self.label.grid(row=0,column=0,sticky=N+E+S+W)
        self.listbox = Listbox(self.f1,yscrollcommand=self.yScroll.set,font=self.helv12,width=50)
        
        self.listbox.grid(row=1,column=0,sticky=N+E+S+W)
        self.yScroll['command'] = self.listbox.yview
        self.listbox.grid_propagate(0)
        self.yScroll['command'] = self.listbox.yview
        fill=Label(self.f2)
        add = ttk.Button(self.f2, text="ADD CARD",command=lambda:controller.show_frame(AddCard))
        delete = ttk.Button(self.f2, text="DELETE CARD")
        edit = ttk.Button(self.f2, text="EDIT CARD")
        imprt = ttk.Button(self.f2, text="IMPORT \n CARDS.TXT",command = self.import_cards)
        export = ttk.Button(self.f2, text="EXPORT \n CARDS.TXT")

        fill.grid(row=0,column=3,columnspan=2,ipady=10, ipadx=10,sticky=N+E+S+W)
        add.grid(row=2,column=3,ipady=10, ipadx=10,sticky=N+E+S+W)
        delete.grid(row=2,column=4,ipady=10, ipadx=10,sticky=N+E+S+W)
        edit.grid(row=1,column=3,columnspan=2,ipady=10, ipadx=10,sticky=N+E+S+W)
        imprt.grid(row=3,column=3,ipady=10, ipadx=10,sticky=N+E+S+W)
        export.grid(row=3,column=4,ipady=10, ipadx=10,sticky=N+E+S+W)
        self.listbox.delete(0, END)
        #self.listbox.pack()
    def import_cards(self):
        list = files.importCards()
        for i in list:
            self.listbox.insert(END, i)

        
    
class AddCard(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        
        x = ttk.Button(self,text="testing",command=lambda:controller.show_frame(StartPage))
        x.pack()
    

app = tscCards()
app.mainloop()