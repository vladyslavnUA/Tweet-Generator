import sys
from random import random, randint

some_file = open("/Users/vladyslav/Desktop/cs12/words.txt", "r")
some_lines = some_file.readlines()


for word in some_lines:
    ran = randint(0, len(some_lines) - 1)
    ind = some_lines[ran]
<<<<<<< HEAD
    print(ind)
=======
    print(ind)
    
>>>>>>> b15db88cc9605244b2ea1024a1756c9d86a1d18f
