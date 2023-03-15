
from pywebio.input import *
from pywebio.output import *

#for addition
def add(n1, n2):
    n = n1 + n2
    return n

#for substration
def substraction(n1, n2):
    n = n1 - n2
    return n

#for multiplecation
def multiplication(n1, n2):
    n = n1 * n2
    return n

#for division
def division(n1, n2):
    n = n1 / n2
    return n

put_markdown('This is my WEB CALCULATOR by using PyWebIo Python Library')
def calculator():
    
    firstNumber = float(input("Enter your first number: "))
    secondNumber = float(input("Enter your second number: "))
    userInput = input('''Enter your choice or operator:\n 
                      1. Addition : + \n
                      2. Substration : - \n
                      3. Multiplecation : * \n
                      4. Division : / ''')
    if userInput == "1" or userInput == "+":
        put_text("Result: ", add(firstNumber, secondNumber))
    elif userInput == "2" or userInput == "-":
        put_text("Result: ", substraction(firstNumber, secondNumber))
    elif userInput == "3" or userInput == "*":
        put_text("Result: ", multiplication(firstNumber, secondNumber))
    elif userInput == "4" or userInput == "/":
        put_text("Result: ", division(firstNumber, secondNumber))
    else:
        put_text("Invalid operator!...Choose correct one")
calculator()

while True:
    next_calculation = input("Want to do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
    else:
        calculator()
                                             