#!/usr/bin/env python

final = []

line = raw_input("Please enter a list of values:\n") # line = "4 5 6"
first = line.split() # first = ["4", "5", "6"]
line = raw_input("Please enter a second list of values:\n") # line = "4 6"
second = line.split() # second = ["4", "6"]
print 'Removing elements of', second, "from", first
for n in first: # n = "4"
	if n not in second:
		final.append(n)
print final
# while 0 < len(line):
# 	i = 0
# 	while i < len(seen) and seen[i] != line:
# 		i = i + 1
#
# 	if i == len(seen):
# 		print line.rstrip()
# 		seen.append(line)
#
# 	line = raw_input("Please enter a second list of values:\n")
