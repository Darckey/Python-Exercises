# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

str_x = "Emma is good developer. Emma is a writer. Emma is a rapper. Emma is good developer. Emma is a writer. Emma is a rapper. Emma is good developer. Emma is a writer. Emma is a rapper. Emma is good developer. Emma is a writer. Emma is a rapper."

e = "Emma"
cnt = str_x.count(e)

print(e + " was mentioned in the string " + str(cnt) + " times.")