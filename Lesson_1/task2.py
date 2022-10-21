FirstNumber = float(input("Select first number: "))
SecondNumber = float(input("Select second number: "))
SelectAction = input("Select action from (+, -, /, *, square, square root): ")
print("========================")
match SelectAction:
    case '+':
        print(FirstNumber + SecondNumber)
    case '-':
        print(FirstNumber - SecondNumber)
    case '*':
        print(FirstNumber * SecondNumber)
    case '/':
        print(FirstNumber / SecondNumber)
    case 'square':
        print("FirstNumber = " + str(FirstNumber ** 2) + " SecondNumber = " + str(SecondNumber ** 2))
    case 'square root':
        print("FirstNumber = " + str(FirstNumber**0.5) + " SecondNumber = " + str(SecondNumber**0.5))
    case other:
        print("Wrong action!")
