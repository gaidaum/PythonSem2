#!/usr/bin/env python
string = str(raw_input("Enter a string:\n"))
substring = str(raw_input("Enter a substring:\n"))

if substring in string:
	print string + " contains " + substring
else :
	print string + " does not contain " + substring