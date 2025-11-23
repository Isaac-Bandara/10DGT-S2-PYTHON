# Ultimate Conversion Task
# Author: Isaac Bandara
# Date: 17/11/2025
# Version 2

'''
This program calculates conversions between units of distance (d), mass (m), and time (t) based on user inputs.
This program is written to do the above effectively in the minimum possible amount of code, so the following abbreviations of variable names mean:
l: loop
ct: conversion type
md: master_dictionary
v: value
fu: from_unit
tu: to_unit
uc(q, ct): unit_checker(question, conversion_type)
Final competition submission:
'''

md = {'d': {"mm": 1000,"cm": 100,"m": 1,"km": 0.001},'m': {"mg": 1000000,"g": 1000,"kg": 1,"T": 0.001},'t': {"ms": 86400000,"s": 86400,"mins": 1440,"h": 24,"d": 1,"w": 1/7,"y": 1/365.25}}
def uc(q,ct): 
    while (u := input(q)) not in md[ct]: print('Invalid unit.')
    return u
while (l := input('\nUnits conversion calculator:\nEnter <r> to run program, or anything else to quit. ')) == 'r':
    while (ct := input('Enter d for distance conversions; m for mass; t for time\n')) not in md: print('Invalid type.')
    while True:
        try: v = float(input('Conversion value: ')); assert v > 0; break
        except (ValueError, AssertionError): print('Enter a number greater than 0.')
    print('Units:',', '.join(md[ct])); fu = uc(f'Convert from:',ct); tu = uc(f'Convert to:',ct); a = v*md[ct][tu]/md[ct][fu]; print(f'{v} {fu} is equal to {a:.8f} {tu} (to 8 decimal places).')

'''
Total script: 10 lines
Total script length: 880 characters
Script length excluding white spaces: 736 characters
'''


# ROUGH COMMENTS
#
#
# Master dictionary with sub-dictionaries for each conversion type labelled by their first letters
# 'md' stands for master dictionary
#
# Function to be called upon to check validity of inputted units. 'uc' stands for unit checker
# When called takes values for the 'q' question and 'ct' type of conversion
#
# Takes input with question prompt. If this unit is within the chosen sub-dictionary, it will be returned and the function ended.
# If not an error message will be given and the while loop within the function will start again and reprompt.
# Variable 'u' stands for 'unit' and is set to the user's input
#
# Main sequence as a loop for repeatability
#
# 'v' is for the value variable of the user's input, which is taken, checked as a float, retried if it isn't one,
# if it is one less than or equal to 0 than the error is given and it is tried again,
# otherwise it will be accepted and the loop broken.
#
# 'ct' variable stands for 'conversion type', as in what type of measurements you wish to convert with (ie distance, mass, or time)
# This is taken as an input, and if the input for the type is not an option within the master dictionary,
# an error message is given and the program will loop. Otherwise, valid inputs will be accepted.
#
# Prints out the list from within the selected dictionary after it has been approved as being within the master dictionary.
# Each item in this chosen dictionary is joined with a ', '.
# 
# Variables 'fu' and 'tu' refer to 'from_unit' and 'to_unit', meaning the units from which the user wishes to convert from and to.
# To receive each a function is called, to which the prompt and selected sub-dictionary is sent
# 
# Variable 'a' stands for 'answer' and calculates the final answer to be given to the user.
# The calculation for this is the same as the original extended form from the tutorial,
# only condensed to one line by substituting values of variables straight into the final equation.
# 
# Prints final response / calculation to the user
# 
# Variable 'l' stands for loop, and if the user does not enter for the input the required letter 'r' to run again,
# the loop will break and the program will end. 
