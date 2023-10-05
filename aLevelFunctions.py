import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

def getSubjectandResults(subject,subjects,resultsAbsoluteValueArr):
    for i in range (0,len(subjects)):
        if subject in subjects[i]:
            return subjects[i],resultsAbsoluteValueArr[i]

def getGrade(subjectGrade, specificResults):
    grades = ["A*","A","B","C","D","E","U"]
    for i in range (0,len(grades)):
        if grades[i] == subjectGrade:
            if i != len(grades):
                gradePercentileLow =  sum(specificResults[:i])
                gradePercentileHigh = sum(specificResults[:i+1])
            else:
                gradePercentileLow =  sum(specificResults[:i])
                gradePercentileHigh = 100
            return  i, gradePercentileLow, gradePercentileHigh
    else:
        return "Not Valid","Not valid"

def drawChart(subject,specificResults,gradeIndex):
    plt.clf()
    grades = ["A*","A","B","C","D","E","U"]
    bars = plt.bar(grades, specificResults)
    bars[gradeIndex].set_color('red')

def getChartSuperFunction(subject,subjectGrade,subjects,resultsAbsoluteValueArr):
    subject, specificResults = getSubjectandResults(subject,subjects,resultsAbsoluteValueArr)
    gradeIndex, gradePercentileLow, gradePercentileHigh = getGrade(subjectGrade, specificResults)
    drawChart(subject, specificResults, gradeIndex)
    return gradePercentileLow,gradePercentileHigh

def plot_to_img():
    img = io.BytesIO()
    plt.savefig(img, format = 'png')
    img.seek(0)

    'Convert BytesIO object to base64 string'
    img_b64 = base64.b64encode(img.getvalue()).decode()

    return img_b64