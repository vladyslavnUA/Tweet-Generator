from flask import Flask, render_template, request, url_for
import random
from histogram import open_this_file, histogram, frequency
from sample import chaotic, words_in_total
from markov_chain_order import Markov

app = Flask(__name__)

text_title = "'the standard lorem ipsum passage, used since the 1500s'"
file_content = open_this_file("words.txt")
markov_chain = Markov(file_content, 2)


@app.route('/')
def index():

    num = request.args.get('length')

    if num:
        sentence = markov_chain.get_sentence(int(num))
        return render_template("base.html", word=sentence, title=text_title)
    else:
        sentence = markov_chain.get_sentence(10)
        return render_template("base.html", word=sentence, title=text_title)


if __name__ == '__main__':
    app.run(debug=True)
