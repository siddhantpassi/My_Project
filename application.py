from flask import Flask, request,render_template
import pandas as pd
import numpy as np

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

from sklearn.preprocessing import StandardScaler

application = Flask(__name__)

app = application

#Route for home page

@app.route('/')
def index():
    #return render_template("test2.html")
    return render_template("index.html")


@app.route('/predictdata', methods = ['GET', 'POST'])
def predict_datapoint():
    if request.method =='GET':
        return render_template('home.html') #home.html will be the simple data input page for now
    else:
        data = CustomData(
            danceability = request.form.get('danceability'),
            energy = request.form.get('energy'),
            key = request.form.get('key'),
            mode = request.form.get('mode'),
            time_signature = request.form.get('time_signature'),
            speechiness = request.form.get('speechiness'),
            acousticness = request.form.get('acousticness'),
            instrumentalness = request.form.get('instrumentalness'),
            liveness = request.form.get('liveness'),
            valence = request.form.get('valence'),
            tempo = request.form.get('tempo'),
            duration_ms = request.form.get('duration_ms'),
            chorus_hit = request.form.get('chorus_hit'),
            sections = request.form.get('sections'),
            loudness = request.form.get('loudness')
        )

        prediction_df = data.get_data_as_data_frame()
        print(prediction_df)
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(prediction_df)

        return render_template('home.html', results = results[0])
    

if __name__ =="__main__":
    app.run(host='0.0.0.0')
    #app.run(host='0.0.0.0', port=5000, debug=True)

    


