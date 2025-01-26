'''
def menu(message):

    return input(message).upper()
'''

def window(question, option_a, option_b, option_c, option_d):
    question = (f'{question}\n'
        f' A: {option_a}\n B: {option_b}\n C: {option_c}\n'
        f' D: {option_d}\n Your answer: ')
    answer = input(question).upper()
    print('You selected: ', answer)


def main():
    window('How do you like to keep active?', 'Running',
           'Birdwatching', 'Swimming', 'Does laying on a couch count?')
    
if __name__ =="__main__":
    main()
