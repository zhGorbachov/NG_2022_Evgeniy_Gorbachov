from task2_log import *


def printString(message):
    return input(message)


def inputText(message):
    return input(message)


def sortString(Text):
    Text = Text.split(" ")
    Text.sort()
    return print(" ".join(Text))


def lenString(Text):
    return print(len(Text))


def vowelORconsonant(Text):
    ListWithVowels = ['a', 'e', 'y', 'u', 'o', 'i']
    EnterVowelOrConsonant = inputText("Select vowel or consonant: ")
    List = []
    for elements in Text:
        if EnterVowelOrConsonant == "vowel":
            if elements in ListWithVowels:
                List.append(elements)

        elif EnterVowelOrConsonant == "consonant":
            if elements not in ListWithVowels:
                List.append(elements)

        else:
            return error("Wrong action")
    return print(", ".join(List))


def reverseString(Text):
    Text = Text.split(" ")
    Text.reverse()
    return print(" ".join(Text))


def wordAsNumber(Text):
    info("First number will start from 0")
    number = int(input("Enter number which you want to get as a word: "))
    Text = Text.split(" ")
    try:
        return print(Text[number])
    except IndexError as e:
        error(e)
    except ValueError as e:
        error(e)


def repeatPrint(Text):
    return print(Text)


def manage():
    info("1 = sort string, \n"
         "2 = count amount of elements, \n"
         "3 = vowels or consonants, \n"
         "4 = reverse string, \n"
         "5 = word by number, \n"
         "6 = print again, \n"
         "7 = exit.")


def main():
    info("Starting")
    Text = printString("Enter your text: ")
    manage()
    info("Write the number next to the action")
    while True:
        info("Waiting")
        Action = inputText("Enter your action: ")
        info("Complete")
        match Action:
            case "7":
                break
            case "2":
                lenString(Text)
            case "6":
                repeatPrint(Text)
            case "5":
                wordAsNumber(Text)
            case "1":
                sortString(Text)
            case "4":
                reverseString(Text)
            case "3":
                vowelORconsonant(Text)
    info("Program shuts down")


if "__name__" == main():
    main()
