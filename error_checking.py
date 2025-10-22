# Error checking
# Author: Isaac Bandara
# Date: 22/10/2025
# Version 1

# Code that tests whether a valid input is given  (V1)
'''done = False   # Boolean variable set to False
while not done:
    num = int(float(input("Please enter your value: ")))
    done = True
    
print(f"The number that you entered is {num}.")'''

# Code that tests whether a valid input is given  (V1.1)
# Use the try and except method to catch errors
'''done = False
while not done:
    try: # This method tries for a valid input
        num = float(input("Please enter a number: "))
        done = True

    except ValueError:
        print("That is not a valid float. \n")

print(f"The number that you entered is {num}.")'''

# Code that tests whether a valid input is given  (V1.2)
# Create a function to call every time I ask the user
# for a number. A function is a chunk of code that does
# something.
# Functions can be used over and over again.
# To use a function (call it), write out its name with
# parentheses at the end.
# To create a function, start with the word def
'''def test_int_num():
    done = False
    while not done:
        try:
            num = int(input("Please enter a number (integer): "))
            done = True
        
        except ValueError:
            print("That is not a valid integer number. \n")

    print(f"The number that you entered is {num}.")

# Main routine
test_int_num() # This calls the function so that we can use it'''

# Code that tests whether a valid input is given (v1.3)
# Use the function parameters to make my code more
# pythonic.

def test_int(question): # 'question' is a placeholder
    done = False
    while not done:
        error = "That is not a valid number."
        print(question)
        try:
            num = int(input())
            done = True

        except ValueError:
            print(error)
    
    return(num) # Gives back the value of num so that I can use it outside of the function.

# Main routine
num1 = test_int("Please enter your first number.")
print(f"Your first number entered is {num1}")

num2 = test_int("Please enter your second number.")
print(f"The second number you entered is {num2}")

sum = num1 + num2
print(f"Your numbers added together equal to {sum}")