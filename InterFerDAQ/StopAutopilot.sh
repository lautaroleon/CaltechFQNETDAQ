echo "stop" > AutoPilot.status
echo "stop" > Qutag.status
echo "0" > /home/sxie/ETL_Agilent_MSO-X-92004A/Acquisition/ScopeStatus.txt
echo "0" > /home/mhussain/InterFerDAQ/LVControl.txt #Stop signal for LV Scan listener
echo "0" > /home/mhussain/InterFerDAQ/IncludeLowVoltageFile.txt #Decouples autopilot and LVListener
echo "0" > /home/mhussain/InterFerDAQ/QutagControl.txt #Stop signal for Qutag script
echo "0" > /home/mhussain/InterFerDAQ/IncludeQutagFile.txt #Decouples autopilot and Qutag script