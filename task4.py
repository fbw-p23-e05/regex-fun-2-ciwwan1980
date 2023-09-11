
# 4. Write a Python program to search for a literal string in a string and also find the location within the original string where the pattern occurs.

#   Sample text : 'The quick brown fox jumps over the lazy dog.'
#   Searched words : 'fox'

import re

print(re.search('fox', 'The quick brown fox jumps over the lazy dog'))