#!/usr/bin/env pytest

"""
Մոդուլը թեստավորում է password_generator մոդուլը
"""

import string
import pytest
from password_generator import generate_password, MIN_PASSWORD_LENGTH


LOWERS = string.ascii_lowercase
UPPERS = string.ascii_uppercase
SPEC_SYMBOLS = string.punctuation
INTEGERS = string.digits


def interest_calculator(type_count, number_of_cycles, password_length):
    """Ֆունկցիան վերադարձնում է առանձին սիմվոլների քանակը գաղտնաբառի մեջ
    ըստ տոկոսների """

    return float('{0:.2f}'.format((type_count * 100) /
                 (number_of_cycles*password_length)))


def counter_of_identical_symbols(string1, string2):
    """Ֆունկցիան վերադարձնում է string1 ի մեջ եղած են սիմվոլների քանակը, որոնք
    կան string2 ի մեջ"""

    result = []
    for i in string2:
        if i in string1:
            result.append(i)

    return len(result)


# TODO: improve function,1
# 1. rename function to a more generic name1
def check_probability(actual_percentage, expected_percent=25, tolerance=5):
    """Թվի հավանականության ստուգում սահմանված միջակայքում"""

    if (expected_percent - tolerance) <= actual_percentage <= (expected_percent
                                                               + tolerance):
        return True
    return False


@pytest.mark.parametrize("number", list(range(1, MIN_PASSWORD_LENGTH, 2)))
# TODO: improve function1
def test_less_minimum_number(number):
    """Ֆունկցիան ստուգում է password_generator մոդուլը մինիմալ երկարությունից
    փոքր երկարություններ ունեցող գաղտնաբառերի դեպքում"""

    try:
        generate_password(number)
    except ValueError as error_desc:
        assert str(error_desc) == "ֆունկցիաին փոխանցած թիվը պետք է " \
                                  "մեծ լինի {} ից".format(MIN_PASSWORD_LENGTH)
    else:
        pytest.fail("Սպասվում էր ValueError {} թվի համար, բայց ֆունկցիան "
                    "աշխատեց նորմալ".format(number))


@pytest.mark.parametrize('password_length',
                         list(range(MIN_PASSWORD_LENGTH, 40, 9)))
def test_for_all_symbols_in_password(password_length):
    """Ֆունկցիան ստուգում է գախտնաբառի մեջ հատուկ սիմվոլների, թվերի,
    մեծատառերի և փոքրատառերի առկայուտյունը """

    password = generate_password(password_length)

    assert set(password).intersection(LOWERS), "գաղտնաբառը "\
        "պետք է բարունակեր {} սիմվոլներից մեկը, բայց չի " \
        "բարունակում".format(LOWERS)

    assert set(password).intersection(UPPERS), "գաղտնաբառը "\
        "պետք է բարունակեր {} սիմվոլներից մեկը, բայց չի " \
        "բարունակում".format(UPPERS)

    assert set(password).intersection(SPEC_SYMBOLS), "գաղտնաբառը "\
        "պետք է բարունակեր {} սիմվոլներից մեկը, բայց չի " \
        "բարունակում".format(SPEC_SYMBOLS)

    assert set(password).intersection(INTEGERS), "գաղտնաբառը "\
        "պետք է բարունակեր {} սիմվոլներից մեկը, բայց չի " \
        "բարունակում".format(INTEGERS)


# TODO: rename function1
@pytest.mark.parametrize("argument", ["string", "16", 7.3, True])
def test_not_natural_number(argument):
    """Ֆունկցիան ստուգում է password_generator մոդուլի աշխատանքը ոչ
    բնական թվերի դեպքում"""

    try:
        generate_password(argument)
    except TypeError as error_desc:
        assert str(error_desc) == "Ֆունկցիան աշխատում է բնական թվի համար. "\
               "'{}'-ը չի համարվում բնական թիվ".format(argument)
    else:
        pytest.fail("ֆունկցիան պետք է կանչեր TypeError <<{}>> արգումենտի "
                    "համար, քանի որ այն աշխատում է {} ից մեծ բնական թվերի "
                    "համար".format(argument, MIN_PASSWORD_LENGTH))


@pytest.mark.parametrize("number", list(range(MIN_PASSWORD_LENGTH, 40, 8)))
# TODO: rename function1
def test_password_length(number):
    """Ֆունկցիան ստուգում է password_generator մոդուլին փոխանցած թվի և հետ
    վերադարձրած գաղտնաբառի երկարության հավասար լինելը"""

    assert len(generate_password(number)) == number, "ֆունկցիաին փոխանցած "\
           "թիվը պետք է հավասար լիներ գաղտնաբառի երկարությանը"


@pytest.mark.parametrize("symbols", [LOWERS, UPPERS, INTEGERS, SPEC_SYMBOLS])
def test_password_randomness(symbols):
    """Ֆունկցիան ստուգում է գաղտնաբառի պատահական լինելը"""

    symbol_count = 0
    number_of_cycles = 100
    password_length = 12

    for _ in range(number_of_cycles):
        password = generate_password(password_length)
        symbol_count += counter_of_identical_symbols(symbols, password)

    symbol_percent = interest_calculator(symbol_count, number_of_cycles,
                                         password_length)
    assert check_probability(symbol_percent), "Փոքրատառերի "\
           "քանակը պետք է կազմեր ընդհանուր սիմվոլների քանակի 25% ից 30% ը "\
           "բայց կազմեց {0:.2f}%".format(symbol_percent)
