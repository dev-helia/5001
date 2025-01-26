from music import PLAYLIST, SONGS
import copy

def display_menu():
    '''
    Function: Display the menu of the program
    '''
    print("ReMix–Master:")
    print("L: Load a different song")
    print("T: Title of current song")
    print("S: Substitute a word")
    print("P: Playback your song")
    print("R: Reverse it!")
    print("X: Reset to original song")
    print("Q: Quit?")
    
def removePunctuation(song: list) -> list:
    '''
    Function: Remove the punctuation from the song
    Input:
    song: A song - a list containing multiple strings
    Output:
    A song - a list containing multiple strings 
    without punctuation
    '''
    punctuation = ['.', '?', ':', ',', '!']
    for i in range(len(song)):
        cleand_line = [char for char in song[i] if char not in punctuation]
        song[i] = ''.join(cleand_line)

# def substitute(song: list, old_word: str, new_word: str) -> bool:
#     '''
#     Function:
#     Substitute individual words of the song with a different word 
#     of the user’s choosing.
#     If the user tries to replace a word that does not exist, 
#     print an error message and do not change the song.

#     Input:
#     song: A song - a list containing 
#     multiple strings
#     old_word: str - The word to be substituted
#     new_word: str - The word to substitute

#     Output: bool - If the song could 
#     be substituted(ignore the punctuation)
#     '''
#     # Check if the song can be changed
#     exist = False
    
#     for line in song:
#         for word in line.split():
#             if old_word.lower() in word.lower():
#                 exist = True
#                 break
        
#     if not exist:
#         return False

#     # Replace the old word
#     for i in range(len(song)):
#         song[i] = song[i].replace(old_word, new_word)
    
#     # Remove the punctuation
#     removePunctuation(song)

#     return True

def substitute(song: list, old_word: str, new_word: str) -> bool:
    '''
    Function:
    Substitute individual words of the song with a different word 
    of the user’s choosing.
    If the user tries to replace a word that does not exist, 
    print an error message and do not change the song.

    Input:
    song: A song - a list containing 
    multiple strings
    old_word: str - The word to be substituted
    new_word: str - The word to substitute

    Output: bool - If the song could 
    be substituted(ignore the punctuation)
    '''


    # Check if the song can be changed
    exist = False
    
    for line in song:
        # Split line into words and check for the exact match
        words = line.split()
        for word in words:
            if word.lower() == old_word.lower():
                exist = True
                break
        if exist:
            break
        
    if not exist:
        return False
    # Remove punctuation first
    removePunctuation(song)
    
    # Replace the old word with the new word
    for i in range(len(song)):
        # Split the line into words, replace only full matches
        song[i] = ' '.join(new_word if word.lower() == old_word.lower()
                           else word for word in song[i].split())
    
    return True


def reverse_it(song: list) -> list:
    '''
    Function:
    Reverse the song so that the words (not letters!) 
    are in the reverse order

    Input:
    song: A song - a list containing multiple strings

    Output:
    reversed_song: A song - a list after reversing the song
    '''
    # Remove the punctuation
    removePunctuation(song)

    # Reverse the song
    return [' '.join(line.split()[::-1]) for line in song]

def load_song(selection: int) -> list:
    '''
    Function:
    Load a song from our list of songs

    Input:
    selection: int - The index of the song to load

    Output:
    the song in our list
    '''
    song_index = selection - 1
    if song_index < 0 or song_index >= len(SONGS):
        return []
    return [SONGS[song_index], PLAYLIST[song_index]]  

def main():
    '''
    Function: Main function to do the main program job.'
    '''
    # Default 
    user_choice = 1
    current_song = copy.deepcopy(load_song(user_choice))
    
    # Main loops
    remix = True
    
    while remix:
        # print(current_song)
        # print('\n')
        # print(SONGS)
        display_menu()
        choice = input("Your choice: ")
        # Quite the program 
        if choice.lower() == 'q':
            remix = False
            print('Thank you for using ReMix-Master!')
        # Load a different song 
        elif choice.lower() == 'l':
            user_choice = int(input("Enter the number of "
                                    "the song you want to load: "))
            current_song = load_song(user_choice)
            while not current_song:
                print('Error: Invalid song number. Please try again.')
                user_choice = int(input("Enter the number of "
                                        "the song you want to load: "))
                current_song = load_song(user_choice)
            print('Successfully loaded the song.')
        # Show the tile
        elif choice.lower() == 't':
            print('-🎵' * 10)
            print('You are remixing the song:', current_song[1])  
        # Substitute a word 
        elif choice.lower() == 's':
            old_word = input("What word do you "
                             "want to substitute? ")
            new_word = input("What new word do you want"
                             " to substitute it with? ")
            if substitute(current_song[0], old_word, new_word):  
                print('You have successfully substituted the word.')
            else:
                print('Error: The word to be replaced does'
                      ' not exist in the song. Remix Failed.') 
        # Play the song           
        elif choice.lower() == 'p':
            print('Here is the remix of your song, enjoy!')
            for line in current_song[0]:  
                print(line)
            print('-🎵' * 10)
        # Reverse the song  
        elif choice.lower() == 'r':
            current_song[0] = reverse_it(current_song[0])  
            print('You have successfully reversed the song.')
        # Reload the song
        elif choice.lower() == 'x':
            current_song = load_song(user_choice)
            print('Successfully reloaded the song.')
        else:
            print('Invalid choice. Please try again.')
               
        print('\n')

if __name__ == "__main__":
    main()
