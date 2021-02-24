working_number = 16
guess_number = 200


quotient = working_number / guess_number
new_guess = (quotient + guess_number) / 2

# print(new_guess)
# if guess_number == new_guess:
#     print('True')
# else:
#     print('False')


while guess_number != new_guess:
    guess_number = new_guess
    quotient = working_number / guess_number
    new_guess = (quotient + guess_number) / 2

    if guess_number == new_guess:
        print(new_guess)
        break
