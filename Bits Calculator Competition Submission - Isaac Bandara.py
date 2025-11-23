# Bits Calculator Competition Submission
# Author: Isaac Bandara
# Date: 19/11/2025
# Version 2

'''
This program calculates the number of bits in image, integer, and text file types based on user inputs.
This program is written to do the above effectively in the minimum possible amount of code, so the following abbreviations of variable names mean:
l: loop
ft: file type
r: response
w: width
h: height
i: integer
ic(q, l): integer_checker(question, low)
Below the following version of the code - which is the shortest possible I could make it - is a more Pythonically formatted copy (commented out), not strictly as short as I could make it, though.
'''

def ic(q, l):
    try: assert (r := int(input(q))) >= l; return r
    except (ValueError, AssertionError): print(f"Enter number that greater than or equal to {l}."); return ic(q, l)
while (l := input('\nBits calculator:\nCalculates bits in different file types\nEnter <r> to run or anything else to quit. ')) == 'r':
    if (ft := input('Enter t for text file, i for integer, or p for picture/image:\n')) == 't': print(f"There are {len(r := input('Enter your text: ')) * 8} bits in '{r}'.")
    elif ft == 'p': print(f'There are {(w := ic('Width (in pixels): ',1)) * (h := ic('Height (in pixels): ',1)) * 24} bits in your image.')
    elif ft == 'i':i = ic("Integer: ",0);print(f'After converting {i} to binary, we need {len(bin(i)[2:])} bits to represent it.')
    else: print('Invalid file type.')

'''
Total script: 8 lines
Total script length: 796 characters
Script length excluding white spaces: 655 characters
'''


# Pythonic copy:

'''
def ic(q, l):
    try: assert (r := int(input(q))) >= l; return r
    except (ValueError, AssertionError): print(f"Enter number that greater than or equal to {l}"); return ic(q, l)
while (l := input('\nBits calculator:\nCalculates bits in different file types\nEnter <r> to run or anything else to quit. ')) == 'r':
    if (ft := input('Enter t for text file, i for integer, or p for picture/image:\n')) == 't':
        print(f"There are {len(r := input('Enter your text: ')) * 8} bits in '{r}'.")
    elif ft == 'p':
        print(f'There are {(w := ic('Width (in pixels): ',1)) * (h := ic('Height (in pixels): ',1)) * 24} bits in your image.')
    elif ft == 'i':
        i = ic("Integer: ",0);print(f'After converting {i} to binary, we need {len(bin(i)[2:])} bits to represent it.')
    else: print('Invalid file type.')
'''