from .item import *

class Potions(Items):
	"""Potions in the game"""
	def __init__(self, name, potion_type, 
				rating, value, modifier):
		Items.__init__(self, "Potion", value)
		self.name = name
		self.potion_type = potion_type
		self.rating = rating
		self.value = value
		self.modifier = modifier

