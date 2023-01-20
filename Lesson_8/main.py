import hashlib
import itertools


alphabetAndNumbers = "abcdefghijklmnopqrstuvwxyz1234567890"
index = 1


def encrypting(hashUser):
    if len(hashUser) == 64:

        for symbol in itertools.product(alphabetAndNumbers, repeat=index):
            text = "".join(symbol)
            if hashUser == hashlib.sha256(text.encode()).hexdigest():
                print("Your encrypted text: " + str(text))
                print("[INFO] Program shuts down!")
                exit()
            else:
                continue
    else:
        print("[INFO] Hash text is wrong type")
        exit()


def main():
    hashUser = input("Enter your hash: ")
    while True:
        encrypting(hashUser)
        global index
        index += 1


main()
