from Items.weapon import *
from Items.potion import *
from Characters.player import *
from Characters.monsters import*
from txt_colors import *
from Items.container import *

#OBJECTS-----------------------------

#Containers----------------------------------------
Backpack = Container("Backpack")

#Entities------------------------------------------

NewHero = Hero("blank")

#WEAPONS-------------------------------------------

#Arguments for Swords (name, length, ar, val, two_handed=False, throwable=False)
Dawn = Swords("Dawn", 3, 10, 200, two_handed=False, throwable=False)
Sting = Swords("Sting", 2, 7, 50, two_handed=False, throwable=True)
Small_Knife = Swords("Small Knife", 1, 1, 1, two_handed=False, throwable=True)

#Arguments for Axes (name, ar, val, two_handed=False, double_sided=False, throwable=False)
War_Ravager = Axes("War Ravager", 15, 500, two_handed=True, double_sided=True, throwable=True)
Brutal_War_Axe = Axes("Brutal War Axe", 12, 300, two_handed=True, double_sided=False, throwable=True)
One_Handed_Axe = Axes("One Handed Axe", 10, 200, two_handed=False, double_sided=False, throwable=True)

#Arguments for Staffs (name, ar, val, throwable=False)
Infamy = Staffs("Infamy", 8, 180, throwable=False)
Exiled_Spirit_Staff = Staffs("Inherited War Staff", 11, 210, throwable=False)

#Arguments for Spears (name, ar, val, throwable=False)
Cold_Forged_Spear = Spears("Cold Forged Spear", 12, 300, throwable=True)
Heartseeker = Spears("Heartseeker", 14, 400, throwable=True)

#Arguments for Hammers (name, ar, val, two_handed=False, double_sided=False, throwable=False)
Worldslayer = Hammers("Worldslayer", 20, 2000, two_handed=True, double_sided=True, throwable=False)
Reckoning = Hammers("Reckoning", 18, 1200, two_handed=True, double_sided=False, throwable=False)

#MONSTERS-----------------------------------------

Bandit1 = Bandit("Bandit")


#ITEMS--------------------------------------------

#Potion Args = (name, potion_type, rating, value, modifier)
Minor_Health_Potion = Potions("Minor Health Potion", "Health Potion", 5, 5, "Health")
Health_Potion = Potions("Health Potion", "Health Potion", 10, 10, "Health")
Major_Health_Potion = Potions("Major Health Potion", "Health Potion", 20, 20, "Health")

Minor_Mana_Potion = Potions("Minor Mana Potion", "Mana Potion", 5, 5, "Mana")
Mana_Potion = Potions("Mana Potion", "Mana Potion", 10, 10, "Mana")
Major_Mana_Potion = Potions("Major Mana Potion", "Mana Potion", 20, 20, "Mana")


