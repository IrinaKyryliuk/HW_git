from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import *



app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()
layout4 = QHBoxLayout()
layout5 = QHBoxLayout()
layout6= QHBoxLayout()
layout.addLayout(layout1)
layout.addLayout(layout2)
layout.addLayout(layout3)
layout.addLayout(layout4)
layout.addLayout(layout5)
layout.addLayout(layout6)
window.setLayout(layout)

result=0
Action=""
num1=""
num2=""

def onClick():
    global num1
    global num2
    if(Action==""):
        num1 = num1+"1"
        label.setText(num1)
    else:
        num2=num2+"1"
        label.setText(num2)

def onClick2():
    global num1
    global num2
    if(Action==""):
        num1 = num1+"2"
        label.setText(num1)
    else:
        num2=num2+"2"
        label.setText(num2)

def onClick3():
    global num1
    global num2
    if(Action==""):
        num1 = num1+"3"
        label.setText(num1)
    else:
        num2=num2+"3"
        label.setText(num2)

def onClick4():
    global num1
    global num2
    if(Action==""):
        num1 = num1+"4"
        label.setText(num1)
    else:
        num2=num2+"4"
        label.setText(num2)

def onClick5():
    global num1
    global num2
    if(Action==""):
        num1 = num1+"5"
        label.setText(num1)
    else:
        num2=num2+"5"
        label.setText(num2)

def onClick6():
    global num1
    global num2
    if(Action==""):
        num1 = num1+"6"
        label.setText(num1)
    else:
        num2=num2+"6"
        label.setText(num2)
    
def onClick7():
    global num1
    global num2
    if(Action==""):
        num1 = num1+"7"
        label.setText(num1)
    else:
        num2=num2+"7"
        label.setText(num2)

def onClick8():
    global num1
    global num2
    if(Action==""):
        num1 = num1+"8"
        label.setText(num1)
    else:
        num2=num2+"8"
        label.setText(num2)

def onClick9():
    global num1
    global num2
    if(Action==""):
        num1 = num1+"9"
        label.setText(num1)
    else:
        num2=num2+"9"
        label.setText(num2)

def onClick0():
    global num1
    global num2
    if(Action==""):
        num1 = num1+"0"
        label.setText(num1)
    else:
        num2=num2+"0"
        label.setText(num2)

def onClickResult():
    global num1, num2, Action, result
    if((num1!="") and (num2!="") and (Action!="")):      
        if(Action == "Add"):
            result = float(num1)+float(num2)
        elif(Action == "Subtract"):
            result = float(num1)-float(num2)
        elif(Action == "Multiply"):
            result = float(num1)*float(num2)
        elif(Action == "Divide"):
            result = float(num1)/float(num2)
    label.setText(str(result))
    num1=str(result)
    result=0
    num2=""
    Action=""
    
def onClickNull():
    global num1, num2, Action, result
    label.setText("0")
    result=0
    num1=""
    num2=""
    Action=""

def onClickAdd():
    global Action
    label.setText("+")
    Action="Add"

def onClickSubtract():
    global Action
    label.setText("-")
    Action="Subtract"

def onClickMultiply():
    global Action
    label.setText("*")
    Action="Multiply"

def onClickDivide():
    global Action
    label.setText("/")
    Action="Divide"

button = QPushButton("1")
button.setStyleSheet('background-color:gray;color: yellow')
button.clicked.connect(onClick)

button2 = QPushButton("2")
button2.setStyleSheet('background-color:gray;color: yellow')
button2.clicked.connect(onClick2)

button3 = QPushButton("3")
button3.setStyleSheet('background-color:gray;color: yellow')
button3.clicked.connect(onClick3)

button4 = QPushButton("4")
button4.setStyleSheet('background-color:gray;color: yellow')
button4.clicked.connect(onClick4)

button5 = QPushButton("5")
button5.setStyleSheet('background-color:gray;color: yellow')
button5.clicked.connect(onClick5)

button6 = QPushButton("6")
button6.setStyleSheet('background-color:gray;color: yellow')
button6.clicked.connect(onClick6)

button7 = QPushButton("7")
button7.setStyleSheet('background-color:gray;color: yellow')
button7.clicked.connect(onClick7)

button8 = QPushButton("8")
button8.setStyleSheet('background-color:gray;color: yellow')
button8.clicked.connect(onClick8)

button9 = QPushButton("9")
button9.setStyleSheet('background-color:gray;color: yellow')
button9.clicked.connect(onClick9)

button0 = QPushButton("0")
button0.setStyleSheet('background-color:gray;color: yellow')
button0.clicked.connect(onClick0)

buttonResult = QPushButton("=")
buttonResult.setStyleSheet('background-color:gray;color: yellow')
buttonResult.clicked.connect(onClickResult)

buttonNull = QPushButton("C")
buttonNull.setStyleSheet('background-color:gray;color: yellow')
buttonNull.clicked.connect(onClickNull)

buttonAdd = QPushButton("+")
buttonAdd.setStyleSheet('background-color:gray;color: yellow')
buttonAdd.clicked.connect(onClickAdd)

buttonSubtract = QPushButton("-")
buttonSubtract.setStyleSheet('background-color:gray;color: yellow')
buttonSubtract.clicked.connect(onClickSubtract)

buttonMultiply = QPushButton("*")
buttonMultiply.setStyleSheet('background-color:gray;color: yellow')
buttonMultiply.clicked.connect(onClickMultiply)

buttondDivide = QPushButton("/")
buttondDivide.setStyleSheet('background-color:gray;color: yellow')
buttondDivide.clicked.connect(onClickDivide)

label = QLabel("0")
label.setAlignment(Qt.AlignCenter)

labelResult = QLabel("Result:")
labelResult.setAlignment(Qt.AlignCenter)

labelCalculator = QLabel("Calculator")
labelCalculator.setAlignment(Qt.AlignCenter)
labelCalculator.setStyleSheet('background-color:gray;color: yellow')

layout1.addWidget(labelCalculator)
layout2.addWidget(labelResult)
layout2.addWidget(label)
layout3.addWidget(button)
layout3.addWidget(button2)
layout3.addWidget(button3)
layout3.addWidget(buttonAdd)
layout4.addWidget(button4)
layout4.addWidget(button5)
layout4.addWidget(button6)
layout4.addWidget(buttonSubtract)
layout5.addWidget(button7)
layout5.addWidget(button8)
layout5.addWidget(button9)
layout5.addWidget(buttonMultiply)
layout6.addWidget(buttonNull)
layout6.addWidget(button0)
layout6.addWidget(buttonResult)
layout6.addWidget(buttondDivide)

window.show()
window.resize(450, 220)
app.exec_()