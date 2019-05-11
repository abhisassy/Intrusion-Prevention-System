import pandas as pd
import numpy as np
from   sklearn.model_selection import train_test_split
from   sklearn.ensemble        import RandomForestClassifier
from   sklearn import metrics
from   sklearn import preprocessing
def encode(df,features):
    for i in features:
        print(i)
        le.fit(df[i].astype(str))
        df[i]=le.transform(df[i])


anom=pd.read_csv("anom.csv")
anom=anom.dropna()
le=preprocessing.LabelEncoder()
features=['method','protocol','pragma','connection','accept','contentType','cacheControl','payload']
encode(anom,features)

anomx=anom[['method','protocol','pragma', 'connection','accept','contentLength','contentType','cacheControl','payload']]
le.fit(anom['label'])
anomy=le.transform(anom['label'])

aX_train, aX_test, ay_train, ay_test = train_test_split(anomx, anomy, test_size=0.3)
#print(ay_test)
#print(aX_test)

aclf=RandomForestClassifier(n_estimators=100)
aclf.fit(aX_train,ay_train)

################################################################################333

from   flask import Flask
from   flask import request
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "KNOW YOUR ENEMY"

@app.route("/ips", methods =['POST'])
def predict():
	d = request.data
	data = d.decode()
	data =json.loads(data)[0]
	print (data)
	data = json.dumps(data)
	data = json.loads(data)
	print (data)

	print(type(data))
	
	df = pd.io.json.json_normalize(data)
	#print (request.data)
	res = aclf.predict(df)
	#res=0
	if res == 1:
		requests.post("http://192.168.99.100/ips",data=d)
		return "accepted"
	
	return "dropped"

app.run(host='0.0.0.0',port=1000)




