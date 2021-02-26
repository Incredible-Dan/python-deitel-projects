# Sum of consecutive integers

# Write a program that asks the user for a number n and
# #prints the sum of the numbers 1 to n




# Multiplication  of consecutive integers

# Write a program that asks the user for a number n and
# #prints the sum of the numbers 1 to n


user_number = int(input('Enter the number: '))
product = 1
counter = 0

while user_number > 0:
    counter = counter + 1
    product = product * counter
    user_number = user_number - 1
    print(product)
