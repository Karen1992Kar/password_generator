#!/usr/bin/env python3

import random
import string

"""
Մոդուլը
"""

for i in rand:
    print(i)



def password(argument):
    """pass"""
    password = ""

    punctuation = string.punctuation
    string = string.ascii_letters

    rand = {random.randint(0,10), random.choice(string[:26]),
            random.choice(string[26:]), random.choice(punctuation)}
    for i in range(argument):
        password += 1


