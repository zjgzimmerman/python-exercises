#!/usr/bin/python3
import math


def checkPrime(num):
	for x in range(2 ,math.ceil(math.sqrt(num))):
		if num % x == 0:
			return False
	return True

primes = []
for x in range (3, 999999):
	if checkPrime(x):
		 primes.append(x)

print(primes)
