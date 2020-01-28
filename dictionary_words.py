import sys
from random import random, randint

if __name__ == '__main__':
    args = sys.argv

some_file = open("/usr/share/dict/words", "r")

some_lines = some_file.readlines()

ran = randint(0, len(some_lines) - 1)
ind = some_lines[ran]
print(ind)

def ran_words(ran):
    words = []
    for i in range(ran):
        # number = int(sys.argv[1])


if __name__ == '__main__':
    print(ran_words(ran))
