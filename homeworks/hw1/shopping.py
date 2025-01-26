'''
    CS5001
    Fall 2024
    HW1

    Tao He
    Online Shopping Program
'''

TWO_PAY_FEE = 0.05

def main():


    # Welcome the user
    print('Welcome to my Online Shopping Program!')

    # Get shopping details from the user
    product_name = input('Enter the product name: ')
    product_price = round(abs(float(input(
        f'What is the price of {product_name}? '))), 2)
    product_num = abs(int(input(
        f'How many {product_name}s are you purchasing? ')))
                            
    # Calculate the results
    total_price = product_price * product_num
    two_pay_price = (total_price * (1 + TWO_PAY_FEE)) / 2

    # Display the results
    print(f'You are buying {product_num} {product_name} '
          f'at ${product_price:.2f} each.')
    print(f'Total Cost for this shopping session is ${total_price:.2f}')
    print(f'Our 2-Pay plan is two equal payments of ${two_pay_price:.2f}')

if __name__ == "__main__":
    main()
