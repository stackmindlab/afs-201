#Criteria 1.
applePrice = 0.50

#Criteria 2.
def get_user_name():
    customer_name = input("Please enter your name: ")
    return customer_name

#Criteria 3. Returns the formatted price dynamically, based on the arguments passed in.
def set_correct_format_price(price, zero):
    return f"{price:.{zero}f}" 

#Prints the message back to user formatted.
def print_formatted_message(name, qty, price):
    print(f"Thank you {name} for your purchase of {qty} apples at a cost of ${price} each.")


#Criteria 4 (Validate user input)
def sell_apple():
    question_text = "How many would you like to buy?"
    customer_name = get_user_name()
    correct_format_price = set_correct_format_price(applePrice, 2)
    while True:
        get_purchase_qty = input(f"Hi {customer_name}. Apples cost ${correct_format_price} each. {question_text}")

        try:
            purchase_int_qty = int(get_purchase_qty)
            break
        except ValueError:
            print('Please enter a valid number.')
        
    print_formatted_message(customer_name, purchase_int_qty, correct_format_price)

#Start of the program.
sell_apple()
