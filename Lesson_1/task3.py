import datetime

TimeInSecond = float(input("How many second do you want to convert: "))
TimeAsData = datetime.datetime.fromtimestamp(TimeInSecond)
print("Time in second => " + str(TimeInSecond))
print("Time as data => " + str(TimeAsData))
