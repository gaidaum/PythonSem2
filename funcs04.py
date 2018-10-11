#!/usr/bin/env python

import sys 

def get_price(age):
	if age < 17:
		return "5"
	elif age >= 60:
		return "7"
	else:
		return "10"

def merge_lists(l1,l2):
	i = 0
	l3 = l1[::2] + l2[::2]
	return l3

def weird_case(some_str):
	string=""
	i = True 
	for char in some_str:
		if i :
			string+= char.upper()
		else:
			string+= char.lower()
		if char != ' ':
			i = not i 
	return string

def remove_zeros(list):

	lis = []
	for element in list:
		if element != "0":
			lis.append(list)
	list = lis
	print list

	



	#if __name__ == '__main__':
   	#	print 'calling weird_case(\'change the case\')'
   	#	print weird_case('change the case')