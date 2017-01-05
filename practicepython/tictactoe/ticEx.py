#!/usr/bin/python3
#Zach Zimmerman 01-03-17
#
#TicTacToe game example
#for practicepython.org
#http://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html
def drawBoard(x, y):
	"""
	Draw a board of any size
	"""
	for row in range(y):
		print(" ---" * x)
		for cell in range(x):
			print("|   ", end='')
		print("|")
	print(" ---" * x)


def drawTic(board):
	"""
	Draw a Tic-Tac-Toe board from a 'board' variable
	which is a list of three lists which represent rows
	"""
	#Possible values for a space and their symbols
	xo = {0: ' ', 1: 'X', 2:'O'}

	#Print out board with player pieces
	for row in range(3):
		print(" ---" * 3)
		for cell in range(3):
			print("| %s " % xo[board[row][cell]], end='')
		print("|")
	print(" ---" * 3)
	
def checkBoard(board):
	#Check rows for winner
	for row in board:
		rowSet = set(row)
		if 0 not in rowSet and len(rowSet) == 1:
			return rowSet.pop()

	#Check columns for winner
	for col in range(len(board[0])):
		colSet = {board[0][col], board[1][col], board[2][col]}	
		if 0 not in colSet and len(colSet) == 1:
			return colSet.pop()

	#Check diagnols for winner
	diag1 = {board[0][0], board[1][1], board[2][2]}
	if 0 not in diag1 and len(diag1) == 1:
		return diag1.pop()
	diag2 = {board[0][2], board[1][1], board[2][0]}
	if 0 not in diag2 and len(diag2) == 1:
		return diag2.pop()

	#Check for draw
	if 0 not in set(board[0] + board[1] + board[2]):
		return -1

def playGame():
	winner = None
	#X and Y coords for different cell numbers
	x = {1: 0, 2: 1, 3: 2, 
			 4: 0, 5: 1, 6: 2,
			 7: 0, 8: 1, 9: 2}

	y = {1: 0, 2: 0, 3: 0, 
			 4: 1, 5: 1, 6: 1,
			 7: 2, 8: 2, 9: 2}

	#Generate empty board
	board = [[0, 0, 0] for x in range(3)]

	player = 1 

	#Main game loop
	while winner == None: 
		print("Player %s" % player)
		drawTic(board)
		try:
			turn = int(input("Input cell (0-9): "))
			print()
			#raise error if input 
			if turn > 9 or board[y[turn]][x[turn]] != 0:
				raise ValueError 
		except ValueError:
			print("Invalid entry, try again")
			continue
		board[y[turn]][x[turn]] = player
		player = 1 if player == 2 else 2
		winner = checkBoard(board)
	return winner	

if __name__ == '__main__':
	winner = playGame()
	print("Player %s won!" % winner)
