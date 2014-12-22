"""
******************************************************************************

SCIM: Interface Init

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

        self.textboxFont = tkFont.Font(family="Constantia", size=12)
        self.labelFont = tkFont.Font(family="Constantia", size = 12, weight='bold')
        self.smallLabelFont = tkFont.Font(family="Constantia", size=11)
        self.statusFont = tkFont.Font(family="Constantia", size=10, weight='bold')

        # title bar on top of window
        titleVariable = Tkinter.StringVar()
        titleVariable.set(u"SCIM: Add a new camera")
        titleLabel = Tkinter.Label(self,textvariable=titleVariable, fg="white",bg="#0154a0",font="Constantia 16")
        titleLabel.grid(column=0,row=0,columnspan=4,sticky='EW')

        # status bar on bottom of window
        self.statusVariable = Tkinter.StringVar()
        self.statusVariable.set("Crime Strategies Unit")
        self.statusLabel = Tkinter.Label(self,textvariable=self.statusVariable, fg="White",bg="#0154a0",font=self.statusFont)
        self.statusLabel.grid(column=0,row=100,columnspan=4,sticky='EW')

        ## Location Name ##
        # location name entry box and label
        self.locationVariable = Tkinter.StringVar()
        self.locationEntry = Tkinter.Entry(self, textvariable = self.locationVariable, font=self.textboxFont, width=48)
        self.locationEntry.insert(0, "Enter location name")
        self.locationEntry.configure(fg="Gray")
        self.locationEntry.grid(column=0,row=2,sticky='W',columnspan=3,padx=5)
        self.locationEntry.bind("<FocusIn>", self.clearLocationName)
        self.locationEntry.bind("<FocusOut>", self.resetLocationPlaceholder)

        locationLabelVar = Tkinter.StringVar()
        locationLabelVar.set("Location Name: ")
        locationLabel = Tkinter.Label(self, textvariable = locationLabelVar, anchor="w", font=self.labelFont)
        locationLabel.grid(column=0,row=1,sticky='W',columnspan=3, pady=7)

        ## Address ##
        # group for address widgets
        addressGroup = Tkinter.LabelFrame(self, bd=0)
        addressGroup.grid(column=0,row=4,sticky='w', padx=5)

        # Address label
        addressLabelVar = Tkinter.StringVar()
        addressLabelVar.set("Address: ")
        addressLabel = Tkinter.Label(self, textvariable = addressLabelVar, anchor='w', font=self.labelFont)
        addressLabel.grid(column=0,row=3, sticky='w', pady=7)

        # Address vars
        self.addressStreetVar = Tkinter.StringVar()
        self.addressLine2Var = Tkinter.StringVar()
        self.addressCityVar = Tkinter.StringVar()
        self.addressCityVar.set("Manhattan")
        self.addressStateVar = Tkinter.StringVar()
        self.addressStateVar.set("NY")

        # Address entry boxes init (row 3 - 10)
        self.addressStreetEntry = Tkinter.Entry(addressGroup, textvariable = self.addressStreetVar, font=self.textboxFont)
        self.addressStreetEntry.insert(0, "123 Street Name")
        self.addressStreetEntry.configure(fg="Gray")
        self.addressStreetEntry.grid(column=0,row=5,sticky='W', columnspan=2)
        self.addressStreetEntry.bind("<FocusIn>", self.clearAddressStreet)
        self.addressStreetEntry.bind("<FocusOut>", self.resetAddressStreetPlaceholder)

        # address 2nd line
        self.addressLine2Entry = Tkinter.Entry(addressGroup, textvariable = self.addressLine2Var, font=self.textboxFont)
        self.addressLine2Entry.grid(column=0,row=6,sticky='W', columnspan=2)
        self.addressLine2Entry.insert(0, "Apt, suite, etc.")
        self.addressLine2Entry.configure(fg="Gray")
        self.addressLine2Entry.bind("<FocusIn>", self.clearAddressLine2)
        self.addressLine2Entry.bind("<FocusOut>", self.resetAddressLine2Placeholder)

        # address city
        self.addressCityEntry = Tkinter.Entry(addressGroup, textvariable = self.addressCityVar, width=16, font=self.textboxFont, bg="#767676")
        self.addressCityEntry.grid(column=0,row=7,sticky='W')
        self.addressCityEntry.configure(state='readonly')
        
        # address state
        self.addressStateEntry = Tkinter.Entry(addressGroup, textvariable = self.addressStateVar, width=3, font=self.textboxFont, bg="#767676")
        self.addressStateEntry.grid(column=1,row=7,sticky='W',padx=4)
        self.addressStateEntry.configure(state='readonly')

        ## Coordinates ##
        # group the Lat/Long entry boxes
        geoGroup = Tkinter.LabelFrame(self, bd=0)
        geoGroup.grid(column=1,row=4,rowspan=4,sticky='nw', padx=5)

        # label the coordinates
        geoLabelVar = Tkinter.StringVar()
        #geoLabelVar.set("Coordinates:    ")
        geoLabel = Tkinter.Label(self, textvariable=geoLabelVar, anchor='w', font=self.labelFont)
        geoLabel.grid(column=1,row=3,sticky='w')

        # lat and long boxes (auto pop when address is completed)
        self.latitudeVar = Tkinter.StringVar()
        self.latitudeEntry = Tkinter.Entry(geoGroup, textvariable=self.latitudeVar, width=20, font=self.textboxFont)
        self.latitudeEntry.grid(column=0,row=2,sticky='w')
        self.latitudeEntry.insert(0, 'Latitude')
        self.latitudeEntry.configure(fg="Gray", state='readonly')

        self.longitudeVar = Tkinter.StringVar()
        self.longitudeEntry = Tkinter.Entry(geoGroup, textvariable=self.longitudeVar, width=20, font=self.textboxFont)
        self.longitudeEntry.grid(column=0,row=4, sticky='w')
        self.longitudeEntry.insert(0, 'Longitude')
        self.longitudeEntry.configure(fg="Gray", state='readonly')

        ## Contact information ##
        # Contact label
        contactInfoLabelVar = Tkinter.StringVar()
        contactInfoLabelVar.set("Contact information:")
        contactInfoLabel = Tkinter.Label(self, textvariable=contactInfoLabelVar, anchor='w',font=self.labelFont)
        contactInfoLabel.grid(column=0,row=5,sticky='w', pady=7)

        # contact group
        contactGroup = Tkinter.LabelFrame(self, bd=0)
        contactGroup.grid(column=0,row=6,columnspan=2,sticky='w',padx=5)

        # first name
        self.contactFirstNameVar = Tkinter.StringVar()
        self.contactFirstNameEntry = Tkinter.Entry(contactGroup, textvariable=self.contactFirstNameVar, width=15, font=self.textboxFont)
        self.contactFirstNameEntry.grid(column=0,row=1,sticky='w')
        self.contactFirstNameEntry.insert(0, "First name")
        self.contactFirstNameEntry.configure(fg="Gray")
        self.contactFirstNameEntry.bind("<FocusIn>", self.clearFirstName)
        self.contactFirstNameEntry.bind("<FocusOut>", self.resetFirstNamePlaceholder)

        # last name
        self.contactLastNameVar = Tkinter.StringVar()
        self.contactLastNameEntry =  Tkinter.Entry(contactGroup, textvariable=self.contactLastNameVar, width=15, font=self.textboxFont)
        self.contactLastNameEntry.grid(column=1,row=1,columnspan=2,sticky='w',padx=5)
        self.contactLastNameEntry.insert(0, "Last name")
        self.contactLastNameEntry.configure(fg="Gray")
        self.contactLastNameEntry.bind("<FocusIn>", self.clearLastName)
        self.contactLastNameEntry.bind("<FocusOut>", self.resetLastNamePlaceholder)

        # title
        self.contactTitleVar = Tkinter.StringVar()
        self.contactTitleEntry = Tkinter.Entry(contactGroup, textvariable=self.contactTitleVar, width=31, font=self.textboxFont)
        self.contactTitleEntry.grid(column=0,row=2,columnspan=3,sticky='w')
        self.contactTitleEntry.insert(0, "Title/rank")
        self.contactTitleEntry.configure(fg='Gray')
        self.contactTitleEntry.bind("<FocusIn>", self.clearTitle)
        self.contactTitleEntry.bind("<FocusOut>", self.resetTitlePlaceholder)

        # email
        self.contactEmailVar = Tkinter.StringVar()
        self.contactEmailVar = Tkinter.StringVar()
        self.contactEmailEntry = Tkinter.Entry(contactGroup, textvariable=self.contactEmailVar, width=31, font=self.textboxFont)
        self.contactEmailEntry.grid(column=0,row=3,columnspan=3,sticky='w')
        self.contactEmailEntry.insert(0, "name@domain.com")
        self.contactEmailEntry.configure(fg='Gray')
        self.contactEmailEntry.bind("<FocusIn>", self.clearEmail)
        self.contactEmailEntry.bind("<FocusOut>", self.resetEmailPlaceholder)

        # phone
        self.contactPhoneVar = Tkinter.StringVar()
        self.contactPhoneVar = Tkinter.StringVar()
        self.contactPhoneEntry = Tkinter.Entry(contactGroup, textvariable=self.contactPhoneVar, width=20, font=self.textboxFont)
        self.contactPhoneEntry.grid(column=0,columnspan=2,row=4,sticky='w')
        self.contactPhoneEntry.insert(0, "xxx-xxx-xxxx")
        self.contactPhoneEntry.configure(fg='Gray')
        self.contactPhoneEntry.bind("<FocusIn>", self.clearPhone)
        self.contactPhoneEntry.bind("<FocusOut>", self.resetPhonePlaceholder)

        # phone extension
        self.contactPhoneExtVar = Tkinter.StringVar()
        self.contactPhoneExtVar = Tkinter.StringVar()
        self.contactPhoneExtEntry = Tkinter.Entry(contactGroup, textvariable=self.contactPhoneExtVar, width=10, font=self.textboxFont)
        self.contactPhoneExtEntry.grid(column=2,row=4,sticky='w',padx=5)
        self.contactPhoneExtEntry.insert(0, "Extension")
        self.contactPhoneExtEntry.configure(fg='Gray')
        self.contactPhoneExtEntry.bind("<FocusIn>", self.clearPhoneExt)
        self.contactPhoneExtEntry.bind("<FocusOut>", self.resetPhoneExtPlaceholder)


        ## Camera Details ##
        # details frame
        detailsFrame = Tkinter.LabelFrame(self, bd=0)
        detailsFrame.grid(column=0,row=12,columnspan=2,padx=5)

        # Camera details multiline box and label
        cameraDetailsLabelVar = Tkinter.StringVar()
        cameraDetailsLabelVar.set("Camera surveillance details:")
        cameraDetailsLabel = Tkinter.Label(self, textvariable=cameraDetailsLabelVar, anchor='w',font=self.labelFont)
        cameraDetailsLabel.grid(column=0,row=11,sticky='w', pady=7)

        # external cameras
        self.numExternalVar = Tkinter.StringVar()
        self.numExternalEntry = Tkinter.Entry(detailsFrame, textvariable=self.numExternalVar, width=3,font=self.textboxFont)
        self.numExternalEntry.grid(column=0,row=1,sticky='w')
        self.numExternalEntry.insert(0, 0)
        self.numExternalEntry.configure(fg="Gray")
        self.numExternalEntry.bind("<FocusIn>", self.clearExternal)
        self.numExternalEntry.bind("<FocusOut>", self.resetExternalPlaceholder)
        
        externalLabelVar = Tkinter.StringVar()
        externalLabelVar.set("External cameras")
        externalLabel = Tkinter.Label(detailsFrame, textvariable=externalLabelVar, anchor='w', font=self.smallLabelFont)
        externalLabel.grid(column=0, row=1, sticky='w', padx=30)

        # internal cameras
        self.numInternalVar = Tkinter.StringVar()
        self.numInternalEntry = Tkinter.Entry(detailsFrame, textvariable=self.numInternalVar, width=3,font=self.textboxFont)
        self.numInternalEntry.grid(column=1,row=1,sticky='w')
        self.numInternalEntry.insert(0, 0)
        self.numInternalEntry.configure(fg="Gray")
        self.numInternalEntry.bind("<FocusIn>", self.clearInternal)
        self.numInternalEntry.bind("<FocusOut>", self.resetInternalPlaceholder)

        internalLabelVar = Tkinter.StringVar()
        internalLabelVar.set("Internal cameras")
        internalLabel = Tkinter.Label(detailsFrame, textvariable=internalLabelVar, anchor='w', font=self.smallLabelFont)
        internalLabel.grid(column=1, row=1, sticky='w', padx=30)

        # retention length
        choices = range(1,32)
        choices.insert(0," ")
        self.retentionVar = Tkinter.StringVar()
        self.retentionVar.set(" ")
        self.retentionOption = Tkinter.OptionMenu(detailsFrame, self.retentionVar, *choices)
        self.retentionOption.grid(column=0, row=2, stick='w')

        # camera details free text
        self.cameraDetailsText = Tkinter.Text(detailsFrame, height=4, width=48)
        self.cameraDetailsText.grid(column=0, row=3, sticky='w', columnspan=2)
        self.cameraDetailsText.insert(Tkinter.END, "Type description of surveillance area here...")
        self.cameraDetailsText.configure(fg="Gray", font=self.textboxFont, wrap=Tkinter.WORD)
        self.cameraDetailsText.bind("<FocusIn>", self.clearDetails)
        self.cameraDetailsText.bind("<FocusOut>", self.resetDetailsPlaceholder)
        self.cameraDetailsText.bind("<Tab>", self.focus_next_window)

        # date of video recovery setup (row 11-20)
            # label
        dateOfRecordingLabelVar = Tkinter.StringVar()
        dateOfRecordingLabelVar.set("Date of video recording: ")
        dateOfRecordingLabel = Tkinter.Label(self, textvariable=dateOfRecordingLabelVar, anchor='w', font=self.labelFont)
        dateOfRecordingLabel.grid(column=0, row=15, sticky='w', pady=7)

            # entry box
        self.dateOfRecordingVar = Tkinter.StringVar()
        self.dateOfRecordingEntry = Tkinter.Entry(self, textvariable=self.dateOfRecordingVar, width=11, font=self.textboxFont)
        self.dateOfRecordingEntry.grid(column=0, row=16, sticky='w', padx=5)
        self.dateOfRecordingEntry.insert(0, "mm/dd/yyyy")
        self.dateOfRecordingEntry.configure(fg="Gray")
        self.dateOfRecordingEntry.bind("<FocusIn>", self.clearDateOfRecording)
        self.dateOfRecordingEntry.bind("<FocusOut>", self.resetDateOfRecordingPlaceholder)


        ## Window size and other options ##
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2 - 210
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2 - 219
        self.grid_columnconfigure(0,weight=1)
        self.resizable(False,False)
        self.update()
        self.geometry("450x600+%d+%d" % (x,y))

    ## Textbox Methods ##
    # location name
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

    # street address
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
            
    # street line 2
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

    # date of recording
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

    # camera details text widget
    def clearDetails(self, event):
        if self.cameraDetailsText.cget('fg') == "Gray":
            self.cameraDetailsText.delete(1.0, Tkinter.END)
            self.cameraDetailsText.configure(fg="Black")

    def resetDetailsPlaceholder(self, event):
        details = self.cameraDetailsText.get(1.0, Tkinter.END)
        if len(details) == 1:
            self.cameraDetailsText.configure(fg="Gray")
            self.cameraDetailsText.insert(1.0, "Type description of surveillance area here...")

    def focus_next_window(self, event):
        event.widget.tk_focusNext().focus()
        return("break")

    # contact methods
    def clearFirstName(self, event):
        name = self.contactFirstNameEntry.get()
        if name == "First name":
            self.contactFirstNameEntry.delete(0, Tkinter.END)
            self.contactFirstNameEntry.configure(fg="Black")

    def resetFirstNamePlaceholder(self, event):
        name = self.contactFirstNameEntry.get()
        if len(name) == 0:
            self.contactFirstNameEntry.configure(fg="Gray")
            self.contactFirstNameEntry.insert(0, "First name")

    def clearLastName(self, event):
        name = self.contactLastNameEntry.get()
        if name == "Last name":
            self.contactLastNameEntry.delete(0, Tkinter.END)
            self.contactLastNameEntry.configure(fg="Black")

    def resetLastNamePlaceholder(self, event):
        name = self.contactLastNameEntry.get()
        if len(name) == 0:
            self.contactLastNameEntry.configure(fg="Gray")
            self.contactLastNameEntry.insert(0, "Last name")

    def clearTitle(self, event):
        title = self.contactTitleEntry.get()
        if title == "Title/rank":
            self.contactTitleEntry.delete(0, Tkinter.END)
            self.contactTitleEntry.configure(fg='Black')

    def resetTitlePlaceholder(self, event):
        title = self.contactTitleEntry.get()
        if len(title) == 0:
            self.contactTitleEntry.configure(fg="Gray")
            self.contactTitleEntry.insert(0, "Title/rank")

    def clearEmail(self, event):
        email = self.contactEmailEntry.get()
        if email == "name@domain.com":
            self.contactEmailEntry.delete(0, Tkinter.END)
            self.contactEmailEntry.configure(fg='Black')

    def resetEmailPlaceholder(self, event):
        email = self.contactEmailEntry.get()
        if len(email) == 0:
            self.contactEmailEntry.configure(fg="Gray")
            self.contactEmailEntry.insert(0, "name@domain.com")

    def clearPhone(self, event):
        phone = self.contactPhoneEntry.get()
        if phone == "xxx-xxx-xxxx":
            self.contactPhoneEntry.delete(0, Tkinter.END)
            self.contactPhoneEntry.configure(fg='Black')

    def resetPhonePlaceholder(self, event):
        phone = self.contactPhoneEntry.get()
        if len(phone) == 0:
            self.contactPhoneEntry.configure(fg="Gray")
            self.contactPhoneEntry.insert(0, "xxx-xxx-xxxx")

    def clearPhoneExt(self, event):
        phoneExt = self.contactPhoneExtEntry.get()
        if phoneExt == "Extension":
            self.contactPhoneExtEntry.delete(0, Tkinter.END)
            self.contactPhoneExtEntry.configure(fg='Black')

    def resetPhoneExtPlaceholder(self, event):
        phoneExt = self.contactPhoneExtEntry.get()
        if len(phoneExt) == 0:
            self.contactPhoneExtEntry.configure(fg="Gray")
            self.contactPhoneExtEntry.insert(0, "Extension")

    # internal, external
    def clearInternal(self,event):
        intr = self.numInternalEntry.get()
        if intr == "0":
            self.numInternalEntry.delete(0, Tkinter.END) 
            self.numInternalEntry.configure(fg="Black")

    def resetInternalPlaceholder(self,event):
        intr = self.numInternalEntry.get()
        if len(intr) == 0:
            self.numInternalEntry.configure(fg="Gray")
            self.numInternalEntry.insert(0, 0)

    def clearExternal(self,event):
        ext = self.numExternalEntry.get()
        if ext == "0":
            self.numExternalEntry.delete(0, Tkinter.END) 
            self.numExternalEntry.configure(fg="Black")
            
    def resetExternalPlaceholder(self,event):
        ext = self.numExternalEntry.get()
        if len(ext) == 0:
            self.numExternalEntry.configure(fg="Gray")
            self.numExternalEntry.insert(0, 0)

    # lat and long methods
