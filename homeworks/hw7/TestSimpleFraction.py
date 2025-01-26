'''
This is a unit test file for SimpleFraction.py.
'''
import unittest
from SimpleFraction import SimpleFraction  

class SimpleFractionTest(unittest.TestCase):
    '''
    This is a class for unit testing SimpleFraction.py.
    '''
    
    def test_initialization(self):
        '''
        This is a test case for testing the initialization of SimpleFraction.
        '''
        fraction = SimpleFraction(3, 4)
        self.assertEqual(fraction.numerator, 3)
        self.assertEqual(fraction.denominator, 4)

    def test_invalid_initialization(self):
        '''
        This is a test case for testing the initialization of SimpleFraction with invalid inputs.
        '''
        with self.assertRaises(ValueError):  
            SimpleFraction(3.5, 4)
        with self.assertRaises(ValueError):  
            SimpleFraction(3, "4")
        with self.assertRaises(ValueError):  
            SimpleFraction("3", 4)
        with self.assertRaises(ValueError):  
            SimpleFraction(3, 0)

    def test_make_reciprocal(self):
        '''
        This is a test case for testing the make_reciprocal method of SimpleFraction.
        '''
        fraction = SimpleFraction(3, 4)
        reciprocal = fraction.make_reciprocal()
        self.assertEqual(reciprocal.numerator, 4)
        self.assertEqual(reciprocal.denominator, 3)
        with self.assertRaises(ZeroDivisionError):
            fraction = SimpleFraction(0, 4)
            reciprocal = fraction.make_reciprocal()

    def test_multiply_with_fraction(self):
        '''
        This is a test case for testing the multiply method of SimpleFraction with another SimpleFraction.
        '''
        fraction1 = SimpleFraction(2, 3)
        fraction2 = SimpleFraction(3, 4)
        result = fraction1.multiply(fraction2)
        self.assertEqual(result.numerator, 6)
        self.assertEqual(result.denominator, 12)
        
        

    def test_multiply_with_integer(self):
        '''
        This is a test case for testing the multiply method of SimpleFraction with an integer.
        '''
        fraction = SimpleFraction(2, 3)
        result = fraction.multiply(4)
        self.assertEqual(result.numerator, 8)
        self.assertEqual(result.denominator, 3)

    def test_divide_with_fraction(self):
        '''
        This is a test case for testing the divide method of SimpleFraction with another SimpleFraction.
        '''
        fraction1 = SimpleFraction(3, 4)
        fraction2 = SimpleFraction(2, 3)
        result = fraction1.divide(fraction2)
        self.assertEqual(result.numerator, 9)
        self.assertEqual(result.denominator, 8)

    def test_divide_with_integer(self):
        '''
        This is a test case for testing the divide method of SimpleFraction with an integer.
        '''
        fraction = SimpleFraction(3, 4)
        result = fraction.divide(2)
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 8)
        with self.assertRaises(ZeroDivisionError):
            fraction = SimpleFraction(3, 4)
            result = fraction.divide(0)

    def test_zero_denominator(self):
        '''
        This is a test case for testing the initialization of SimpleFraction with zero denominator.
        '''
        with self.assertRaises(ValueError):
            SimpleFraction(3, 0)

    def test_equality(self):
        '''
        This is a test case for testing the equality of two SimpleFractions.
        '''
        fraction1 = SimpleFraction(1, 2)
        fraction2 = SimpleFraction(2, 4)
        self.assertTrue(fraction1 == fraction2)

    def test_string_representation(self):
        '''
        This is a test case for testing the string representation of SimpleFraction.
        '''
        fraction = SimpleFraction(3, 4)
        self.assertEqual(str(fraction), "3/4")

# Run the tests
if __name__ == "__main__":
    unittest.main()
