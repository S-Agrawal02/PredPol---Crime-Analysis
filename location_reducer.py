#!/usr/bin/python

#  Write a MapReduce program which will display the number of hits for each different file on the Web site.

import sys
tab = []
quad = []

times=1

c1=0
c1x1=1095000
c1x2=1117000

c2=0
c2x1=1117000
c2x2=1139000

c3=0
c3x1=1139000
c3x2=1161000

c4=0
c4x1=1161000
c4x2=1183000

c5=0
c5x1=1183000
c5x2=1205000

rows=[]
tuples=[]

count=0
errors=10

for i in range(5):
	quad.append([])
	tab.append([])

for input_line in sys.stdin:
	line = input_line.strip().split("\t")		# X-coordinate \t Y-coordinate \t crime
	
	x = float(line[0])	# x-coordinate
	y = float(line[1])	# y-coordinate
	temp = str(x) + "\t" + str(y) + "\t" + str(line[2])
	
	count=count+1
	
	
	if x>=c1x1 and x<c1x2:
		temp = temp + "\t" + str(1)
		quad[0].append(temp)
		c1=c1+x

	elif x>=c2x1 and x<c2x2:
		temp = temp + "\t" + str(2)
		quad[1].append(temp)
		c2=c2+x

	elif x>=c3x1 and x<c3x2:
		temp = temp + "\t" + str(3)
		quad[2].append(temp)
		c3=c3+x

	elif x>=c4x1 and x<c4x2:
		temp = temp + "\t" + str(4)
		quad[3].append(temp)
		c4=c4+x

	elif x>=c5x1 and x<c5x2:
		temp = temp + "\t" + str(5)
		quad[4].append(temp)
		c5=c5+x

	rows.append(temp)	#added row with current cluster (x,y,crime,cluster)

tuples=list(rows)


#=========== CLustering ==========================

while True:
	rows[:]=[]
	errors=0
	times=times+1
	c1=(float)(c1*1.0/(len(quad[0])*1.0))
	c2=(float)(c2*1.0/(len(quad[1])*1.0))
	c3=(float)(c3*1.0/(len(quad[2])*1.0))
	c4=(float)(c4*1.0/(len(quad[3])*1.0))
	c5=(float)(c5*1.0/(len(quad[4])*1.0))
	c11=0
	c22=0
	c33=0
	c44=0
	c55=0

	quad[0][:]=[]
	quad[1][:]=[]
	quad[2][:]=[]
	quad[3][:]=[]
	quad[4][:]=[]

	for input_line in tuples:
		line = input_line.strip().split("\t")		# X-coordinate \t Y-coordinate \t crime \t cluster
	
		x = float(line[0])	# x-coordinate
		y = float(line[1])	# y-coordinate
		temp = str(x) + "\t" + str(y) + "\t" + str(line[2])
		dis1=abs(c1-x)
		dis2=abs(c2-x)
		dis3=abs(c3-x)
		dis4=abs(c4-x)
		dis5=abs(c5-x)

		dis=min(dis1,dis2,dis3,dis4,dis5)
	
		if dis==dis1:
			temp = temp + "\t" + str(1)
			quad[0].append(line[2])
			c11=c11+x
			if line[3]!='1':	#checking the cluster
				errors = errors+1

		elif dis==dis2:
			temp = temp + "\t" + str(2)
			quad[1].append(line[2])
			c22=c22+x
			if line[3]!='2':
				errors = errors+1

		elif dis==dis3:
			temp = temp + "\t" + str(3)
			quad[2].append(line[2])
			c33=c33+x
			if line[3]!='3':
				errors = errors+1

		elif dis==dis4:
			temp = temp + "\t" + str(4)
			quad[3].append(line[2])
			c44=c44+x
			if line[3]!='4':
				errors = errors+1

		elif dis==dis5:
			temp = temp + "\t" + str(5)
			quad[4].append(line[2])
			c55=c55+x
			if line[3]!='5':
				errors = errors+1

		rows.append(temp)	#added row with current cluster (x,y,crime,cluster)
	c1=c11
	c2=c22
	c3=c33
	c4=c44
	c5=c55
	tuples[:]=[]
	tuples=list(rows)
	print ""
	print "Errors faced  : ",errors," Out of ",count
	print "Percentage : ",(float)(errors*1.0/count*1.0)*100, " %"
	print ""
	if (float)(errors*1.0/count*1.0)*100 <= 0.1:		#Percentage error
		break


#============== Displaying the results ============================

for i in range(0,5):
	theft_c = 0
	criminal_c=0
	burglary_c=0
	assault_c=0
	narcotics_c=0

	for j in range(len(quad[i])):
		crime_type = quad[i][j]
		
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

	print '\n\nFor Area ' + str(i+1) + ' - Occurrence of Crime types are:  '
	print '-------------------------------------------------------------'
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

	print '\n\t\t=> Total Crimes occured and reported in above Area is : ' + str(total_crimes) + ' reports.'
	print '\n\t\t=> Also the most occured crime in above Area is : ' + most_crime + ' - ' +str(most) + ' times.'
	print '\n\t\t=> Policing guidlines / Strategy to be followed : ' + strategy
	# Now on the basis of counts of the crime type we will proceed
	tab[i].append(theft_c)
	tab[i].append(criminal_c)
	tab[i].append(burglary_c)
	tab[i].append(assault_c)
	tab[i].append(narcotics_c)
	
	# Now on the basis of counts of the crime type we will proceed

print '\n\n**************************************************************************************************'
print '\n\t\t\tTHEFT\t\tCRIMINAL\tBURGLARY\tASSAULT\t\tNARCOTICS'
for i in range(0,5):
	#for j in range(0,5):
	print "\nArea "+str(i+1)+"\t\t\t"+str(tab[i][0])+"\t\t"+str(tab[i][1])+"\t\t"+str(tab[i][2])+"\t\t"+str(tab[i][3])+"\t\t"+str(tab[i][4])
		
print '\n\n**************************************************************************************************'
print '\n\t* Total number of Tuples analysed are : ' + str(count)
print '\n**************************************************************************************************\n\n'

		
print '**************************************************************************************************'
print '\n\t* Total number of times clusters were formed are : ' + str(times)
print '\n**************************************************************************************************\n\n'

