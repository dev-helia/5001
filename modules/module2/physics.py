import math

GRAVITY = 9.8

def calculate_velocity(distance, initial_velocity):
    '''
    This function calculates the final velocity of an object,
    given the distance it travels before stopping & it's initial velocity
    Input: distance, initial_velocity -> float
    Output: the final velocity -> float
    '''
                                
    return math.sqrt(initial_velocity ** 2 + (2 * GRAVITY * distance))

