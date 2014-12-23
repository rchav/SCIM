"""
******************************************************************************

SCIM: Interface Init

Robert Chavez
All rights reserved

******************************************************************************
"""

import Tkinter
import ttk
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
        self.smallerLabelFont = tkFont.Font(family="Constantia", size=10)
        self.statusFont = tkFont.Font(family="Constantia", size=10, weight='bold')

        ## Window size and other options ##
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2 - 300
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2 - 400
        self.grid_columnconfigure(0,weight=1)
        self.resizable(False,False)
        self.update()
        self.geometry("800x715+%d+%d" % (x,y))

        style = ttk.Style()
        style.map("TCombobox", 
            selectbackground=[
                ('!readonly', '!focus', 'SystemWindow'),
                ('readonly', '!focus', 'SystemButtonFace'),
            ],
        )

        # title bar on top of window
        titleVariable = Tkinter.StringVar()
        titleVariable.set(u"SCIM: Add a new camera")
        titleLabel = Tkinter.Label(self,textvariable=titleVariable, fg="white",bg="#0154a0",font="Constantia 16")
        titleLabel.grid(column=0,row=0,columnspan=3,sticky='EW')

        # status bar on bottom of window
        self.statusVariable = Tkinter.StringVar()
        self.statusVariable.set("Crime Strategies Unit")
        self.statusLabel = Tkinter.Label(self,textvariable=self.statusVariable, fg="White",bg="#0154a0",font=self.statusFont)
        self.statusLabel.grid(column=0,row=100,columnspan=3,sticky='EW')



        ## Location Name ##
        # location name entry box and label
        self.locationVariable = Tkinter.StringVar()
        self.locationEntry = Tkinter.Entry(self, textvariable = self.locationVariable, font=self.textboxFont, width=40)
        self.locationEntry.insert(0, "Enter location name")
        self.locationEntry.configure(fg="Gray")
        self.locationEntry.grid(column=0,row=2,columnspan=3)
        self.locationEntry.bind("<FocusIn>", self.clearLocationName)
        self.locationEntry.bind("<FocusOut>", self.resetLocationPlaceholder)

        locationLabelVar = Tkinter.StringVar()
        locationLabelVar.set("Location Name: ")
        locationLabel = Tkinter.Label(self, textvariable = locationLabelVar, anchor="w", font=self.labelFont)
        locationLabel.grid(column=0,row=1,columnspan=3, pady=7)

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
        self.addressStateVar = Tkinter.StringVar()

        # Address entry boxes init (row 3 - 10)
        self.addressStreetEntry = Tkinter.Entry(addressGroup, textvariable = self.addressStreetVar, font=self.textboxFont)
        self.addressStreetEntry.insert(0, "123 Street Name")
        self.addressStreetEntry.configure(fg="Gray")
        self.addressStreetEntry.grid(column=0,row=5,sticky='W', columnspan=2)
        self.addressStreetEntry.bind("<KeyPress>", self.clearAddressStreet)
        self.addressStreetEntry.bind("<FocusOut>", self.resetAddressStreetPlaceholder)

        # address 2nd line
        self.addressLine2Entry = Tkinter.Entry(addressGroup, textvariable = self.addressLine2Var, font=self.textboxFont)
        self.addressLine2Entry.grid(column=0,row=6,sticky='W', columnspan=2)
        self.addressLine2Entry.insert(0, "Apt, suite, etc.")
        self.addressLine2Entry.configure(fg="Gray")
        self.addressLine2Entry.bind("<KeyPress>", self.clearAddressLine2)
        self.addressLine2Entry.bind("<FocusOut>", self.resetAddressLine2Placeholder)

        # address city
        self.addressCityEntry = Tkinter.Entry(addressGroup, textvariable = self.addressCityVar, width=16, font=self.textboxFont)
        self.addressCityEntry.grid(column=0,row=7,sticky='W')
        self.addressCityEntry.insert(0, "City")
        self.addressCityEntry.configure(fg="Gray")
        self.addressCityEntry.bind("<KeyPress>", self.clearAddressCity)
        self.addressCityEntry.bind("<FocusOut>", self.resetAddressCityPlaceholder)
        
        # address state
        self.addressStateEntry = Tkinter.Entry(addressGroup, textvariable = self.addressStateVar, width=3, font=self.textboxFont)
        self.addressStateEntry.grid(column=1,row=7,sticky='W',padx=5)
        self.addressStateEntry.insert(0, "XX")
        self.addressStateEntry.configure(fg="Gray")
        self.addressStateEntry.bind("<KeyPress>", self.clearAddressState)
        self.addressStateEntry.bind("<FocusOut>", self.resetAddressStatePlaceholder)

        ## Coordinates ##
        # lat and long boxes (auto pop when address is completed)
        self.latitudeVar = Tkinter.StringVar()
        self.latitudeEntry = Tkinter.Entry(addressGroup, textvariable=self.latitudeVar, width=10, font=self.textboxFont)
        self.latitudeEntry.grid(column=2,row=5,sticky='w', padx=10)
        self.latitudeEntry.insert(0, 'Latitude')
        self.latitudeEntry.configure(fg="Gray", state='readonly')

        self.longitudeVar = Tkinter.StringVar()
        self.longitudeEntry = Tkinter.Entry(addressGroup, textvariable=self.longitudeVar, width=10, font=self.textboxFont)
        self.longitudeEntry.grid(column=2,row=6, sticky='w', padx=10)
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
        self.contactFirstNameEntry.bind("<KeyPress>", self.clearFirstName)
        self.contactFirstNameEntry.bind("<FocusOut>", self.resetFirstNamePlaceholder)

        # last name
        self.contactLastNameVar = Tkinter.StringVar()
        self.contactLastNameEntry =  Tkinter.Entry(contactGroup, textvariable=self.contactLastNameVar, width=15, font=self.textboxFont)
        self.contactLastNameEntry.grid(column=1,row=1,columnspan=2,sticky='w',padx=5)
        self.contactLastNameEntry.insert(0, "Last name")
        self.contactLastNameEntry.configure(fg="Gray")
        self.contactLastNameEntry.bind("<KeyPress>", self.clearLastName)
        self.contactLastNameEntry.bind("<FocusOut>", self.resetLastNamePlaceholder)

        # title
        self.contactTitleVar = Tkinter.StringVar()
        self.contactTitleEntry = Tkinter.Entry(contactGroup, textvariable=self.contactTitleVar, width=31, font=self.textboxFont)
        self.contactTitleEntry.grid(column=0,row=2,columnspan=3,sticky='w')
        self.contactTitleEntry.insert(0, "Title/rank")
        self.contactTitleEntry.configure(fg='Gray')
        self.contactTitleEntry.bind("<KeyPress>", self.clearTitle)
        self.contactTitleEntry.bind("<FocusOut>", self.resetTitlePlaceholder)

        # email
        self.contactEmailVar = Tkinter.StringVar()
        self.contactEmailVar = Tkinter.StringVar()
        self.contactEmailEntry = Tkinter.Entry(contactGroup, textvariable=self.contactEmailVar, width=31, font=self.textboxFont)
        self.contactEmailEntry.grid(column=0,row=3,columnspan=3,sticky='w')
        self.contactEmailEntry.insert(0, "name@domain.com")
        self.contactEmailEntry.configure(fg='Gray')
        self.contactEmailEntry.bind("<KeyPress>", self.clearEmail)
        self.contactEmailEntry.bind("<FocusOut>", self.resetEmailPlaceholder)

        # phone
        self.contactPhoneVar = Tkinter.StringVar()
        self.contactPhoneVar = Tkinter.StringVar()
        self.contactPhoneEntry = Tkinter.Entry(contactGroup, textvariable=self.contactPhoneVar, width=20, font=self.textboxFont)
        self.contactPhoneEntry.grid(column=0,columnspan=2,row=4,sticky='w')
        self.contactPhoneEntry.insert(0, "xxx-xxx-xxxx")
        self.contactPhoneEntry.configure(fg='Gray')
        self.contactPhoneEntry.bind("<KeyPress>", self.clearPhone)
        self.contactPhoneEntry.bind("<FocusOut>", self.resetPhonePlaceholder)

        # phone extension
        self.contactPhoneExtVar = Tkinter.StringVar()
        self.contactPhoneExtVar = Tkinter.StringVar()
        self.contactPhoneExtEntry = Tkinter.Entry(contactGroup, textvariable=self.contactPhoneExtVar, width=10, font=self.textboxFont)
        self.contactPhoneExtEntry.grid(column=2,row=4,sticky='w',padx=5)
        self.contactPhoneExtEntry.insert(0, "Extension")
        self.contactPhoneExtEntry.configure(fg='Gray')
        self.contactPhoneExtEntry.bind("<KeyPress>", self.clearPhoneExt)
        self.contactPhoneExtEntry.bind("<FocusOut>", self.resetPhoneExtPlaceholder)


        ## Camera Details ##
        # details frame
        detailsFrame = Tkinter.LabelFrame(self, bd=0)
        detailsFrame.grid(column=0,row=12,padx=5,sticky='w')

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
        self.numExternalEntry.bind("<KeyPress>", self.clearExternal)
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
        self.numInternalEntry.bind("<KeyPress>", self.clearInternal)
        self.numInternalEntry.bind("<FocusOut>", self.resetInternalPlaceholder)

        internalLabelVar = Tkinter.StringVar()
        internalLabelVar.set("Internal cameras")
        internalLabel = Tkinter.Label(detailsFrame, textvariable=internalLabelVar, anchor='w', font=self.smallLabelFont)
        internalLabel.grid(column=1, row=1, sticky='w', padx=30)

        # camera details free text
        self.cameraDetailsText = Tkinter.Text(detailsFrame, height=4, width=41)
        self.cameraDetailsText.grid(column=0, row=3, sticky='w', columnspan=2)
        self.cameraDetailsText.insert(Tkinter.END, "Type description of surveillance area here...")
        self.cameraDetailsText.configure(fg="Gray", font=self.textboxFont, wrap=Tkinter.WORD)
        self.cameraDetailsText.bind("<KeyPress>", self.clearDetails)
        self.cameraDetailsText.bind("<FocusOut>", self.resetDetailsPlaceholder)
        self.cameraDetailsText.bind("<Tab>", self.focus_next_window)


        ## DVR Information ##
        DVRLabelVar = Tkinter.StringVar()
        DVRLabelVar.set("DVR Information:")
        DVRLabel = Tkinter.Label(self, textvariable=DVRLabelVar, anchor='w', font=self.labelFont)
        DVRLabel.grid(column=0, row=13, sticky='w',pady=7)       

        DVRFrame = Tkinter.LabelFrame(self, bd=0)
        DVRFrame.grid(column=0, row=14,padx=5, sticky='w')

        # retention length
        retentionLengthLabelVar = Tkinter.StringVar()
        retentionLengthLabelVar.set("Retention length:")
        retentionLengthLabel = Tkinter.Label(DVRFrame, textvariable=retentionLengthLabelVar, anchor='w', font=self.smallLabelFont)
        retentionLengthLabel.grid(column=0, row=1, sticky='nsw',pady=7)

        choices = range(1,32)
        self.retentionValueVar = Tkinter.StringVar()
        self.retentionValueVar.set("#")
        self.retentionValue = ttk.Combobox(DVRFrame, textvariable=self.retentionValueVar, state='readonly', width=4)
        self.retentionValue['values'] = choices
        self.retentionValue.grid(column=1, row=1, sticky='w',padx=5)
        
        units = ['Days', 'Months', 'Years']
        self.retentionUnitsVar = Tkinter.StringVar()
        self.retentionUnitsVar.set("Units")
        self.retentionUnits = ttk.Combobox(DVRFrame, textvariable=self.retentionUnitsVar, state='readonly', width=8)
        self.retentionUnits['values'] = units
        self.retentionUnits.grid(column=2, row=1, sticky='w',padx=5)

        Acc = ['Approximately', 'Exactly']
        self.retentionAccVar = Tkinter.StringVar()
        self.retentionAccVar.set("Accuracy")
        self.retentionAcc = ttk.Combobox(DVRFrame, textvariable=self.retentionAccVar, state='readonly', width=13)
        self.retentionAcc['values'] = Acc
        self.retentionAcc.grid(column=3, row=1, sticky='w',padx=5)

        style.configure('Combobox', background='white', fieldbackground='white')

        # DVR make
        makeLabelVar = Tkinter.StringVar()
        makeLabelVar.set("DVR make:")
        makeLabel = Tkinter.Label(DVRFrame, textvariable=makeLabelVar, anchor='w', font=self.smallLabelFont)
        makeLabel.grid(column=0, row=2, sticky='nsw',pady=7)
        
        self.makeVar = Tkinter.StringVar()
        self.makeEntry = Tkinter.Entry(DVRFrame, textvariable=self.makeVar, width=27, font=self.textboxFont)
        self.makeEntry.grid(column=1, row=2, columnspan=3, sticky='w', padx=5)
        
        # DVR model
        modelLabelVar = Tkinter.StringVar()
        modelLabelVar.set("DVR model:")
        modelLabel = Tkinter.Label(DVRFrame, textvariable=modelLabelVar, anchor='w', font=self.smallLabelFont)
        modelLabel.grid(column=0, row=3, sticky='nsw',pady=7)
        
        self.modelVar = Tkinter.StringVar()
        self.modelEntry = Tkinter.Entry(DVRFrame, textvariable=self.modelVar, width=27, font=self.textboxFont)
        self.modelEntry.grid(column=1, row=3, columnspan=3, sticky='w', padx=5)


        timeFrame = Tkinter.LabelFrame(DVRFrame,bd=0)
        timeFrame.grid(column=1,row=4, rowspan=2, columnspan=3, sticky='s')

        # Time adjustment
        timeAdjLabelVar = Tkinter.StringVar()
        timeAdjLabelVar.set("Time adjustment:")
        timeAdjLabel = Tkinter.Label(DVRFrame, textvariable=timeAdjLabelVar, anchor='w', font=self.smallLabelFont)
        timeAdjLabel.grid(column=0, row=4, sticky='nw',pady=7)

        timeAdjLabelVar2 = Tkinter.StringVar() 
        timeAdjLabelVar2.set("     Years              Months              Days")
        timeAdjLabel2 = Tkinter.Label(timeFrame, textvariable=timeAdjLabelVar2, anchor='w', font=self.smallerLabelFont)
        timeAdjLabel2.grid(column=1, row=5, columnspan=3,padx=5, sticky='nw')

        years = range(0,51)
        self.timeAdjYearVar = Tkinter.StringVar()
        self.timeAdjYearVar.set(0)
        self.timeAdjYearCB = ttk.Combobox(timeFrame, textvariable=self.timeAdjYearVar, state='readonly', width=4)
        self.timeAdjYearCB['values'] = years
        self.timeAdjYearCB.grid(column=1, row=4,padx=15)
        
        months = range(0,12)
        self.timeAdjMonthVar = Tkinter.StringVar()
        self.timeAdjMonthVar.set(0)
        self.timeAdjMonthCB = ttk.Combobox(timeFrame, textvariable=self.timeAdjMonthVar, state='readonly', width=4)
        self.timeAdjMonthCB['values'] = months
        self.timeAdjMonthCB.grid(column=2, row=4,padx=15)

        days = range(0,31)
        self.timeAdjDaysVar = Tkinter.StringVar()
        self.timeAdjDaysVar.set(0)
        self.timeAdjDaysCB = ttk.Combobox(timeFrame, textvariable=self.timeAdjDaysVar, state='readonly', width=4)
        self.timeAdjDaysCB['values'] = days
        self.timeAdjDaysCB.grid(column=3, row=4, padx=15)

        ## Recording Details ##
        # label
        recordingLabelVar = Tkinter.StringVar()
        recordingLabelVar.set("Recording Details:")
        recordingLabel = Tkinter.Label(self, textvariable=recordingLabelVar, width=34, anchor='w', font=self.labelFont)
        recordingLabel.grid(column=2, row=3, sticky='w', pady=7)

        # Recording frame
        recordingFrame = Tkinter.LabelFrame(self, bd=0)
        recordingFrame.grid(column=2, row=4, rowspan=2, sticky='nw', padx=5)

        # start date label
        startDateLabelVar = Tkinter.StringVar()
        startDateLabelVar.set("Start date:")
        startDateLabel = Tkinter.Label(recordingFrame, textvariable=startDateLabelVar, anchor='w', font=self.smallLabelFont)
        startDateLabel.grid(column=0, row=1, sticky='nsw',pady=7)

        # start date of video recording entry box
        self.startDateOfRecordingVar = Tkinter.StringVar()
        self.startDateOfRecordingEntry = Tkinter.Entry(recordingFrame, textvariable=self.startDateOfRecordingVar, width=11, font=self.textboxFont)
        self.startDateOfRecordingEntry.grid(column=1, row=1, sticky='w')
        self.startDateOfRecordingEntry.insert(0, "mm/dd/yyyy")
        self.startDateOfRecordingEntry.configure(fg="Gray")
        self.startDateOfRecordingEntry.bind("<FocusIn>", self.clearStartDateOfRecording)
        self.startDateOfRecordingEntry.bind("<FocusOut>", self.resetStartDateOfRecordingPlaceholder)
        
        # end date label
        endDateLabelVar = Tkinter.StringVar()
        endDateLabelVar.set("End date:")
        endDateLabel = Tkinter.Label(recordingFrame, textvariable=endDateLabelVar, anchor='w', font=self.smallLabelFont)
        endDateLabel.grid(column=2, row=1, sticky='nsw',pady=7)

        # end date of video recording entry box
        self.endDateOfRecordingVar = Tkinter.StringVar()
        self.endDateOfRecordingEntry = Tkinter.Entry(recordingFrame, textvariable=self.endDateOfRecordingVar, width=11, font=self.textboxFont)
        self.endDateOfRecordingEntry.grid(column=3, row=1, sticky='w')
        self.endDateOfRecordingEntry.insert(0, "mm/dd/yyyy")
        self.endDateOfRecordingEntry.configure(fg="Gray")
        self.endDateOfRecordingEntry.bind("<FocusIn>", self.clearEndDateOfRecording)
        self.endDateOfRecordingEntry.bind("<FocusOut>", self.resetEndDateOfRecordingPlaceholder)

        # start time of video label
        startTimeLabelVar = Tkinter.StringVar()
        startTimeLabelVar.set("Start time:")
        startTimeLabel = Tkinter.Label(recordingFrame, textvariable=startTimeLabelVar, anchor='w', font=self.smallLabelFont)
        startTimeLabel.grid(column=0, row=2, sticky='nsw',pady=7)
        
        # start time of video recording entry box
        self.startTimeOfRecordingVar = Tkinter.StringVar()
        self.startTimeOfRecordingEntry = Tkinter.Entry(recordingFrame, textvariable=self.startTimeOfRecordingVar, width=11, font=self.textboxFont)
        self.startTimeOfRecordingEntry.grid(column=1, row=2, sticky='w')
        self.startTimeOfRecordingEntry.insert(0, "hh:mm:ss")
        self.startTimeOfRecordingEntry.configure(fg="Gray")
        self.startTimeOfRecordingEntry.bind("<FocusIn>", self.clearStartTimeOfRecording)
        self.startTimeOfRecordingEntry.bind("<FocusOut>", self.resetStartTimeOfRecordingPlaceholder)

        # end time of video label
        endTimeLabelVar = Tkinter.StringVar()
        endTimeLabelVar.set("End time:")
        endTimeLabel = Tkinter.Label(recordingFrame, textvariable=endTimeLabelVar, anchor='w', font=self.smallLabelFont)
        endTimeLabel.grid(column=2, row=2, sticky='nsw',pady=7)

        # end time of video recording entry box
        self.endTimeOfRecordingVar = Tkinter.StringVar()
        self.endTimeOfRecordingEntry = Tkinter.Entry(recordingFrame, textvariable=self.endTimeOfRecordingVar, width=11, font=self.textboxFont)
        self.endTimeOfRecordingEntry.grid(column=3, row=2, sticky='w')
        self.endTimeOfRecordingEntry.insert(0, "hh:mm:ss")
        self.endTimeOfRecordingEntry.configure(fg="Gray")
        self.endTimeOfRecordingEntry.bind("<FocusIn>", self.clearEndTimeOfRecording)
        self.endTimeOfRecordingEntry.bind("<FocusOut>", self.resetEndTimeOfRecordingPlaceholder)

        # recovery date label
        recoveryDateLabelVar = Tkinter.StringVar()
        recoveryDateLabelVar.set("Recovery date:")
        recoveryDateLabel = Tkinter.Label(recordingFrame, textvariable=recoveryDateLabelVar, anchor='w', font=self.smallLabelFont)
        recoveryDateLabel.grid(column=0, row=3, columnspan=2, sticky='nsw',pady=7)

        # recovery date entry
        self.recoveryDateVar = Tkinter.StringVar()
        self.recoveryDateEntry = Tkinter.Entry(recordingFrame, textvariable=self.recoveryDateVar, width=11, font=self.textboxFont)
        self.recoveryDateEntry.grid(column=1, row=3, columnspan=2, sticky='w', padx=28)
        self.recoveryDateEntry.insert(0, "mm/dd/yyyy")
        self.recoveryDateEntry.configure(fg="Gray")
        self.recoveryDateEntry.bind("<FocusIn>", self.clearRecoveryDate)
        self.recoveryDateEntry.bind("<FocusOut>", self.resetRecoveryDatePlaceholder)

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
    
    # city
    def clearAddressCity(self, event):
        city = self.addressCityEntry.get()
        if city == "City":
            self.addressCityEntry.delete(0, Tkinter.END)
            self.addressCityEntry.configure(fg="Black")

    def resetAddressCityPlaceholder(self, event):
        city = self.addressCityEntry.get()
        if len(city) == 0:
            self.addressCityEntry.configure(fg="Gray")
            self.addressCityEntry.insert(0, "City")

    # state
    def clearAddressState(self, event):
        state = self.addressStateEntry.get()
        if state == "XX":
            self.addressStateEntry.delete(0, Tkinter.END)
            self.addressStateEntry.configure(fg="Black")

    def resetAddressStatePlaceholder(self, event):
        state = self.addressStateEntry.get()
        if len(state) == 0:
            self.addressStateEntry.configure(fg="Gray")
            self.addressStateEntry.insert(0, "XX")

    # date of recording
    def clearStartDateOfRecording(self, event):
        date = self.startDateOfRecordingEntry.get()
        if date == "mm/dd/yyyy":
            self.startDateOfRecordingEntry.delete(0, Tkinter.END)
            self.startDateOfRecordingEntry.configure(fg="Black")
    
    def resetStartDateOfRecordingPlaceholder(self, event):
        date = self.startDateOfRecordingEntry.get()
        if len(date) == 0:
            self.startDateOfRecordingEntry.configure(fg="Gray")
            self.startDateOfRecordingEntry.insert(0, "mm/dd/yyyy")

    def clearEndDateOfRecording(self, event):
        date = self.endDateOfRecordingEntry.get()
        if date == "mm/dd/yyyy":
            self.endDateOfRecordingEntry.delete(0, Tkinter.END)
            self.endDateOfRecordingEntry.configure(fg="Black")
    
    def resetEndDateOfRecordingPlaceholder(self, event):
        date = self.endDateOfRecordingEntry.get()
        if len(date) == 0:
            self.endDateOfRecordingEntry.configure(fg="Gray")
            self.endDateOfRecordingEntry.insert(0, "mm/dd/yyyy")

    # time of recording
    def clearStartTimeOfRecording(self, event):
        time = self.startTimeOfRecordingEntry.get()
        if time == "hh:mm:ss":
            self.startTimeOfRecordingEntry.delete(0, Tkinter.END)
            self.startTimeOfRecordingEntry.configure(fg="Black")
    
    def resetStartTimeOfRecordingPlaceholder(self, event):
        time = self.startTimeOfRecordingEntry.get()
        if len(time) == 0:
            self.startTimeOfRecordingEntry.configure(fg="Gray")
            self.startTimeOfRecordingEntry.insert(0, "hh:mm:ss")

    def clearEndTimeOfRecording(self, event):
        time = self.endTimeOfRecordingEntry.get()
        if time == "hh:mm:ss":
            self.endTimeOfRecordingEntry.delete(0, Tkinter.END)
            self.endTimeOfRecordingEntry.configure(fg="Black")
    
    def resetEndTimeOfRecordingPlaceholder(self, event):
        time = self.endTimeOfRecordingEntry.get()
        if len(time) == 0:
            self.endTimeOfRecordingEntry.configure(fg="Gray")
            self.endTimeOfRecordingEntry.insert(0, "hh:mm:ss")
    
    # date of recording
    def clearRecoveryDate(self, event):
        date = self.recoveryDateEntry.get()
        if date == "mm/dd/yyyy":
            self.recoveryDateEntry.delete(0, Tkinter.END)
            self.recoveryDateEntry.configure(fg="Black")
    
    def resetRecoveryDatePlaceholder(self, event):
        date = self.recoveryDateEntry.get()
        if len(date) == 0:
            self.recoveryDateEntry.configure(fg="Gray")
            self.recoveryDateEntry.insert(0, "mm/dd/yyyy")


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
