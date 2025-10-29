# Area Perimeter Task
# Author: Isaac Bandara
# Date: 29/10/2025
# Version 1

def num_check(question):
    
    error = f"\nSorry {name}, please enter a number that is greater than 0."

    while True:

        try:
            # Ask the user for a number
            response = float(input(question))

            # Check that the number is more than 0
            if response > 0:
                return response
            else:
                print(error)
        
        # Ignores value errors
        except ValueError:
            print(error)


# Main routine

# Welcoming user
name = input("\nHello user! What is your name?\n")
print (f"\nWelcome, {name}, to this perimeter and area calculator. Please enter your dimensions below to begin calculations.")

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("\nWidth: ")
    height = num_check("\nHeight: ")

    # Calculate area and perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print()
    print(f"Perimeter: {perimeter} units.")
    print(f"Area: {area} square units.\n")

    # Ask user if they want to keep going
    keep_going = input("Press <enter> to repeat or any other key to quit. ")

# Farewells user
print(f"\nThank you {name} for using this area / perimeter calculator. Have an enjoyable day!")
