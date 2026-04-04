"""
M02_list_of_honor.py

This app calculates if a student is on the honor roll based on their grades. 

Author: Andrés Succar

"""
while True:
    # Student's name
    name = input("Enter the student's name (or ZZZ to quit): ")
    
    # Exit condition
    if name == 'ZZZ':
        print("Exiting program...")
        break
    #Student's GPA
    try:
        gpa = float(input("Enter the student's GPA: "))
    except ValueError:
        print("invalid GPA. Please enter a number.\n")
        continue

    # Determine if the student is on the honor roll
    if gpa >= 3.5:
        print(f"{name} is on the Dean's List.\n")
    elif gpa >= 3.25:
        print(f"{name} is on the Honor Roll.\n")
    else:
        print(f"{name} did not qualify for honors.\n")