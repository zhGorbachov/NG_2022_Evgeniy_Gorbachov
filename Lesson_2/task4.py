number = int(input("Enter your number, which need to convert: "))
factorial = 1
for number in range(1, number+1):
    factorial = factorial * number

print("Factorial of number: " + str(factorial))
