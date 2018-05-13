#Market
from utilities import *
from Items.container import *
import time

MarketInventory = Container('Market Inventory')

MarketInventory.add(Dawn.name, 1)
MarketInventory.add(Minor_Health_Potion.name, 5)
MarketInventory.add(Health_Potion.name, 3)
MarketInventory.add(Sting.name, 1)
MarketInventory.add(Rejuvenation_Potion.name, 1)
MarketInventory.add(Minor_Mana_Potion.name, 5)
MarketInventory.add(Small_Knife.name, 1)
MarketInventory.add(The_Silmarillion.name, 1)
MarketInventory.add(The_Sorcerers_Stone.name, 1)
MarketInventory.add(Worldslayer.name, 1)
MarketInventory.add(A_Song_Of_Fire_and_Ice.name, 1)

Market = True

#I want the market menu to display Name, Price and Quantity.
#Try to make the command be: 'buy 1 (item name)'
#Then the response be: Buy (quantity) + (item)'s for (gold)?
#Also add an INFO command

def return_Market_inventory():
    ordered_inventory = collections.OrderedDict((MarketInventory.inside))
    print ("\n----" + red + MarketInventory.name + end + "----")
    for k, v in ordered_inventory.items():
        print (str(k) + " qty(" + str(v) + ") " + red + str(find_item_value(k)) + end + "g")
    print ("------------------------\n")

def return_Backpack_inventory():
    ordered_inventory = collections.OrderedDict((Backpack.inside))
    print ("\n----" + red + Backpack.name + end + "----")
    for k, v in ordered_inventory.items():
        print (str(k) + " qty(" + str(v) + ") " + red + str(find_item_value(k)) + end + "g")
    print ("----------------\n")


def buy(arg):
	return_Market_inventory() 
	print ("You have " + red + str(NewHero.gold) + end + " gold. What would you like to buy?")
	ask = (input(">> "))
	ask = ask.title()
	if ask == "Leave" or ask == "No" or ask == "Exit" or ask == 'Back':
		market('arg')
	elif ask in MarketInventory.inside:
		if find_all_item_names(ask) == ask:
			print ("\n")
			get_item_stats(ask)
			print ('\nBuy item? yes or no')
			ask2 = (input(">> "))
			if ask2 == 'yes':
				price = find_item_value(ask)
				if NewHero.gold < price:
					print ("\nYou do not have enough gold for that item.")
					time.sleep(2)
					buy('arg')
				elif NewHero.gold >= price:
					MarketInventory.remove(ask, 1)
					NewHero.remove_gold(price)
					Backpack.add(ask, 1)
					buy('arg')
			else:
				buy('arg')
	else:
		buy('arg')

def sell(arg):
		
	print ("What would you like to sell? ")
	return_Backpack_inventory()
	ask = (input(">> "))
	ask = ask.title()
	if ask == "Leave" or ask == "No" or ask == "Exit" or ask == 'Back':
		market('arg')
	elif ask in Backpack.inside:
		if find_all_item_names(ask) == ask:
			get_item_stats(ask)
			print ('Sell item? yes or no')
			ask2 = (input(">> "))
			if ask2 == 'yes':
				price = find_item_value(ask)
				Backpack.remove(ask, 1)
				NewHero.update_gold(price)
				MarketInventory.add(ask, 1)
				sell('arg')
			else:
				sell('arg')
	else:
		sell('arg')




commands ={
	'buy'  : buy,
	'sell' : sell,  
}

def isValidCMD(cmd):
	if cmd in commands:
		return True
	return False

def runCMD(cmd, arg):
	commands[cmd](arg)


def market(arg):
	print ("\n" + underline + "Welcome to the Market" + end)
	print ("buy, sell, or leave.\n")
	input_l = input(">> ").split()
	if input_l[0] == "leave" or input_l == "no" or input_l == "exit" or input_l == "back":
		print ("Leaving")
	elif isValidCMD(input_l[0]):
			runCMD(input_l[0], "")
	else:
		print ("Not a valid command.")
		market('arg')