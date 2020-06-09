# imports
import numpy as np
import pickle
from flask import Flask, Response, request, jsonify, render_template

app = Flask('myApp')

@app.route('/')

#home page
def home():
    return 'Beer Recommender!'
#route page 2
@app.route('/hc_page')
def hc_page():
    return '<html><body><h1>This is a hard coded page!</h1><p>Here is some hard-coded content. Isn\'t it pretty?</p></body></html>'



if __name__ == '__main__': #if user runs 'app.py' in terminal
    app.run(debug=True) 
    