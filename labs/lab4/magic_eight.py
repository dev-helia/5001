from random import randint
    
RESPONSES = ['As I see it, yes.', ' Ask again later.', 'Better not tell you now.',

            'Cannot predict now.', 'Concentrate and ask again.',

            'Don’t count on it.', 'It is certain.',

            'It is decidedly so.', 'Most likely.', 'My reply is no.',

            'My sources say no.', 'Outlook not so good.',

            'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.',

            'Very doubtful.', 'Without a doubt.', 'Yes.',

            'Yes – definitely.', 'You may rely on it.']

def main():
    print('Welcome to my magic book.\nEnter your question')
    question = input('What is on your mind?(print q to quit)')
    while question != 'q':
        answer = RESPONSES[randint(0,19)]
        print(answer)
        question = input('What is on your mind?(print q to quit)')
    
    
    
    
    
if __name__ == '__main__':
    main()