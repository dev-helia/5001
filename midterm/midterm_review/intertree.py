'''
simulte zip()
'''

def interleave(x, y):
    '''

    '''
    # same length
    l = len(x)

    # define new return list
    ans = []

    # iterate and concact
    for i in range(l):
        ans.append(x[i]+y[i])

    return ans