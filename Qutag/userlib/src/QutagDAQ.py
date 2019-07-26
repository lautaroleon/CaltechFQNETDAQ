#*****************************************************************************
#
#  Project:        quTAG User Library
#
#  Filename:       example.cs
#
#  Purpose:        Minimal example for Python
#
#  Author:         N-Hands GmbH & Co KG
#
#*****************************************************************************
# $Id: example0.py,v 1.2 2019/04/02 19:31:55 trurl Exp $
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/QUTAG-LX64-V1.1.6

import ctypes
import os
import time
import platform
import numpy as np

# API --------------------------------------------------------------    

class QuTAG:
            
    def __init__(self):

        # load Lib -------------------------------------------
        if (platform.system()=="Windows"):
            self.tdclib = ctypes.windll.LoadLibrary('tdcbase.dll')
            self.usblib = ctypes.windll.LoadLibrary('FTD3XX.dll')
        if (platform.system()=="Linux"):
            self.tdclib = ctypes.cdll.LoadLibrary('/home/sxie/QUTAG-LX64-V1.1.6/userlib/lib/libtdcbase.so') ## way to load a linux dll into an object

        # ------- tdcbase.h --------------------------------------------------------
        self.tdclib.TDC_getVersion.argtypes = None
        self.tdclib.TDC_getVersion.restype = ctypes.c_double
        self.tdclib.TDC_perror.argtypes = [ctypes.c_int32]
        self.tdclib.TDC_perror.restype = ctypes.c_char_p
        self.tdclib.TDC_init.argtypes = [ctypes.c_int32]
        self.tdclib.TDC_init.restype = ctypes.c_int32
        self.tdclib.TDC_deInit.argtypes = None
        self.tdclib.TDC_deInit.restype = ctypes.c_int32
        self.tdclib.TDC_setCoincidenceWindow.argtypes = [ctypes.c_int32]
        self.tdclib.TDC_setCoincidenceWindow.restype = ctypes.c_int32
        self.tdclib.TDC_setExposureTime.argtypes = [ctypes.c_int32]
        self.tdclib.TDC_setExposureTime.restype = ctypes.c_int32
        self.tdclib.TDC_getCoincCounters.argtypes = [ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_int32)]
        self.tdclib.TDC_getCoincCounters.restype = ctypes.c_int32
        self.tdclib.TDC_getLastTimestamps.argtypes = [ctypes.c_int32, ctypes.POINTER(ctypes.c_int64), ctypes.POINTER(ctypes.c_int8), ctypes.POINTER(ctypes.c_int32)]
        self.tdclib.TDC_getLastTimestamps.restype = ctypes.c_int32

    # Error Check --------------------------------------------------------------
    def perror(self,environ,returnCode):
        if (returnCode != 0):
            msg = self.tdclib.TDC_perror(returnCode)
            print("Error in ", environ, ": ", msg)

# Example --------------------------------------------------------------    

print("QuTAG Python Demo")
qutag = QuTAG()
rc = qutag.tdclib.TDC_init(-1)  # accept any device
qutag.perror("TDC_init", rc)

if (rc == 0):
    print("Initialized with QuTAG DLL v%f"%(qutag.tdclib.TDC_getVersion()))

    rc = qutag.tdclib.TDC_setCoincidenceWindow(20000)  # 20ns coincidence window
    qutag.perror("TDC_setCoincidenceWindow", rc)
    rc = qutag.tdclib.TDC_setExposureTime(100)
    qutag.perror("TDC_setExposureTime", rc)

    for i in range(1):
        time.sleep(0.09)
        data = np.zeros(int(31),dtype=np.int32)
        updates = ctypes.c_int32()

        tsvalid = ctypes.c_int32()
        TimestampData = np.zeros(int(100000),dtype=np.int64)
        ChannelData = np.zeros(int(100000),dtype=np.int32)
        rc = qutag.tdclib.TDC_getLastTimestamps[1, TimestampData.ctypes.data_as(ctypes.POINTER(ctypes.c_int64)), ChannelData.ctypes.data_as(ctypes.POINTER(ctypes.c_int8)), ctypes.byref(tsvalid)]
        qutag.perror("TDC_getLastTimestamps", rc)
        print TimestampData
        print ChannelData
        print tsvalid

        
        #rc = qutag.tdclib.TDC_getCoincCounters(data.ctypes.data_as(ctypes.POINTER(ctypes.c_int32)),ctypes.byref(updates))
        #if (updates.value > 1 and i > 0):
        #    print("Missed ", updates.value-1, "updates")
        #if (updates.value > 0):
        #    print("1:", data[1], " 2:", data[2], " 3:", data[3], "   1-2:", data[5], " 1-3:", data[6], " 1-2-3:", data[15])
	
    # deinitialize device
    rc = qutag.tdclib.TDC_deInit()
    qutag.perror("TDC_deInit", rc)
