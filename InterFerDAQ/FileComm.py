from AllModules import *

########## Autopilot function

def WriteStatusFile(FileName, Message):
	if os.path.exists(FileName):
		os.remove(FileName)
	statusFile = open(FileName,"w") 
	statusFile.write(Message) 
	statusFile.close() 
	if Message == "START":
		Status = True
	else:
		Status = False
	return Status

def ReadStatusFile(FileName):
	tmpStatus = True
	tmpStatusFile = open(FileName,"r") 
	tmpString = (tmpStatusFile.read().split())[0]
	if (tmpString == "STOP" or tmpString == "stop"):
		print "Detected stop signal.\nStopping the script ...\n\n"
		tmpStatus = False
	tmpStatusFile.close()
	return tmpStatus

def GetNextNumber(RunOrScanFileName):
    FileHandle = open(RunOrScanFileName)
    nextNumber = int(FileHandle.read().strip())
    FileHandle.close()
    FileHandle = open(RunOrScanFileName,"w")
    FileHandle.write(str(nextNumber+1)+"\n") 
    FileHandle.close()
    return nextNumber



########## LV functions

def ReceiveLVGreenSignal():
    while True:
        LowVoltageControlFileHandle = open(LowVoltageControlFileName, "r")
        GreenSignalState = str(LowVoltageControlFileHandle.read().strip())
        if GreenSignalState != "0": break
        time.sleep(0.5)
    LowVoltageControlFileHandle.close()
    return int(GreenSignalState)

def SendLVGreenSignal(RunNumber):
    LowVoltageControlFileHandle = open(LowVoltageControlFileName, "w")
    LowVoltageControlFileHandle.write(str(RunNumber))
    LowVoltageControlFileHandle.close()
    return

def IncludeLowVoltageScan(IncludeBool):
    # Function to tell autopilot when to include Low voltage scan 
    IncludeLowVoltageHandle = open(IncludeLowVoltageFileName, "w")
    if IncludeBool:
        IncludeLowVoltageHandle.write("1")
    else:
        IncludeLowVoltageHandle.write("0")
    IncludeLowVoltageHandle.close()
    return

def LowVoltageBoolean():
    # Function that autopilot uses to find when to include LV Scan
    IncludeLowVoltageHandle = open(IncludeLowVoltageFileName, "r")
    LowVoltageBoolean = str(IncludeLowVoltageHandle.read().strip())
    if LowVoltageBoolean == "1":
        LVBool = True
    else:
        LVBool = False
    IncludeLowVoltageHandle.close()
    return LVBool

def WriteVoltageScanDataFile(ScanNumber, RunNumber, Voltage, TempActual):
    ScanDataFileHandle = open(VoltageScanDataFileName + 'scan' + str(ScanNumber) + '.txt' ,"a+")
    ScanDataFileHandle.write(str(RunNumber) + "\t" + str(Voltage) + "\t" + str(TempActual) + "\n")
    ScanDataFileHandle.close()

def ReceiveAutopilotGreenSignalFromLV():
    while True:
        LowVoltageControlFileHandle = open(LowVoltageControlFileName, "r")
        GreenSignalState = str(LowVoltageControlFileHandle.read().strip())
        if GreenSignalState == "0": break
        time.sleep(0.5)
    LowVoltageControlFileHandle.close()
    return

def SendAutopilotGreenSignalFromLV():
    LowVoltageControlFileHandle = open(LowVoltageControlFileName, "w")
    LowVoltageControlFileHandle.write("0")
    LowVoltageControlFileHandle.close()




######### Qutag Functions

def SendQutagGreenSignal(RunNumber):
    QutagControlFileHandle = open(QutagControlFileName, "w")
    QutagControlFileHandle.write(str(RunNumber))
    QutagControlFileHandle.close()
    return

def ReceiveQutagGreenSignal():
    while True:
        QutagControlFileHandle = open(QutagControlFileName, "r")
        GreenSignalState = str(QutagControlFileHandle.read().strip())
        if GreenSignalState != "0": break
        time.sleep(0.5)
    QutagControlFileHandle.close()
    return int(GreenSignalState)

def ReceiveAutopilotGreenSignalFromQutag():
    while True:
        QutagControlFileHandle = open(QutagControlFileName, "r")
        GreenSignalState = str(QutagControlFileHandle.read().strip())
        if GreenSignalState == "0": break
        time.sleep(0.5)
    QutagControlFileHandle.close()
    return

def SendAutopilotGreenSignalFromQutag():
    QutagControlFileHandle = open(QutagControlFileName, "w")
    QutagControlFileHandle.write("0")
    QutagControlFileHandle.close()

def QutagBoolean():
    # Function that autopilot uses to find when to include Qutag Scan
    IncludeQutagHandle = open(IncludeQutagFileName, "r")
    QutagBoolean = str(IncludeQutagHandle.read().strip())
    if QutagBoolean == "1":
        QutagBool = True
    else:
        QutagBool = False
    IncludeQutagHandle.close()
    return QutagBool

def IncludeQutagScan(IncludeBool):
    # Function to tell autopilot when to include Qutag scan 
    IncludeQutagHandle = open(IncludeQutagFileName, "w")
    if IncludeBool:
        IncludeQutagHandle.write("1")
    else:
        IncludeQutagHandle.write("0")
    IncludeQutagHandle.close()
    return

def WriteQutagScanDataFile(ScanNumber, RunNumber):
    ScanDataFileHandle = open(QutagScanDataFileName + 'scan' + str(ScanNumber) + '.txt' ,"a+")
    ScanDataFileHandle.write(str(RunNumber) + "\n")
    ScanDataFileHandle.close()
