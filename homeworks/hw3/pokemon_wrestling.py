import random

def get_player(number):
    """ 
    Returns the name of the Pokemon associated with the numbering scheme 
    described. Any value 'out of bounds' returns Diglett by default.
    """
    if number == 1:
        return 'Bulbasaur'
    elif number == 2:
        return 'Charmander'
    elif number == 3:
        return 'Butterfree'
    elif number == 4:
        return 'Rattata'
    elif number == 5:
        return 'Weedle'
    elif number == 6:
        return 'Pikachu'
    elif number == 7:
        return 'Sandslash'
    elif number == 8:
        return 'Jigglypuff'
    elif number == 9:
        return 'Raichu'
    else:
        return 'Diglett'

def roll_dice():
    """
    Returns a random integer in the range 2..12 (inclusive).
    """
    return random.randint(2, 12)

def is_power_up_active(number):
    """
    Returns True or False based on the 'power-up' rules.
    The parameter value passed in is the value from a valid roll
    of the dice to determine the power-up status.
    """
    return number == 7 or number == 11

def check_battle(computer, player):
    """
    Determines the winner of the 1-1 matchup.
    Returns 'COMPUTER', 'PLAYER', or 'DRAW!' based on the power scores.
    """
    if computer > player:
        return "COMPUTER"
    elif player > computer:
        return "PLAYER"
    else:
        return "DRAW!"

def main():
    """
    Main function to run the Pokemon Arm Wrestling Tournament.
    """
    # Initialize
    user_wins = 0
    computer_wins = 0
    
    # Welcome the user
    print("Welcome to the Pokemon Arm Wrestling Tournament!")

    # User chooses a team
    user_team = input('What team do you want to (red or blue)? ').upper()
    if user_team == "RED":
        computer_team = "BLUE"
    else:
        computer_team = "RED"

    # Pokemon wrestling
    while True:
        # Choose pokemon
        user_pokemon = get_player(random.randint(1, 10))
        computer_pokemon = get_player(random.randint(1, 10))
        print(f'{user_team} pokemon {user_pokemon} vs {computer_team} '
              f'pokemon {computer_pokemon}')
        
        # Game start
        print('Highest dice roll wins. If you don\'t roll,'
              'we\'ll end the match.')
        roll = input('Roll the dice for your character (y/n)? ')
        if roll == 'y':
            # Roll dice
            user_roll = roll_dice()
            computer_roll = roll_dice()
            
            # Power up
            if is_power_up_active(user_roll):
                print(f'*** {user_pokemon} gets POWER-UP!')
                user_roll += 1
                
            if is_power_up_active(computer_roll):
                print(f'*** {computer_pokemon} gets POWER-UP!')
                computer_roll += 1

            # Show results
            print(f'{user_pokemon} rolls {user_roll}. {computer_pokemon} '
                  f'rolls {computer_roll}')
            result = check_battle(computer_roll, user_roll)
            if result == "PLAYER":
                user_wins += 1
                print(f"Your {user_team} wins with {user_pokemon}")
            elif result == "COMPUTER":
                computer_wins += 1
                print(f"My {computer_team} wins with {computer_pokemon}")
            else:
                print("It's a draw! No winner!")

            # Play again
            again = input('\nPlay again? (y/n) ')
            if again != 'y':
                print('You selected to end the match early.')
                print('Arm Wrestling Tournament has ended.')
                print(f'{user_team} team: {user_wins} \t {computer_team} '
                      f'team: {computer_wins}')
                final_result = check_battle(computer_wins, user_wins)
                if final_result == "PLAYER":
                    print("You win! Congrats!")
                elif final_result == "COMPUTER":
                    print("You lose! Great game!")
                else:
                    print("DRAW! We are tied! Great game!")
                break
            
        else:
            print('You selected to end the match early.')
            print('Arm Wrestling Tournament has ended.')
            print(f'{user_team} team: {user_wins} \t {computer_team} '
                  f'team: {computer_wins}')
            final_result = check_battle(computer_wins, user_wins)
            if final_result == "PLAYER":
                print("You win! Congrats!")
            elif final_result == "COMPUTER":
                print("You lose! Great game!")
            else:
                print("DRAW! We are tied! Great game!")
            break

if __name__ == "__main__":
    main()
