# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string
"""
user_input123 = input("Give me any string: ")
removeChars = int(input("How meny cachracters you want to remove from the beginning? "))

strLen4 = len(user_input123)

if strLen4 > removeChars:
    charCycle = 0
    i = 0
    while removeChars > charCycle:
        newUserInput = user_input123.replace(user_input123[0], "")
        charCycle = charCycle + 1
        i = i + 1
    print(newUserInput)
else:
    print("Char count cannot be greater than srting length!")

    """
b = "banana"
for x in b:
  print(b.replace(b[0], ""))


