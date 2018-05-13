from .character import *

class NPC(Entity):
	"""Player's character"""
	def __init__(self, name, NPC_Type, health, attackrating, mana, block, xp):
		Entity.__init__(self, "NPC", 1)
		self.name = name
		self.health = health
		self.attackrating = attackrating
		self.mana = mana
		self.block = block
		self.xp = xp

class Bandit(NPC):
	"""Bandit enemy class"""
	def __init__(self, name):
		NPC.__init__(self, name, "Monster", 100, 10, 10, 5, 25)
		self.name = name
