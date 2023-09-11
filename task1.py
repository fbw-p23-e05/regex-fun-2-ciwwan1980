
#1. Write a Python program to check for a number at the end of a string.


import re


#+ is a quantifier that matches one or more occurrences of the preceding element, which in this case is the digit character class [0-9].
# $ still represents the end of the string anchor, which mandatory for $ sign.

input_string = input("Enter a string: ")
# pattern = "\d+$" this is the same as below one
pattern = "[0-9]+$"

match = re.findall(pattern, input_string)
print(match)
#  in this case, when there is no digit, match will be zero, and then it will print else part
if len(match) > 0:
    print("A number is at the end of the string.")
else:
    print("No number at the end of the string.")


