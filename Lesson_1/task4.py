print("a*x**2 + b*x + c = 0")
a_firstCoefficient = float(input("Write value of a: "))
b_secondCoefficient = float(input("Write value of b: "))
c_freeMember = float(input("Write value of c: "))
print("==================================")
D_discriminant = b_secondCoefficient**2 - 4*a_firstCoefficient*c_freeMember
x1 = (-b_secondCoefficient + D_discriminant**0.5)/(2*a_firstCoefficient)
x2 = (-b_secondCoefficient - D_discriminant**0.5)/(2*a_firstCoefficient)
if D_discriminant < 0:
    print("Doesnt have roots")
elif D_discriminant == 0:
    print("x1 = x2 = " + str(x1) + " as D = 0 ")
else:
    print("x1 = " + str(x1) + " x2 = " + str(x2))
