"""
M03_lab_lists_AndresSuccar.py
Author: Andres Succar

This program demonstrates the use of lists in Python. 

It creates a class of vehicles, performs various operations on the list, and prints the results.

"""

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, make, model, year, doors, roof):
        super().__init__("car")
        self.make = make
        self.model = model
        self.year = year
        self.doors = doors
        self.roof = roof

def main():
    print("Enter the details of the automobile:\n")

    # Get user input for the automobile details
    make = input("Make: ")
    model = input("Model: ")
    
    # Validate year input
    while True:
        year = input("Year: ")
        if year.isdigit() and 1886 <= int(year) <= 2024:
            year = int(year)
            break
        print("Invalid input. Please enter a valid year between 1886 and 2024.")
    # Validate doors input  
    while True:
        doors = input("Number of doors (2 or 4): ")
        if doors in ['2', '4']:
            doors = int(doors)
            break
        print("Invalid input. Please enter 2 or 4.")

    # Validate roof input
    while True:
        roof = input("Roof type (solid or sun roof): ").lower()
        if roof in ['solid', 'sun roof']:
            break
        print("Invalid input. Please enter 'solid' or 'sun roof'.")

    # Create Automobile object
    car = Automobile(make, model, year, doors, roof)

    # Output results
    print("\nVehicle Information:")
    print(f"Vehicle type: {car.vehicle_type}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Year: {car.year}")
    print(f"Number of doors: {car.doors}")
    print(f"Roof type: {car.roof}")

 # Run the app
if __name__ == "__main__":
    main()