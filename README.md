# Autotab Webpage 
is a Heroku Web App Interface that allows the user to upload .wav Files and get back Tablature as "heard" from a trained Convolutional Neural Network. 

From the app the user queries to load/store .wav files are send to the google storage bucket and a server hosted on google cloud run.   

If you'd like to replicate this Web Interface App on your machine, all there is to do is: 

1. ```Clone or Fork this repo```
2. ```run pip install -e . ``` 
3. ```treamlit run streamlit_app/autotab-app.py```

