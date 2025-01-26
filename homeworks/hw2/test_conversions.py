'''
    Problem 1
    Test for conversions.py
    
    TEST CASES:
    test_inches_to_mm:
    INPUT: 1.0 OUTPUT: 25.4
    INPUT: 0.0 OUTPUT: 0.0
    INPUT: -1.0 OUTPUT: -25.4
    INPUT: 0.5 OUTPUT: 12.7
    
    test_feet_to_fathom
    INPUT: 1.0 OUTPUT: 0.2
    INPUT: 25.5 OUTPUT: 4.2
    INPUT: 0.0 OUTPUT: 0.0
    INPUT: -25.5 OUTPUT: -4.2
'''

import conversions

def test_inches_to_mm(inches, expected):
    '''
        Function to validate inches_to_mm(inches)
        
        INPUT PARAMETERS:
        inches: 1-decimal-place float
        expected: 1-decimal-place float
        
    '''
    actual = conversions.inches_to_mm(inches)
    print('Converting {} inches to millimeters (mm)'.format(inches))
    print(f'result = {actual:.1f}')
    print('expected =', expected, '\n')

def test_feet_to_fathom(feet, expected):
    '''
        Function to validate feet_to_fathom(feet)
        
        INPUT PARAMETERS:
        feet: 1-decimal-place float
        expected: 1-decimal-place float
        
    '''
    actual = conversions.feet_to_fathom(feet)
    print('Converting {} feet to fathoms'.format(feet))
    print(f'result = {actual:.1f}')
    print('expected =', expected, '\n')

def main():
    '''
    validation of inches_to_mm(inches) and feet_to_fathom(feet)
    '''
    
    # validate inches_to_mm(inches)
    test_inches_to_mm(1.0, 25.4)
    test_inches_to_mm(0.0, 0.0)
    test_inches_to_mm(-1.0, -25.4)
    test_inches_to_mm(0.5, 12.7)

    # validate feet_to_fathom(feet)
    test_feet_to_fathom(1.0, 0.2)
    test_feet_to_fathom(25.5, 4.2)
    test_feet_to_fathom(0.0, 0.0)
    test_feet_to_fathom(-25.5, -4.2)


if __name__ == '__main__':
    main()
