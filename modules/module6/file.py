import os.path
def write_file(filename, additional_msg):
    with open(filename, 'w') as f:  
        f.write('Holton is fantasitic!')
        f.write('Yes she is!')
        f.write(additional_msg)          
    print(f'File {filename} has been written.')                 

def read_msg(filename):
    with open(filename, 'r') as f:
        for each in f:
            print(each.strip('/n'))
