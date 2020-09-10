#!/usr/bin/env python3

"""
Հրամանը ստանում է 1 բնական թիվ, հետ է վերադարձնում այդ թվի չափին համապատասխանող
երկարության գախտնաբառ
"""

import random
import argparse
import string

# TODO: Try not to use abbreviations
SPEC_SYMBOLS = string.punctuation
LOWERS = string.ascii_lowercase
UPPERS = string.ascii_uppercase
INTEGERS = string.digits

MIN_PASSWORD_LENGTH = 8


def parse_input_argument():
    """Ֆունկցիան ստուգում է հրամանին ուղարկված արգումենտները"""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('argument', type=int, help="բնական թիվ")
    parser = parser.parse_args()

    return parser.argument


def check_natural_number(argument):
    """Ֆունկցիան ստուգում է արգումենտի բնական թիվ լինելը."""

    if not isinstance(argument, int) or isinstance(argument, bool) or \
       argument < 1:
        raise TypeError("Ֆունկցիան աշխատում է բնական թվի համար. "
                        "'{}'-ը չի համարվում բնական թիվ".format(argument))


def check_min_password_length(number):
    """Գաղտնաբառի մինիմալ երկարության ստուգում"""

    if number < MIN_PASSWORD_LENGTH:
        raise ValueError("ֆունկցիաին փոխանցած թիվը պետք է մեծ լինի {} "
                         "ից".format(MIN_PASSWORD_LENGTH))


def generate_random_symbols(total):
    """Ֆունկցիան վերցնում է բնական թիվ և այդ թվին համապատասխան երկարության հետ
    վերադարձնում random սիմվոլներ"""

    all_types = [SPEC_SYMBOLS, LOWERS, UPPERS, INTEGERS]

    rand_symbols = [random.choice(SPEC_SYMBOLS), random.choice(LOWERS),
                    random.choice(UPPERS), random.choice(INTEGERS)]

    for _ in range(total - 4):
        index = random.randint(0, 3)
        rand_symbols.append(random.choice(all_types[index]))

    random.shuffle(rand_symbols)
    return ''.join(rand_symbols)


def generate_password(length):
    """Ֆունկցիան ստանում է բնական թիվ, հետ է վերադարձնում գախտանբառ,որի
    երկարությունը համապատասխանում է  այդ թվի չափին"""

    check_natural_number(length)
    check_min_password_length(length)
    password = generate_random_symbols(length)
    return password


if __name__ == "__main__":
    passwoerd_length_from_terminal = parse_input_argument()
    print(generate_password(passwoerd_length_from_terminal))
