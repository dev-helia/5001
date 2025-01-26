def read(line:str):
    '''
    function:
    read the lines for one word a line with its index.
    input:
    one line
    output:
    print
    '''
    words = line.split()
    for i in range(len(words)):
        print(i,'.\t\t',words[i])

def main():
    read('This is a line.')
    read('哈 哈 哈 哈 哈哈')



if __name__ == '__main__':
    main()

punct = ''
word = sentance.split()
for i in range(len(word)):
    word[i] = word[i].strip(punct)
