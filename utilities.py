#Functions, and lists
#--------------------------------

from Objects import *
import time
import sys

#Listed item objects
all_items_in_game = [Dawn, Sting, Small_Knife, War_Ravager, Brutal_War_Axe, One_Handed_Axe,
		 		Infamy, Exiled_Spirit_Staff, Cold_Forged_Spear, Heartseeker, Reckoning,
		 		Minor_Health_Potion, Health_Potion, Minor_Mana_Potion, Mana_Potion,
		 		Major_Health_Potion, Major_Mana_Potion]

weapons_in_game = [Dawn, Sting, Small_Knife, War_Ravager, Brutal_War_Axe, One_Handed_Axe,
		 		Infamy, Exiled_Spirit_Staff, Cold_Forged_Spear, Heartseeker, Reckoning]

other_items_in_game = [Minor_Health_Potion, Health_Potion, Minor_Mana_Potion, Mana_Potion,
		 		Major_Health_Potion, Major_Mana_Potion]

#input is a string
#find_item_value('Infamy')
def find_all_item_names(item):
   	for i in all_items_in_game:
   		if i.name == item:
   			return i.name

def find_weapon_name(weapon):
	for i in weapons_in_game:
   		if i.name == weapon:
   			return i.name

def find_item_name(item):
	for i in other_items_in_game:
   		if i.name == item:
   			return i.name

def get_item_stats(item):
	for i in all_items_in_game:
		if i.name == item:
			print i.item_stats()
			return True

def get_item_modifier(item):
	for i in other_items_in_game:
		if i.name == item:
			return i.modifier
			return True

def get_item_rating(item):
	for i in other_items_in_game:
		if i.name == item:
			return i.rating


def find_item_value(item):
	for i in all_items_in_game:
		if i.name == item:
			return i.value
			return True

def attackrating(weapon):
	for i in weapons_in_game:
		if i.name == weapon:
			return i.attackrating
			return True


def check_inventory(args):
	ordered_inventory = collections.OrderedDict((Backpack.inside))
	print "-----" + red + "Backpack" + end + "-----"
	for k, v in ordered_inventory.iteritems():
		print str(k) + " (" + str(v) + ")"
	print "------------------"
	while True:
		ask = raw_input('Type an item name to get info on it or type \'no\' ')
		ask = ask.title()
		if (ask in Backpack.inside):
			get_item_stats(ask)
		elif ask == "No":
			break
		else:
			print "Can't find item in backpack"


def slowText(word): #Add a paramater 'speed' to control speeds of different things
	#Makes the text type letter by letter slowly.
	for i in word:
		time.sleep(0) #switch to .04 when done testing
		sys.stdout.write(i)
	time.sleep(1)
	print "\t"


#for i in all_items_in_game:
#	print (i.name + " " + str(i.value) + 'g')