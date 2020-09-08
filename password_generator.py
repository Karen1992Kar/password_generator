#!/usr/bin/env python3

"""
Հրամանը ստանում է 1 բնական թիվ, հետ է վերադարձնում այդ թվի չափին համապատասխանող
երկարության գախտնաբառ
"""

import numpy
import random
import argparse
import string

PUNCTUATION = string.punctuation
LOWERS = string.ascii_lowercase
UPPERS = string.ascii_uppercase
INTS = string.digits


def generator_random_simbols(total):
    """Ֆունկցիան վերադարձնում է quantity բնական թվի երկարության ցուցակ,
    որի անդամները պատահական թվեր են, և այդ թվերի գումարը հավասար է total ի"""

    all_types = [PUNCTUATION, LOWERS, UPPERS, INTS]

    rand_simbols = [random.choice(PUNCTUATION), random.choice(LOWERS),\
           random.choice(UPPERS), random.choice(INTS)]

    for _ in range(total - 4):
        index = random.randint(0, 3)
        rand_simbols.append(random.choice(all_types[index]))

    return rand_simbols


def parse_input_argument():
    """Ֆունկցիան ստուգում է հրամանին ուղարկված արգումենտները"""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('argument', type=int, help="բնական թիվ")
    parser = parser.parse_args()

    return parser.argument


def check_the_size_number(number):
    "ֆունկցիան ստուգում է իրեն փոխանցած արժեքի 7 ից մեծ լինելը"

    if number < 8:
        raise ValueError("ֆունկցիաին փոխանցած թիվը պետք է մեծ լինի 7 ից")


def check_natural_number(argument):
    """Ֆունկցիան ստուգում է արգումենտի բնական թիվ լինելը."""

    if not isinstance(argument, int) or isinstance(argument, bool) or \
        argument < 1 and argument != 0:
        raise TypeError("Ֆունկցիան աշխատում է բնական թվի համար. "
                        "'{}'-ը չի համարվում բնական թիվ".format(argument))


def password_generator(length):
    """ֆունկցիան ստանում է բնական թիվ, հետ է վերադարձնում գախտանբառ,որի
    երկարությունը համապատասխանում է  այդ թվի չափին"""

    check_natural_number(length)
    check_the_size_number(length)
    result = generator_random_simbols(length)
    # TODO: the algorithm needs to be improved. Currently upper case, integers
    # and punctuations max size is predictable.

    return ''.join(random.sample(result,len(result)))


if __name__ == "__main__":
    num = parse_input_argument()
    print(password_generator(num))
