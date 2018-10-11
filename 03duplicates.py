#!/usr/bin/env python

import sys

final = []

line = sys.stdin.readline().rstrip()

first = line.split()
line = sys.stdin.readline().rstrip()
second = line.split()
print 'Removing elements of', second, "from", first
for n in first: 
	if n not in second:
		final.append(n)
print final

