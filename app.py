#Code modified from Riley's Lecture

import numpy as np
import pandas as pd
import beer_rec
from flask import Flask, Response, request, jsonify, render_template

#read in data
data = pd.read_csv('./data/km_data.csv')

app = Flask('my_app')

@app.route('/')
def home():
    return render_template('form.html')
 
@app.route('/submit')
def submit():
    user_submission = request.args
    response = str(user_submission['beer_style'])
    rec = data.recommender(response)
    #data.track_output(response, rec)
    #html output on page
    return render_template('results.html', pred1=rec[0], pred2=rec[1], pred3=rec[2], pred4=rec[3], pred5=rec[4])

    
    
    # #load in form data from incoming request
    # user_submission = request.args
    # #manipulate data into a format that we pass to our model
    # X_test = np.array([
    #     int(user_submission['review_overall']),
    #     int(user_submission['review_aroma']),
    #     int(user_submission['review_appearance']),
    #     int(user_submission['review_palate']),
    #     int(user_submission['review_taste'])
    # ]).reshape(1, -1) #turns [1,2,3,4,5] into [[1,2,3,4,5]]

    # model = pickle.load(open('assets/model.p', 'rb'))
    # pred = model.predict(X_test )[0]
    #return render_template('results.html', prediction=pred)




if __name__ == '__main__': 
    app.run(debug=True)