
# 5. Write a Python program to find the substrings within a string.

#   Sample text :
  
#   'Python exercises, PHP exercises, C# exercises'
  
#   Pattern :
  
#   'exercises'
  
#   Note: There are two instances of exercises in the input string.



import re

print(re.findall('exercises', 'Python exercises, PHP exercises, C# exercises'))