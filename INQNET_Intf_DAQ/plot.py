#!/usr/bin/python2.7

import numpy as np
import matplotlib.pyplot as plt

import datetime
import math
import mysql.connector
import os

def string_to_date(time):
    return time[2:4]+time[5:7]+time[8:10]+time[11:13]+time[14:16]+time[17:19]
#parameters
START_TIME = '2019-08-01 11:44:00'
END_TIME = '2019-08-01 13:24:00'
TABLE_NAME = 'interf'


#connect to database
  
db = mysql.connector.connect(host="localhost",  # this PC      
		     user="root",        
                     passwd="Teleport1536!",  # your password
                     db="teleportcommission")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need

Vmax0,Vmax1,Vmax2 = [],[],[]
time_u = []

cur = db.cursor()


query = "SELECT * FROM "+TABLE_NAME+" WHERE datetime BETWEEN {ts %s} AND {ts %s}"


cur.execute(query,(START_TIME,END_TIME,))


row = cur.fetchone()

while row is not None:
	Vmax0.append(row[1])
#sometimes the scope give me a crazy number like 99999999999 so I replace those values by the first measurement
	
#if row[2]<10:
	Vmax1.append(row[2])
	#else:
		#Vmax.append(Vmax[0])
	Vmax2.append(row[3])
	time_u.append(row[4])
	row = cur.fetchone()       


db.close()

time_u_first = str(time_u[0])
first_time = datetime.datetime.strptime(time_u_first,'%Y-%m-%d %H:%M:%S')

time_s = []

for i in time_u:
	i=str(i)
	elapsed = datetime.datetime.strptime(i,'%Y-%m-%d %H:%M:%S') - first_time
	time_s.append((elapsed.total_seconds())/60)

#second parameter is the variable to be ploted
plt.plot(time_s, Vmax1,  linestyle = 'none', marker = '.', markersize = 2)


plt.xlabel('Time / min', fontsize =16)
plt.ylabel('Vmax', fontsize =16)

plt.title('Vmax, ', fontsize =16)
plt.legend(prop={'size':14})
plt.grid()

plt.show()
