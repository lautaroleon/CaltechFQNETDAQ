from AllModules import *

def InitiateResource():
    VISAInstance=visa.ResourceManager('@py')
    ResourceList=VISAInstance.list_resources()
    for index in range(len(ResourceList)):
        print("Device number " + str(index) + " - " + ResourceList[index])
    DeviceNumber = raw_input("Which device would you like to use?")
    Resource = VISAInstance.open_resource(ResourceList[int(DeviceNumber)])
#    if int(DeviceNumber) == 2:
#        print 'Temperature contoller'
#        Resource.baud_rate = 115200
#        Resource.data_bits = 8
#        Resource.stop_bits = visa.constants.StopBits.one
#        Resource.parity = visa.constants.Parity.none
#        Resource.read_termination = '\r'
#        Resource.write_termination = '\r'
    return Resource

def SetVoltage(Resource, ChannelNumber, ChVoltage, VoltageSettleTime = 120, Debug = False):
    #print(Resource.query("*idn?"))

    Resource.write("outp on")
    if ChannelNumber == 1:
        cmd1 = "inst first"
    elif ChannelNumber == 2:
        cmd1 = "inst second"
    elif ChannelNumber == 3:
        cmd1 = "inst third"

    Resource.write(cmd1)
    cmd2 = "volt " + str(ChVoltage) + "V"

    if ChVoltage <= 2 and ChVoltage >= 0:
        Resource.write(cmd2)
        if not Debug:
            print 'Sleeping for %ds, for voltage to take effect' % VoltageSettleTime
            time.sleep(VoltageSettleTime)
#           print 'Now returning the program flow to Autopilot'
    else:
        print '[WARNING] : The voltage is out of the bounds [0-2V], not changing the low voltage supply output'

def SetTempFunc(Resource, Debug = False):
    #print(Resource.query("*idn?"))

    Resource.write("tact?")
    Resource.read()
    TActualread = float(Resource.read().strip(" C")) 

    if SetTemp > TActualread:

        Resource.write("tset=%f" % SetTemp)
        Resource.read()

        Resource.write("tset?")
        Resource.read()
        TempAfterSetting = float(Resource.read().strip(" Celsius")) 

        if SetTemp == TempAfterSetting:
            print 'The set temperature has been changed'
    else:
        print '[WARNING] : The set temperature is less than the actual temperature'

def ReadTempFunc(Resource, Debug = False):
    #print(Resource.query("*idn?"))

    Resource.write("tact?")
    Resource.read()
    TActualread = float(Resource.read().strip(" C")) 
    print 'The actual temperature is %f C' % TActualread
    return TActualread

def DisableLVOutput(Resource):
    Resource.write("outp off")
