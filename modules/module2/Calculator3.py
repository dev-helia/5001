'''
    Example 2: Without user defined function
    Speed of an object when it hits the ground
    Formula: v  = sqrt(v(i) ** 2 + (2 * a * d))

    Test case 1: Distance = 10, Vi = 0, Final Velocity = 14.0
    Test case 2: Distance = 55.5, Vi = 0, Final Velocity = 32.98
    
'''

#import math
import physics

def main():
    print("Final velocity calculator")

    # Read the height from which the object is dropped
    distance = float(input("What is the height/distance (in meters)"))
    
    

    # Display the result SIsHEWURU
    print('Object will hit ground at speed '
          f'of {physics.calculate_velocity(distance, 0):.1f} m/s')



if __name__ == "__main__":
    main()
