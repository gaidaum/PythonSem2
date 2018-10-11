#!/usr/bin/env python
vals = raw_input("Enter a list of numbers:\n").split()

count = 0 
i = 0 
while i <len(vals):
	if int(vals[i]) >= 1000:
		count = count + 1
	i = i + 1
print count 