'''
dictionary example
'''

def build_dict(a,b):
    logos = {}
    for i, word in enumerate(a):
        logos[word] = b[i]      
    return logos
                
        
def main():
    english = ['hello', 'world']
    korean = ['안녕하세요', '세계']
    translator = {}
    translator[(english, korean) ] = build_dict(english, korean)
    print(translator)
    
    word = input("Enter a word in English/EXIT to quit: ")
    while word.upper != 'EXIT':
        if word.lower() in translator:
            print(f'Translated word is {translator[(english, korean)][word.lower()]}')
        else:
            print(f'Word not found in dictionary')       
        word = input("Enter a word in English/EXIT to quit:: ")

if __name__ == '__main__':       
    main()                                      