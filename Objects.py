from Items.weapon import *
from Items.potion import *
from Characters.player import *
from Characters.monsters import*
from txt_colors import *
from Items.container import *
from Items.books import *

# OBJECTS-----------------------------

# Containers----------------------------------------
Backpack = Container("Backpack")

# Entities------------------------------------------

NewHero = Hero("blank")

# WEAPONS-------------------------------------------

# Arguments for Swords (name, length, ar, val, two_handed=False, throwable=False)
Dawn = Swords("Dawn", 3, 10, 200, two_handed=False, throwable=False)
Sting = Swords("Sting", 2, 7, 50, two_handed=False, throwable=True)
Small_Knife = Swords("Small Knife", 1, 1, 1, two_handed=False, throwable=True)
Needle = Swords("Needle", 1, 1.5, 10, two_handed=False, throwable=False)

# Arguments for Axes (name, ar, val, two_handed=False, double_sided=False, throwable=False)
War_Ravager = Axes("War Ravager", 15, 500, two_handed=True, double_sided=True, throwable=True)
Brutal_War_Axe = Axes("Brutal War Axe", 12, 300, two_handed=True, double_sided=False, throwable=True)
One_Handed_Axe = Axes("One Handed Axe", 10, 200, two_handed=False, double_sided=False, throwable=True)

# Arguments for Staffs (name, ar, val, throwable=False)
Infamy = Staffs("Infamy", 8, 180, throwable=False)
Exiled_Spirit_Staff = Staffs("Inherited War Staff", 11, 210, throwable=False)

# Arguments for Spears (name, ar, val, throwable=False)
Cold_Forged_Spear = Spears("Cold Forged Spear", 12, 300, throwable=True)
Heartseeker = Spears("Heartseeker", 14, 400, throwable=True)

# Arguments for Hammers (name, ar, val, two_handed=False, double_sided=False, throwable=False)
Worldslayer = Hammers("Worldslayer", 20, 2000, two_handed=True, double_sided=True, throwable=False)
Reckoning = Hammers("Reckoning", 18, 1200, two_handed=True, double_sided=False, throwable=False)


# MONSTERS-----------------------------------------

Bandit1 = Bandit("Bandit")


# ITEMS--------------------------------------------

# Potion Args = (name, potion_type, rating, value, modifier)
Minor_Health_Potion = Potions("Minor Health Potion", "Health Potion", 5, 5, "Health")
Health_Potion = Potions("Health Potion", "Health Potion", 10, 10, "Health")
Major_Health_Potion = Potions("Major Health Potion", "Health Potion", 20, 20, "Health")

Minor_Mana_Potion = Potions("Minor Mana Potion", "Mana Potion", 5, 5, "Mana")
Mana_Potion = Potions("Mana Potion", "Mana Potion", 10, 10, "Mana")
Major_Mana_Potion = Potions("Major Mana Potion", "Mana Potion", 20, 20, "Mana")

Rejuvenation_Potion = Potions("Rejuvenation Potion", "Health Potion", 20, 20, "Health")

# Books
The_Silmarillion = Books("The Silmarillion", 50, 5, "J.R.R Tolkien", """                   AINULINDALE:\n
              The Music of the Ainur\n
     There was Eru, the One, who in Arda is called
     Ilúvatar ; and he made first the Ainur, the
     Holy Ones, that were the offspring of his
     thought, and they were with im before aught else
     was made. And he spoke to them, propounding to
     them themes of music ; and they sang before
     him, and he was glad...""")


The_Sorcerers_Stone = Books("The Sorcerers Stone", 50, 5, "J.K. Rowling", """                    Chapter one\n
                 The Boy Who Lived\n
     Mr. and Mrs. Dursley, of number four, Privet
     Drive, were proud to say that they were perfectly
     normal, thank you very much, They were the last
     people you'd expect to be in anything involved
     in anything strange or mysterious, because they
     just don't hold such nonsense...""")


A_Song_Of_Fire_and_Ice = Books("A Song Of Fire and Ice", 50, 5, "J.R.R Martin", "Winter is Coming...")

