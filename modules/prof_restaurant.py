def main():
    TAX_RATE = 0.08
    TIP_RATE = 0.18

    #Get the cost of the meal from the user
    cost = float(input('Enter the cost of the meal$ :'))

    #Compute the tax and tip
    tax = cost * TAX_RATE
    tip = cost * TIP_RATE
    total = cost + tax + tip

    #Print the final value
    print(f"The tax is ${tax:.2f}. The tip is ${tip:.2f}")
    print(f"The total cost is ${total:.2f}")

if __name__ == '__main__':
    main()