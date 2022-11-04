CardNumber = list(input("Enter card number: "))

if len(CardNumber) != 16:
    print("Wrong number of card")
    quit()

if CardNumber[0] == "3":
    NameOfCard = "Amex"
elif CardNumber[0] == "4":
    NameOfCard = "Visa"
elif CardNumber[0] == "5":
    NameOfCard = "MasterCard"
else:
    print("Only Visa, MasterCard or Amex")
    quit()

ListIntNumber = CardNumber

for elements in range(len(CardNumber)):
    ListIntNumber[elements] = int(CardNumber[elements])

index, sumOfMultiplyByTwo = 0, 0
while index < 16:
    if ListIntNumber[index] * 2 >= 10:
        ListIntNumber[index] = ListIntNumber[index] * 2
        Number = str(ListIntNumber[index])
        Number = ",".join(Number)
        Number = Number.split(",")
        for element in range(len(Number)):
            ListIntNumber[element] = int(Number[element])
        multiplyByTwo = ListIntNumber[0] + ListIntNumber[1]
    else:
        multiplyByTwo = ListIntNumber[index] * 2
    sumOfMultiplyByTwo = sumOfMultiplyByTwo + multiplyByTwo
    index += 2

index -= 1
while index > 1:
    sumOfMultiplyByTwo += ListIntNumber[index]
    index -= 2

sumOfMultiplyByTwo = str(sumOfMultiplyByTwo)
sumOfMultiplyByTwo = ",".join(sumOfMultiplyByTwo)
sumOfMultiplyByTwo = sumOfMultiplyByTwo.split(",")

for element in range(len(sumOfMultiplyByTwo)):
    sumOfMultiplyByTwo[element] = sumOfMultiplyByTwo[element]

if int(sumOfMultiplyByTwo[1]) == 0:
    print("Card is " + NameOfCard)
elif sumOfMultiplyByTwo[1] != 0:
    print("Card is invalid")
