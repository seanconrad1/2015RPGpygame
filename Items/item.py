from txt_colors import *


class Items(object):
	"""Envoloping class for all items in the game"""
	def __init__(self, item_type, value, quantity=1):
		#Rating for example is how much you'll get healed by.
		self.item_type = item_type
		self.value = value
		self.quantity = quantity
		self.netValue = quantity * value

	def recalc(self):
		self.netValue = self.quantity * self.value


	def item_stats(self):
		if self.item_type == "Potion":
			return"----" + red + self.name + end + "----\nRestores {} {}.\nValue: {} gold\n---------------------".format(self.rating, self.modifier, self.value)
		elif self.item_type == "Weapon":
			return"----" + red + self.name + end + "----\nType: {}\nAttack Rating: {}\nDurability: {}\nUsable: {}\nIs throwable: {}\nValue: {} gold\n-------------------".format(self.weapon_type, self.attackrating, self.durability, self.usable, self.throwable, self.value)

	def itemReceived(item):
		pass