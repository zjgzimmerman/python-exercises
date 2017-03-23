#!/usr/bin/python3
#Ask user for number, print out different message for even/odd
#Extra: if it is a multiple of 4, print a different message
#Ask for 2 numbers, one number to check and one number to divide by
#Different message if number does/doesn't divide evenly 

num1 = int(input("Enter number to divide: "))
div = int(input("Enter number to divide by: "))

output = list()

if (num1 % 2 == 0):
	output.append('{0} is Even'.format(num1))
	if (num1 % 4 == 0):
		output.append('{0} is also a multiple of 4'.format(num1))
else:
	output.append('{0} is Odd'.format(num1))

if (num1 % div == 0):
	output.append("{0} divides evenly with {1}".format(num1, div))
else:
	output.append("{0} does not divide evenly with {1}".format(num1, div))
	
for line in output:
	print(line)
