#!/usr/bin/python3
#Print out all even elements of a list

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = [x for x in a if x % 2 == 0]
print(even)
