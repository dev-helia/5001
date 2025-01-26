'''
    CS5001
    Lab 1
    Fall 2024
    Tao He
    Car Expense
'''

#Define the constant
INSURANCE_PER_MONTH = 1600/12
MAINTAINANCE_RATE = 0.005

def main():
    
    #Get User's input
    miles = float(input("How many miles per month do you drive?"))
    price_per_gallon = float(input("What is the average price of a gallon of gas?"))
    miles_per_gallon = float(input("How many miles per gallon does your car get on average?"))

    #Compute the total expense
    total_expense = (INSURANCE_PER_MONTH + miles * MAINTAINANCE_RATE 
    + miles * price_per_gallon / miles_per_gallon)
    
    #Ouput the result
    print(f'Your total expense per month is ${total_expense:0.2f}')
    
if __name__ == "__main__":
    main()
    
    