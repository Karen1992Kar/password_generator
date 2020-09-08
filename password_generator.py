#!/usr/bin/env python3

"""
Հրամանը ստանում է 1 բնական թիվ, հետ է վերադարձնում այդ թվի չափին համապատասխանող
երկարության գախտնաբառ
"""


import random
import argparse
import string


def constrained_sum_sample_pos(quantity, total):
    """Ֆունկցիան վերադարձնում է quantity բնական թվի երկարության ցուցակ,
    որի անդամները պատահական թվեր են, և այդ թվերի գումարը հավասար է total ի"""

    count_type_args = []

    dividers = sorted(random.sample(range(1, total), quantity - 1))

    for a, b in zip(dividers + [total], [0] + dividers):
        count_type_args.append(a-b)

    return count_type_args


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

    punctuation = string.punctuation
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    ints = string.digits

    div_length = constrained_sum_sample_pos(4, length)

    # TODO: the algorithm needs to be improved. Currently upper case, integers
    # and punctuations max size is predictable.
    r_low = ''.join(random.choice(uppers) for i in range(div_length[0]))
    r_upp = ''.join(random.choice(lowers) for i in range(div_length[1]))
    r_int = ''.join(random.choice(ints) for i in range(div_length[2]))
    r_punt =''.join(random.choice(punctuation) for i in range(div_length[3]))

    result = r_low + r_upp + r_int + r_punt

    return ''.join(random.sample(result,len(result)))


if __name__ == "__main__":
    num = parse_input_argument()
    print(password_generator(num))
