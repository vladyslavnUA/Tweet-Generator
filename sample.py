import random
from histogram import open_this_file, histogram, frequency


def words_in_total(histogram):
    total = 0
    for value in histogram.values():
        total += value
    return total

    # total number of words in the file(values)


histogram = (histogram(open_this_file('words.txt')))

words_in_total = words_in_total(histogram)
# print(words_in_total)

# special function
def chaotic(dict, words_in_total):
    random_number = random.randint(1, words_in_total)
    total_value = 0
    for word, value in dict.items():
        if random_number - value - total_value <= 0:
            return word
        else:
            total_value += value