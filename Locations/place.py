class Place(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		#self.look = look
		#self.examine = examine
		self.north = None
		self.south = None
		self.east = None
		self.west = None

	def connect(self, north='', south='', east='', west=''):
		self.north = north
		if north:
			north.south = self
		self.south = south
		if south:
			south.north = self
		self.east = east
		if east:
			east.west = self
		self.west = west
		if west:
			west.east = self


#Westeros land

field1 = Place('Field', "You are in a grassy field.")
field2 = Place('Field', "You are in a grassy field.")
field3 = Place('Field', "You are in a grassy field.")
field4 = Place('Field', "You are in a grassy field.")
field5 = Place('Field', "You are in a grassy field.")
field6 = Place('Field', "You are on a grassy pathway.")
field7 = Place('Field', "You are in a grassy field.")

forest1 = Place('Forest', "You are in a forest and it is dark.")
forest2 = Place('Forest', "You are in a forest and it is dark.")
forest3 = Place('Forest', "You are in a forest and it is dark.")
forest4 = Place('Forest', "You are in a forest and it is dark.")
forest5 = Place('Forest', "You are in a forest and it is dark.")
forest6 = Place('Forest', "You are in a forest and it is dark.")
forest7 = Place('Forest', "You are on a grassy pathway.")
forest8 = Place('Forest', "You are on a grassy pathway.")
forest9 = Place('Forest', "You are in a forest and it is dark.")
forest10 = Place('Forest', "You are in a forest and it is dark.")
forest11 = Place('Forest', "You are in a forest and it is dark.")
forest12 = Place('Forest', "You are in a forest and it is dark.")
forest13 = Place('Forest', "You are in a forest and it is dark.")
forest14 = Place('Forest', "You are in a forest and it is dark.")
forest15 = Place('Forest', "You are in a forest and it is dark.")
forest16 = Place('Forest', "You are in a forest and it is dark.")
House = Place('House', "You are in a house.")
Winterfell = Place('Winterfell', "You have entered Winterfell.")
Cave = Place('Cave', "You are in a cave.")

Winterfell.connect(east=field7, west=field2, north=field4, south=field5)

field1.connect(north=forest3,    		  east=field4,     south=field2)
field2.connect(north=field1,     west=None,       east=Winterfell, south=field3)
field3.connect(north=field2,     west=None,       east=field5,     south=None)
field4.connect(north=forest6,    west=field1,     east=field6,     south=Winterfell)
field5.connect(north=Winterfell, west=field3,     east=House, 	   south=None)
field6.connect(north=forest8,    west=field4,     east=forest12,   south=field7)
field7.connect(north=field6,     west=Winterfell, east=forest13,   south=House)

forest1.connect(north=None,      west=None,		  east=forest4,    south=forest2)
forest2.connect(north=forest1,   west=None,		  east=forest5,    south=forest3)
forest3.connect(north=forest2,   west=None,		  east=forest6,    south=field1)
forest4.connect(north=None,      west=forest1,	  east=Cave,       south=forest5)
forest5.connect(north=forest4,   west=forest2,    east=forest7,    south=forest6)
forest6.connect(north=forest5,   west=forest3,    east=forest8,    south=field4)
forest7.connect(north=Cave,      west=forest5,    east=forest10,   south=forest8)
forest8.connect(north=forest7,   west=forest6,    east=forest11,   south=field6)
forest9.connect(north=None, 	 west=Cave,       east=None,       south=forest10)
forest10.connect(north=forest9,  west=forest7,    east=None,       south=forest11)
forest11.connect(north=forest10, west=forest8,    east=None,       south=forest12)
forest12.connect(north=forest11, west=field6,     east=None,       south=forest13)
forest13.connect(north=forest12, west=field7,     east=None,       south=forest14)
forest14.connect(north=forest13, west=House,      east=None,       south=forest15)
forest15.connect(north=forest14, west=forest16,   east=None,       south=None)
forest16.connect(north=House,    west=None,       east=forest15,    south=None)

''' Use try if statements for falling off the map'''