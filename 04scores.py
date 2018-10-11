#!/usr/bin/env python

import sys 

wins = 0
draws = 0
losses = 0
file = sys.argv[1]


with open(file,"r") as f:
	data = f.read().rstrip().split(",")
	for line in data:
	
		if line == "3" :
			wins = wins + 1
		elif line == "1":
			draws = draws + 1
		elif line == "0":
			losses = losses + 1
		
print "Wins:", wins
print "Draws:", draws
print "Losses:", losses
