import time
from datetime import datetime
import os

ScopeStateFileName = '%sAcquisition/RunLog.txt' % "/home/sxie/ETL_Agilent_MSO-X-92004A/"
TimestampFilePath = "QutagTimestampFile.txt"
AutoPilotStatusFile = '%sAcquisition/ScopeStatus.txt' % "/home/sxie/ETL_Agilent_MSO-X-92004A/"
DAQTime = 10 #in seconds

while True:

	inFile = open(AutoPilotStatusFile,"r")
	runNumber = inFile.readline().strip()
	time.sleep(1)
	if (runNumber != str(0)):

			ScopeStateHandle = open(ScopeStateFileName, "r")
			ScopeState = str(ScopeStateHandle.read().strip())

			############### checking the status for the next runs #################  
			with open(AutoPilotStatusFile,'w') as file:
				file.write(str(0))
			
			print "\n ####################### Running the Qutag acquisition ##################################\n"

			Command = 'source /home/sxie/QUTAG-LX64-V1.1.6/userlib/QuTagDAQ/RunFQNETDAQ.sh %d %d' % (int(runNumber), DAQTime) 
			print Command

			StartTime = datetime.now()
			StartTimeSinceEpoch = float(time.time())
			#### Starting the acquisition script ####
			os.system(Command)
			StopTime = datetime.now()

			RunTimeSinceEpoch = float((StopTime - StartTime).total_seconds())/2 + StartTimeSinceEpoch 
			RunTimeHuman = str((StartTime - StopTime)/2 + StartTime)
			TimestampFileHandle = open(TimestampFilePath,"a+")
			TimestampFileHandle.write(str(runNumber) + "\t" + str(RunTimeSinceEpoch) + "\t" + str(RunTimeHuman) + "\n")
			TimestampFileHandle.close()

			print "Acquisition complete"
			print "\n ####################### Done with the Qutag acquisition ##################################\n"
