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