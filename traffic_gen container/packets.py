from   flask import Flask
from   flask import request
import json
import pandas as pd
import requests
import time 

flag = 0
def sendpackets():
	global flag
	df = pd.read_csv("testdata.csv")
	df2 = df[1:2]
	jsonfiles = df2.to_json(orient='records')

	for i in range(len(df.index)):
		r= requests.post("http://192.168.99.100:1000/ips",data=jsonfiles) #replace your ip here 
		print(r.text)
		df2 = df[i:i+1]
		jsonfiles = df2.to_json(orient='records')
		#time.sleep(5)
		if flag==1:
			return


app = Flask(__name__)

@app.route("/")
def hello():
    return "KNOW YOUR ENEMY"

@app.route("/start_traffic", methods =['GET'])
def packet():
	global flag 
	flag = 0
	sendpackets()
	return "DONE"

@app.route("/stop_traffic", methods =['GET'])
def stop():
	global flag
	flag=1
	return "STOPPED"
app.run(host='0.0.0.0',port=2000)