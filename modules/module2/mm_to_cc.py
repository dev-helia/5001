'''
    Problem 2
    Create a function named millimeters_to_cc
    
'''

import conversions

def millimeters_to_cc(length, width, height):
    '''
    Function: millimeters_to_cc(length, width, height)
    Given length & width in mm, and height in inches:
    return the volume of rainfall in cc, rounded to 1 decimal place.
    Result should be NON-NEGATIVE values only

    >>> millimeters_to_cc(0, 0, 0)
    0.0
    
    >>> millimeters_to_cc(1, 0, 0)
    0.0

    >>> millimeters_to_cc(0, 1, 0)
    0.0

    >>> millimeters_to_cc(0, 0, 1)
    0.0

    >>> millimeters_to_cc(100, 50, 2)
    1000.0

    >>> millimeters_to_cc(-100, 50, 2)
    1000.0
    
    '''
    height_mm = conversions.inches_to_mm(height)

    return round(abs((length * width * height_mm) / 1000), 1)
