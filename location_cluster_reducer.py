#!/usr/bin/python

#  Write a MapReduce program which will display the number of hits for each different file on the Web site.

import sys
tab = []
quad = []
count=0
times=0
for i in range(5):
	quad.append([])
	tab.append([])

errors=0
rows=[]
tuples=[]

c1=c2=c3=c4=c5=0
c11=c12=c21=c22=c31=c32=c41=c42=c51=c52=0

x1=float(1106000)
x2=float(1128000)
x3=float(1150000)
x4=float(1172000)
x5=float(1194000)

y1=float(1846300)
y2=float(1866900)
y3=float(1887500)
y4=float(1908100)
y5=float(1928700)

for input_line in sys.stdin:
	line = input_line.strip().split("\t")		# X-coordinate \t Y-coordinate \t Type_of_crime \t cluster
	
	x = float(line[0])	# x-coordinate
	y = float(line[1])	# y-coordinate
	temp = str(x) + "\t" + str(y) + "\t" + str(line[2])
	count=count+1

	dist1 = ((x1 - x)**2+(y1 - y)**2)**0.5
	dist2 = ((x2 - x)**2+(y2 - y)**2)**0.5
	dist3 = ((x3 - x)**2+(y3 - y)**2)**0.5
	dist4 = ((x4 - x)**2+(y4 - y)**2)**0.5
	dist5 = ((x5 - x)**2+(y5 - y)**2)**0.5

	dist=min(dist1,dist2,dist3,dist4,dist5)
	
	if dist==dist1:
		temp = temp + "\t" + str(1)
		quad[0].append(temp)
		c11=c11+x
		c12=c12+y

	elif dist==dist2:
		temp = temp + "\t" + str(2)
		quad[1].append(temp)
		c21=c21+x
		c22=c22+y

	elif dist==dist3:
		temp = temp + "\t" + str(3)
		quad[2].append(temp)
		c31=c31+x
		c32=c32+y

	elif dist==dist4:
		temp = temp + "\t" + str(4)
		quad[3].append(temp)
		c41=c41+x
		c42=c42+y

	elif dist==dist5:
		temp = temp + "\t" + str(5)
		quad[4].append(temp)
		c51=c51+x
		c52=c52+y

	rows.append(temp)	#added row with current cluster (x,y,crime,cluster)

tuples=list(rows)
x1=c11
y1=c12
x2=c21
y2=c22
x3=c31
y3=c32
x4=c41
y4=c42
x5=c51
y5=c52

#=========== CLustering ==========================

while True:
	rows[:]=[]
	errors=0
	times=times+1
	x1=(float)(x1*1.0/((len(quad[0])+1)*1.0))
	x2=(float)(x2*1.0/((len(quad[1])+1)*1.0))
	x3=(float)(x3*1.0/((len(quad[2])+1)*1.0))
	x4=(float)(x4*1.0/((len(quad[3])+1)*1.0))
	x5=(float)(x5*1.0/((len(quad[4])+1)*1.0))

	y1=(float)(y1*1.0/((len(quad[0])+1)*1.0))
	y2=(float)(y2*1.0/((len(quad[1])+1)*1.0))
	y3=(float)(y3*1.0/((len(quad[2])+1)*1.0))
	y4=(float)(y4*1.0/((len(quad[3])+1)*1.0))
	y5=(float)(y5*1.0/((len(quad[4])+1)*1.0))
	
	c11=c12=c21=c22=c31=c32=c41=c42=c51=c52=0

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

		dis1=((x1-x)**2 + (y1-y)**2)**0.5
		dis2=((x2-x)**2 + (y2-y)**2)**0.5
		dis3=((x3-x)**2 + (y3-y)**2)**0.5
		dis4=((x4-x)**2 + (y4-y)**2)**0.5
		dis5=((x5-x)**2 + (y5-y)**2)**0.5

		dis=min(dis1,dis2,dis3,dis4,dis5)
	
		if dis==dis1:
			temp = temp + "\t" + str(1)
			quad[0].append(line[2])
			c11=c11+x
			c12=c12+y
			
			if line[3]!='1':	#checking the cluster
				errors = errors+1

		elif dis==dis2:
			temp = temp + "\t" + str(2)
			quad[1].append(line[2])
			c21=c21+x
			c22=c22+y

			if line[3]!='2':
				errors = errors+1

		elif dis==dis3:
			temp = temp + "\t" + str(3)
			quad[2].append(line[2])
			c31=c31+x
			c32=c32+y

			if line[3]!='3':
				errors = errors+1

		elif dis==dis4:
			temp = temp + "\t" + str(4)
			quad[3].append(line[2])
			c41=c41+x
			c42=c42+y

			if line[3]!='4':
				errors = errors+1

		elif dis==dis5:
			temp = temp + "\t" + str(5)
			quad[4].append(line[2])
			c51=c51+x
			c52=c52+y

			if line[3]!='5':
				errors = errors+1

		rows.append(temp)	#added row with current cluster (x,y,crime,cluster)
	x1=c11
	y1=c12
	x2=c21
	y2=c22
	x3=c31
	y3=c32
	x4=c41
	y4=c42
	x5=c51
	y5=c52

	tuples[:]=[]
	tuples=list(rows)
	print ""
	print "Errors faced  : ",errors," Out of ",count
	print "Percentage : ",(float)(errors*1.0/count*1.0)*100, " %"
	print ""
	if (float)(errors*1.0/count*1.0)*100 <= 1:		#Percentage error
		break


#====================== Displaying the results =============================
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


	"""for j in range(len(quad[i])):
		l=int(quad[i][j].strip().split(",")[10].split(":")[0])
		print quad[i][j]+"\n"
	"""
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
