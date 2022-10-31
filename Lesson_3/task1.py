from task1_log import *


def askYourNumbers(message):
    try:
        return float(input(message))
    except ValueError as e:
        error(e)
        return "Wrong type!"


def plus(firstNumber, secondNumber):
    return firstNumber + secondNumber


def division(firstNumber, secondNumber):
    try:
        return firstNumber / secondNumber
    except ZeroDivisionError as e:
        error(e)
        return "Division by zero!"


def multiply(firstNumber, secondNumber):
    return firstNumber * secondNumber


def minus(firstNumber, secondNumber):
    return firstNumber - secondNumber


def square(firstNumber, secondNumber):
    return firstNumber ** 2, secondNumber ** 2


def squareRoot(firstNumber, secondNumber):
    firstNumber = firstNumber ** (1/2)
    secondNumber = secondNumber ** (1/2)
    return firstNumber, secondNumber


def selectAction(message):
    return input("Enter your action: " + message)


def main():
    firstNumber = askYourNumbers("Enter first number: ")
    secondNumber = askYourNumbers("Enter second number: ")
    match selectAction("Select the action: plus, minus, division, multiply, square, square root: "):
        case "plus":
            print("Plus = " + str(plus(firstNumber, secondNumber)))
        case "minus":
            print("Minus = " + str(minus(firstNumber, secondNumber)))
        case "division":
            print("Division = " + str(division(firstNumber, secondNumber)))
        case "multiply":
            print("Multiply = " + str(multiply(firstNumber, secondNumber)))
        case "square":
            print("Square = " + str(square(firstNumber, secondNumber)))
        case "square root":
            if firstNumber < 0 or secondNumber < 0:
                print("Negative number at the root")
            else:
                print("Square root = " + str(squareRoot(firstNumber, secondNumber)))
        case other:
            print("Wrong action!")


if "__name__" == main():
    main()
