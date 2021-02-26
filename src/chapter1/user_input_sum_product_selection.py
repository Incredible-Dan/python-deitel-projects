# Write a program that asks the user for a number n
# and gives them the possibility to choose
# between computing the sum and computing
# the product of 1,…,n.

# user_input_sum_product_selection

# sum of user number
# user_number = int(input('Enter the number: '))
total = 0
product = 1
counter = 0

user_number = int(input('Enter the number: '))
while user_number > 0:
    counter = counter + 1
    total = total + counter
    user_number = user_number - 1
# product of user number

user_number = int(input('Enter the number: '))
while user_number > 0:
    counter = counter + 1
    product = product * counter
    user_number = user_number - 1

    print(total)
    print(product)
user_choice = int(input('Enter the sum or product of your choice: '))
while user_choice > 0:
    counter = counter + 1
if user_choice == total & user_choice == product:
    print('Your number of choice from sum and product:', user_choice)
