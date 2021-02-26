# Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17

user_number = int(input('Enter the number: '))
total = 0
counter = 0

while user_number > 0:
    if user_number % 3 == 0 & user_number % 5 == 0:
    counter = counter + 1
    total = total + counter
    user_number = user_number - 1
    print(total)
