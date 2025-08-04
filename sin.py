import numpy as np
import pickle
import joblib
import matplotlib
import matplotlib.pyplot as ply
import time
import pandas
import os
from flask import flask,request,jsonify,render_template


app =flask()
modle= pickle.load(open())
scale= pickle.load(())
@app.route('/')
def home():
    return render_template('')
@app.route('/predict',method=["POST","GET"])
def predict();

input_feature=[float(x)for x in request.form.values()]
features_vlues=[np.arry(input_feature)]
names = [['holiday','temp','rain','snow','weather','year','month','day','hours','minute','seconds']]
data=pandas.dataframe(features_vlues,columns=names)
data =scale.fit_transform(data)
data=pandas.data frame(data,colums = names)
prediction=modle.predicty(data)
print(prediction)
text ="Estimatead traffic volume is:"
return render_template("index.html",prediction_text=test+str(prediction))
if -name--=="sandeep":
    port=int(os.environ.get('port,5000'))
    app.run(port=port,debug=true,use_reloder=flase)