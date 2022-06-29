import pandas as pd
import plotly.express as pe
import numpy as np

data = pd.read_csv("data.csv")

score = data["TOEFL Score"].tolist()

chances = data["Chance of Admit "].tolist()

graph = pe.scatter( data , x = score , y = chances)

#graph.show()

#Line Equation : y = mx + c

#-------------------- Using Hit 🎯 and Trial Method 💥--------------------------

m = 1
c = 0
y = []

for x in score :
    y2 = m*x+c
    y.append(y2)

graph = pe.scatter(data , x = score , y = chances)
graph.update_layout(shapes=[
    dict(
        type="line",
        x0 = min(score) , x1 = max(score),
        y0 = min(y) , y1 = max(y)
    )
])
graph.show()

#------------------------------------------Failed 😔--------------------------------------
#-----------------------------------------Let's Try Again 😉------------------------------

m = 0.93
c = -95
y = []
for x in score :
     y2 = m*x+c
     y.append(y2)
graph = pe.scatter(data , x = score , y = chances)
graph.update_layout(shapes=[
    dict(
        type="line",
        x0 = min(score) , x1 = max(score),
        y0 = min(y) , y1 = max(y)
    )
])
#graph.show()
#------------------------------------Bakwass Technique 😫 (just joking🤣🤣🤣)-----------------

#----------------------------------Pro-Technique 😎--------------------------
scoreArray = np.array(score)
chanceArray = np.array(chances)

m , c = np.polyfit(scoreArray , chanceArray , 1)

y = []

for x in scoreArray :
    y2 = m*x+c
    y.append(y2)
graph = pe.scatter(data , x = scoreArray , y = chanceArray)
graph.update_layout(shapes=[
    dict(
        type="line",
        x0 = min(scoreArray) , x1 = max(scoreArray),
        y0 = min(y) , y1 = max(y)
    )
])
#graph.show()

print("M and C are" ,m,c)
