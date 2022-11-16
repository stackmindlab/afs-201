#Helper function to check for an integer.
def confirm_input_is_digit(string):
    return string.isdigit()

#Helper function to check if int is more than 0
def confirm_positive_input(number):
    return int(number) >= 0


#Prompt user for a positive number.
def get_positive_number():
    user_input = input("Please enter a positive number: ")
    while confirm_input_is_digit(user_input) != True or confirm_positive_input(user_input) != True:
        user_input = input("Invalid Input. Please enter a positive number: ")
    return int(user_input)

def check_for_even(number):
    for x in range(number + 1):
        if( x % 2 == 0):
            print(x)

check_for_even(get_positive_number())