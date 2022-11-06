Text = input("Enter your text: ")
EncryptionForOneLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                             "bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA")
EncryptionForTwoLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                             "cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB")
EncryptionForThreeLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                               "defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC")
EncryptionForFourLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                              "efghijklmnopqrstuvwxyzabcdEFGHIJKLMNOPQRSTUVWXYZABCD")
EncryptionForFiveLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                              "fghijklmnopqrstuvwxyzabcdeFGHIJKLMNOPQRSTUVWXYZABCDE")
EncryptionForSixLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                             "ghijklmnopqrstuvwxyzabcdefGHIJKLMNOPQRSTUVWXYZABCDEF")
EncryptionForSevenLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                               "hijklmnopqrstuvwxyzabcdefgHIJKLMNOPQRSTUVWXYZABCDEFG")
EncryptionForEightLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                               "ijklmnopqrstuvwxyzabcdefghIJKLMNOPQRSTUVWXYZABCDEFGH")
EncryptionForNineLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                              "jklmnopqrstuvwxyzabcdefghiJKLMNOPQRSTUVWXYZABCDEFGHI")
EncryptionForTenLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                             "klmnopqrstuvwxyzabcdefghijKLMNOPQRSTUVWXYZABCDEFGHIJ")
EncryptionForElevenLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                "lmnopqrstuvwxyzabcdefghijkLMNOPQRSTUVWXYZABCDEFGHIJK")
EncryptionForTwelveLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                "mnopqrstuvwxyzabcdefghijkmMNOPQRSTUVWXYZABCDEFGHIJKL")
EncryptionForThirteenLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                  "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")
EncryptionForFourteenLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                  "opqrstuvwxyzabcdefghijklmnOPQRSTUVWXYZABCDEFGHIJKLMN")
EncryptionForFifteenLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                 "pqrstuvwxyzabcdefghijklmnoPQRSTUVWXYZABCDEFGHIJKLMNO")
EncryptionForSixteenLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                 "qrstuvwxyzabcdefghijklmnopQRSTUVWXYZABCDEFGHIJKLMNOP")
EncryptionForSeventeenLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                   "rstuvwxyzabcdefghijklmnopqRSTUVWXYZABCDEFGHIJKLMNOPQ")
EncryptionForEighteenLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                  "stuvwxyzabcdefghijklmnopqrSTUVWXYZABCDEFGHIJKLMNOPQR")
EncryptionForNineteenLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                  "tuvwxyzabcdefghijklmnopqrsTUVWXYZABCDEFGHIJKLMNOPQRS")
EncryptionForTwentyLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                "uvwxyzabcdefghijklmnopqrstUVWXYZABCDEFGHIJKLMNOPQRST")
EncryptionForTwentyOneLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                   "vwxyzabcdefghijklmnopqrstuVWXYZABCDEFGHIJKLMNOPQRSTU")
EncryptionForTwentyTwoLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                   "wxyzabcdefghijklmnopqrstuvWXYZABCDEFGHIJKLMNOPQRSTUV")
EncryptionForTwentyThreeLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                    "xyzabcdefghijklmnopqrstuvwXYZABCDEFGHIJKLMNOPQRSTUVW")
EncryptionForTwentyFourLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                    "yzabcdefghijklmnopqrstuvwxYZABCDEFGHIJKLMNOPQRSTUVWX")
EncryptionForTwentyFiveLetterShift = Text.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                    "zabcdefghijklmnopqrstuvwxyZABCDEFGHIJKLMNOPQRSTUVWXY")

print("=========================")
print("ForOneLetterShift: " + Text.translate(EncryptionForOneLetterShift))
print("=========================")
print("ForTwoLetterShift: " + Text.translate(EncryptionForTwoLetterShift))
print("=========================")
print("ForThreeLetterShift: " + Text.translate(EncryptionForThreeLetterShift))
print("=========================")
print("ForFourLetterShift: " + Text.translate(EncryptionForFourLetterShift))
print("=========================")
print("ForFiveLetterShift: " + Text.translate(EncryptionForFiveLetterShift))
print("=========================")
print("ForSixLetterShift: " + Text.translate(EncryptionForSixLetterShift))
print("=========================")
print("ForSevenLetterShift: " + Text.translate(EncryptionForSevenLetterShift))
print("=========================")
print("ForEightLetterShift: " + Text.translate(EncryptionForEightLetterShift))
print("=========================")
print("ForNineLetterShift: " + Text.translate(EncryptionForNineLetterShift))
print("=========================")
print("ForTenLetterShift: " + Text.translate(EncryptionForTenLetterShift))
print("=========================")
print("ForElevenLetterShift: " + Text.translate(EncryptionForElevenLetterShift))
print("=========================")
print("ForTwelveLetterShift: " + Text.translate(EncryptionForTwelveLetterShift))
print("=========================")
print("ForThirteenLetterShift: " + Text.translate(EncryptionForThirteenLetterShift))
print("=========================")
print("ForFourteenLetterShift: " + Text.translate(EncryptionForFourteenLetterShift))
print("=========================")
print("ForFifteenLetterShift: " + Text.translate(EncryptionForFifteenLetterShift))
print("=========================")
print("ForSixteenLetterShift: " + Text.translate(EncryptionForSixteenLetterShift))
print("=========================")
print("ForSeventeenLetterShift: " + Text.translate(EncryptionForSeventeenLetterShift))
print("=========================")
print("ForEighteenLetterShift: " + Text.translate(EncryptionForEighteenLetterShift))
print("=========================")
print("ForNineteenLetterShift: " + Text.translate(EncryptionForNineteenLetterShift))
print("=========================")
print("ForTwentyLetterShift: " + Text.translate(EncryptionForTwentyLetterShift))
print("=========================")
print("ForTwentyOneLetterShift: " + Text.translate(EncryptionForTwentyOneLetterShift))
print("=========================")
print("ForTwentyTwoLetterShift: " + Text.translate(EncryptionForTwentyTwoLetterShift))
print("=========================")
print("ForTwentyThreeLetterShift: " + Text.translate(EncryptionForTwentyThreeLetterShift))
print("=========================")
print("ForTwentyFourLetterShift: " + Text.translate(EncryptionForTwentyFourLetterShift))
