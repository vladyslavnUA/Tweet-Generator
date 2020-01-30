import random
import sys

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
