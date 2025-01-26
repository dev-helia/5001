from mbta_data import WORKING_LINES 
from mbta_data import T_LINES

def preprocess_data():
    ''' Function preprocess data
        Mutate the WORKING_LINES list to create a list of lists with the
        SAME data as T_LINES, but HOMOGENIZED such that all elements are
        UPPERCASED
    '''
    for line in T_LINES:  
        new_line = []
        for station in line:
            new_line.append(station.upper()) 
        WORKING_LINES.append(new_line) 

def is_valid_station(station, line):
    ''' Function is_valid_station
        Input: a T station (string), a T line (string)
        Returns: boolean
        Does: Looks for the station in all the lists,
            returns True if found for the line, False otherwise
    '''
    for working_line in WORKING_LINES:
        if working_line[0] == line.upper() and station.upper() in working_line:
            return True
    return False

def get_num_stops(start, end, line):
    ''' Function get_num_stops
        Input: two T stations (must be on the same line), strings
        Returns: number of stops between the two, a positive integer
    '''
    # Homogenize inputs
    start = start.upper()
    end = end.upper()
    
    # Find the line in WORKING_LINES
    for working_line in WORKING_LINES:
        if working_line[0].upper() == line.upper():
            # Validate the start and end
            if start in working_line and end in working_line:
                for i in range(len(working_line)):
                    if working_line[i] == start:
                        start_idx = i
                    if working_line[i] == end:
                        end_idx = i
                
                return abs(start_idx - end_idx)
    return 0

def get_direction(start, end, line):
    ''' Function get_direction
        Input: start and end stations (both strings), and a line (string)
        Returns: the final stop in the direction
        from start to end (a string)
        
        Does: Finds the line both stops are on.
        Counts the number of stops from start to end.
        If it's negative, return the first station from that
        line, otherwise return the final station.
        If the line is invalid or not found, return a string "line not found"
        If the destination or start is not found, return "no destination found"
    '''
    # Homogenize inputs
    start = start.upper()
    end = end.upper()
    
    # Find the line in WORKING_LINES
    for working_line in WORKING_LINES:
        if working_line[0].upper() == line.upper():
            # Validate the start and end
            if start in working_line and end in working_line:
                # Find the indices of start and end
                for i in range(len(working_line)):
                    if working_line[i] == start:
                        start_idx = i
                    if working_line[i] == end:
                        end_idx = i  
                # Determine direction based on index comparison
                if start_idx > end_idx:
                    return working_line[0]  
                else:
                    return working_line[-1]   
            else:
                return "no destination found"
    return "line not found"
