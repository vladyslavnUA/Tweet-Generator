# import sys
# from random import random, randint

# # if __name__ == '__main__':
# #     args = sys.argv

# some_file = open("/usr/share/dict/words", "r")
# some_lines = some_file.readlines()

# for word in some_lines:
#     ran = randint(0, len(some_lines) - 1)
#     ind = some_lines[ran]
#     # ind.append(ran)
#     print(" ".join(ind[0:-1] for word in some_lines))
#     some_file.close()

import sys
from random import random, randint

some_file = open("/Users/vladyslav/Desktop/cs12/words.txt", "r")
some_lines = some_file.readlines()


for word in some_lines:
    ran = randint(0, len(some_lines) - 1)
    ind = some_lines[ran]
    print(ind)
    # print(" ".join(ind[0:-1] for word in some_lines))
    # some_file.close()


# if __name__ == '__main__':
#     print(ran_words(ran))