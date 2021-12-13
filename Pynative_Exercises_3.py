# Exercise 3: Print characters from a string that are present at an even index number 
#Write a program to accept a string from the user and display characters that are present at an even index number.

user_input = input("Give me any string: ")

i = 0 
cycles = 0
stringLength = len(user_input)

while cycles < stringLength:
    print(user_input[i])
    i = i + 2
    cycles =  cycles + 2
else:
    print("Even index number printed!")