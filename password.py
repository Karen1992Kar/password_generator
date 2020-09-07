#!/usr/bin/env python3

"""
Հրամանը ստանում է 1 բնական թիվ, հետ է վերադարձնում այդ թվի չափին համապատասխանող
երկարության գախտնաբառ
"""

import random
import argparse
import string


def parse_input_argument():
    """Ֆունկցիան ստուգում է հրամանին ուղարկված արգումենտները"""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('argument', type=int,
                        help="բնական թիվ")
    parser = parser.parse_args()

    return parser.argument


def check_the_size_number(number):
    "ֆունկցիան ստուգում է իրեն փոխանցած արժեքի 7 ից մեծ լինելը"

    if number < 8:
        raise ValueError("ֆունկցիաին փոխանցած թիվը պետք է մեծ լինի 7 ից")


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
    check_the_size_number(length)

    punctuation = string.punctuation
    alpha = string.ascii_letters

    # TODO: the algorithm needs to be improved. Currently upper case, integers
    # and punctuations max size is predictable.
    result_rand_str2 = ''.join(random.choice(alpha[26:]) for i in
                              range(random.randint(1, length//4+1)))
    result_rand_int = ''.join(str(random.randint(0,9)) for i in
                              range(random.randint(1, length//4+1)))
    result_rand_punt =''.join(random.choice(punctuation) for i in
                              range(random.randint(1, length//4+1)))
    result_rand_str1 = ''.join(random.choice(alpha[:26]) for i in
                              range(length-len(result_rand_punt +
                                    result_rand_str2 + result_rand_int)))

    result = result_rand_str1 + result_rand_str2 + result_rand_int +\
             result_rand_punt

    return ''.join(random.sample(result,len(result)))


if __name__ == "__main__":
    num = parse_input_argument()
    print(password(num))
