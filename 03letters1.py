#!/usr/bin/env python

sentence = raw_input("Please enter a sentence:\n")


counts = {}
i = 0 
while i < len(list(sentence)):
	letter = list(sentence)[i].lower()
	if letter == " " or letter == ".":
		i = i 
	elif letter not in counts:
		counts[letter] = 1
	else : 
		counts[letter] = counts[letter] + 1
	i +=1
for key in sorted(counts):
	print key, counts[key]