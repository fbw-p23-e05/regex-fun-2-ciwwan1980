# 3. Write a Python program to search for literal strings within a string.
#   Sample text : 'The quick brown fox jumps over the lazy dog.'
#   Searched words : 'fox', 'dog', 'horse'


import re

text = 'the quick brown fox jumps over the lazy dog.'
words=['fox', 'dog', 'horse']

for word in words: 
    print(f'Searching for "{word}" in "{text}" ->')
    if re.search(word, text):
            print('Matched!')
    else:
         print('Not Matched!')