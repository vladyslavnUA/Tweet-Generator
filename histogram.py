import random
from random import randint
import sys
import dictionary_words

some_file = "words.txt"
some_lines = open(some_file, "r")

histoogram = {"one": 2,
            "fish": 4, "red": 2, "blue": 2
        }

def histogram(histoogram):
    for word in some_lines:
        word = word.rstrip()
    
        if word in histoogram:
            histoogram[word] += 1
        else:
            histoogram[word] = 1
    random_index = randint(0, len(histoogram)-2)
    print(histoogram, random_index)

def unique_words():
    count = 0
    for word in histoogram:
        #check if word is unique, only seen once
        if histoogram[word] == 1:
            count += 1
        else:
            return('error')
    return(count)

def frequency():
    for word in histoogram:
        print(f'the word {word} is repeated {histoogram[word]} times.')

# word_list = histoogram.sorted()
# for word in word_list:
#     value = word_list[word]
#     print(value)



if __name__ == '__main__':
    print(histogram(histoogram))
    print(unique_words())
    print(frequency())
