"""
******************************************************************************

SCIM: Interface

Robert Chavez
All rights reserved

******************************************************************************
"""

import Tkinter, tkFileDialog

class interface(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        # label bar on top of window
        titleVariable = Tkinter.StringVar()
        titleVariable.set(u"   Welcome to SCIM   ")
        titleLabel = Tkinter.Label(self,textvariable=titleVariable, anchor="w", fg="white",bg="#0154a0",font="Constantia 12 bold")
        titleLabel.grid(column=0,row=0,columnspan=3,sticky='EW')


        # status bar on bottom of window
        self.statusVariable = Tkinter.StringVar()
        self.statusVariable.set(u"<init status>")
        self.statusLabel = Tkinter.Label(self,textvariable=self.statusVariable, anchor="w", fg="#f6731b",bg="#0154a0",font="Constantia 11")
        self.statusLabel.grid(column=0,row=100,columnspan=4,sticky='EW')


        # location name entry box and label
        self.locationVariable = Tkinter.StringVar()
        self.locationEntry = Tkinter.Entry(self, textvariable = self.locationVariable)
        self.locationEntry.grid(column=1,row=1,sticky='EW',padx=10)

        locationLabelVar = Tkinter.StringVar()
        locationLabelVar.set("Location Name: ")
        locationLabel = Tkinter.Label(self, textvariable = locationLabelVar, anchor="w")
        locationLabel.grid(column=0,row=1)

        # setting up window size and other options
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2 - 210
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2 - 219
                    
        self.grid_columnconfigure(0,weight=1)
        self.resizable(False,False)
        self.update()

        self.geometry("420x438+%d+%d" % (x,y))
        