# Coffee Program
# Creating an input system for our coffee program
# Isaac Bandara
# Date: 17/10/2025

# TODO: Ask the user whether they like coffee
#       Record the answer
#       Give a response back to the answer

# Version 1
# Ask the user whether they like coffee or not

'''like_coffee = input("Do you like coffee?")
print(f'Your answer was "{like_coffee}".')
if like_coffee == "yes" or "Yes":
    print("That's great! I like coffee too!")
else:
    print("You're missing out! Why not give it a try?")'''


# Version 2
# While lopp

'''keep_going = ""
while keep_going == "":
    like_coffee = input("Do you like coffee?")
    
    if like_coffee == "yes" or like_coffee == "Yes" or like_coffee == "y" or like_coffee == "Y":
        print("That's great! I like coffee too!")
        keep_going = "Finished"
    elif like_coffee == "no" or like_coffee == "No" or like_coffee == "N" or like_coffee == "n":    
        print("You're missing out! Why not give it a try?")
        keep_going = "Finished"
    
    else:print("I don't understand")'''


# Version 3
# Making the program more pythonic.
def coffee_program():
    keep_going = ""
    while keep_going == "":
        # Convert answer to lowercase using .lower()
        like_coffee = input("Do you like coffee?\n").lower()
        
        if like_coffee == "yes" or like_coffee == "y":
            print("That's great! I like coffee too!")
        
        elif like_coffee == "no" or like_coffee == "n":
            print("You're missing out! Why not give it a try?")

            like_tea = input("Do you like tea instead\n").upper()
            if like_tea == "YES" or like_tea == "Y":
                print("Good for you. Give coffee another try. :)")
            
            elif like_tea == "NO" or like_tea == "N":
                print("I am sorry. That's all I have for now.")
            
            else:
                print("I don't understand. Please answer with either a 'Yes' or a 'No'.")

        else:
            print("I don't understand. Please answer with either a 'Yes' or a 'No'.")

        keep_going = input("Press <ENTER> to continue, or any other key to quit. Thanks!\n")

if __name__ == "__main__":
    coffee_program()