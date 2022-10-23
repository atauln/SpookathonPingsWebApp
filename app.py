import os
from flask import Flask, render_template, session, request, redirect
from dotenv import load_dotenv
import requests

app = Flask(__name__)
load_dotenv()
app.secret_key = os.urandom(16)


@app.route("/")
def root():
    return render_template('index.html', session=session)

@app.route("/", methods=['POST'])
def root_change():
    session['name'] = request.form['text']
    return render_template('index.html', session=session)

# args: message, name_of_sender
@app.route("/discord")
def discord():
    print (request.args)
    payload = {
        "content": request.args.get('message'),
        "username": request.args.get('username')
    }
    
    print (requests.post(os.getenv("WEBHOOK_URL"), json=payload))
    return redirect('/')

@app.route("/slack")
def slack():
    payload = {
        "text": request.args.get("message")
    }
    print (payload)
    print (requests.post(os.getenv("SLACK_WH_URL"), json=payload))
    return redirect('/')

