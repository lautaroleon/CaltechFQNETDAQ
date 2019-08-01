#!/usr/bin/python

 

#This code will open socket port 5025 and send *IDN to instrument.

import time
import socket
import math
import mysql.connector

db = mysql.connector.connect(host="localhost",  # this PC       
		     user="root",         # this user only has access to CPTLAB database
                     passwd="Teleport1536!",  # your password
		     auth_plugin='mysql_native_password',
		     database="teleportcommission") # name of the data base


input_buffer = 4096 #Temp buffer for rec data.
exRat = 0
 

pna = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

pna.connect(("192.168.0.136", 5025))
#pna.connect(("192.168.0.177", 5025))

 

 

pna.send("*idn?" + "\n")

id = pna.recv(input_buffer)

print id
cur = db.cursor()

cur.execute("SHOW TABLES")

for x in cur:
  print(x) 

i=1
while 1:
	pna.send("meas:vmax? func1" + "\n") 
	vmax0 = pna.recv(input_buffer)
	print vmax0
	pna.send("meas:vmax? func2" + "\n") 
	vmax1 = pna.recv(input_buffer)
	print vmax1
	
	pna.send("meas:vmax? func3" + "\n") 
	vmax2 = pna.recv(input_buffer)
	print vmax2
	

	query = "INSERT INTO interf(Vmax0, Vmax1, Vmax2, datetime) values("+str(vmax0)+ ","+ str(vmax1)+ ","+ str(vmax2)+", NOW());"
	#query = "INSERT INTO teleportcommission (Vmax0, Vmax1,) values("+str(vmax0)+ ","+ str(vmax1)+ ", NOW());"
	cur.execute(query)
	db.commit()
	print(cur.rowcount, "record inserted.")

	i +=1
	time.sleep(1)



pna.close()
