import collections
from txt_colors import *


class Container:
	def __init__(self, name):
		self.name = name
		self.inside = dict()

	def add(self, item, quantity):
		if quantity < 0:
			raise ValueError("Negative quantity. Use remove() instead.")
		if item in self.inside:
			self.inside[item] += quantity
		else:
			self.inside.update({item:quantity})
			if self.name == ("Backpack"):
				print (str(item) + " (" + str(quantity) + ")" + " added to " + str(self.name) + ".")

	def remove(self, item, quantity):
		if item not in self.inside:
			raise KeyError("Item not in container.")
		if quantity < 0:
			raise ValueError("Negative quantity. Use add() instead.")

		if self.inside[item] <= quantity:
			del self.inside[item]
		else:
			self.inside[item] -= quantity
			if self.name == "Backpack":
				print (item + " (" + str(quantity) + ") " "was removed from your inventory.")

	
	def return_formatted_inventory(self):
		ordered_inventory = collections.OrderedDict((self.inside))
		print ("----" + red + self.name + end + "----")
		for k, v in ordered_inventory.items():
			print (str(k) + " (" + str(v) + ")")