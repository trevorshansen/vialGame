import numpy as np 
from random import shuffle

class Error(Exception):
		pass

class OutOfRangeError(Error):
		pass

class vialGame:

	def __init__(self, numColors=5, isTest=False):
		self.numColors = numColors
		if(isTest):
			self.testGame()
		else:
			self.randomGame()
		self.gameHistory = []

	# This will create a random new game
	def randomGame(self):
		self.vials =[]
		# Makes a list of 4 of 1 to numColors and then shuffles
		options = ((np.array(range(self.numColors * 4)) + 1) % self.numColors) + 1
		shuffle(options)
		# Creates number of vials + 2 empty vials
		for i in range(0, (self.numColors * 4),4):
			self.vials.append(options[i:i+4].tolist())
		for i in range(2):
			self.vials.append([])

	# Want to read this in from file
	def testGame(self):
		self.vials = []
		self.vials.append([5, 4, 1, 1])
		self.vials.append([3, 5, 1, 2])
		self.vials.append([5, 2, 4, 1])
		self.vials.append([5, 4, 3, 3])
		self.vials.append([2, 4, 3, 2])
		self.vials.append([])
		self.vials.append([])

	# Want to display this vertically
	def printGame(self):
		print("      top<-------->bottom")
		for i in range(len(self.vials)):
			print("Vial " + str(i + 1) + ": " + str(self.vials[i]))

	def getInputFromCLI(self):
		fromVial = toVial = None
		while(fromVial == toVial == None):
			try:
				fromVial, toVial = input("Please enter the fromVial then the toVial: ").split()
				fromVial = int(fromVial)
				toVial = int(toVial)
				if(fromVial < 1 or fromVial > self.numColors + 2  or toVial < 1 or toVial > self.numColors + 2):
					raise OutOfRangeError
			except (ValueError, TypeError):
				print("Please enter two numbers with a space between them")
				fromVial = toVial = None
			except OutOfRangeError:
				print("Please enter a number between 1 and " + str(self.numColors + 2))
				fromVial = toVial = None
		return fromVial, toVial

	def move(self, fromVial, toVial):
		if(len(self.vials[toVial - 1]) == 4):
			print("That vial is full, please pick a vial with space to move too")
			return
		if(len(self.vials[fromVial - 1]) == 0):
			print("That vial is empty, please pick a filled vial to move from")
			return

		# Save the last move
		self.gameHistory.insert(0, self.vials)

		# If the toVial is empty
		if(len(self.vials[toVial - 1]) == 0):
			self.vials[toVial - 1].append(self.vials[fromVial - 1].pop(0))
		# Check if the vials have the same top color
		if(self.vials[toVial - 1][0] == self.vials[fromVial - 1][0]):
			while(len(self.vials[fromVial - 1]) != 0 and self.vials[toVial - 1][0] == self.vials[fromVial - 1][0]):
				self.vials[toVial - 1].insert(0, self.vials[fromVial - 1].pop(0))
		return

	def checkWin(self):
		for i in self.vials:
			if(len(i) == 0 or (len(i) == 4 and all(x == i[0] for x in i))):
				continue
			else:
				return False
		return True

	# Undo last move - need a stack to save the game states
	def undoLastMove(self):
		if(len(self.gameHistory) == 0):
			print("Can't undo first move!")
		else:
			self.vials = self.gameHistory.pop(0)

# game = vialGame()
# while(game.checkWin() != True):
# 	game.printGame()
# 	fromVial, toVial = game.getInputFromCLI()
# 	game.move(fromVial, toVial)
# game.printGame()
# print("Great job, you won!")