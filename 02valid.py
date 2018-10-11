#!/usr/bin/env python
n = str(raw_input("Enter a sentence:\n"))

if n[0] >= "A" and n[0] <= "Z" and n[len(n)-1] == ".":
	print "VALID"
else: 
	print "INVALID"