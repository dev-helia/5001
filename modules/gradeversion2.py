'''
Grades version2
Allows for grade entry by semester, uses meta data
NB: There is a BETTER WAY coming... with dictionaries later.
But for now...
'''

def main():
    # data schema
    grades = [] # empty list for grades. This time will be nested
    
    my_grade = float(input('Enter a grade, negative to stop:'))
    while my_grade >= 0:
        semester = input('Which semester(F24, SP23, etc.)')
        found = False # flag for finding appropriate list for semester
        for each in grades:
            if semester.upper() in each: # nested list exists in grades
                each.append(my_grade) # add new grade in list
                found = True # found list that has metadata
                break
            # else is not right here
        if not found: # aka gound is False
            grades.append([semester.upper(),my_grade])
        my_grade = float(input('Enter a grade, negative to stop:'))
    
if __name__ == '__main__':
    main()