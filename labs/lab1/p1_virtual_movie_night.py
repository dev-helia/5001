'''
    CS5001
    Lab 1
    Fall 2024
    Tao He
    Movie Calculation
'''
#注意计算的在assign value 后面。
#python是按照顺序的
#以及注意除法产生的小数位要${total_price_after_discount:0.2f}

def main():
    
    #Initialize the constant
    TICKET_PRICE = 7.95
    POPCORN_PRICE = 8.95
    DRINK_PRICE = 4.25
    DISCOUNT = 0.90
    

    #Get the user's input
    tickets = int(input("How many tickets do you want?"))
    popcorns = int(input("How many buckets of popcorn?"))
    drinks = int(input("How many drinks?"))

    # Calculate the total price
    total_price = TICKET_PRICE * tickets + POPCORN_PRICE * popcorns + DRINK_PRICE * drinks
    total_price_after_discount = (TICKET_PRICE * tickets + POPCORN_PRICE * popcorns + DRINK_PRICE * drinks) * DISCOUNT

    #Output the result
    print(f'Total cost is ${total_price}')
    print(f'Your price after the discount is: ${total_price_after_discount:0.2f}')
    
    
    
if __name__ == '__main__':

    main()
    