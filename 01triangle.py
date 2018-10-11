#!/usr/bin/env python

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

if a == b == c:
	print "equilateral" 

elif (a==b) or (a==c) or (b==c):

	print "isosceles"
else :
	print "neither"
