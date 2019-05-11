from   flask import Flask
from   flask import request
import json
import pandas as pd
import requests
import time 


app = Flask(__name__)

@app.route("/")
def hello():
    return "KNOW YOUR ENEMY"

@app.route("/ips", methods =['POST'])
def receive():
    d = request.data
    print(d)
    return "Sucess"



app.run(host='0.0.0.0',port=80)