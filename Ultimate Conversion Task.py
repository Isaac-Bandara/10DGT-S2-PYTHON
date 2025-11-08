# Ultimate Conversion Task
# Author: Isaac Bandara
# Date: 30/10/2025
# Version 1

# Makes one main dictionary containing sub-dictionaries for the different measurement types,
# with the units of measurement and assigned values to each inside.
conversion_dict = {
    "distance_dict": {
        "mm": 1000,
        "cm": 100,
        "m": 1,
        "km": 0.001
    },
    
    "mass_dict": {
        "mg": 1000000,
        "g": 1000,
        "kg": 1,
        "T": 0.001
    },
    
    "time_dict": {
        "ms": 86400000,
        "s": 86400,
        "mins": 1440,
        "h": 24,
        "d": 1,
        "w": 1/7,
        "y": 1/365.25
    },

    "volume_dict": {
        "mL": 1000,
        "L": 1,
        "kL": 0.001,
        "ML": 0.000001
    }
}

# Creates function to be called upon when the user enters their value to check the validity of the input
def num_check(question):
    
    # Forms reusable error message
    error = f"\nSorry {name}, please enter a number that is greater than 0."

    while True:

        try:
            # Ask the user for a number
            response = float(input(question))

            # Check that the number is more than 0
            # Returning the input ends the loop
            if response > 0:
                return response
            
            # Prints error if response is not > 0
            else:
                print(error)
        
        # Shows chosen error message for value errors
        except ValueError:
            print(error)

# Like the number checker above, forms callable function to check validity of user-inputted units
def unit_check(question):
    
    while True:
        # Gets input from user for the question specified when the function is called
        response = input(question)

        # The variable 'unit_dict' is set to each sub-dictionary (one at a time) within the main 'conversion_dict'
        for category in conversion_dict:
            unit_dict = conversion_dict[category]

            # It is checked whether the user's input is in each sub-dictionary, and when it is found in one both the
            # response and the category it was found in are returned, ending the loop
            if response in unit_dict:
                return category, response
            
        # Prints error message if the user input is not found in any of the sub-dictionaries
        print("That is not a valid unit of measurement. Please enter a correctly capitalised unit in abbreviated form.")


# MAIN SEQUENCE

# Asks user their name
name = input("Hello user! What is your name? \n")

# Welcoming user
print(f"Welcome, {name}, to this Ultimate Conversion Calculator! ")

# Presets reusable string to query if instructions are wanted
instr = "Press <enter> to view instructions, or any other key to begin. \n"

# Sets variable 'instructions' to the user's input to the question stated above
instructions = input(instr)

# Running instructions and allowing them to loop
# (based on whether or not the user changes the value of the 'instructions' variable)
while instructions == "":
    print("First, enter the value then the unit you are converting from, and then the unit which you are converting to. \nThis calculator works for measurements of Time, Distance, Mass, and Volume. \nPlease provide units of measurement in abbreviated (or minimised) form.\n")
    instructions = input(instr)

# Creates a loop for the user inputting system, allowing it to be repeated after completion
keep_going = ""
while keep_going == "":
    # Get amount / inputs
    amount = num_check("\nValue: \n")

    # Calls 'unit_check' function to validate the inputted unit of measurement and find the sub-dictionary
    # for both the 'From' and 'To' units.
    from_category, from_unit = unit_check("\nFrom unit? \n")
    to_category, to_unit = unit_check("\nTo unit? \n")

    if from_category == to_category:
        # Multiply to get our standard value (eg the 'm' is set to 1)
        multiply_by = conversion_dict[to_category][to_unit]
        standard = amount * multiply_by

        # Divide to get our desired value (for converting between units uninclusive of the standard value of 1)
        divide_by = conversion_dict[from_category][from_unit]
        answer = (standard / divide_by)

        # Print answer
        print(f"\nThere are {answer:.6f} {to_unit} in {amount} {from_unit} (rounded to 6 decimal places).")

    # If the calculation is not possible print error message
    else:
        print("Those two units can not be converted between.")

    # Give option to quit or repeat code based on input into 'keep_going' (the dependent of the current loop)
    keep_going = input("\nPress <enter> to run again or any other key to quit.")

# Prints farewell
print(f"\nThank you, {name}, for using this units conversion calculator.")