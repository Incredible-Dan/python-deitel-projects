# Sum of consecutive integers
user_number = int(input('Enter the number: '))
total = 0
counter = 0

while user_number > 0:
    counter = counter + 1
    total = total + counter
    user_number = user_number - 1
print(total)


# Multiplication  of consecutive integers
user_number = int(input('Enter the number: '))
product = 1
counter = 0

while user_number > 0:
    counter = counter + 1
    product = product * counter
    user_number = user_number - 1
print(product)
