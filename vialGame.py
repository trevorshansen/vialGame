import numpy as np 
from random import shuffle
class vialGame:

	def __init__(self, numColors):
		self.numColors = numColors
		self.vials = self.randomGame()
		printGame()

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

		return self.vials

	def printGame(self):
		print("      top<-------->bottom")
		for i in range(len(self.vials)):
			print("Vial " + str(i + 1) + ": " + str(self.vials[i]))

	def move(self, fromVial, toVial):
		if(0 > fromVial > self.numColors + 2 or 0 > toVial > self.numColors + 2):
			print("Please enter a number between 1 and " + str(self.numColors + 2))
		if(len(self.vials[toVial - 1]) == 4):
			print("That vial is full, please pick a vial with space to move too")
			return
		if(len(self.vials[fromVial - 1]) == 0):
			print("That vial is empty, please pick a filled vial to move from")
			return

		# If the toVial is empty
		if(len(self.vials[toVial - 1]) == 0):
			self.vials[toVial - 1].append(self.vials[fromVial - 1].pop(0))
		# Check if the vials have the same top color
		if(self.vials[toVial - 1][0] == self.vials[fromVial - 1][0]):
			# This doesn't work when emptying a vial
			while(self.vials[toVial - 1][0] == self.vials[fromVial - 1][0]):
				self.vials[toVial - 1].insert(0, self.vials[fromVial - 1].pop(0))
		printGame()
		return