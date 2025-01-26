
def broccoli_ice_cream():
    ''' if u like to try the brocolli ice cream? '''
    i = input('Do you like ice cream?(yes/no)').lower()
    if i == 'yes':
        print('Yay! So do I!')
    b = input('Do you like brocolli?(yes/no)').lower()
    if b == '1':
        print('I like it with cheese')
    else:
        print("But it's healthy")
    if i == '1' and b == '1':
        print('Time for a healthy broccoli ice cream sundae. Yum!')

def main():
    broccoli_ice_cream()

if __name__ == "__main__":
    main()
