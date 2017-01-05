#!/usr/bin/python3
#99 bottles of beer song thing

def bottles():
	x = 99
	while x > 1:
		print("{0} bottles of beer on the wall\n{0} bottles of beer\nTake one down, pass it around\n {1} bottles of beer on the wall\n".format(str(x), str(x-1)))
		x -= 1
	else:
		print("{0} last bottle of beer on the wall\n{0} last bottle of beer\nTake it down, pass it around\nNo more bottles of beer on the wall :(".format(str(x)))

repeat = True
while repeat:
	bottles()
	ans = input("Would you like to hear it again? ")
	if ans.lower() in ('no', 'n', 'nope', 'nah', 'never', 'q'):
		repeat = False
	
