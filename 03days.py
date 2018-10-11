#!/usr/bin/env python
my_input = raw_input("Please enter a month:\n").lower()

if my_input.lower() == 'september' or my_input == 'april' or my_input == 'june' or my_input == 'november':
    print 30

elif my_input.lower() == 'january' or my_input == 'march' or my_input == 'may' or my_input== 'july' or my_input == 'august' or my_input == 'october' or my_input== 'december':
     print 31
elif my_input.lower() == "february" :
	print 28 

else:
	print "Invalid month!"

