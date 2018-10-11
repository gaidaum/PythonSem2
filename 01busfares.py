#!/usr/bin/env python

age = int(raw_input("Please enter your age:"))

if age <= 16:
	print "Your fare is: 0.75 euro."

elif age >= 17 and age <= 20:
	print "Your fare is: 1.25 euro."

elif age >= 21 and age <= 64:
	print "Your fare is: 1.5 euro."



else :
	print "You go free!"