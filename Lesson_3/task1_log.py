def log(type, message):
    print("{" + str(type) + "}" + str(message))


def error(message):
    log("Error", message)


def info(message):
    log("Info", message)
