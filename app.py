#Code modified from Riley's Lecture

import numpy as np
import pandas as pd
from flask import Flask, Response, request, jsonify, render_template

#read in data
data = pd.read_csv('./data/km_data.csv')
recommender = pd.read_csv('./data/recommender.csv', index_col=0)


app = Flask('my_app')

@app.route('/')
def home():
    return render_template('form.html')
 
@app.route('/submit')
def submit():
    user_submission = request.args['beer_style']
    beers = recommender[recommender.index.str.contains(user_submission)].index
    beer_dic = {}
    for beer in beers:
        beer_dic[beer] = list(recommender[beer].sort_values()[1:6].index)


    return render_template('results.html', beer_dic = beer_dic)



if __name__ == '__main__': 
    app.run(debug=True)