<h1>About this Project</h1>

Predict Ferrari's Lowest price of the day with no proven accuracy🙂🥲!

## Disclaimer:

Further Research are Necessary:v

Do it on Your Own Risk!

<h2>Datasets</h2>
Here, are the datasets that are collected from yahoo finance taken within the last 5 years (7 July 2018 - 3 July 2023).

Mercedes
https://finance.yahoo.com/quote/MBG.DE/history?period1=1530835200&period2=1688601600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true

Honda
https://finance.yahoo.com/quote/HMC/history?period1=1530835200&period2=1688601600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true

Ferrari
https://finance.yahoo.com/quote/RACE/history?period1=1530835200&period2=1688601600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true

Renault
https://finance.yahoo.com/quote/RNO.PA/history?period1=1530835200&period2=1688601600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true


<h1>How to use this project locally</h1>

git clone https://github.com/Rayhand117/CapstoneHosting

### open web-app directory, then open vs code or any text editor, on terminal install flask:

### go to api directory

cd api

python3 -m pip install flask flask-wtf urllib3 requests

### rename index.py to app.py

### before running the project, make sure to replace the token by generating a new one, because the token is valid for 1 hour only. (run this command on terminal, then copy paste on app.py:

curl -X POST 'https://iam.cloud.ibm.com/oidc/token' -H 'Content-Type: application/x-www-form-urlencoded' -d 'grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=bzwtYyFZaRPc5f-pOsJ0dd0Jo_RgU1cjbRF7Nyz_dAu4'

### change line 2 on app.py:

from .forms import PredictForm

### to (delete the dot (.) on from .forms

### so it'll look like this:

from forms import PredictForm

### finally, to run the project:
python3 -m flask run

### then copy paste the localhost server url on your web, usually look like this:
http://127.0.0.1:5000

### You can stop the localhost by pressing Ctrl + C on the current active server.

# See more:

https://github.com/IBM/predict-insurance-charges-with-autoai


<h1>Capstone Project</h1>

1. Project Related to AI or Cyber
- AI

2. Project Name
- Prediksi Harga Saham Ferrari

3. Pattern yang diambil
- Create a machine learning web app to predict your insurance premium cost

https://github.com/IBM/predict-insurance-charges-with-autoai

4. Used Features
- Cloud Object Storage
- Watson Assistant
- Watson Machine Learning
- Watson Studio

5. Code yang di upload di Github di tampilkan
- https://github.com/Rayhand117/CapstoneHosting

6. Result dari Project yang dibuat
- https://capstoneferraristock-rayhand117.vercel.app/
