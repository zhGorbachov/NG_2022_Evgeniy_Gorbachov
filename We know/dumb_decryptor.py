Text = input("Enter your text: ").lower()
AlphSmallLetters = "abcdefghijklmnopqrstuvwxyz"

for key in range(len(AlphSmallLetters)):
    encrypted = ""
    for element in Text:
        if element in AlphSmallLetters:
            number = AlphSmallLetters.find(element)
            number = number - key
            if number < 0:
                number = number + len(AlphSmallLetters)
            encrypted = encrypted + AlphSmallLetters[number]
        else:
            encrypted = encrypted + element
    print("Encrypted text №%s: %s" % (key, encrypted))
