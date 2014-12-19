"""
******************************************************************************

SCIM: Interface

Robert Chavez
All rights reserved

******************************************************************************
"""

import Tkinter

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
        titleLabel.grid(column=0,row=0,columnspan=4,sticky='EW')


        # status bar on bottom of window
        self.statusVariable = Tkinter.StringVar()
        self.statusLabel = Tkinter.Label(self,textvariable=self.statusVariable, anchor="w", fg="#f6731b",bg="#0154a0",font="Constantia 11")
        self.statusLabel.grid(column=0,row=100,columnspan=4,sticky='EW')


        # location name entry box and label
        self.locationVariable = Tkinter.StringVar()
        self.locationEntry = Tkinter.Entry(self, textvariable = self.locationVariable, width=35)
        self.locationEntry.grid(column=1,row=1,sticky='E',columnspan=3)

        locationLabelVar = Tkinter.StringVar()
        locationLabelVar.set("Location Name: ")
        locationLabel = Tkinter.Label(self, textvariable = locationLabelVar, anchor="w")
        locationLabel.grid(column=0,row=1,sticky='W',columnspan=3)

        # Address vars
        self.addressStreetVar = Tkinter.StringVar()
        self.addressLine2Var = Tkinter.StringVar()
        self.addressCityVar = Tkinter.StringVar()
        self.addressCityVar.set("Manhattan")
        self.addressStateVar = Tkinter.StringVar()
        self.addressStateVar.set("NY")

        # Address entry boxes init (row 2 - 10)
        self.addressStreetEntry = Tkinter.Entry(self, textvariable = self.addressStreetVar)
        self.addressStreetEntry.grid(column=2,row=2,sticky='E',columnspan=2)

        self.addressLine2Entry = Tkinter.Entry(self, textvariable = self.addressLine2Var)
        self.addressLine2Entry.grid(column=2,row=3,sticky='E',columnspan=2)

        self.addressCityEntry = Tkinter.Entry(self, textvariable = self.addressCityVar, width=15)
        self.addressCityEntry.grid(column=2,row=4,sticky='W',columnspan=2,padx=35)

        self.addressStateEntry = Tkinter.Entry(self, textvariable = self.addressStateVar, width=3)
        self.addressStateEntry.grid(column=3,row=4,sticky='E')

        # Address label
        addressLabelVar = Tkinter.StringVar()
        addressLabelVar.set("Address: ")
        addressLabel = Tkinter.Label(self, textvariable = addressLabelVar, anchor='w')
        addressLabel.grid(column=0,row=2, sticky='w')


        # setting up window size and other options
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2 - 210
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2 - 219
                    
        self.grid_columnconfigure(0,weight=1)
        self.resizable(False,False)
        self.update()

        self.geometry("420x438+%d+%d" % (x,y))
        