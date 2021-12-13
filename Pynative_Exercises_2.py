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