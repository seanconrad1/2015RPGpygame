class Entity():
	"""All beings in the game"""
	def __init__(self, entity_type, gold):
		self.entity_type = entity_type
		self.gold = gold

	def dead(self):
		if self.entity_type == "Human":
			if self.health == 0:
				return "You have died. Game Over"
		elif self.entity_type == "NPC":
			if self.health == 0:
				return "Monster has died"