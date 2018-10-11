#!/usr/bin/env python
import sys
sentence = sys.stdin.readlines()


counts = {}
k = 0 
while k < len(sentence):
	i = 0 
	string = sentence[k].rstrip()
	while i < len(string):
		letter = list(string)[i].lower()
		if letter == " " or letter == ".":
			i = i 
		elif letter not in counts:
			counts[letter] = 1
		else : 
			counts[letter] = counts[letter] + 1
		i +=1
	k +=1
for key in sorted(counts):
	print key, counts[key]