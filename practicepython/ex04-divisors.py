#!/usr/bin/python3
#Ask user for number and print out list of all divisors of that number
import math

def getDivisors(num):
	r = range(2, num)
	out = list()
	if (num < 2):
		return []
	for i in r:
		if (num % i == 0):
			out.append(i)
	return out

testNum = input("Enter number to test: ")
divisors = getDivisors(int(testNum))

if (len(divisors) == 0):
	print("Number is prime!")
else:
	print(divisors)
