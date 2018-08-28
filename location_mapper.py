#!/usr/bin/python

#  Write a MapReduce program which will display the number of hits for each different file on the Web site.

import sys


for input_line in sys.stdin:
	line = input_line.strip().split(",")
	x = line[12]	# x-coordinate
	y = line[13]	# y-coordinate
	print "{0}\t{1}\t{2}\t{3}".format(x,y,line[5],str(0))
