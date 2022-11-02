from collections import Counter


def askString(Text):
    return input(Text)


def countElements(Text):
    return print(Counter(Text))


def main():
    Text = askString("Enter your text: ").split(" ")
    Text = "".join(Text)
    countElements(Text)


main()
