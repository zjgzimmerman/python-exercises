#!/usr/bin/python3

import random
#original sets from problem definition
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12]

#Randomly generate list a and b
#list size and elements between 1-100
#a = []
#b = []

#for x in range(random.randint(1, 100)):
	#a.append(random.randint(1,100))
#for x in range(random.randint(1, 100)):
	#b.append(random.randint(1,100))

#a = random.sample(range(100), random.randint(1,100))
#b = random.sample(range(100), random.randint(1,100))

#print(a)
#print(b)

#intersect = set([x for x in a if x in b])

#intersection between 2 randomly generated 
#lists of random ints 1-100 in one line
intersect = list(set([x for x in random.sample(range(100), random.randint(1,100)) if x in random.sample(range(100), random.randint(1,100))]))

prin(intersect)
