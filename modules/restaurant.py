def main():

    print("Hello!Welcome to Taotao Restaurant! There is our menu! Enjoy!")
    print("Chicken : $5 enter 1")
    print("Mediterranean set : $20 enter 2")
    print("Soy Milk : $2 enter 3")
    order = input("What would you like to order?")
    grand_food = 0
    if order == "1":
        grand_food = 5
    if order == "2":
        grand_food = 20
    if order == "3":
        grand_food = 2
    tax = grand_food * 0.08
    tip = grand_food * 0.18
    print(f"Thanks for ordering!The tax for your ordering is ${tax:.02f}, your tip is ${tip:.02f},and the total is ${grand_food + tip:.02f}")
    print("Enjoy your food!😁")
if __name__ == '__main__':
    main()