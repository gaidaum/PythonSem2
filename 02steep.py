#!/usr/bin/env python
vals = raw_input("Please enter a list of numbers:\n") # vals = "3 7 11 24"



total = 0 # total so far
steep = True
nums = vals.split() # num = ["3", "7", "9", "24"]
for n in nums:
	n = int(n) # n = 3

	if n > total:
		total += n
	else:
		steep = False

print steep
