from flask import Flask,render_template,request
main=Flask(__name__)
from function import function

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/predict",methods=["POST"])
def predict():
    data=request.form
    age=int(data["age"])
    education=int(data["education"])
    default=int(data["default"])
    balance=int(data["balance"])
    housing=int(data["housing"])
    loan=int(data["loan"])
    contact=int(data["contact"])
    day=int(data["day"])
    month=int(data["month"])
    duration=int(data["duration"])
    campaign=int(data["campaign"])
    pdays=int(data["pdays"])
    previous=int(data["previous"])
    poutcome=int(data["poutcome"])
    job=data["job"]
    marital=data["marital"]

    output=function(age,education,default,balance,housing,loan,contact,day,month,duration,campaign,pdays,previous,poutcome,job,marital).final()

    return render_template("index.html",output=output)

if __name__=="__main__":
    main.run(host="0.0.0.0", port=8080)
     
    