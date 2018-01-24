def Print (board):
	for i in range (0,4):
		for j in range (0,4):
			print board[i][j],
		print
	print
	print

class Moves():
	def __init__(self, direction):
		if direction == "up": self.n1, self.n2 = 0, -1
		elif direction == "down": self.n1, self.n2 = 0, 1
		elif direction == "left": self.n1, self.n2 = -1, 0
		elif direction == "right": self.n1, self.n2 = 1, 0

	def add (self, board):
		for col in range (0,4): #n1 = 0 n2 = -1
			for row in range (0,4):
				try:
					if row + self.n2 >= 0 and col + self.n1 >= 0 \
					and board[row + self.n2][col + self.n1] == board[row][col]:
						board[row + self.n2][col + self.n1] *= 2
						board[row][col] = 0
						continue

				except:
					pass

		return board

	def move (self, board):
		for col in range (0,4): #n1 = 0 n2 = -1
			for row in range (0,4):
				try:
					if row + self.n2 >= 0 and col + self.n1 >= 0 \
					and board[row + self.n2][col + self.n1] == 0 and board[row][col]  != 0:
						board[row][col], board[row + self.n2][col + self.n1] = board[row + self.n2][col + self.n1], board[row][col]
						board = self.move(board)
					else:
						pass
				except:
					pass
		return board

	def function(self, board):
		#while self.move(board) != self.add(board):
		#board = self.move(board)
		board = self.add(board)
		board = self.move(board)
		return board


board = [[8,4,0,2],[8,8,4,0],[0,0,0,0],[0,0,0,0]]
Print(board)
RIGHT = Moves('right')
board = RIGHT.function(board)
Print(board)
