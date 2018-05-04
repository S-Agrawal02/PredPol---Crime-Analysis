#!/usr/bin/python

#  Write a MapReduce program which will display the number of hits for each different file on the Web site.

import sys

for input_line in sys.stdin:
	line = input_line.strip().split(",")
	#print 'Line : '+str(line)
	#time = line[10].split(":")	#time 	this is the random time generated
	time = line[2].split(" ")[1].split(":")	#time	this is the real time
	#print 'Time : '+str(time[0])
	#print 'line '
	#print time[0]
	#count=count+1
	#print 'count'+str(count)
	hour = float(str(time[0]))
	print "{0}\t{1}".format(hour,str(input_line.strip()))

"""
	if hour>=0 and hour<3:
		quad[0].append(input_line)
	elif hour>=3 and hour<6:
		quad[1].append(input_line)
	elif hour>=6 and hour<9:
		quad[2].append(input_line)
	elif hour>=9 and hour<12:
		quad[3].append(input_line)
	elif hour>=12 and hour<15:
		quad[4].append(input_line)
	elif hour>=15 and hour<18:
		quad[5].append(input_line)
	elif hour>=18 and hour<21:
		quad[6].append(input_line)
	elif hour>=21 and hour<24:
		quad[7].append(input_line)


for i in range(0,8):
	#theft_c=0,murder_c=0,robbery_c=0,rape_c=0,drugs_c=0
	theft_c = 0
	murder_c=0
	robbery_c=0
	assault_c=0
	drugs_c=0
	kidnap_c=0
	for j in range(len(quad[i])):
		crime_array = quad[i][j].strip().split(',')
		#print 'QUAD : '+ quad[i][j]
		crime_type = str(crime_array[11])	#INDEX : index daal dena jo bhi hoga crime type dataset me
		#print ' Crime type : '+crime_type
		if crime_type == 'THEFT':
			theft_c = theft_c + 1
		elif crime_type=='MURDER':
			murder_c = murder_c + 1
		elif crime_type=='ROBBERY':
			robbery_c = robbery_c + 1
		elif crime_type=='ASSAULT':
			assault_c = assault_c + 1
		elif crime_type=='DRUGS':
			drugs_c = drugs_c + 1
		elif crime_type=='KIDNAPPING':
			kidnap_c = kidnap_c + 1

	total_crimes = theft_c + murder_c + robbery_c + assault_c + drugs_c + kidnap_c
	print 'THEFT : '+str(theft_c)
	print 'MURDER : '+str(murder_c)
	print 'ROBBERY : '+str(robbery_c)
	print 'ASSAULT : '+str(assault_c)
	print 'DRUGS : '+str(drugs_c)
	print 'KIDNAP : ' + str(kidnap_c)
	
	most = max(int(theft_c),int(murder_c), int(robbery_c), int(assault_c), int(drugs_c), int(kidnap_c))
	if most==theft_c:
		most_crime='THEFT'
	elif most==murder_c:
		most_crime='MURDER'
	if most==robbery_c:
		most_crime='ROBBERY'
	if most==assault_c:
		most_crime='ASSAULT'
	if most==drugs_c:
		most_crime='DRUGS'
	if most==kidnap_c:
		most_crime='KIDNAPPING'

	for j in range(len(quad[i])):
		l=int(quad[i][j].strip().split(",")[10].split(":")[0])
		print quad[i][j]+"\n"
	
	print 'Most kind in array ' + str(i+1) + ' is : ' + most_crime + ' - ' +str(most)
	# Now on the basis of counts of the crime type we will proceed
		
print 'Count : ' + str(count)

for i in range(0,8):		#displaying the arrays created
	print 'Array '+ str(i+1) + ' : '
	for j in range(len(quad[i])):
		l=int(quad[i][j].strip().split(",")[10].split(":")[0])
		print str(l)+"newLine"
#print "{0}\t{1}".format(output, 1)
"""
