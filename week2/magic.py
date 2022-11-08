
#Prompt the user for an input (Int).

def multiply_number(number):
    return number * 3

def add_number(number):
    return number + 6

def divide_number(number):
    return number // 3

def subtract_number(x, y):
    return x - y

def display_result(result):
    print(result)

def get_number():

    while True:
        user_number_string = input("Please enter a number: ")

        try:
            user_number = int(user_number_string)
            break
        except:
            print("Please enter a valid number.")


    multiplied_number = multiply_number(user_number)
    added_number = add_number(multiplied_number)
    divided_number = divide_number(added_number)
    subtracted_number = subtract_number(divided_number, user_number)

    display_result(subtracted_number)

get_number()
