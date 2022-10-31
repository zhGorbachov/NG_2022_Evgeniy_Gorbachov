Numbers = input("Enter random int numbers: ")
List = Numbers.split(", ", -1)
for elements in range(len(List)):
    List[elements] = int(List[elements])

List.sort()
print("Min values = " + str(List[0]) + ";" + " Max values = " + str(List[-1]))
MinNumber, MaxNumber = List[0], List[-1]
List.remove(MinNumber)
List.remove(MaxNumber)
print("Sum of central numbers = " + str(sum(List)))
