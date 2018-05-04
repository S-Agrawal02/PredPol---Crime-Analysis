#!/usr/bin/python

#  Write a MapReduce program which will display the number of hits for each different file on the Web site.

import sys
tab = []
quad = []
centerx = []
centery = []
count=0
for i in range(4):
	quad.append([])
	tab.append([])
	centerx.append([])
	centery.append([])

#x5=float(1106000)
x1=float(1128000)
x2=float(1150000)
x3=float(1172000)
x4=float(1194000)
centerx[0].append(x1)
centerx[1].append(x2)
centerx[2].append(x3)
centerx[3].append(x4)
#centerx[4].append(x5)
#y5=float(1846300)
y1=float(1866900)
y2=float(1887500)
y3=float(1908100)
y4=float(1928700)
centery[0].append(y1)
centery[1].append(y2)
centery[2].append(y3)
centery[3].append(y4)
#centery[4].append(y5)


for input_line in sys.stdin:
	#print "Output : "+str(input_line)
	line = input_line.strip().split("\t")		# X-coordinate \t Y-coordinate \t Tuple
	#print 'Line : '+str(line)
	#print 'x : '+str(line[0])
	#print 'y : '+str(line[1])
	x = float(line[0])	# x-coordinate
	y = float(line[1])	# y-coordinate
	#print 'line '+str(line)
	#print time+ "---"
	count=count+1
	#print 'count'+str(count)
	dist1 = ((x1 - x)**2+(y1 - y)**2)**0.5
	dist2 = ((x2 - x)**2+(y2 - y)**2)**0.5
	dist3 = ((x3 - x)**2+(y3 - y)**2)**0.5
	dist4 = ((x4 - x)**2+(y4 - y)**2)**0.5
	#dist5 = ((x5 - x)**2+(y5 - y)**2)**0.5

	dist=min(dist1,dist2,dist3,dist4)
	
	if dist==dist1:
		quad[0].append(line[2])
	elif dist==dist2:
		quad[1].append(line[2])
	elif dist==dist3:
		quad[2].append(line[2])
	elif dist==dist4:
		quad[3].append(line[2])
	#elif dist==dist5:
	#	quad[4].append(line[2])


for i in range(0,4):
	#theft_c=0,murder_c=0,robbery_c=0,rape_c=0,drugs_c=0
	theft_c = 0
	criminal_c=0
	burglary_c=0
	assault_c=0
	narcotics_c=0

	for j in range(len(quad[i])):
		crime_array = quad[i][j].strip().split(',')
		#print 'QUAD : '+ quad[i][j]
		crime_type = str(crime_array[5])	#INDEX : index daal dena jo bhi hoga crime type dataset me
		#print ' Crime type : '+crime_type
		if crime_type == 'THEFT':
			theft_c = theft_c + 1
		elif crime_type=='CRIMINAL DAMAGE':
			criminal_c = criminal_c + 1
		elif crime_type=='BURGLARY':
			burglary_c = burglary_c + 1
		elif crime_type=='ASSAULT':
			assault_c = assault_c + 1
		elif crime_type=='NARCOTICS':
			narcotics_c = narcotics_c + 1


	total_crimes = theft_c + criminal_c + burglary_c + assault_c + narcotics_c

	print '\n\nFor Area ' + str(i+1) + ' with centroid at : ('+ str(centerx[i])+','+str(centery[i])+')'+' - Occurrence of Crime types are:  '
	print '----------------------------------------------------------------------------------------------'
	print '\t\tTHEFT\t\t\t: '+str(theft_c)
	print '\t\tCRIMINAL DAMAGE\t\t: '+str(criminal_c)
	print '\t\tBURGLARY\t\t: '+str(burglary_c)
	print '\t\tASSAULT\t\t\t: '+str(assault_c)
	print '\t\tNARCOTICS\t\t: '+str(narcotics_c)

	most = max(int(theft_c),int(criminal_c), int(burglary_c), int(assault_c), int(narcotics_c))
	if most==theft_c:
		most_crime='THEFT'
		strategy = 'Security surviellance cameras to be installed, Focus on awareness regarding security systems in the area'
	elif most==criminal_c:
		most_crime='CRIMINAL DAMAGE'
		strategy = 'Petrolling to be increased in area, Focus on suspicious personnels with damage history'
	elif most==burglary_c:
		most_crime='BURGLARY'
		strategy = 'Alarming systems and emergency alarm button to be installed, Focus on quicker action plan to avoid delays'
	elif most==assault_c:
		most_crime='ASSAULT'
		strategy = 'Security surviellance cameras to be installed, Citizens should be taught about Self Defence and corresponding techniques for safety.'
	elif most==narcotics_c:
		most_crime='NARCOTICS'
		strategy = 'Planting of spy personnels for inside information, Secret operations to be conducted targeting locality responsible for circulation and supplies.'

	"""for j in range(len(quad[i])):
		l=int(quad[i][j].strip().split(",")[10].split(":")[0])
		print quad[i][j]+"\n"
	"""
	print '\n\t\t=> Total Crimes occured and reported in above Area is : ' + str(total_crimes) + ' reports.'
	print '\n\t\t=> Also the most frequent crime in above Area is : ' + most_crime + ' - ' +str(most) + ' times.'
	print '\n\t\t=> Policing guidlines / Strategy to be followed : ' + strategy	
	# Now on the basis of counts of the crime type we will proceed
	tab[i].append(theft_c)
	tab[i].append(criminal_c)
	tab[i].append(burglary_c)
	tab[i].append(assault_c)
	tab[i].append(narcotics_c)
	
	# Now on the basis of counts of the crime type we will proceed

print '\n\n**************************************************************************************************'
print '\n\t\t\t\t\t\t\t\t\tTHEFT\t\tCRIMINAL\tBURGLARY\tASSAULT\t\tNARCOTICS'
for i in range(0,4):
	#for j in range(0,5):
	print "\nArea "+str(i+1)+' with centroid at : ('+ str(centerx[i])+','+str(centery[i])+')'+"\t\t\t"+str(tab[i][0])+"\t\t"+str(tab[i][1])+"\t\t"+str(tab[i][2])+"\t\t"+str(tab[i][3])+"\t\t"+str(tab[i][4])
		
print '\n\n**************************************************************************************************'
print '\n\t* Total number of Tuples analysed are : ' + str(count)
print '\n**************************************************************************************************\n\n'

"""displaying the arrays created
i=0
#print 'Array '+ str(i+1) + ' : '
for j in range(len(quad[i])):
	l=int(quad[i][j].strip().split(",")[10].split(":")[0])
	print str(l)+"\n"

i=4
print 'Array '+ str(i+1) + ' : '
for j in range(len(quad[i])):
	l=int(quad[i][j].strip().split(",")[10].split(":")[0])
	print str(l)+"\n"
"""
	#print "{0}\t{1}".format(output, 1)
	#print "{0}\t{1}".format(output, 1)
