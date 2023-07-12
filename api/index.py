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
                  + "eyJraWQiOiIyMDIzMDcxMDA4MzMiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02NjQwMDRVOFEyIiwiaWQiOiJJQk1pZC02NjQwMDRVOFEyIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiNjRiNDdlNjYtOGUyMy00ZDdjLTg2N2MtNWVlZjI2OGRhOTgyIiwiaWRlbnRpZmllciI6IjY2NDAwNFU4UTIiLCJnaXZlbl9uYW1lIjoiUmF5aGFuZCBGZXJuYW5kYSIsImZhbWlseV9uYW1lIjoiVmlhbnRhbWEiLCJuYW1lIjoiUmF5aGFuZCBGZXJuYW5kYSBWaWFudGFtYSIsImVtYWlsIjoiMTExMjAyMDEyNDM5QG1ocy5kaW51cy5hYy5pZCIsInN1YiI6IjExMTIwMjAxMjQzOUBtaHMuZGludXMuYWMuaWQiLCJhdXRobiI6eyJzdWIiOiIxMTEyMDIwMTI0MzlAbWhzLmRpbnVzLmFjLmlkIiwiaWFtX2lkIjoiSUJNaWQtNjY0MDA0VThRMiIsIm5hbWUiOiJSYXloYW5kIEZlcm5hbmRhIFZpYW50YW1hIiwiZ2l2ZW5fbmFtZSI6IlJheWhhbmQgRmVybmFuZGEiLCJmYW1pbHlfbmFtZSI6IlZpYW50YW1hIiwiZW1haWwiOiIxMTEyMDIwMTI0MzlAbWhzLmRpbnVzLmFjLmlkIn0sImFjY291bnQiOnsidmFsaWQiOnRydWUsImJzcyI6ImVlYWRjOGZhNGY5MTRmZTBiMzkxOTNhOWU3MTY4NmZlIiwiaW1zX3VzZXJfaWQiOiIxMDgyNDc3NyIsImZyb3plbiI6dHJ1ZSwiaW1zIjoiMjYzNDIzNSJ9LCJpYXQiOjE2ODkyMDQxMDEsImV4cCI6MTY4OTIwNzcwMSwiaXNzIjoiaHR0cHM6Ly9pYW0uY2xvdWQuaWJtLmNvbS9vaWRjL3Rva2VuIiwiZ3JhbnRfdHlwZSI6InVybjppYm06cGFyYW1zOm9hdXRoOmdyYW50LXR5cGU6YXBpa2V5Iiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiZGVmYXVsdCIsImFjciI6MywiYW1yIjpbInRvdHAiLCJtZmEiLCJvdHAiLCJwd2QiXX0.YuIReuo93gHHlRrHslBvJF11F5SwRvJ6qrDnZK5qWuozpy438THvW1STYUYCIocM641EE1tTJTEo31ZluTXe_UIz8paRKPfZ3r5e_0Kyef4pQ9Kc83-YEHE1o7IeKea0EZTcRYPxCXnHu0iDezlBslbiNitDJ4hefKnfORw6KigubOWwPcRz_8AWLSlVb-1kS2QUPp83y9kPbQpeLeMnjRaoiB74sxaNwzOWPgGhkK5pped5dR1NP_Tx4Wpg7wjwlYFE_Ejvj2OVNiQ0F1XqYTQKFAphufNoc8tJvtLv7VE3yRqjhhB-W7kAWl1eE9px171uEfjLt4g8KPFOAuxW3Q"}

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
