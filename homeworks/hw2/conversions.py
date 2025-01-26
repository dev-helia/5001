"""
    Homework 2:
    Functions and Testing
    conversions.py
    This module contains the length conversion functions that you must use
    for the homework. Call these functions with the correct parameters
    when converting from inches to millimeters, or when converting from
    feet to fathoms. Further conversion calculations may need to be provided
    by you, but these are the basic functions you MUST use for this assignment.
    Notes:
        1. Do NOT copy/paste these functions into your solution. Import the
        funcntions as appropriate. If you copy/paste this code into your
        solution, marks will be deducted from your assignment.
"""



INCHES_TO_MM = 25.4
FEET_TO_FATHOMS = 1/6


def inches_to_mm(inches):
    """
    Given inches as the input parameter, this function returns the result of
    converting that length to millimeters, rounded to 1 decimal place.
    No alteration of the signage is performed: negative values remain negative.
    """
    return round((inches * INCHES_TO_MM), 1)



def feet_to_fathom(feet):
    """
    Given feet as the input parameter, this function returns the result of
    converting that length to fathoms, rounded to 1 decimal place.
    No alteration of the signage is performed: negative values remain negative.
    """
    return round((feet * FEET_TO_FATHOMS), 1)

