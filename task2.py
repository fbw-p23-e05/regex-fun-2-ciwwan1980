

# 2. Write a Python program to search for numbers (0-9) of length between 1 and 3 in the given string.

# "Exercises number 1, 12, 13, and 345 are important"

# input_string = "Exercises number 1, 12, 13, and 34544 are important"



import re

text = "Exercises number 1, 12, 13, and 34544 are important"

pattern = "\d{1,3}"
matches = re.findall(pattern, text)

print(matches)
# Output: ['123', '456', '7', '789', '01']
