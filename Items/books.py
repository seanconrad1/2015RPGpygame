from .item import *


class Books(Items):
    """Books in the game"""
    def __init__(self, name,
				exp, value, author, contents):
        Items.__init__(self, "Book", value)
        self.name = name
        self.exp = exp
        self.author = author
        self.context = contents
