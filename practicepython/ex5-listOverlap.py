#!/usr/bin/python3
#Practice python exercise 5
#Output the elements that 2 lists have in common

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(set(a).intersection(b))
