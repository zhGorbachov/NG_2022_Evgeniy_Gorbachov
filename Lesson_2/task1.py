List = list(input("Enter your text: "))
while " " in List:  # We delete all probels in the list.
    List.remove(" ")
List.sort()
ListForResult = {}  # Here we will add letters from List, which will count.
for letter in List:
    if letter in ListForResult:
        ListForResult[letter] += 1
    else:
        ListForResult[letter] = 1

print("Letters counted: " + str(ListForResult))
