from tkinter import *
from tkinter import messagebox
import os


class Application(Frame):
    def developer_info(self):
        messagebox.showinfo( "Developer: Vel", "Always be yourself and have faith in yourself. Do not go out and look for a successful personality and try to duplicate it")

    
    def CallBacks(self,value):
        s = 'start explorer'
        s+=value
        #print (s)
        os.system(s)

    def createWidgets(self):
     
        self.hi_there = Button(self)
        self.hi_there["text"] = "Developer",
        self.hi_there["command"] = self.developer_info
        self.hi_there.pack()


        
        newDict = {}
        
        f = open('Info.txt', 'r')
        for line in f:
            listedline = line.strip().split('=')
            if len(listedline) > 1:
                newDict[listedline[0]] = listedline[1]

        for key in newDict:
            Button(self,text=key, command = lambda value=newDict[key]:self.CallBacks(value)).pack()
    
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack()
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()




root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
