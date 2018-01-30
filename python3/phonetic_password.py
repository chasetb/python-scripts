#!/usr/bin/env python3

__author__ = ['[Brandon Amos](http://bamos.github.io)', '[Chase Thompson-Baugh](https://amoreopensource.wordpress.com)']
__date__ = '2014.02.14'

"""
Obtain the NATO phonetic alphabet representation from short phrases or passwords

```
$ phonetic.py Github/1
G - Golf
i - india
t - tango
h - hotel
u - uniform
b - bravo
/ - Forward Slash
1 - One
```
"""

import sys

phonetic_table = {
    'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliet',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray',
    'y': 'yankee', 'z': 'zulu',
}

# Contains ASCII characters found in passwords
symbol_table = {
    '~': 'Tilde', '`': 'Back tick', '!': 'Exclamation Mark', '@': 'At Symbol', 
    '#': 'Hash', '$': 'Dollar sign', '%': 'Percent', '^': 'Caret', '*': 'Star',
    '(': 'Open Parenthesis', ')': 'Close Parenthesis', '-': 'Hyphen', '_': 'Underscore',
    '+': 'Plus', '=': 'Equal', '{': 'Open Brace', '}': 'Close Brace', '[': 'Open Bracket',
    ']': 'Close Bracket', '|': 'Pipe', '\\': 'Backslash', '/': 'Forward Slash', ':': 'Colon', 
    ';': 'Semicolon', '"': 'Double Quote', '\'': 'Single Quote', '<': 'Less Than', 
    '>': 'Greater Than', ',': 'Comma', '.': 'Period', '?': 'Question Mark', '&': 'Ampersand'
}

number_table = {
    '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', 
    '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '0': 'Zero'
}

for word in sys.argv[1:]:
    for char in word:
        title = False
        if char.istitle():
            title = True
        char = char.lower()
        if char not in phonetic_table:
            if char not in symbol_table:
                if char not in number_table:
                    print('Please define: {}'.format(char))
                else:
                    print("{0} - {1}".format(char, number_table[char]))
            else:
                print("{0} - {1}".format(char, symbol_table[char]))
        else:
            if title:
                print("{0} - {1}".format(char.upper(), phonetic_table[char].title()))
            else:
                print("{0} - {1}".format(char, phonetic_table[char]))
