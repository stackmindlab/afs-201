
def get_product_description():
    #STRING RETURNED WITH THE PRODUCT DESCRIPTION.
    return input("Please enter a product: ")

def get_product_quantity(description):
    #RETURNS THE QUANTITY AND SAVED AS AN INTEGER TYPE NUMBER.
    return int(input(f"How many of ({description}) are being purchased?"))

def get_product_price():
    #RETURNS THE PRODUCT PRICE AS A FLOAT.
    return float((input("What is the regular price? ")))

def format_number(price, zero):
    #HELPER FUNCTION TO OUTPUT PRICE CORRECTLY.
    return f"{price:.{zero}f}"

def get_discount_value(product_price):
    #RETURNS A DISCOUNT VALUE AFTER CALCULATING THE INITIAL PRICE.
    price_one = float(19.99)
    price_two = float(39.99)
    discount_percentage = 0

    if(product_price > price_two ):
        discount_percentage = .25
    elif(product_price > price_one):
        discount_percentage = .15
    discount_value = product_price * discount_percentage
    return discount_value

def calculate_state_tax(total_purchase):
    #CALCULATE THE STATE TAX AFTER CALCULATING THE TOTAL_PURCHASE PRICE.
    sales_tax = float(0.065)
    sales_tax_value = sales_tax * total_purchase
    return sales_tax_value

def total_amount(total_amount):
    #RECEIPT FUNCTION TO PRINT NICELY. (MAYBE NOT USED IN FINAL SUBMISSION).
    return f"${format_number(total_amount, 1)}"

def print_receipt(qty, description, price, sales_tax, total_due, total_saved):
    
    print("YOUR RECEIPT")
    print("--------------------")
    print(f"{qty} {description} @ ${price} each.")
    print(f"Sales Tax ${sales_tax:.{2}f}")
    print(f"TOTAL AMOUNT DUE ${total_due:.{2}f} TODAY")
    print(f"You saved ${total_saved:.{2}f} today")

def init():
    product_description = get_product_description()
    product_quantity = get_product_quantity(product_description)
    product_price = get_product_price()
    discount_amount_value = get_discount_value(product_price)
    state_tax = calculate_state_tax( product_price - discount_amount_value)
    print_receipt(
        product_quantity, 
        product_description,  
        product_price  - discount_amount_value,
        state_tax * product_quantity,
        ((product_price - discount_amount_value) * product_quantity) + state_tax * product_quantity ,
        product_quantity * discount_amount_value    
        )

init()




