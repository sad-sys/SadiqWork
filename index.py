from flask import Flask, render_template, request
from gradeData import *

ucatDataArr = [2120,2250,2340,2420,2500,2570,2660,2750,2880]

app = Flask(__name__, template_folder='templates', static_folder='static')
app.debug = True

@app.route("/" ,methods = ["GET"])
def index():
    if request.method == "GET":
        print("GET")
        return render_template("sizeUp.html")
    
@app.route("/ucat", methods = ["POST","GET"])    
def ucatQuant():
    if request.method == "POST" or request.method == "GET":
        print(request.method)
        return render_template("ucatQuant.html", ucatDataArr=ucatDataArr)

@app.route("/ucatPost", methods = ["POST","GET"])
def ucatPost():
    if request.method == "POST" or request.method == "GET":
        print(request.method)
        score = int(request.form.get("score"))
        decile = compareScore(score, ucatDataArr)
        print (f"Decile is {decile}")
        scoreCalc = True
        return render_template("ucatQuant.html", ucatDataArr=ucatDataArr, scoreCalc = scoreCalc, decile = decile)
    
@app.route("/aLevel", methods = ["POST","GET"])
def aLevel():
    if request.method == "POST":
        print ("POST, ALEVEL")
        return render_template("aLevelQuant.html")
    
@app.route("/aLevelPost", methods = ["POST","GET"])
def aLevelQuant():
    if request.method == "POST" or request.method == "GET":
        print (request.method)
        score = request.form.get("score")
        if score:
            score = int(score)
            print (f"Score is {score}")
            scoreCalc = True
        else:
            score = "Not entered"
            scoreCalc = True
        return render_template("aLevelQuant.html", scoreCalc= scoreCalc, score = score)

def compareScore(score, rankings):
    for i in range(0,len(rankings)):
        if score > rankings[len(rankings)-1]:
            return len(rankings) + 1
        elif score < rankings[0]:
            return 0
        if score >= rankings[i] and score < rankings[i + 1]:
            return i + 1