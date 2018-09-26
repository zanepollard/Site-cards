from tkinter import *
from tkinter import font
import os
import csv

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        
        self.f1 = Frame(self.master)
        self.f2 = Frame(self.master)
        self.f1.grid(row=0, column=0, columnspan=3,padx =15,pady=15)
        self.f2.grid(row=0, column=3,padx =15,pady=15, sticky=(N, S, E, W))
        self.helv14 = font.Font(family='Helvetica',size=14)
        self.helv14B = font.Font(family='Helvetica',size=14,weight='bold')
        self.helv12 = font.Font(family='Helvetica',size=12)
        for x in range(60):
            Grid.columnconfigure(master, x, weight=1)
        for y in range(30):
            Grid.rowconfigure(master, y, weight=1)
        self.grid()
        self.init_window()

    def init_window(self):
        self.master.title("TSC Card Manager")
        self.grid(sticky=N+S+E+W) 
        #self.pack(fill = BOTH, expand = 1)
        self.yScroll = Scrollbar(self.f1,orient=VERTICAL)
        self.yScroll.grid(row=1,column=1,rowspan=5,sticky=N+S)
        self.label =Label(self.f1,text="Select card below:",font=self.helv12)
        self.label.grid(row=0,column=0,sticky=N+E+S+W)
        self.listbox = Listbox(self.f1,yscrollcommand=self.yScroll.set,font=self.helv12)
        
        self.listbox.grid(row=1,column=0,sticky=N+E+S+W)
        self.yScroll['command'] = self.listbox.yview
        self.listbox.grid_propagate(0)
        self.yScroll['command'] = self.listbox.yview
        self.init_menu()
        self.init_list()
        self.init_buttons()

    def init_menu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)
        f = Menu(menu)

        f.add_command(label='Import Cards.txt',command=self.import_cards)
        f.add_command(label='Export Cards.txt',command=self.client_exit)
        f.add_command(label='Exit',command=self.client_exit)
        menu.add_cascade(label='File',menu=f)

        edit = Menu(menu)
        edit.add_command(label='Add Card')
        edit.add_command(label='Remove Card')
        menu.add_cascade(label='Edit',menu=edit)

    def import_cards(self):
        self.listbox.delete(0, END)
        self.listbox.insert(END, "Test")

    def init_list(self):
        print("hmm")
        self.listbox.delete(0, END)
        #self.listbox.pack()
        with open(".\\}h180924.d1c", newline='') as csvfile: 
            reader = csv.reader(csvfile, quotechar="\"")
            for row in reader:
                self.listbox.insert(END, row[3] + " "+ row[11])
    
    def init_buttons(self):
        add = Button(self.f2, text="ADD CARD",padx =15,pady=18,font=self.helv14B)
        delete = Button(self.f2, text="DELETE CARD",padx =15,pady=18,font=self.helv14B)
        edit = Button(self.f2, text="EDIT CARD",padx =15,pady=18,font=self.helv14B)
        export = Button(self.f2, text="EXPORT \n CARDS.TXT",padx =15,pady=18,font=self.helv14B)

        add.grid(row=1,column=3,sticky=N+E+S+W)
        delete.grid(row=2,column=3,sticky=N+E+S+W)
        edit.grid(row=3,column=3,sticky=N+E+S+W)
        export.grid(row=4,column=3,sticky=N+E+S+W)
    

    def client_exit(self):
        exit()
    

root = Tk()
#root.geometry("400x300")
app = Window(root)
root.mainloop()