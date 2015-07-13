from flask import Flask
from flask import render_template

from wordsalad import random_words

app = Flask(__name__)

@app.route("/")
def homepage():

    filepath = './dictionaries/'
    sample_words = random_words(filepath, 40)

    paragraph = ' '.join(sample_words).decode('utf-8')
    return render_template(
                            "main.html",
                            paragraph = paragraph
                            )


if __name__ == "__main__":
    app.debug = True
    app.run()