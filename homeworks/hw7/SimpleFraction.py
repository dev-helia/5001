'''
This is the implementation of SimpleFraction class in Python.
'''


class SimpleFraction:
    '''
    This is the SimpleFraction class.
    '''
    def __init__(self, numerator=1, denominator=1):
        '''
        This is the constructor of SimpleFraction class.
        '''
        self.numerator = numerator
        self.denominator = denominator
        self.validate()

    def get_numerator(self):
        '''
        This method returns the numerator of the fraction.
        '''
        return self.numerator

    def get_denominator(self):
        '''
        This method returns the denominator of the fraction.
        '''
        return self.denominator

    def make_reciprocal(self):
        '''
        This method returns the reciprocal of the fraction.
        '''
        if self.numerator == 0:
            raise ZeroDivisionError("Cannot make reciprocal of 0.")
        return SimpleFraction(self.denominator, self.numerator)

    def validate(self):
        '''
        This method validates if the numerator and denominator are integers.
        '''
        if (
            not isinstance(self.numerator, int) or
            not isinstance(self.denominator, int)
        ):
            raise ValueError("Numerator and denominator must be integers.")
        if self.denominator == 0:
            raise ZeroDivisionError("Denominator cannot be 0.")

    def multiply(self, other):
        '''
        This method returns the product of two fractions.
        '''
        if isinstance(other, SimpleFraction):
            self.validate()
            other.validate()
            return SimpleFraction(
                self.numerator * other.numerator,
                self.denominator * other.denominator
            )
        if isinstance(other, int):
            self.validate()
            return SimpleFraction(self.numerator * other, self.denominator)
        raise ValueError(
            "The second operand must be a SimpleFraction or an integer."
        )

    def divide(self, other):
        '''
        This method returns the quotient of two fractions.
        '''
        if isinstance(other, SimpleFraction):
            self.validate()
            other.validate()
            return SimpleFraction(
                self.numerator * other.denominator,
                self.denominator * other.numerator
            )
        if isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by 0.")
            self.validate()
            return SimpleFraction(self.numerator, self.denominator * other)
        raise ValueError(
            "The second operand must be a SimpleFraction or an integer."
        )

    def __str__(self):
        '''
        This method returns the string representation of the fraction.
        '''
        return str(self.numerator) + "/" + str(self.denominator)

    def __eq__(self, other):
        '''
        This method checks if two SimpleFraction instances are equal.
        '''
        return (
            self.numerator / self.denominator ==
            other.numerator / other.denominator
        )
