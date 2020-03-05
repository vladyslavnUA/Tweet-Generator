from flask import Flask, render_template, request, redirect, url_for
import os
import random 
from histogram.histogram import Histogram
from histogram.sample import sample, words_list
from histogram.dictogram import Dictogram


app = Flask(__name__)


def get_sentence_from_histogram(count=50):
    dictonary_words = Histogram.histogram()
    sentence = ''
    navBar_message = ''

    while count > 0:
        sentence += sample(dictonary_words)+" "
        if count < 10:
            navBar_message += sample(dictonary_words)+" "

        count -= 1
    return [sentence, navBar_message]



def build_markov(word_list):
        markov_chain = {}

        for i in range(len(word_list) - 1):
            #get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i+1]

            if current_word in markov_chain.keys(): #already there
                #get the histogram for that word in the chain
                histogram = markov_chain[current_word]
                #add to count
                histogram[next_word] = histogram.get(next_word, 0) + 1
            else: #first entry
                markov_chain[current_word] = Dictogram([next_word]) 

        return markov_chain

def walk(num_words, markov_chain, first_word):
        #TODO: generate a sentence num_words long using the markov chain
        sentence = ''
        word = first_word
        
        # for i in range(0, num_words):
        for i in range(num_words):

            histogram = markov_chain[word]
            next_word = sample(histogram)
            sentence += next_word+" "
            word = next_word
        
        return sentence


def markov(num=0):

    list_of_words = words_list()
    # print(list_of_words)
    first_word = random.choice(list_of_words)
    
    chain = build_markov(list_of_words)
    if num == 0:
        num = 10
    sentence = walk(num, chain, first_word)

    return sentence


# helper function to get number 
def check_number(num):
    try:
        count = int(num)
        return count
    except ValueError as verr:
        print("Invalid number enter a number")
        return False
    except Exception as ex:
        print(ex)
        return False



# home page markov default 10 words
@app.route('/markov')
@app.route('/')
def home_route():
    tweet = markov()
    navBar_message = markov()
    return render_template('index.html', tweet=tweet, navBar_message=navBar_message)

# markov get n words
@app.route('/markov/<num>')
@app.route('/<num>')
def dict_home_route(num):
    count = check_number(num)
    tweet = markov(count)
    navBar_message = markov(10)
    return render_template('index.html', tweet=tweet, navBar_message=navBar_message)


# dictogram default 10 words
@app.route('/dictogram')
def dict_limit_words_route():
    tweet = get_sentence_from_histogram(10)
    navBar_message = get_sentence_from_histogram(random.randint(0, 10))
    return render_template('index.html', tweet=tweet[0], navBar_message=navBar_message)


# get n of words in a tweets 
@app.route('/dictogram/<num>')
def limit_words_route(num):
    count = check_number(num)
    tweet = get_sentence_from_histogram(count)
    return render_template('index.html', tweet=tweet[0], navBar_message=tweet[1])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))