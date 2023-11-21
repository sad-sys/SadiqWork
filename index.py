from flask import Flask, render_template, request
from gradeData import *
from aLevelFunctions import *

ucatDataArr = [2120,2250,2340,2420,2500,2570,2660,2750,2880]
numberOfGrades = []
chosenGradesLow   = []
chosenGradesHigh  = []
images = []

app = Flask(__name__, template_folder='templates', static_folder='static')
app.debug = True

@app.route("/" ,methods = ["GET"])
def index():
    if request.method == "GET":
        numberOfGrades = []
        print("GET")
        return render_template("sizeUp.html")
    
@app.route("/ucat", methods = ["POST","GET"])    
def ucatQuant():
    if request.method == "POST" or request.method == "GET":
        numberOfGrades = []
        print(request.method)
        return render_template("ucatQuant.html", ucatDataArr=ucatDataArr)

@app.route("/ucatPost", methods = ["POST","GET"])
def ucatPost():
    if request.method == "POST" or request.method == "GET":
        numberOfGrades = []
        print(request.method)
        score = int(request.form.get("score"))
        decile = compareScore(score, ucatDataArr)
        print (f"Decile is {decile}")
        scoreCalc = True
        return render_template("ucatQuant.html", ucatDataArr=ucatDataArr, scoreCalc = scoreCalc, decile = decile)
    
@app.route("/aLevel", methods = ["POST","GET"])
def aLevel():
    if request.method == "POST":
        
        numberOfGrades = []
        print ("POST, ALEVEL")
        return render_template("aLevelQuant.html", subjects = subjects, resultsAbsoluteValueArr = resultsAbsoluteValueArr)
    
@app.route("/aLevelPost", methods = ["POST","GET"])
def aLevelQuant():
    if request.method == "POST" or request.method == "GET":

        print (request.method)

        subject = request.form.get("subject")
        grade   = request.form.get("grade")
        subject = subject.upper()
        grade   = grade.upper()

        if subject:
            subject,placeHolder = getSubjectandResults(subject,subjects,resultsAbsoluteValueArr)
            scoreCalc = True
            gradePercentileLow, gradePercentileHigh = getChartSuperFunction(subject,grade,subjects,resultsAbsoluteValueArr)
            numberOfGrades.append(subject)
            print ("Placeholder is ", placeHolder)
            print ("numberOfGrades is ",numberOfGrades)
            img_b64 = plot_to_img()
            chosenGradesLow.append(gradePercentileLow)
            chosenGradesHigh.append(gradePercentileHigh)
            images.append(img_b64)
            print ("Done")
        else:
            scoreCalc = False
            subject = "Not entered"
            print ("Not done")
        return render_template("aLevelQuant.html", subjects = subjects, resultsAbsoluteValueArr = resultsAbsoluteValueArr, scoreCalc = scoreCalc, subject = subject,img_b64 = img_b64, grade = grade, gradePercentileLow = gradePercentileLow, gradePercentileHigh = gradePercentileHigh, numberOfGrades = numberOfGrades, images = images, chosenGradesLow = chosenGradesLow, chosenGradesHigh = chosenGradesHigh)

def compareScore(score, rankings):
    for i in range(0,len(rankings)):
        if score > rankings[len(rankings)-1]:
            return len(rankings) + 1
        elif score < rankings[0]:
            return 0
        if score >= rankings[i] and score < rankings[i + 1]:
            return i + 1