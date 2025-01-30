from flask import Flask, render_template, request, redirect, url_for
import os
import numpy as np
import pandas as pd
import pickle 

#loading model
ModelJan = pickle.load(open('TrainedModels/ModelJan.pkl','rb'))
ModelFeb = pickle.load(open('TrainedModels/ModelFeb.pkl','rb'))
ModelMar = pickle.load(open('TrainedModels/ModelMar.pkl','rb'))
ModelApr = pickle.load(open('TrainedModels/ModelApr.pkl','rb'))
ModelMay = pickle.load(open('TrainedModels/ModelMay.pkl','rb'))
ModelJun = pickle.load(open('TrainedModels/ModelJun.pkl','rb'))
ModelJul = pickle.load(open('TrainedModels/ModelJul.pkl','rb'))
ModelAug = pickle.load(open('TrainedModels/ModelAug.pkl','rb'))
ModelSep = pickle.load(open('TrainedModels/ModelSep.pkl','rb'))
ModelOct = pickle.load(open('TrainedModels/ModelOct.pkl','rb'))
ModelNov = pickle.load(open('TrainedModels/ModelNov.pkl','rb'))
ModelDec = pickle.load(open('TrainedModels/ModelDec.pkl','rb'))

dict = {
    'JAN' : ModelJan,
    'FEB' : ModelFeb,
    'MAR' : ModelMar,
    'APR' : ModelApr,
    'MAY' : ModelMay,
    'JUN' : ModelJun,
    'JUL' : ModelJul,
    'AUG' : ModelAug,
    'SEP' : ModelSep,
    'OCT' : ModelOct,
    'NOV' : ModelNov,
    'DEC' : ModelDec,
}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save-date', methods=['POST'])
def save_date():
    if request.method=='POST':
        month = request.form.get('month')
        year = request.form.get('year')
        res = dict[month].predict([[year]])
        if(res > 110):
            results = 'YES,there is a possibility of flood'
        else:
            results = 'No,there is no possibility of flood'

        return render_template('index.html',results = results)


if __name__ == '__main__':
    app.run(debug=True)