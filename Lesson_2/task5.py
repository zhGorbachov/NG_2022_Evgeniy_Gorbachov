Numbers = input("Enter random int numbers: ")
List = Numbers.split(", ", -1)

for elements in range(len(List)):
    List[elements] = int(List[elements])

List.sort()
print("Min values = " + str(List[0]) + ";" + " Max values = " + str(List[-1]))
SumOfCentralNumbers = sum(List)-int(List[0])-int(List[-1])
print("Sum of central numbers = " + str(SumOfCentralNumbers))
