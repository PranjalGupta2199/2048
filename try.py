def move (board):
	n = 4
	for col in range (0,n):
		for row in range (0,n):
			if row-1 >= 0 and board[row-1][col] == 0 and board[row][col]  != 0:
				board[row][col], board[row-1][col] = board[row-1][col], board[row][col]
				board = move(board)
			else:
				pass
	return board





def Print (board):
	for i in range (0,4):
		for j in range (0,4):
			print board[i][j],
		print

board = [[0,0,0,2],[2,0,2,2],[0,4,32,4],[0,4,8,32]]
Print(board)
board = move(board)
print
print
Print(board)
