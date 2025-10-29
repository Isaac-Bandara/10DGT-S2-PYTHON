# Fence Cost Calculator Task
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
print (f"\nWelcome, {name}, to this fencing perimeter and cost calculator. Please enter your dimensions below to begin calculations.")

keep_going = ""
while keep_going == "":

    # Get width, height, and cost per metre
    width = num_check("\nWidth: ")
    length = num_check("\nLength: ")
    cost = num_check("\nCost per metre of fencing ($): ")

    # Calculate perimeter and price for the fence
    perimeter = 2 * (width + length)
    price = perimeter * cost

    # Display output
    print()
    print(f"Perimeter: {perimeter} metres.")
    print(f"Price: ${price:.2f}.\n")

    # Ask user if they want to keep going
    keep_going = input("Press <enter> to repeat or any other key to quit. ")

# Farewells user
print(f"\nThank you {name} for using this fencing perimeter and cost calculator. Have an enjoyable day!")