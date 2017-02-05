#!/usr/bin/python3
#Iterate through a list and print elements that are less than 10
#Extra: do it in one line
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(list(filter(lambda x: x < 10, a))) #one line!
