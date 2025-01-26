'''
    An example of DocTest for Python
'''

def foo(x):
    '''
        Return the value passed in, added to 1.
        
        >>> foo(1)
        999
    '''
    return x + 1

def main():
    print(foo(2))

if __name__ == '__main__':
    #main()
    import doctest
    doctest.testmod()  # test the module's documentation
