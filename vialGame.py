import numpy as np 
from random import shuffle
class vialGame:

	def __init__(self, numColors):
		self.vials = self.randomGame(numColors)

	# This will create a random new game
	def randomGame(self, numColors):
		self.vials =[]
		# Makes a list of 4 of 1 to numColors and then shuffles
		options = ((np.array(range(numColors * 4)) + 1) % numColors) + 1
		shuffle(options)
		# Creates number of vials + 2 empty vials
		for i in range(0, (numColors * 4),4):
			self.vials.append(options[i:i+4].tolist())
		for i in range(2):
			self.vials.append([])

		return self.vials

	def printGame(self):
		print("      top<-------->bottom")
		for i in range(len(self.vials)):
			print("Vial " + str(i + 1) + ": " + str(self.vials[i]))

	def move(self, fromVial, toVial):
		if(len(self.vials[toVial - 1]) == 4):
			print("That vial is full, please pick a vial with space to move too")
			return
		if(len(self.vials[fromVial - 1]) == 0):
			print("That vial is empty, please pick a filled vial to move from")
			return
		# Check if the vials have the same top color
		# if(self.vials[toVial - 1][0] == self.vials[fromVial - 1][0]):
		# 	self.vials[toVial - 1].insert(0, self.vials[fromVial - 1].pop(0))