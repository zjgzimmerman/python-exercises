#!/usr/bin/python3

def isPalindrome(string):
	string = string.replace(" ","").lower()
	if string == string[::-1]:
		return True
	else:
		return False

testString = "tacocat"
if isPalindrome(testString):
	print("Palindrome!")
else:
	print("No Palindrome")
