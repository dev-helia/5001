
import random
def gamestart():
    player = random.randint(0,1)
    computer = random.randint(0,1)
    print('Your number is', player)
    if player == 0:
        print('Your coin is head!')
    else:
        print('Your coin is tail')
    if player > computer:
        print('You win!')
    elif player < computer:
        print('You lose!')
    else:
        print('It is a draw')

def flip_coin():
    coin = random.randint(0,1)
    if coin == 0:
        return 'Heads'
    return 'Tails'


def main():
    gamestart()
    i = 0
    while i < 10:
        print(flip_coin())
        i += 1


if __name__ == '__main__':
    main()
