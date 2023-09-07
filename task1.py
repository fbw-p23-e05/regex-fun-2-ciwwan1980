
#1. Write a Python program to check for a number at the end of a string.

import re

input_string = input("Enter a string: ")
#Hello234 match
# 1212212 match
#  hello therr 33333 match
# d is for any digit, + to insure there is a number at least one time or more, $ insure its at ending of th string
pattern = "\d+$"

match = re.search(pattern, input_string)

if match:
    print("A number is at the end of the string.")
else:
    print("No number at the end of the string.")
