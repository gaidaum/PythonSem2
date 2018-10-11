#!/usr/bin/env python


x = 1 
while x <= 100:
	if (x%3) == (x%5) ==0:
		print "fizzbuzz"
	elif  (x%3)==0:
		print "fizz"
	elif (x%5)==0:
		print "buzz"
	else: 
		print x 
	x = x + 1
