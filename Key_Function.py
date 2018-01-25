import random
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
			row = 0
			while row < 4:
				try:
					if row + self.n2 >= 0 and col + self.n1 >= 0 \
					and board[row + self.n2][col + self.n1] == board[row][col]:
						board[row + self.n2][col + self.n1] *= 2
						board[row][col] = 0
						row +=2
						continue

				except:
					pass
				row += 1

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
		board = self.append(board)
		return board

	def append(self, board):
		block = random.choice([2,4])
		i,j = random.randint(0,3), random.randint(0,3)
		print i, j, board[i][j]
		while board[i][j] != 0:
			i,j = random.randint(0,3), random.randint(0,3)
			print i, j, board[i][j]
			print
		board[i][j] = block
		return board




board = [[0,0,0,2],[0,0,0,2],[0,0,0,4],[0,0,0,4]]
Print(board)
down = Moves('down')
board = down.function(board)
Print(board)
