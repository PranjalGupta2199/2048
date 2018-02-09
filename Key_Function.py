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
		row, col = 0, 0
		if direction == "up": self.var1 , self.var2,self.n1, self.n2 = col, row, 0, -1
		elif direction == "down": self.var1, self.var2 ,self.n1, self.n2 = col, row, 0, 1
		elif direction == "left": self.var1, self.var2 ,self.n1, self.n2 = row, col, -1, 0
		elif direction == "right": self.var1, self.var2, self.n1, self.n2 = row, col, 1, 0

	def add (self, board):
		# define logical variable names
		for self.var1 in range (0,4): #n1 = 0 n2 = -1
			for self.var2 in range(0,4):
				try:
					if self.var2 + self.n2 >= 0 and self.var1 + self.n1 >= 0\
					 and board[self.var2 + self.n2][self.var1 + self.n1] == board[self.var2][self.var1]:
						board[self.var2 + self.n2][self.var1 + self.n1] *= 2
						board[self.var2][self.var1] = 0

				except:
					pass

		return board

	def move (self, board):
		for self.var1 in range (0,4): #n1 = 0 n2 = -1
			for self.var2 in range(0,4):
				try:
					if self.var2 + self.n2 >= 0 and self.var1 + self.n1 >= 0 \
					and board[self.var2 + self.n2][self.var1 + self.n1] == 0 \
					and board[self.var2][self.var1]  != 0:
						board[self.var2][self.var1], board[self.var2 + self.n2][self.var1 + self.n1] \
						= board[self.var2 + self.n2][self.var1 + self.n1], board[self.var2][self.var1]
						board = self.move(board)
				except:
					pass
		return board

	def function(self, board):
		if self.move(board) != board :
			temp1 = self.add(self.move(board))
			temp2 = self.add(self.move(temp1))
			while temp1 != temp2:
				temp1, temp2 = temp2, self.add(self.move(temp2))
		else:
			return self.append(self.move(self.add(board)))
		return self.append(temp1)


	def append(self, board):
		block = random.choice([2,4])
		i, j = random.randint(0,3), random.randint(0,3)
		while board[i][j] != 0:
			i, j = random.randint(0,3), random.randint(0,3)
		board[i][j] = block
		return board
