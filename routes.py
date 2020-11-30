from app import app
from flask import render_template, request, send_file
from app.models.model import getDadJoke
from gtts import gTTS
import os 

@app.route('/')
@app.route('/index')
def index():
        return render_template('index.html')
    
    
@app.route('/dadjoke', methods=['GET','POST'])
def dadjoke():
    if request.method == 'GET':
        return "Please use the form."
    else:
        userdata=request.form
        print(userdata)
        joke=getDadJoke(userdata['search'])
        language = 'en'
        myobj = gTTS(text=joke, lang=language, slow=False) 
        myobj.save("app/static/output.mp3") 
        return render_template('dadjoke.html',joke=joke)

