# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

myArrey1 = [10, 34, 55, 61, 45, 66, 35, 98, 90, 23, 30]

for x in myArrey1:
    reminder = x % 5
    if reminder == 0:
        print(x)