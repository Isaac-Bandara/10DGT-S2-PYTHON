# Bits Calculator Task
# Author: Isaac Bandara
# Date: 9/11/2025
# Version 1

# This program takes user inputs of images, text, and integers and calculates the total number of bits within them.

# Makes reusable heading printer, where the heading is styled with the chosen surroudning decorations
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}\n")

# Forms reusable instructions function, which when called prints instructions
def instructions():
    statement_generator("Instructions","-")
    print('''This program takes inputs of different file types and calculates the number of bits needed to represent the data in uncompressed form.
After these instructions, you first enter your file type of an integer, image, or text.
Then, you enter the specifications of that file type, such as the integer, image dimensions, or text string, before the program calculates the bits needed.
''')

# Reusable function which gets user input of which file type they would like to work with
def get_filetype():

    # Makes it into a loop so that if the error message ends up being needed the user will be able to reenter
    # their chosen file type
    while True:

        # Gets user input for their chosen file type, and changes it to fully lowercase for ease of utilisation
        response = input("\nFile type: ").lower()

        # Returns response instantly if it is 'xxx' or 'i', which are certain inputs utilised later
        if response == "xxx" or response == "i":
            return response

        # For the following 3 elif statements the code returns either 'integer', 'image', or 'text' to whatever called the 
        # function based on whether the user inputted a variety of possible abbreviations of the file type as specified in the
        # square brackets of each statement.
        elif response in ["integer", "int"]:
            return "integer"

        elif response in ["image",'picture','img', 'p', 'pic']:
            return "image"

        elif response in ["text",'t','txt']:
            return "text"
        
        # Prints error message and returns no value, allowing the input to be tried again, if the input isn't a valid
        # file type or abbreviation
        else:
            print(f"Sorry {name}, please enter a valid file type.")

# Integer checker - reusable function to check that user integer inputs are valid
def int_check(question, low):
    
    # Forms reusable error message
    error = f"\nSorry {name}, please enter a number that is more than or equal to {low}\n"

    while True:

        try:
            # Ask the user for an input to the question specified when the function is called
            response = int(input(question))

            # Check that the number is more the lowest number allowed, which was specified when the function was called
            # Returning the input ends the loop
            if response >= low:
                return response
            
            # Prints error if response is not greater than the 'low'
            else:
                print(error)
        
        # Displays chosen error message for value errors
        except ValueError:
            print(error)

# Image Bit Calculator - function which calculates and returns the bits of an image based on user inputs when it is called
def image_calc():
    
    # Gets user inputs and checks them through above integer checker, with a lowest allowed number specified as 1
    width = int_check("Width (in pixels): ",1)
    height = int_check("Height (in pixels): ",1)

    # Calculates total number of pixels in the image
    num_pixels = width * height
    # Calculates total number of bits in image assuming a 24 bit colour representation
    num_bits = num_pixels * 24
    # Converts this to kB
    kb = num_bits / 1024

    # Stores the answer which will be printed along with the calculations it took to reach it,
    # and returns this value to what called the function
    answer = f"\nNumber of pixels: {width} x {height} = {num_pixels} pixels.\nNumber of bits: {num_pixels} x 24 = {num_bits} bits.\nNumber of kB (rounded to 2dp): {num_bits} / 1024 = {kb:.2f} kB.\n\nThere are {num_bits} bits in your image."
    return answer

# Text Bit Calculator - function which calculates and returns the bits of a string based on user inputs when it is called 
def text_calc():
    # Asks user to input their text
    response = input("Enter your text: ")
    
    # Counts the length (or number of characters) of the string,
    # and multiplies this by 8 bits per character to find total bits of the text
    num_chars = len(response)
    num_bits = num_chars * 8

    # Stores the answer which will be printed along with the calculations it took to reach it,
    # and returns this value to what called the function
    answer = f"\n'{response}' has {num_chars} characters.\nWe need {num_chars} x 8 bits to represent it, which is {num_bits} bits.\n\nThere are {num_bits} bits in '{response}'."
    return answer

# Integer Bit Calculator - function which calculates and returns the bits and binary representation
# of an integer based on user inputs when it is called 
def int_calc():
    
    # Gets user input and checks it through above integer checker, with a lowest allowed number specified as 0
    integer = int_check("Integer: ",0)
    
    # Convert the number to binary and work out the number of bits needed
    raw_bin = bin(integer)

    # Removes the leading '0b' from the raw binary conversion
    binary = raw_bin[2:]
    num_bits = len(binary)

    # Stores the answer which will be printed along with the binary form of the integer,
    # and returns this value to what called the function
    answer = f"\n{integer} in binary is {binary}. We need {num_bits} bits to represent it.\n\nThere are {num_bits} bits in {integer}."
    return answer

# Gets user input for their name, to personalise later outputs
name = input("Hello User! What is your name?\n")

# Sets variable of 'want_instruction' to the user's input, meaning that if they press enter the instructions will be displayed,
# following which they will be given the option to loop (or print them again) the instructions as many times as they wish,
# or to skip the instructions entirely.
want_instructions = input(f"Welcome, {name}, to this bits calculator!\nPress enter to view instructions or any key to continue. ")
while want_instructions == "":
    instructions()
    want_instructions = input("Press <enter> to view instructions or any other key to continue. ")

# Sets variable of 'keep_going" to nothing, and creates a loop so that as long as 'keep_going' is empty the code will repeat.
# This continues until a user inputs can either change 'keep_going' and end the loop, or leave it and repeat the program
keep_going = ""
while keep_going == "":

    # Calls file type function to find out what type of file the user wishes to operate with
    file_type = get_filetype()
    
    # Exit code of 'xxx' breaks while loop
    if file_type == 'xxx':
        break
    
    # If file type was entered by user as 'i', this clarifies whether the user was referring to an image or integer for later use.
    if file_type == 'i':
        want_image = input("Press enter for an integer or any other key for an image. ")
        if want_image == '':
            file_type = 'integer'
        else:
            file_type = 'image'
    
    # Clarifies with the user which file type they have chosen by printing it out
    print(f"\nYou chose a {file_type} file type.\n")

    # Depending on the file type returned, calls the appropriate function to calculate the total bits for each type,
    # and then prints this out
    if file_type == "image":            
        image_ans = image_calc()
        print(image_ans)

    elif file_type == "text":        
        text_ans = text_calc()
        print(text_ans)

    else:
        integer_ans = int_calc()
        print(integer_ans)

    # Gives user option to continue or loop program by leaving 'keep_going' at its value, or end the loop to quite the program
    # by entering something else.
    keep_going = input("\nPress <enter> to run program again, or any other key to exit. ")

# Prints farewell and thank you message
print(f"\nThank you, {name}, for using this bits calculator.\n")
