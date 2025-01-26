"""
Age Minder in-class example
CS 5001 Fall 2024
Author: Tao He
"""


def main():
    """
        This docString is a comment for a function
    """

    #Input the information of the user.
    name = input("What is your name? ")
    age  = int(input("What is your age? "))
    age = abs(age)

    #Output the results.
    print(f"Hello {name}!")
    print(f"This year you are {age} years old.And next year you are {age+1} years old.😭")
    print(f"That is your {age//10} decades")
    

if __name__ == '__main__':
    main()
