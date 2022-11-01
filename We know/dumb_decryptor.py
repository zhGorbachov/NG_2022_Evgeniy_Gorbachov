Text = input("Enter your text: ")
Encryption = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                            "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")
print("=========================")
print(Text.translate(Encryption))  # Quis custodiet ipsos custodes?
