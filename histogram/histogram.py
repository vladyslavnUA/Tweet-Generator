# from flask import Flask, render_template, request, redirect, url_for
# import random
# from random import randint
# import os
# import sys
# import dictionary_words


# app = Flask(__name__)

# @app.route("/")
# def index():
# 	return render_template("home.html")

# some_file = "words.txt"
# some_lines = open(some_file, "r")

# histoogram = {"one": 2,
#             "fish": 4, "red": 2, "blue": 2
#             }
class Histogram():

    def __init__(self, data):
        pass

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
    histo_result = histogram()
    print("Histogram: ")
    print(histo_result)

    unique_result = unique_words(histo_result)
    print("Unique words: ", unique_result)

    word="Americano"

    frequency_of_word = frequency(word, histo_result)

    print("the word " + word + "appeared " + str(frequency_of_word), "times")
# 	app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

    # print(histogram(histoogram))
    # print(unique_words())
    # print(frequency())