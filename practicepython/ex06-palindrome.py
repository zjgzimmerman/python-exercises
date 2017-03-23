#!/usr/bin/python3
#Find out if input string is a palindrome

testString = input("Enter string: ")
testString = testString.replace(" ", "").lower()

if testString == testString[::-1]:
	print("String is a plaindrome!")
else:
	print("String is not a palindrome!")
