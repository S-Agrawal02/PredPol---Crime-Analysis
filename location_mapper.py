#!/usr/bin/python

#  Write a MapReduce program which will display the number of hits for each different file on the Web site.

import sys


for input_line in sys.stdin:
	line = input_line.strip().split(",")
	#print 'Line : '+str(line)
	x = line[12]	# x-coordinate
	y = line[13]	# y-coordinate
	#print 'Time : '+str(time[0])
	#print 'line '
	#print time[0]
	#count=count+1
	#print 'count'+str(count)
	print "{0}\t{1}\t{2}".format(x,y,str(input_line.strip()))
