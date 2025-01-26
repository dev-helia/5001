FPS_TO_MPH = 0.681818

def fps_to_mph(speed : float) -> float:
    """
    Converts speed from miles per hour to feet per second.
    1.round to 1 decimal place
    2.negative number not allowed
    
    Parameters: 
    speed (float): a superhero's speed in feet-per-second (fps)
    
    Returns:
    float: the speed converted to miles-per-hour (mph)

    """
    speed = abs(speed) * FPS_TO_MPH
    return round(speed, 1)

def update_hero_team(hero : str, speed : float, team : list) -> None:
    """
    Given input parameters hero (a string), speed (a Float) and team (a list),
    Update the superhero list with member details. 
    Use Uppercase.
    
    Parameters:
    hero (str): name of the superhero
    speed (float): speed of the superhero in miles per hour
    team (list): list of superheroes and their details
    
    Returns:
    None

    """
    if hero.upper() not in team:
        team.append(hero.upper())
        team.append(speed)
    else:
        hero_index = team.index(hero.upper())
        team[hero_index + 1] = speed
        
        
def conga_line(_list : list) -> list:
    """
    For each inner list, calculate the sum of the integers. 
     Add each of those summated values together to produce a grand total. 
     
    Parameters:
    _list (list): list of lists containing integers
     
    Returns:
    list: Add a list of ONE element: the grand total you've calculated 
    as a member of a COPY of the incoming parameter list.
     
    """
    total_sum = 0
    new_list = _list.copy()
    
    if not _list:
        return [[0]]
        
    total_sum = sum([sum(inner) for inner in _list])
    return new_list + [[total_sum]]

def uniques(first : str, second : str) -> str: 
    """
    Given two strings, return a string containing only the unique characters from both strings. 
    
    Parameters:
    first (str): first string
    second (str): second string    
     
    Returns:
    str: string containing only the unique characters from both strings.
     
    """
    unique_string = ""
    for char in first:
        if char not in second and char not in unique_string:
            unique_string += char
    for char in second:
        if char not in first and char not in unique_string:
            unique_string += char
    return unique_string

def count_odds(_list : list) -> int:
    """
    This function returns the total count of odd integers in a list. 

    Parameters:
    _list (list): list of integers
    
    Returns:
    int: total count of odd integers in the list.
    """
    if not _list:
        return 0
    count = 0
    for num in _list:
        if num % 2!= 0:
            count += 1
    return count

def bin_flip(bits : str) -> str:
    """
    This function flip 1's to 0 and 0's to 1. 

    Parameters:
    bits (str): string only contains 0's and 1's
    
    Returns:
    string: string from flipped bits
    """
    flipped_bits = ""
    for bit in bits:
        if bit == "0":
            flipped_bits += "1"
        else:
            flipped_bits += "0"
    return flipped_bits

     
     
         
         
             