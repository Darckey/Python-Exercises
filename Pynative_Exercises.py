# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is greater than 1000, else return their sum.

def product_or_sum(a, b):

    product = a * b
    plus = a + b

    if product > 1000:
        return print(product)
    else: 
        return print(plus)

product_or_sum(13, 400)

# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

def print_sum(iterations):

    current_number = 0
    previous_number = 0

    i = 0

    while i < iterations:
        su_m = current_number + previous_number
        print(f'Current number is {current_number} and prevous number is {previous_number}, Sum: {su_m}')
        i += 1
        previous_number = current_number
        current_number += 1
    else:
        print(f'Stopped after {iterations} iterations!')

user_iterations = input("Give how meny iterations to run: ")
print_sum(int(user_iterations))

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

# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string



# Exercise 5: Check if the first and last number of a list is the same
#Write a function to return True if the first and last number of a given list is same. If #numbers are different then return False.

def checkList(array):

    if array[0] == array[-1]:
        return print(True)
    else:
        return print(False)

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
checkList(numbers_x)
checkList(numbers_y)