ValuesMaxString = int(input("Enter your number: "))
while ValuesMaxString >= 1:
    ValuesForCalculations = ValuesMaxString
    while ValuesForCalculations >= 1:
        print(ValuesForCalculations, end=" ")
        ValuesForCalculations -= 1
    print(end="\n")
    ValuesMaxString -= 1
