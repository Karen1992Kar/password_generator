#!/usr/bin/env python3

"""
Հրամանը ստանում է 1 բնական թիվ, հետ է վերադարձնում այդ թվի չափին համապատասխանող
երկարության գախտնաբառ
"""

import random
import argparse
import string

SPEC_SYMBOLS = string.punctuation
LOWERS = string.ascii_lowercase
UPPERS = string.ascii_uppercase
INTEGERS = string.digits

MIN_LENGTH_PASSWORD = 8


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


# TODO: Rename function
def check_min_length_password(number):
    # TODO: Improve docstring and provide more generic information
    """Գաղտնաբառի մինիմալ երկարության ստուգում"""

    if number < MIN_LENGTH_PASSWORD:

        raise ValueError("ֆունկցիաին փոխանցած թիվը պետք է մեծ լինի {} "
                         "ից".format(MIN_LENGTH_PASSWORD))


def generate_random_symbols(total):
    """Ֆունկցիան վերցնում է բնական թիվ և այդ թվին համապատասխան երկարության հետ
    վերադարձնում random սիմվոլներ"""

    all_types = [SPEC_SYMBOLS, LOWERS, UPPERS, INTEGERS]

    # TODO: Correct typos in 'simbol'
    rand_simbols = [random.choice(SPEC_SYMBOLS), random.choice(LOWERS),
                    random.choice(UPPERS), random.choice(INTEGERS)]

    for _ in range(total - 4):
        index = random.randint(0, 3)
        rand_simbols.append(random.choice(all_types[index]))

    random.shuffle(rand_simbols)
    return ''.join(rand_simbols)


# TODO: Rename function
def generate_password(length):
    """Ֆունկցիան ստանում է բնական թիվ, հետ է վերադարձնում գախտանբառ,որի
    երկարությունը համապատասխանում է  այդ թվի չափին"""

    check_natural_number(length)
    check_min_length_password(length)
    # TODO: Renamne 'result' variable
    password = generate_random_symbols(length)
    # TODO: Move suffle to the function above
    return password


if __name__ == "__main__":
    num = parse_input_argument()
    print(generate_password(num))
