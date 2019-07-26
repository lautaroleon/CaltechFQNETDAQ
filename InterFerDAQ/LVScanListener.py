from LVScanFunc import * 
from FileComm import *
from AllModules import *

print 'Please initiate the low voltage'
Resource = InitiateResource()

Voltage = InitialVoltage
SetTempBool = False

SetTemp = raw_input("Do you want to set the temperature and include temperature logging (y/n) ? ")
if SetTemp == "y" or SetTemp == "Y" :
    print 'Now initiate the temperature controller'
    TempCont = InitiateResource()
    SetTempBool = True
    SetTempFunc(TempCont, False)

IncludeLowVoltageScan(True) #Tells Autopilot to include low voltage scan

if LowVoltageBoolean():
    ScanNumber = GetNextNumber(ScanFilename)
    print "\n*********************** Starting scan %d ****************************" % ScanNumber

while Voltage <= FinalVoltage:
    print '\n*************************'
    print 'Waiting for the green signal from the autopilot\n'
    RunNumber = ReceiveLVGreenSignal()

    if RunNumber != 0:

        print 'Changing the Voltage to %f V' % Voltage
        SetVoltage(Resource, ChannelNumber, Voltage, VoltageSettleTime, False)
        
        if SetTempBool: 
            TempActual = ReadTempFunc(TempCont, Debug = False)
        else:
            TempActual = -999

        ##### Write scan data for this run
        WriteVoltageScanDataFile(ScanNumber, RunNumber, Voltage, TempActual)
        
        if InitialVoltage != FinalVoltage:
            Voltage = Voltage + VoltageStep

        if Voltage > FinalVoltage:
            
            StopAutopilot = raw_input("This is the last allowed voltage value. Do you want to stop the autopilot after this iteration (y/n) ? ")
            if StopAutopilot == "y" or StopAutopilot == "Y" : 
                os.system("source %s" % StopAutopilotFileName)
            else:
                print 'Now the autopilot will keep on taking data even after the scan completes, at Voltage %f V' % (Voltage - VoltageStep)
                IncludeLowVoltageScan(False) # Tells Autopilot to keep on running without including the LV scan program

        print 'The current run number is ', RunNumber
        print '*************************\n'
        SendAutopilotGreenSignal()

print "\n*********************** Scan %d complete ****************************" % ScanNumber

time.sleep(10)
DisableOutput = raw_input("Do you want to disable Low Voltage Output (y/n) ?")
if  DisableOutput == "y" or DisableOutput == "Y" :
    DisableLVOutput(Resource)
