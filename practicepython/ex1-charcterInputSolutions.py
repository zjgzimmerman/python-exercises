#!/usr/bin/python3

#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old
import datetime

today = datetime.date.today()

name = input("What is your name? ")
age = int(input("What is your age? "))

hundredYear = str(today.year + (100 - age))

print("Hey {0}, you will be 100 in {1}".format(name, hundredYear))
