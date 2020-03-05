# frequency()
# freq of all words in histogram
# get randint
# loop through histogram
# check if randint = frequency

from random import randint

def histogram(some_lines):
    histogram = {}
    for some_line in some_lines:
        words = line.rstrip('\n').split()
        for some_word in words:
            if some_word in histogram:
                histogram[some_word] += 1
            else:
                histogram[some_word] = 1

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
    filename = './histogram/words.txt'
    file = open(filename, 'r')
    lines = file.readlines()

    words_list = []

    for line in lines:
        words = line.rstrip('\n').split()
        for word in words:
            words_list.append(word)
    
    
    return words_list

if __name__ == "__main__":
    histo_result = histogram(lines)
    print(histo_result)
    print(sample(histo_result))
    # print(sample(histogram_result))