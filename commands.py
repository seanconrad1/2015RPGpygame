#Player command functions

import sys
import utilities
import Characters.player
from txt_colors import *
from Locations.place import *


def help(arg):
	print "Here are some commands to type:\n" + red + "go " + end + "(compass direction)\n" + red + "use " + end + "(item name)\n" + end + red + "stats" + end + red + "\ni" + end + " (inventory)" + red + "\nsw weapons " + end + "(switch weapons)" + red + "\nmarket " + end + red + "\nmap" + end

def function():
	pass

def exit(arg):
	ask = raw_input("Are you sure you want to exit? ")
	if (ask == 'yes'):
		sys.exit()
	elif (ask == 'no'):
		pass

def check_inventory(args):
	utilities.check_inventory()

def switch_weapons(weapon):
	pass

def use_item(item):
	if item not in utilities.Backpack.inside:
		print ("Item is not in your backpack")

	if item in utilities.Backpack.inside:
		a = utilities.find_item_name(item)
		if a != item:
			print ("Item is not usable")

		elif a == item:
			rating = utilities.get_item_rating(item)
			mod = utilities.get_item_modifier(item)
			if mod == 'Health':
				utilities.NewHero.replenish_health(rating)
				utilities.Backpack.remove(item, 1)
			elif mod == 'Mana':
				utilities.NewHero.replenish_mana(rating)
				utilities.Backpack.remove(item, 1)


current_location = House
def go(direction):
	global current_location
	if direction == 'North':
		current_location = current_location.north
		print str(current_location.description)
		
	elif direction == 'East':
		current_location = current_location.east
		print str(current_location.description)

	elif direction == 'West':
		current_location = current_location.west
		print str(current_location.description)

	elif direction == 'South':
		current_location = current_location.south
		print str(current_location.description)
	else:
		print 'you did not specify what direction you wanted to go.'
