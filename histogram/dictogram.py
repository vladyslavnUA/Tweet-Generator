from __future__ import division, print_function  # Python 2 and 3 compatibility
from random import randint

class Dictogram(dict):
    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__() #creating new list
    
    self.types = 0 # unique words
    self.tokens = 0 # all words
    if word_list != None:
        for word in word_list: # loop
            self.add_count(word) # add word

    def add_count(self, word, count=1):
        if word in self.keys(): # if word is displayed
            self[word] += count # increase frequency count
        else:
            self[word] = count
            self.types += 1 # add word type

        self.tokens += count # add count to total words

    def frequency(self, word):
        """ returns frequency of given word, or 0 """
        if word in self.keys():
            return self[word]
        else:
            return 0