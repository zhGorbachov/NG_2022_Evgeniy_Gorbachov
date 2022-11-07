Text = input("Enter your text: ").lower()
AlphSmallLetters = "abcdefghijklmnopqrstuvwxyz"
iteration = 1

while iteration < 26:
    EncryptedText = str.maketrans(AlphSmallLetters, AlphSmallLetters[iteration:]+AlphSmallLetters[:iteration])
    print("Encrypted text shifted on " + str(iteration) + " letter" + " : " + str(Text.translate(EncryptedText)))
    EncryptedText = ""
    iteration += 1
