import cmath

FirstNumber = float(input("Select first number: "))
SecondNumber = float(input("Select second number: "))
SelectAction = input("Select action from (+, -, /, *, square, square root): ")
print("========================")
if SelectAction == "+":
    print(FirstNumber + SecondNumber)
else:
    if SelectAction == "-":
        print(FirstNumber - SecondNumber)
    else:
        if SelectAction == "*":
            print(FirstNumber * SecondNumber)
        else:
            if SelectAction == "/":
                print(FirstNumber / SecondNumber)
            else:
                if SelectAction == "square root":
                    print(cmath.sqrt(FirstNumber + SecondNumber))
                else:
                    print((FirstNumber + SecondNumber)**2) 
