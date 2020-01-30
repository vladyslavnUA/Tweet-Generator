import random
import sys

# filen = open("/Users/vladyslav/Desktop/cs12/somewords.txt", "r")
# some_lines = filen.readlines()

# histoogram = {}

# def histogram():
#     for any_word in some_lines:
#         any_word = any_word.rstrip()
#         histoogram[any_wordouch ] = histoogram.get(word, 0) + 1
#     return histoogram
# def unique_words():
#     c = 0
#     for any_word in histoogram:
#         print(int(i))

some_file = "words.txt"
some_lines = open(some_file, "r")

histoogram = {}

for word in some_lines:
  word = word.rstrip()
  
  if word in histoogram:
    histoogram[word] += 1
  else:
    histoogram[word] = 1

print(histoogram)