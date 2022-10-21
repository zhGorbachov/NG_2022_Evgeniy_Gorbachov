TimeInSeconds = int(input("How many second do you want to convert: "))
TimeInMinutes = int(TimeInSeconds / 60)
TimeInHours = int(TimeInSeconds / 3600)
TimeInDays = int(TimeInSeconds / 86400)

print(str(TimeInDays) + ": " + str(TimeInHours % 24) + ": " + str(TimeInMinutes % 60) + ": " + str(TimeInSeconds % 60))
