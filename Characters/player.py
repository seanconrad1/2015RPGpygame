from character import *

class txt_colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

blue = txt_colors.BLUE
purple = txt_colors.PURPLE
red = txt_colors.RED
yellow = txt_colors.YELLOW
end = txt_colors.END
underline = txt_colors.UNDERLINE


class Hero(Entity):
	"""Player's character"""

	def __init__(self, name):
		Entity.__init__(self, "Human", 25)
		self.level = 1
		self.name = name
		self.health = 100
		self.attackrating = 5
		self.mana = 5
		self.block = 5
		self.currentXP = 0
		self.currentWeapon = None
	
	def replenish_health(self, amount):
		self.health += amount
		print "Replenished " + str(amount) + " health."
		if self.health > 100:
			self.health = 100
		print "Current health: " + str(self.health)
		return True

	def subtract_health(self, amount):
		self.health -= amount
		if self.health <= 0:
			print "GAME OVER"
			sys.exit()
		return True

	def replenish_mana(self, amount):
		self.mana += amount
		print "Replenished " + str(amount) + " mana."
		if self.mana > 20:
			self.mana = 20
		print "Current mana: " + str(self.mana)
		return True

	def subtract_mana(self, amount):
		self.mana -= amount
		return True

	def change_weapon(self, newweapon):
		self.currentWeapon = newweapon
		return True

	def update_gold(self, amount):
		#Updates gold.
		self.gold += amount
		print ("\nYou have " + str(self.gold) + " gold.")

	def remove_gold(self, amount):
		#Removes gold.
		self.gold -= amount
		print ("\nYou have " + str(self.gold) + " gold.")

	#def level_up(self):
	#	if(self.currentXP*(self.level/2) * 2.1 > self.currentXP):
	#		self.level += 1
	#		return "You lvled up!"
	#		return "You are now level " + self.level
		
	def __str__(self):
		#Prints player's stats
		return("----" + red + "{}'s stats".format(self.name) + end + "----\nLevel: {}\nGold: {}\nHealth: {}\nMana: {}\nCurrent Weapon: {}\nAttack Rating: {}\nBlock: {}\nCurrent XP: {}\n--------------------".format(self.level, self.gold, self.health,self.mana, self.currentWeapon, self.attackrating, self.block, self.currentXP))


