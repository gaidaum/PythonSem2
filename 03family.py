#!/usr/bin/env python


import sys

lines = sys.stdin.readlines()
families = {}
name_to_find = lines[-1].rstrip()

for line in lines[:-1]:
	name = line.split()
	firstname=name[0]
	surname = name[1]
	if surname not in families:
		families[surname] = []
	families[surname].append(firstname)

if name_to_find in families:
	print families[name_to_find]
else :
	print "Not there!"