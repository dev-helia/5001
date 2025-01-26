'''
    Example 1: Without user defined function
    Speed of an object when it hits the ground
    Formula: v  = sqrt(v(i) ** 2 + (2 * a * d))

    Test case 1: Distance = 10, Vi = 0, Final Velocity = 14.0
    Test case 2: Distance = 55.5, Vi = 0, Final Velocity = 32.98
    
'''



GRAVITY = 9.8

def main():
    print("Final velocity calculator")

    # Read the height from which the object is dropped
    distance = float(input("What is the height/distance (in meters)"))
    
    initial_velocity = 0
    
    final_velocity = math.sqrt(initial_velocity ** 2 +
                               (2 * GRAVITY * distance))

    # Display the result
    print('Object will hit ground at speed '
          f'of {final_velocity:.1f} m/s')


if __name__ == "__main__":
    main()
