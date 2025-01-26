class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_subtotal(self):
        return sum(item.price for item in self.items)

    def calculate_tax(self, tax_rate=0.08):
        return self.calculate_subtotal() * tax_rate

    def calculate_tip(self, tip_rate=0.18):
        return self.calculate_subtotal() * tip_rate

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_tax() + self.calculate_tip()

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_menu_item(self, item):
        self.menu.append(item)

    def show_menu(self):
        print(f"Welcome to {self.name}! Here is our menu:")
        for index, item in enumerate(self.menu, 1):
            print(f"{index}. {item}")

    def take_order(self):
        order = Order()
        while True:
            self.show_menu()
            choice = input("Please enter the number of the item you'd like to order (or 'done' to finish): ")
            if choice.lower() == 'done':
                break
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.menu):
                    order.add_item(self.menu[index])
                    print(f"{self.menu[index].name} added to your order!")
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Please enter a valid number.")
        return order

def main():
    # 创建餐厅并添加菜单项
    restaurant = Restaurant("Taotao Restaurant")
    restaurant.add_menu_item(MenuItem("Chicken", 5))
    restaurant.add_menu_item(MenuItem("Mediterranean set", 20))
    restaurant.add_menu_item(MenuItem("Soy Milk", 2))

    # 处理订单
    order = restaurant.take_order()
    subtotal = order.calculate_subtotal()
    tax = order.calculate_tax()
    tip = order.calculate_tip()
    total = order.calculate_total()

    print(f"\\nThanks for ordering! Your subtotal is ${subtotal:.2f}.")
    print(f"Tax: ${tax:.2f}, Tip: ${tip:.2f}")
    print(f"Your total is ${total:.2f}. Enjoy your food! 😁")

if __name__ == '__main__':
    main()
