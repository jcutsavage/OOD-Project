#!/usr/bin/env python

#author John Cutsavage

import math
#this code was taken from stackoverflow.com/questions/18833759/python-prime-number-checker
def is_prime(n):
	if n < 2: #0 and 1 aren't prime; assume only positive integers
		return False
	if n % 2 == 0 and n > 2:
		return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True

#this is my own code
def primes():
	n = int(raw_input("Enter a positive integer "))
	for i in range(0,n):
		if is_prime(i):
			print i #print the number if prime

