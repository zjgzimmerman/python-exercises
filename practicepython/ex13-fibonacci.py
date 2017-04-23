#!/usr/bin/python3
# Practice python exercise 13
# write script to generate x numbers of the fibonacci sequence

#Generator to make fibonacci numbers
def fib():
    n1, n2 = 0, 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2

num = input("Enter number of fibonacci elements to generate: ")
output = fib()
for x in range(0, int(num)):
    print(next(output))