
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    gender : int
    age : int
    hypertension : int
    heart_disease : int
    bmi : float
    HbA1c_level : float
    blood_glucose_level : int
    smoking_history_No_Info : int
    smoking_history_current : int
    smoking_history_ever : int
    smoking_history_former : int
    smoking_history_never : int
    smoking_history_not_current : int
    
    
#loading the saved trained model

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

#creating the api

app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input) : 
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    gen = input_dictionary('gender')
    Age = input_dictionary('age')
    hyperTen= input_dictionary('hypertension')
    Heart_disease = input_dictionary('heart_disease')
    BMI = input_dictionary('bmi')
    HbA1c = input_dictionary('HbA1c_level')
    glucose = input_dictionary('blood_glucose_level')
    smoking_No_Info = input_dictionary('smoking_history_No_Info')
    smoking_current = input_dictionary('smoking_history_current')
    smoking_ever = input_dictionary('smoking_history_ever')
    smoking_former = input_dictionary('smoking_history_former')
    smoking_never = input_dictionary('smoking_history_never')
    smoking_not_current = input_dictionary('smoking_history_not_current')
    
    input_list = [gen, Age, hyperTen, Heart_disease, BMI, HbA1c, glucose, smoking_No_Info, smoking_current, smoking_ever, smoking_former, smoking_never, smoking_not_current]

    
    
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0: 
        return 'the person is not diabetic'
    else:
        return ' the person is diabetic'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    