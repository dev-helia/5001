'''
    CS 5001
    problem about acrostic
'''
from labs.lab5.acrostic_data import DREAM, POEM


def print_acrostic(poem_and_column):
    '''
    function:

    input:

    output:

    '''
    poem = poem_and_column[0]
    column = poem_and_column[1]
    poem_split = poem.split('\n')
    char_list = []
    for line in poem_split:
        if line == '':
            char_list.append(' ')
        else:
            char_list.append(line[column])
    ans = ''.join(char_list)
    return ans

    #return "".join([ line[column] for line in poem_split] )

def main():
    acrostics = [[POEM, 0], [DREAM, 3]]
    for each in acrostics:
        print(print_acrostic(each))

if __name__ == '__main__':
    main()

