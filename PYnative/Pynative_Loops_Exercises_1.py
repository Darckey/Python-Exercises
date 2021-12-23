# PYnative loop exercise 

# 1: Print First 10 natural numbers using while loop
#for
print("forLoop")
for i in range(1,11):
    print(i)

print("whileLoop")

k = 1
#whiel
while k <= 10:
    print(k)
    k += 1

#print triangle pattern
for z in range(1,6):
    myList = range(1, z+1, 1)
    list1 = list(myList)
    # for a in list1:
    #     print(list1[z-1])


# Calculate the sum of all numbers from 1 to a given number
# user_input = input("Enter number: ")
givenNumber = int(input("Enter number: "))

n = 1
result = 1
#while
while n < givenNumber:
    result = result + n + 1
    n += 1
print(result)

f = 0
#for
for i in range(1, givenNumber + 1, 1):
    f = f + i
print(f)

# Write a program to print multiplication table of a given number

multiPlicationNumber = int(input("Enter number to be muptiplied by 10-table: "))
for i in range(1,11):
    product =  i * multiPlicationNumber
    print(product) 

# Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

numbers1 = [12, 75, 150, 180, 145, 25, 50, 18, 15, 55, 50, 180, 145, 525, 50]

# for1
for s in numbers1:
    if s%5 == 0 and s <= 150:
        print(f"for1 {s}")
    if s > 500:
        break
# for2
for s in numbers1:
    if s > 500:
        break
    elif s > 150:
        continue
    elif s%5 == 0:
        print(f"for2 {s}")

# Count the total number of digits in a number
# Write a program to count the total number of digits in a number using a while loop.

user_input222 = input("Enter any string or number: ")
strLen = (len(user_input222))

# for
r = 1
for r in range(1,strLen):
    r += 1
print(r)


# while
l = 0
while l < strLen:
    l += 1
print(l)

assert l == strLen, "While-loop output doesn't match the actual input lenght"

# Display numbers from -10 to -1 using for loop

for q in range(-10, 0, 1):
    print(q)

list11 = [10, 20, 30, 40, 50]
rList11 = reversed(list11)
for w in rList11:
    print(w)

# Use else block to display a message “Done” after successful execution of for loop
for d in range(5):
    print(d)
else:
    print("Done!")







