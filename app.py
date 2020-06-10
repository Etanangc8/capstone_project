import numpy as np
import pickle
from flask import Flask, Response, request, jsonify, render_template

app = Flask('my_app')

@app.route('/')
def home():
    return render_template('form.html')
 
@app.route('/submit')
def submit():
    #load in form data from incoming request
    user_submission = request.args
    #manipulate data into a format that we pass to our model
    X_test = np.array([
        int(user_submission['review_overall']),
        int(user_submission['review_aroma']),
        int(user_submission['review_appearance']),
        int(user_submission['review_palate']),
        int(user_submission['review_taste'])
    ]).reshape(1, -1) #turns [1,2,3,4,5] into [[1,2,3,4,5]]

    model = pickle.load(open('assets/model.p', 'rb'))

    pred = model.predict(X_test )[0]
    return render_template('results.html', prediction=pred)




if __name__ == '__main__': 
    app.run(debug=True)