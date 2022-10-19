TimeInSeconds = int(input("How many second do you want to convert: "))
TimeInMinutes = int(TimeInSeconds / 60)
TimeInHours = int(TimeInMinutes / 60)
TimeInDays = int(TimeInHours / 24)

if TimeInSeconds >= 60:
    TimeInSeconds = TimeInSeconds % 60

    if TimeInMinutes >= 60:
        TimeInMinutes = TimeInMinutes % 60

        if TimeInHours >= 24:
            TimeInHours = TimeInHours % 24

print(str(TimeInDays) + ": " + str(TimeInHours) + ": " + str(TimeInMinutes) + ": " + str(TimeInSeconds))
