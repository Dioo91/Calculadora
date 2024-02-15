import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)
windowCalc = QWidget()
windowCalc.resize(328,510)

box = QLineEdit("",windowCalc)
box.setGeometry(5,5,327,85)
    
valor1 = 0 
valor2 = 0
operador = ""


def captarNumber(button):
    textoAtual = box.text()
    novaTexto = textoAtual + button
    box.setText(novaTexto)
    
def operations(y):
    global valor1
    global valor2
    global operador
    if y == "X":
        valor1 = float(box.text())
        box.setText("")
        operador = "X"
    elif y == "-":
        valor1 = float(box.text())
        box.setText("")
        operador = "-"
    elif y == "+":
        valor1 = float(box.text())
        box.setText("")
        operador = "+"
    elif y == "/":
        valor1 = float(box.text())
        box.setText("")
        operador = "/"
    elif y == "CLEAR":
        box.setText("")
    elif y == "=":
        valor2 = float(box.text())
        if operador == "X":
            mult = valor1 * valor2
            box.setText(f"{mult}")
        elif operador == "+":
            sum = valor1 + valor2
            box.setText(f"{sum}")
        elif operador == "-":
            sub = valor1 - valor2
            box.setText(f"{sub}")
        elif operador == "/":
            div = valor1 / valor2
            box.setText(f"{div  }")
   
   
with open("style.css", "r") as file:
    app.setStyleSheet(file.read())
    
    
clear = QPushButton("CLEAR",windowCalc)
clear.setProperty("class","buttonsCD")
clear.setStyleSheet("color: black")
clear.setGeometry(5,96,153,70)
clear.clicked.connect(lambda:operations("CLEAR"))
delete = QPushButton("DEL", windowCalc)
delete.setProperty("class","buttonsCD")
delete.setStyleSheet("color: black")
delete.setGeometry(170,96,70,70)
division = QPushButton("/",windowCalc)
division.setProperty("class", "coloroperations")
division.setGeometry(252,96,70,70)
division.clicked.connect(lambda: operations("/"))

number7 = QPushButton("7", windowCalc)
number7.setGeometry(5,178,70,70)
number7.clicked.connect(lambda: captarNumber("7"))
number8 = QPushButton("8", windowCalc)
number8.setGeometry(88,178,70,70)
number8.clicked.connect(lambda: captarNumber("8"))
number9 = QPushButton("9", windowCalc)
number9.setGeometry(170,178,70,70)
number9.clicked.connect(lambda: captarNumber("9"))
multiplication = QPushButton('X',windowCalc)
multiplication.setProperty("class", "coloroperations")
multiplication.setGeometry(252,178,70,70)
multiplication.clicked.connect(lambda: operations("X"))

number4 = QPushButton("4", windowCalc)
number4.setGeometry(5,260,70,70)
number4.clicked.connect(lambda: captarNumber("4"))
number5 = QPushButton("5", windowCalc)
number5.setGeometry(88,260,70,70)
number5.clicked.connect(lambda: captarNumber("5"))
number6 = QPushButton("6", windowCalc)
number6.setGeometry(170,260,70,70)
number6.clicked.connect(lambda: captarNumber("6"))
subtraction = QPushButton("-",windowCalc)
subtraction.setProperty("class", "coloroperations")
subtraction.setGeometry(252,260,70,70)
subtraction.clicked.connect(lambda: operations("-"))

number1 = QPushButton("1", windowCalc)
number1.setGeometry(5,342,70,70)
number1.clicked.connect(lambda: captarNumber("1"))
number2 = QPushButton("2", windowCalc)
number2.setGeometry(88,342,70,70)
number2.clicked.connect(lambda: captarNumber("2"))
number3 = QPushButton("3", windowCalc)
number3.setGeometry(170,342,70,70)
number3.clicked.connect(lambda: captarNumber("3"))
sum = QPushButton("+",windowCalc)
sum.setProperty("class", "coloroperations")
sum.setGeometry(252,342,70,70)
sum.clicked.connect(lambda: operations("+"))

number0 = QPushButton("0",windowCalc)
number0.setGeometry(5,424,153,70)
number0.clicked.connect(lambda: captarNumber("0"))
point = QPushButton(".", windowCalc)
point.setGeometry(170,424,70,70)
point.clicked.connect(lambda: captarNumber("."))
result = QPushButton("=",windowCalc)
result.setProperty("class", "coloroperations")
result.setGeometry(252,424,70,70)
result.clicked.connect(lambda: operations("="))



windowCalc.show()
windowCalc.setWindowTitle("Calculadora")
app.exec()