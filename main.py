import uvicorn
from fastapi import FastAPI
import pickle
import numpy as np
import pandas as pd

app= FastAPI()

pickle_file_open = open("heart_predict.pkl","rb")
lg = pickle.load(pickle_file_open)

from pydantic import BaseModel
class request_body(BaseModel):
    male : float
    age : float
    education : float
    currentSmoker : float
    cigsPerDay : float
    BPMeds : float
    prevalentStroke : float
    prevalentHyp : float
    diabetes : float
    totChol : float
    sysBP : float
    diaBP : float
    BMI : float
    heartRate : float
    glucose : float

@app.get('/')
def base_route():
    return {'message':"Welcome to Heart Disease Prediction"}

@app.post('/predict')
def predict(data : request_body):
    test_data = [[data.male,
    data.age, 
    data.education, 
    data.currentSmoker,
    data.cigsPerDay,
    data.BPMeds,
    data.prevalentStroke, 
    data.prevalentHyp,
    data.diabetes,
    data.totChol, 
    data.sysBP,
    data.diaBP,
    data.BMI,
    data.heartRate,
    data.glucose
    ]]

    result = lg.predict(test_data)
    return { 'class' :int(result)}



if __name__=="__main__":
    uvicorn.run(app,host="127.1.2.3",port=5000)
    