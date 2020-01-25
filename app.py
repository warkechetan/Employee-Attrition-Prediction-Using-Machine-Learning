from flask import Flask,render_template,request
import numpy as np
import pandas as pd
from sklearn.externals import joblib
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
  if request.method=="POST":
    result = request.form
    bt={'Travel_Rarely':1,'Travel_Frequently':2,'Non-Travel':0}
    dept={'Sales':0,'Research & Development':1,'Human Resources':2}
    gender={'Female':0,'Male':1}
    jobrole={'Sales Executive':0,'Research Scientist':1,'Laboratory Technician':2,'Manufacturing Director':3,'Healthcare 			Representative':4,'Manager':5,'Sales Representative':6,'Research Director':7,'Human Resources':8}
    educ={'Life Sciences':0,'Medical':1,'Marketing':2,'Technical Degree':3,'Human Resources':4,'Other':5}
    mar={'Single':0,'Married':1,'Divorced':2}
    b=result['distance']
    c=result['workex']
    d=result['income']
    
    if b=="":
      ib=0
    else:
      ib=int(b)
    if c=="":
      ic=0
    else:
      ic=int(c)
    if d=="":
      id1=0
    else:
      id1=int(d)

    a=[[bt[result['travel']],dept[result['dept']],ib,
gender[result['gender']],jobrole[result['jobrole']],educ[result['educ']],ic,id1,mar[result['mar']]]]
    model = joblib.load('model.sav')
    a=[a[0]]
    pred=model.predict(a)
    if pred>0:
      pred="YES"
    else:
      pred="NO"

																														 																			   								              
  return render_template('index.html',res=pred)
		

if __name__ == "__main__":
	app.run(debug=True)
#print(model)
