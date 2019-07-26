from TCPComm import *  
from FileComm import *
from AllModules import *

#################################Parsing arguments######################################
parser = argparse.ArgumentParser(description='Information for running the AutoPilot program. /n /n General Instructions: Start OTSDAQ and Configure by hand.')
parser.add_argument('-rd', '--RunDuration', type=float,required=True)
Debug = False

args = parser.parse_args()
RunDuration = args.RunDuration

AutoPilotStatus = WriteStatusFile("AutoPilot.status", "START")

print "*********************************************************************"
print "######################## Starting AutoPilot #########################"
print "*********************************************************************"

while AutoPilotStatus:
	
	### Function to read run number and increment it in the file
	RunNumber = GetNextNumber(RunFilename)

	####### Incrementing the Intereferometer low voltage ########
	if LowVoltageBoolean(): 
		print 'Sending Low Voltage Supply a signal to increment the voltage'
		SendLVGreenSignal(RunNumber) 
		print 'Waiting for the Low Voltage Supply to complete the action'
		ReceiveAutopilotGreenSignalFromLV()

	StartTime = datetime.now()  
	print "\nRun %i starting at %s" % (RunNumber,StartTime)

	if not Debug: start_ots(RunNumber,False)

	time.sleep(RunDuration)

	if not Debug: stop_ots(False)

	StopTime = datetime.now()
	print "\nRun %i stopped at %s" % (RunNumber,StopTime)
	print "\n*********************************************************************"

	####### Saving Qutag file ########
	if QutagBoolean(): 
		print 'Appending Qutag scan file for current run data'
		SendQutagGreenSignal(RunNumber)
		ReceiveAutopilotGreenSignalFromQutag() 

	#################################################
	#Check for Stop signal in AutoPilot.status file
	#################################################
	AutoPilotStatus = ReadStatusFile("AutoPilot.status")


print "\n*********************************************************************"
print "######################## AutoPilot Stopped ##########################"
print "*********************************************************************"