number = int(input("Enter your number, which need to convert: "))
factorial = 1
while number >= 1:
    factorial = factorial * number
    number -= 1
print("Factorial of number: " + str(factorial))
