import random
import sys

some_file = "words.txt"
some_lines = open(some_file, "r")

histoogram = {}
def histogram():
    for word in some_lines:
        word = word.rstrip()
    
        if word in histoogram:
            histoogram[word] += 1
        else:
            histoogram[word] = 1

    print(histoogram)

def unique_words():
    count = 0
    if word in histoogram:
        #check if word is unique, only seen once
        if histoogram[word] == 1:
            count += 1
    return(count)

def frequency():
    for word in histoogram:
        print(f'the word {word} is repeated {histoogram[word]} times.')

if __name__ == '__main__':
    print(histogram())
    print(frequency())
