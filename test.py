

import math

users_xp = 0
new_xp = 10


def level_up(level):
	global exp
	exp = level * math.log10(level)
	exp = exp * 100
	return exp

def add_xp(exp):
	pass



print(level_up(2))