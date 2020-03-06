from __future__ import division, print_function  # Python 2 and 3 compatibility
from random import randint
import re

class Listogram(list):
    def __init__(self, word_list=None):
        """Listogram is a histogram implemented as a subclass of the list type."""
        super(Dictogram, self).__init__() #creating new list
    
        self.types = 0 # unique words
        self.tokens = 0 # all words
        if word_list != None:
            for word in word_list: # loop
                self.add_count(word) # add word


    def add_count(self, word, count=1):
        # active defines whether word is active in list
        active = False
        for index in range(len(self)):
            if self[index][0] == word: # if it's the word
                self[index][1] += count # increase the frequency count or else
                active = True
                
                break
        if ! active: # if not in list, append it
            self.append([word, count])
            self.types += 1
        self.tokens += count # add count to all words


    def frequency(self, word):
        """ returns frequency of given word, or 0 """
        for index in range(len(self)):
            if self[index][0] == word: # if it's the word
                self[index][1] += count 

    
    def sample(self):
        """ return random word from sample """
        tokens = 0
        sum_of_all = sum(self.values()) # sum of all words to randomize
        get_random_number = randint(0, sum_of_all - 1) # random number

        for something in self.items():
            if get_random_number == 0: # if no word picked, return [word]
                return something[0]
            elif get_random_number > 0: # if int over 0
                get_random_number -= something[1]
            elif get_random_number <= 0: # if int below 0, return [word]
                return something[0]

def print_histogram(word_list):
    print("")
    print("~~~~~~~~~~~~~~")
    print('  Histogram:')
    print("~~~~~~~~~~~~~~")
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]: #loop from the last 2 word from list
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_histogram_samples(histogram)

def print_histogram_samples(histogram): #MARK: Find out why the word is always NONE
    print('Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [histogram.sample() for _ in range(10000)]
    samples_hist = Dictogram(samples_list)
    print('samples: {}'.format(samples_hist))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in histogram.items():
        # Calculate word's observed frequency
        observed_freq = count / histogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
            + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
            + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
            + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()