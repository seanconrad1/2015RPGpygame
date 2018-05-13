from .item import *

import random

class Weapons(Items):
	"""Weapons in the game"""
	def __init__(self, name, weapon_type, 
				attackrating, value,):
		Items.__init__(self, "Weapon", value)
		self.name = name
		self.weapon_type = weapon_type
		self.attackrating = attackrating
		self.value = value
		self.durability = 100
		self.usable = True

	def break_weapon(self, dmg):
		self.durability -= dmg
		if self.durability <= 0:
			self.usable = False
			return True
		else:
			return True

	def repair_weapon(self):
		self.durability = 100
		self.usable = True
		return True

	#TEST ME. To be imported and used before every roll on attacking
	def critical_hit(self):
		self.random = random.random(1,10)
		if self.random == 1:
			Weapons.attackrating = Weapons.attackrating * 2
			return True
		else:
			return True

	def damage(self):
		return random.randint(0, self.attackrating)


class Swords(Weapons):
	'''Sword class that inherits Weapons'''
	def __init__(self, name, length, ar, val, 
				two_handed=False, throwable=False):
		Weapons.__init__(self, name, "Sword", ar, val)
		self.name = name
		self.length = length
		self.two_handed = two_handed
		self.throwable = throwable

class Axes(Weapons):
	'''Axe class that inherits Weapons'''
	def __init__(self, name, ar, val, two_handed=False, 
				double_sided=False, throwable=False):
		Weapons.__init__(self, name, "Axe", ar, val)
		self.name = name
		self.two_handed = two_handed
		self.double_sided = double_sided
		self.throwable = throwable

class Staffs(Weapons):
	'''Staff class that inherits Weapons'''
	def __init__(self, name, ar, val, throwable=False):
		Weapons.__init__(self, name, "Staff", ar, val)
		self.name = name
		self.throwable = throwable

class Spears(Weapons):
	'''Spear class that inherits Weapons'''
	def __init__(self, name, ar, val, throwable=False):
		Weapons.__init__(self, name, "Spear", ar, val)
		self.name = name
		self.throwable = throwable

class Hammers(Weapons):
	'''Hammer class that inherits Weapons'''
	def __init__(self, name, ar, val, two_handed=False, 
				double_sided=False, throwable=False):
		Weapons.__init__(self, name, "Hammer", ar, val)
		self.name = name
		self.double_sided = double_sided
		self.two_handed = two_handed
		self.throwable = throwable