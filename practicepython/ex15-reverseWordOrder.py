#!/usr/bin/python3
#Practice python exercise 15
#Reverse word order
#Take a string and reverse the order of words, not letters

def revString(strInput):
	words = strInput.split()
	words = words[::-1]
	return " ".join(words)

testString = input("Enter sentence to reverse: ")

print(revString(testString))
