#!/usr/bin/env python
vals = raw_input("Enter a list of numbers:\n")



n = []

num = vals.split()	
for numbers in num:
		
	n.append(int(numbers))

print max(n),"@",n.index(max(n))+1