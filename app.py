import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/lifts')
def lifts():
    return render_template('lifts.html')

@app.route('/races')
def races():
    return render_template('races.html')

@app.route('/sliceoflife')
def sliceoflife():
    return render_template('sliceoflife.html')

if __name__ == '__main__':
   app.run()
