#!/usr/bin/env python3

"""
Հրամանը ստանում է 1 բնական թիվ, հետ է վերադարձնում այդ թվի չափին համապատասխանող
երկարության գախտնաբառ
"""

import random
import argparse
import string

PUNCTUATION = string.punctuation
LOWERS = string.ascii_lowercase
UPPERS = string.ascii_uppercase
INTS = string.digits


#TODO: Move this function up
def parse_input_argument():
    """Ֆունկցիան ստուգում է հրամանին ուղարկված արգումենտները"""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('argument', type=int, help="բնական թիվ")
    parser = parser.parse_args()

    return parser.argument


def check_natural_number(argument):
    """Ֆունկցիան ստուգում է արգումենտի բնական թիվ լինելը."""

    if not isinstance(argument, int) or isinstance(argument, bool) or \
        argument < 1 and argument != 0:
        raise TypeError("Ֆունկցիան աշխատում է բնական թվի համար. "
                        "'{}'-ը չի համարվում բնական թիվ".format(argument))


# TODO: Rename function
def check_size_number(number):
    # TODO: Improve docstring and provide more generic information
    "ֆունկցիան ստուգում է իրեն փոխանցած արժեքը"

    len_pass = 8

    if number < len_pass:
        raise ValueError("ֆունկցիաին փոխանցած թիվը պետք է մեծ լինի {} "
                        "ից".format(len_pass))


def generator_random_simbols(total):
    """ֆունկցիան վերցնում է բնական թիվ և այդ թվին համապատասխան երկարության հետ
    վերադարձնում random սիմվոլներ"""

    all_types = [PUNCTUATION, LOWERS, UPPERS, INTS]

    rand_simbols = [random.choice(PUNCTUATION), random.choice(LOWERS),
           random.choice(UPPERS), random.choice(INTS)]

    for _ in range(total - 4):
        index = random.randint(0, 3)
        rand_simbols.append(random.choice(all_types[index]))

    return rand_simbols


# TODO: Rename function
def generator_password(length):
    """ֆունկցիան ստանում է բնական թիվ, հետ է վերադարձնում գախտանբառ,որի
    երկարությունը համապատասխանում է  այդ թվի չափին"""

    check_natural_number(length)
    check_size_number(length)
    result = generator_random_simbols(length)
    # TODO: Use some shuffling function instead of random.sample
    random.shuffle(result)
    return ''.join(result)


if __name__ == "__main__":
    num = parse_input_argument()
    print(generator_password(num))
