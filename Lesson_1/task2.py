FirstNumber = float(input("Select first number: "))
SecondNumber = float(input("Select second number: "))
SelectAction = input("Select action from (+, -, /, *, square, square root): ")
print("========================")
if SelectAction == "+":
    print(FirstNumber + SecondNumber)
elif SelectAction == "-":
    print(FirstNumber - SecondNumber)
elif SelectAction == "*":
    print(FirstNumber * SecondNumber)
elif SelectAction == "/":
    print(FirstNumber / SecondNumber)
elif SelectAction == "square root":
    print("FirstNumber = " + str(FirstNumber**0.5) + " SecondNumber = " + str(SecondNumber**0.5))
elif SelectAction == "square":
    print("FirstNumber = " + str(FirstNumber**2) + " SecondNumber = " + str(SecondNumber**2))
else:
    print("Wrong action!")
