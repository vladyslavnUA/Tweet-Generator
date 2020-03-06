import sys


# open text file
def open_this_file(text):
    some_file = open(text, "r")
    file_content = []

    for line in some_file:
        # split creates another list, if you use append, you will create a list of lists; but with extend you create just 1
        file_content.extend(line.split())
    return file_content


def histogram(file_content):
    """ take a filename or content_file as
     a string and return histogram data
     that stores words with the number of times the word appears"""
    histogram = {}
    for word in file_content:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


def unique_words(histogram):
    """returns the total count of unique words"""
    unique_words = 0
    for value in histogram.values():
        if value == 1:
            unique_words += 1
    return unique_words


def frequency(word, histogram):
    """returns the number of times that word appears in the  text"""
    for key, value in histogram.items():
        if key == word:
            return value


if __name__ == "__main__":
    some_words = open_file("words.txt")
    print(histogram(words))