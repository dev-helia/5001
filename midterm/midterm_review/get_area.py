'''

'''
import math


def get_area(shape, para):
    '''

    '''

    if shape == 'circle'.upper():
        return math.pi * para ** 2
    elif shape == 'square'.upper():
        return para ** 2
    return -1

