#------------------------
#Sean Conrad Oct 2016 
#------------------------

"""Wanting to create a fantasy rpg text-based game that allows you to traverse through an area,
fight different creatures, complete quests, obtain gold.
Game is going to be small but can be expanded upon later.
"""

#TODO
#Create storyline
#Create inventory
#Add movemnt on the map

#Imports
import time
import pygame
import utilities
from Characters.player import *
from commands import *
from Market import *
from txt_colors import *
from Locations.place import *



#Booleans
gameOn = True

#Prints Hero class __str__
def print_hero_stats(args):
	print NewHero

def jump(args):
	print "You jump as high as you can."

#Commands that the user will type
commands = {
	 'Help': help,
	 'H'   : help,
	 '?'   : help,
	 'Go'  : go,
	# 'look': look,
	 'Exit': exit,
	    'I': check_inventory,
	'Inventory': check_inventory,
   	'Stats': print_hero_stats,
   	'Jump' : jump,
   	'Sw Weapons' : 'pass',
   	'Market': market,
   	'Use': use_item,
}

#Validates input and then sends to runCMD
def isValidCMD(cmd):
	if cmd in commands:
		return True
	return False

#After the command is validate, it gets
#ran in the commands dictionary
def runCMD(cmd, args):
	commands[cmd](args)

#MAIN LOOP--------------
def main():
	while gameOn:
		print '..'
		line = raw_input(">> ")
		line = line.title()
		input = line.split()
		#input.append("EOI")
		if len(input) == 1:
			if isValidCMD(input[0]):
				runCMD(input[0], "")

		if len(input) == 2:
			if isValidCMD(input[0]):
				runCMD(input[0], input[1])

		if len(input) == 3:
			a = input[1] + " " + input[2]
			if isValidCMD(input[0]):
				runCMD(input[0], a)

		if len(input) == 4:
			a = input[1] + " " + input[2] + " " + input [3]
			if isValidCMD(input[0]):
				runCMD(input[0], a)




#INTRO-------------------------------------------------------------------------

utilities.slowText("What is your name?")
heroname = raw_input()
NewHero.name = heroname

'''utilities.slowText("Welcome to Miami, " + heroname + ", it's a ")
utilities.slowText("good thing you arrived. We've been dealing ")
utilities.slowText("lots of issues with bandits raiding our village. ")
utilities.slowText("See if you can check out the market for anything ")
utilities.slowText("that will scare them away.")'''
print "Type 'help' for a list of commands"
main()
