from Items.books import *
from Items.weapon import *
from utilities import *

Dawn = Swords("Dawn", 3, 10, 15, two_handed=False, throwable=False)

The_Sorcerers_Stone = Books("The Sorcerers Stone", 50, 50, "J.K. Rowling", "TEST")




def find_all_item_names(item):
   	for i in all_items_in_game:
   		if i.name == item:
   			return i.name


print (find_item_value(Dawn.name))

print (find_all_item_names(A_Song_Of_Fire_and_Ice.name))