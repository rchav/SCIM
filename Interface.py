"""
******************************************************************************

SCIM: Interface

Robert Chavez
All rights reserved

******************************************************************************
"""

import Tkinter
import tkFont


class interface(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.textboxFont = tkFont.Font(family="Helvetica", size=12)
        self.labelFont = tkFont.Font(family="Helvetica", size = 13, weight="bold")

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
        self.locationEntry = Tkinter.Entry(self, textvariable = self.locationVariable, font=self.textboxFont, width=35)
        self.locationEntry.insert(0, "Enter location name")
        self.locationEntry.configure(fg="Gray")
        self.locationEntry.grid(column=0,row=2,sticky='W',columnspan=3,padx=5)
        self.locationEntry.bind("<FocusIn>", self.clearLocationName)
        self.locationEntry.bind("<FocusOut>", self.resetLocationPlaceholder)

        locationLabelVar = Tkinter.StringVar()
        locationLabelVar.set("Camera Location Name: ")
        locationLabel = Tkinter.Label(self, textvariable = locationLabelVar, anchor="w", font=self.labelFont)
        locationLabel.grid(column=0,row=1,sticky='W',columnspan=3)

        # Address vars
        self.addressStreetVar = Tkinter.StringVar()
        self.addressLine2Var = Tkinter.StringVar()
        self.addressCityVar = Tkinter.StringVar()
        self.addressCityVar.set("Manhattan")
        self.addressStateVar = Tkinter.StringVar()
        self.addressStateVar.set("NY")

        # Address entry boxes init (row 3 - 10)
        self.addressStreetEntry = Tkinter.Entry(self, textvariable = self.addressStreetVar, font=self.textboxFont)
        self.addressStreetEntry.insert(0, "123 Street Name")
        self.addressStreetEntry.configure(fg="Gray")
        self.addressStreetEntry.grid(column=0,row=5,sticky='W',columnspan=2,padx=5)
        self.addressStreetEntry.bind("<FocusIn>", self.clearAddressStreet)
        self.addressStreetEntry.bind("<FocusOut>", self.resetAddressStreetPlaceholder)

        # address 2nd line
        self.addressLine2Entry = Tkinter.Entry(self, textvariable = self.addressLine2Var, font=self.textboxFont)
        self.addressLine2Entry.grid(column=0,row=6,sticky='W',columnspan=2,padx=5)
        self.addressLine2Entry.insert(0, "Apt, suite, etc.")
        self.addressLine2Entry.configure(fg="Gray")
        self.addressLine2Entry.bind("<FocusIn>", self.clearAddressLine2)
        self.addressLine2Entry.bind("<FocusOut>", self.resetAddressLine2Placeholder)

        # address city
        self.addressCityEntry = Tkinter.Entry(self, textvariable = self.addressCityVar, width=16, font=self.textboxFont, bg="#767676")
        self.addressCityEntry.grid(column=0,row=7,sticky='W',columnspan=2,padx=5)
        self.addressCityEntry.configure(state='readonly')
        
        # address state
        self.addressStateEntry = Tkinter.Entry(self, textvariable = self.addressStateVar, width=3, font=self.textboxFont, bg="#767676")
        self.addressStateEntry.grid(column=0,row=7,sticky='W',padx=158)
        self.addressStateEntry.configure(state='readonly')

        # Address label
        addressLabelVar = Tkinter.StringVar()
        addressLabelVar.set("Address: ")
        addressLabel = Tkinter.Label(self, textvariable = addressLabelVar, anchor='w', font=self.labelFont)
        addressLabel.grid(column=0,row=3, sticky='w')


        # date of video recovery setup (row 11-20)
            # label
        dateOfRecordingLabelVar = Tkinter.StringVar()
        dateOfRecordingLabelVar.set("Date of video recording: ")
        dateOfRecordingLabel = Tkinter.Label(self, textvariable=dateOfRecordingLabelVar, anchor='w', font=self.labelFont)
        dateOfRecordingLabel.grid(column=0, row=11, sticky='w')

            # entry box
        self.dateOfRecordingVar = Tkinter.StringVar()
        self.dateOfRecordingEntry = Tkinter.Entry(self, textvariable=self.dateOfRecordingVar, width=10, font=self.textboxFont)
        self.dateOfRecordingEntry.grid(column=0, row=12, sticky='w', padx=5)
        self.dateOfRecordingEntry.insert(0, "mm/dd/yyyy")
        self.dateOfRecordingEntry.configure(fg="Gray")
        self.dateOfRecordingEntry.bind("<FocusIn>", self.clearDateOfRecording)
        self.dateOfRecordingEntry.bind("<FocusOut>", self.resetDateOfRecordingPlaceholder)




        # setting up window size and other options
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2 - 210
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2 - 219
                    
        self.grid_columnconfigure(0,weight=1)
        self.resizable(False,False)
        self.update()

        self.geometry("420x438+%d+%d" % (x,y))


#Textbox clear and placeholder methods
    # methods for location name box
    def clearLocationName(self, event):
        locationName = self.locationEntry.get()
        if locationName == "Enter location name":
            self.locationEntry.delete(0, Tkinter.END)
            self.locationEntry.configure(fg="Black")
    
    def resetLocationPlaceholder(self, event):
        locationName = self.locationEntry.get()
        if len(locationName) == 0:
            self.locationEntry.configure(fg="Gray")
            self.locationEntry.insert(0, "Enter location name")


    # methods for street address box
    def clearAddressStreet(self, event):
        street = self.addressStreetEntry.get()
        if street == "123 Street Name":
            self.addressStreetEntry.delete(0, Tkinter.END)
            self.addressStreetEntry.configure(fg="Black")

    def resetAddressStreetPlaceholder(self, event):
        street = self.addressStreetEntry.get()
        if len(street) == 0:
            self.addressStreetEntry.configure(fg="Gray")
            self.addressStreetEntry.insert(0, "123 Street Name")
            

    # methods for street line 2 box
    def clearAddressLine2(self, event):
        street2 = self.addressLine2Entry.get()
        if street2 == "Apt, suite, etc.":
            self.addressLine2Entry.delete(0, Tkinter.END)
            self.addressLine2Entry.configure(fg="Black")

    def resetAddressLine2Placeholder(self, event):
        street2 = self.addressLine2Entry.get()
        if len(street2) == 0:
            self.addressLine2Entry.configure(fg="Gray")
            self.addressLine2Entry.insert(0, "Apt, suite, etc.")


    # methods for date of recording box
    def clearDateOfRecording(self, event):
        date = self.dateOfRecordingEntry.get()
        if date == "mm/dd/yyyy":
            self.dateOfRecordingEntry.delete(0, Tkinter.END)
            self.dateOfRecordingEntry.configure(fg="Black")
    
    def resetDateOfRecordingPlaceholder(self, event):
        date = self.dateOfRecordingEntry.get()
        if len(date) == 0:
            self.dateOfRecordingEntry.configure(fg="Gray")
            self.dateOfRecordingEntry.insert(0, "mm/dd/yyyy")
