Text = input("Enter your text, which need to encrypt: ")
Encryption = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                           "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")
TextEncrypted = Text.translate(Encryption)
print("Your encrypted text: " + str(TextEncrypted))
