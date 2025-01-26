import hw4data

def decode(data: list) -> list:
    '''
    Function:
        decode the RLE-coded values
    Parameter: 
        a list containing RLE-coded values
        strings and integers are interleaved in the list
    Return:  
        a list containing the decoded values with the “runs” expanded
    '''
    
    # Define the parameter
    decoded_data = []
    
    # Iterate the data
    # Strings are laid on the even indices
    for i in range(0, len(data), 2):
        # Integers are laid on the odd indices
        new_decoded_data = [data[i]] * data[i + 1]
        decoded_data.extend(new_decoded_data)
    
    # Return the decoded data
    return decoded_data