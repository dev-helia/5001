'''
    CS5001
    Fall 2024
    HW1

    Tao He
    Bike Shop Program

    Test Cases:
    Inputs:0,0,100 Output:0,0,0,100
    Inputs:100,0,0 Output:0,100,0,0
    Inputs:0,100,0 Output:0,0,100,0
    Inputs:50,50,50 Ouput:1,48,49,0
    
'''

def main():

    # Get the spare parts from the customer
    wheels = abs(int(input('How many wheels do you have? ')))
    frames = abs(int(input('How many frames do you have? ')))
    links = abs(int(input('How many links do you have? ')))
    
    # Calculate the bikes can make
    bikes = min(wheels // 2, frames, links // 50)

    # Calculate the leftovers
    left_wheels = wheels - bikes * 2
    left_frames = frames - bikes
    left_links = links - bikes * 50

    # Print the results
    print('Total bikes I can make:', bikes)
    print("I'm keeping the leftovers for myself")
    print(f'Leftover:\n{left_wheels} wheels\n{left_frames} '
          f'frames\n{left_links} links')

if __name__ == "__main__":
    main()
