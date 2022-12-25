import pickle
import json
import numpy as np

class function():
    def __init__(self,age,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous,poutcome,job,marital):
        self.age=age
        self.education=education
        self.default=default
        self.balance=balance
        self.housing=housing
        self.loan=loan
        self.contact=contact
        self.day=day
        self.month=month
        self.duration=duration
        self.campaign=campaign
        self.pdays=pdays
        self.previous=previous
        self.poutcome=poutcome
        self.job=job
        self.marital=marital

    def models(self):
        with open("rf_model.pickle","rb") as f:
            self.rf_model=pickle.load(f)

        with open("norm_scale.pickle","rb") as f:
            self.norm_scale=pickle.load(f)

        with open("columns_list.json","r") as f:
            self.columns_list=json.load(f)

    def final(self):
        self.models()
        arr=np.zeros(len(self.columns_list["columns"]))

        arr[0]=self.age
        arr[1]=self.education
        arr[2]=self.default
        arr[3]=self.balance
        arr[4]=self.housing
        arr[5]=self.loan
        arr[6]=self.contact
        arr[7]=self.day
        arr[8]=self.month
        arr[9]=self.duration
        arr[10]=self.campaign
        arr[11]=self.pdays
        arr[12]=self.previous
        arr[13]=self.poutcome

        char="job_"+self.job
        char_index=self.columns_list["columns"].index(char)
        arr[char_index]=1

        char1="marital_"+self.marital
        char_index1=self.columns_list["columns"].index(char)
        arr[char_index1]=1

        arr_data=self.norm_scale.transform([arr])

        result=self.rf_model.predict(arr_data)

        return result



        
