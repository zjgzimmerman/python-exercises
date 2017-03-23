#!/usr/bin/python3
#Create a guessing game where user guesses random number between 1 and 9
#keep track of guesses and print at end of game

import random

def printStats(high, low, correct):
	print("----Game Stats----")
	print("Correct: {0}".format(correct))
	print("High: {0}".format(high))
	print("Low: {0}".format(low))
	print("------------------")

high = 0
low = 0
correct = 0

while True:
	answer = random.randint(1,9)
	guess = input("Enter guess (1,9): ")


	#validate input, and see if user wants to exit
	if guess.lower() == 'exit':
		break
	elif int(guess) not in range(1,10):
		print("Invalid input")
		continue

	#Test user input against answer
	if ( int(guess) == answer):
		print("Your gues was correct!")
		correct += 1
	elif (int(guess) > answer):
		print("Your gues was too high")
		high += 1
	elif (int(guess) < answer):
		print("Your gues was too low")
		low += 1
		
printStats(high, low, correct)
print("exiting")

