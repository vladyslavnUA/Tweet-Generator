# frequency()
# freq of all words in histogram
# get randint
# loop through histogram
# check if randint = frequency

from random import randint

def histogram(lines):
    histogram = {}
    for line in lines:
        words = line.rstrip('\n').split()
        for word in words:
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1

    return histogram


def sample(histogram):
    tokens = 0
    for k,v in histogram.items():
        tokens += v

    dart = randint(1, tokens)

    fence = 0

    for word,count in histogram.items():
        fence += count
        if fence >= dart:
            return word

def words_list():
    filename = './text/adventure_holmes.txt'
    file = open(filename, 'r')
    lines = file.readlines()

    words_list = []

    for line in lines:
        words = line.rstrip('\n').split()
        for word in words:
            words_list.append(word)
    
    
    return words_list

if __name__ == "__main__":
    file = open('onefix.txt', 'r')
    lines = file.readlines()

    histogram_result = histogram(lines)
    print(histogram_result)
    print(sample(histogram_result))
    # print(sample(histogram_result))