from flask import Flask, url_for, render_template, redirect
from .forms import PredictForm
from flask import request, sessions
import requests
from flask import json
from flask import jsonify
from flask import Request
from flask import Response
import urllib3
import json
# from flask_wtf import FlaskForm

app = Flask(__name__, instance_relative_config=False)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'development key'  # you will need a secret key

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


@app.route('/', methods=('GET', 'POST'))
def startApp():
    form = PredictForm()
    return render_template('index.html', form=form)


@app.route('/predict', methods=('GET', 'POST'))
def predict():
    form = PredictForm()
    if form.submit():

        # NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer '
                  + "eyJraWQiOiIyMDIzMDYxMDA4MzIiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02NjQwMDRVOFEyIiwiaWQiOiJJQk1pZC02NjQwMDRVOFEyIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiNTJkMWRjMDEtYTdlNy00NjRkLTkwOWQtNzEwNDc2NmEwMGY5IiwiaWRlbnRpZmllciI6IjY2NDAwNFU4UTIiLCJnaXZlbl9uYW1lIjoiUmF5aGFuZCBGZXJuYW5kYSIsImZhbWlseV9uYW1lIjoiVmlhbnRhbWEiLCJuYW1lIjoiUmF5aGFuZCBGZXJuYW5kYSBWaWFudGFtYSIsImVtYWlsIjoiMTExMjAyMDEyNDM5QG1ocy5kaW51cy5hYy5pZCIsInN1YiI6IjExMTIwMjAxMjQzOUBtaHMuZGludXMuYWMuaWQiLCJhdXRobiI6eyJzdWIiOiIxMTEyMDIwMTI0MzlAbWhzLmRpbnVzLmFjLmlkIiwiaWFtX2lkIjoiSUJNaWQtNjY0MDA0VThRMiIsIm5hbWUiOiJSYXloYW5kIEZlcm5hbmRhIFZpYW50YW1hIiwiZ2l2ZW5fbmFtZSI6IlJheWhhbmQgRmVybmFuZGEiLCJmYW1pbHlfbmFtZSI6IlZpYW50YW1hIiwiZW1haWwiOiIxMTEyMDIwMTI0MzlAbWhzLmRpbnVzLmFjLmlkIn0sImFjY291bnQiOnsidmFsaWQiOnRydWUsImJzcyI6ImVlYWRjOGZhNGY5MTRmZTBiMzkxOTNhOWU3MTY4NmZlIiwiaW1zX3VzZXJfaWQiOiIxMDgyNDc3NyIsImZyb3plbiI6dHJ1ZSwiaW1zIjoiMjYzNDIzNSJ9LCJpYXQiOjE2ODg4OTk1ODAsImV4cCI6MTY4ODkwMzE4MCwiaXNzIjoiaHR0cHM6Ly9pYW0uY2xvdWQuaWJtLmNvbS9vaWRjL3Rva2VuIiwiZ3JhbnRfdHlwZSI6InVybjppYm06cGFyYW1zOm9hdXRoOmdyYW50LXR5cGU6YXBpa2V5Iiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiZGVmYXVsdCIsImFjciI6MywiYW1yIjpbInRvdHAiLCJtZmEiLCJvdHAiLCJwd2QiXX0.OI0NTYJ6hRG20qKSAFmj-DUmdUKqR1u5lEKvSrPab9jGvvXd5Mb8IuCw6P8M4iKUwKeeNcXU5W5dLpLiZxNitPOZ7yZwT5TY84Xq9O4KoWfsZAOimjQbdrMxlp1jHX0xBuT1RnOHGd8Bg1q70gShV5FcdtBbgIQMN9cI8TIPYZa4bbDLiWAwn55XaTP2T_qNioj9fA-QgD3o3skLi0YZGp3jw5LO37eMdpSA9On4BZQRr-lDn89LgGscQXTtQaPFzPbxmR0PZFxJshAT0UFAr7v8nO4pQE_r-IEzjxA56z3-EghClHFOYl3TwYfU0waCi1rd6i0Hz4JKJH1TtVS6NA"}

        if (form.High.data == None):
            python_object = []
        else:
            python_object = [str(form.Date.data), float(form.High.data), float(form.Low.data), float(
                form.Close.data), float(form.AdjClose.data), int(form.Volume.data)]
        # Transform python objects to Json

        userInput = []
        userInput.append(python_object)

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields": ["Date", "High", "Low", "Close", "Adj Close", "Volume"],
                                           "values": userInput}]}
        print(payload_scoring)

        response_scoring = requests.post(
            "https://us-south.ml.cloud.ibm.com/ml/v4/deployments/287a9126-abb9-487f-b905-6fd6bc5c00bb/predictions?version=2021-05-01", json=payload_scoring, headers=header)

        output = json.loads(response_scoring.text)
        ab = None
        print(output)
        for key in output:
            ab = output[key]

        for key in ab[0]:
            bc = ab[0][key]

        roundedCharge = round(bc[0][0], 2)

        form.abc = roundedCharge  # this returns the response back to the front page
        return render_template('index.html', form=form)
