from menu import menu

def main():
    question = ('How do you like to keep active?\n'
        ' A: Running\n B: Birdwatching\n C: Swimming\n'
        ' D: Does laying on a couch count?\n Your answer: ')
    answer = menu(question).upper()
    print('You selected: ', answer)


if __name__ =="__main__":
    main()
