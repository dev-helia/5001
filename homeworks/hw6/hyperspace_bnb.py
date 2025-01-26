'''
This program is used to book a week in a hyperspace bnb.
'''

import os

BOOKING_FEE = 500
OUTPUT_FILE = 'bookings.txt'

def load_travelers(travelers_file_name):  
    '''
    Loads the travelers data from a file and returns 
    a dictionary of travelers.
    
    Args:
        travelers_file_name (str): The name of the file 
        containing the travelers data.
    
    Returns:
        dict: A dictionary of travelers, where the keys are the 
        user IDs and the values are dictionaries containing the 
        name and credits of the traveler.
    '''
    travelers = {}
    try:
        with open(travelers_file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    name, user_id, credits = line.split('@')
                    travelers[user_id] = {
                        'name': name,
                        'credits': int(credits)
                    }
    except FileNotFoundError:
        print(f"Error: The file does not exist.")
    return travelers

def process_requests(travelers, request_file_name):
    '''
    Processes the requests data and books the requested weeks.
    Args:
        travelers (dict): A dictionary of travelers, where the keys are the 
        user IDs and the values are dictionaries containing the 
        name and credits of the traveler.
        request_file_name (str): The name of the file containing the 
        requests data.
    Returns:
        None
    '''
    # Initialize set of booked weeks
    booked_weeks = set()
    
    try:
        with open(request_file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    user_id, week = line.split()
                    week = int(week)

                    # Check if traveler exists
                    if user_id in travelers:
                        traveler = travelers[user_id]
                        # Check if week is already booked
                        if week not in booked_weeks:
                            # Check credits
                            if traveler['credits'] >= BOOKING_FEE:
                                traveler['credits'] -= BOOKING_FEE
                                booked_weeks.add(week)
                                with open(OUTPUT_FILE, 'a') as booking_file:
                                    booking_file.write(
                                        f"{week} - {user_id} " 
                                        f"- {traveler['name']}\n"
                                    )
                            else:
                                print(
                                    f"{traveler['name']} ({user_id}) "
                                    f"does not have enough credits."
                                )
                        else:
                            print(f"Week {week} is already booked.")
                    else:
                        print(f"User ID {user_id} not found "
                              "in travelers data.")
    except FileNotFoundError:
        print(f"Error: The file '{request_file_name}' does not exist.")