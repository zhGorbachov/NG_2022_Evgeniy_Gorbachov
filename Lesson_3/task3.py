from collections import Counter

Text = input("Enter your text: ")
Text = Text.split()
Text = "".join(Text)
print(Counter(Text))
