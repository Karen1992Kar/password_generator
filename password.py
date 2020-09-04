#!/usr/bin/env python3

"""
Մոդուլը
"""

import random
import string


def random_simbol_string(st):
    """Ֆունկցիան ստանում է տող, հետ է վերադարձնում այդ տողի խառը տասավորված
    տեսակը"""

    res = ""
    indexes = []

    while len(res) < len(st):
        index = random.randint(0, len(st)-1)
        if index not in indexes:
            res += st[index]
            indexes.append(index)

    return(res)


def check_natural_number(argument):
    """Ֆունկցիան ստուգում է արգումենտի բնական թիվ լինելը."""

    if not isinstance(argument, int) or isinstance(argument, bool) or \
        argument < 1:
        raise TypeError("Ֆունկցիան աշխատում է բնական թվի համար. "
                        "'{}'-ը չի համարվում բնական թիվ".format(argument))


def password(length):
    """ֆունկցիան ստանում է բնական թիվ, հետ է վերադարձնում գախտանբառ,որի
    երկարությունը համապատասխանում է  այդ թվի չափին"""

    check_natural_number(length)

    punctuation = string.punctuation
    alpha = string.ascii_letters

    result_rand_str1 = ''.join(random.choice(alpha[:26]) for i in
                               range(length-length//4-1))
    result_rand_str2 = ''.join(random.choice(alpha[26:]) for i in
                               range(length//4+1))
    result_rand_int = ''.join(str(random.randint(0,9)) for i in
                              range(length//4))
    result_rand_punt =''.join(random.choice(punctuation) for i in
                              range(length//4))

    result = result_rand_str1 + result_rand_str2 + result_rand_int +\
             result_rand_punt

    return random_simbol_string(result)


print(password(6))


