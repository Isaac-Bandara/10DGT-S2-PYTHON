# Finding Factors Task
# Author: Isaac Bandara
# Date: 10/11/2025
# Version 1

# Creates function to be called upon when the user enters their value to check the validity of the input
def num_check(question):
    
    # Forms reusable error message
    error = f"\nSorry {name}, please enter an integer from 1 to 10000."

    while True:
    
        # Ask the user for a number and instantly returns it to what called the function if is the exit code 'xxx'
        response = input(question)
        if response == 'xxx':
            return response

        try:
            # Converts the user input to an integer; will procure ValueError message if impossible
            response = int(response)
            # Check that the number is between the two parameters
            # Returning the input ends the loop
            if 0 < response < 10001:
                return response
            
            # Prints error if response is not within the parameters
            else:
                print(error)
        
        # Shows chosen error message for value errors
        except ValueError:
            print(error)

# Creates function to be called upon with the user's input number to calculate its factors - reusable
def factor_calc(number):
    # Forms empty list in which the factors will be stored when calculated
    all_factors = []
       
    # For all numbers from 1 to 1 more than the square root of the number
    for i in range (1,int(number**0.5)+1):
        # If the 'i' number divides 'number' so that it leaves no remainder
        if number % i == 0:
            # The factor pair will be found by dividing the original number by the first found factor
            pair = number // i
            # And then these as a pair will be added to the previously empty list
            all_factors.append((i,pair))
    # Which will all be returned as a list to what called the function
    return all_factors


# Gets user input for their name to personalise later outputs
name = input("Hello User! What is your name?\n")

# Sets variable of 'want_instruction' to the user's input, meaning that if they press enter the instructions will be displayed,
# following which they will be given the option to loop (or print them again) the instructions as many times as they wish,
# or to skip the instructions entirely.
want_instructions = input(f"\nWelcome, {name}, to this Finding Factors program!\nPress enter to view instructions or any key to continue. ")
while want_instructions == "":
    print("\nEnter an integer from 1 to 10000, press <enter>, and let the program do the magic!\nThis program will not only print out all the factors of the input, but also whether it is a perfect square, unity, prime, or composite number.")
    want_instructions = input("\nPress <enter> to view instructions again or any other key to continue. ")

# Sets variable of 'keep_going" to nothing, and creates a loop so that as long as 'keep_going' is empty the code will repeat.
# This continues until a user inputs can either change 'keep_going' and end the loop, or leave it and repeat the program
keep_going = ""
while keep_going == "":

    # Gets user input of the integer they wish to factorise, and runs it through the number checker to ensure its validity
    to_factor = num_check("\nPlease enter an integer: ")

    # Exits loop if the exit code is returned
    if to_factor == 'xxx':
        print("\nExit code accepted.")
        break
 
    # Otherwise if the number being factorised is 1, it will be returned to the user with a message stating that it is called a unity (and a description)
    elif to_factor == 1:
        print("This number is called a unity.\nIt's only factor is 1.")
   
    # If neither an exit code or the number 1, the new variable 'factors' will be set to the output (a list of factors) of the factor calculating function
    else:
        factors = factor_calc(to_factor)
        # Message is printed listing the factor pairs for the user's input
        print(f"The factor pairs of {to_factor} are:\n{factors}")

        # After ouputting the factor pairs, it is checked if the number is a perfect square, and if it is, a special message is printed
        # This is check by square-rooting the number, then rounding it to a whole integer (for perfect squares this will already be an integer),
        # then squaring this integer.
        # If this integer form of the square root gives is equal to the original number when squared, it is a perfect square and the message is printed.
        if int(to_factor ** 0.5) ** 2 == to_factor:
            print(f"{to_factor} is a perfect square.")
       
        # If there is only one pair of factors (ie 1 and the number), it must be prime (only having two factors), so a special message is printed
        elif len(factors) == 1:
            print(f"{to_factor} is a prime number; it has only two factors.")

        # If none of the above, the number must be composite, so this message is printed
        else:
            print(f"{to_factor} is a composite number.")

    # Gives user option to continue or loop program by leaving 'keep_going' at its value, or end the loop to quite the program
    # by entering something else.
    keep_going = input("\nPress <enter> to run program again, or any other key to exit. ")

# Prints personalised farewell message
print(f"\nThank you {name} for using this Finding Factors program.\n")
