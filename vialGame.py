import numpy as np 
from random import shuffle
class vialGame:
# def vialGame(numColors):

	def __init__(self, numColors):
		self.vials = self.randomGame(numColors)

	def randomGame(self, numColors):
		self.vials =[]
		options = ((np.array(range(numColors * 4)) + 1) % numColors) + 1
		shuffle(options)
		# Creates number of vials + 2
		for i in range(0, (numColors * 4),4):
			self.vials.append(options[i:i+4].tolist())
			
		for i in range(2):
			self.vials.append([0,0,0,0])

		return self.vials

	def printGame(self):
		for i in range(len(self.vials)):
			print("Vial " + str(i + 1) + ": " + str(self.vials[i]))

	def move(self, fromVial, toVial):
		return
	# Need 4 units of each color randomized between numColors # of vials
