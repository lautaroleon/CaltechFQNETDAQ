from FileComm import *
from AllModules import *

IncludeQutagScan(True) #Tells Autopilot to include Qutag scan

if QutagBoolean():
    ScanNumber = GetNextNumber(ScanFilename)
    print "\n*********************** Starting scan %d ****************************" % ScanNumber
    QutagStatus = WriteStatusFile("Qutag.status", "START")

while QutagStatus:
    print '\n*************************'
    print 'Waiting for the green signal from the autopilot\n'
    RunNumber = ReceiveQutagGreenSignal()

    if RunNumber != 0:

        ##### Write scan data for this run
        WriteQutagScanDataFile(ScanNumber, RunNumber)
        
        print 'The current run number is ', RunNumber
        print '*************************\n'

    SendAutopilotGreenSignalFromQutag()
    #################################################
    #Check for Stop signal in Qutag.status file
    #################################################
    QutagStatus = ReadStatusFile("Qutag.status")

print "\n*********************** Scan %d complete ****************************" % ScanNumber

IncludeQutagScan(False) # Tells Autopilot to keep on running without including the LV scan program

