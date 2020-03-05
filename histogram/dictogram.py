from __future__ import division, print_function  # Python 2 and 3 compatibility
from random import randint

class Dictogram(dict):
    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__() #creating new list
        
