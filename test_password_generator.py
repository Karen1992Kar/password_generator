#!/usr/bin/env pytest

"""
Մոդուլը թեստավորում է password_generator մոդուլը
"""

import string
import pytest
from password_generator import generate_password, MIN_LENGTH_PASSWORD


LOWERS = string.ascii_lowercase
UPPERS = string.ascii_uppercase
SPEC_SYMBOLS = string.punctuation
INTEGERS = string.digits


def interest_calculator(count_type, number_of_cycles, length_password):
    """Ֆունկցիան վերադարձնում է առանձին սիմվոլների քանակը գաղտնաբառի մեջ
    ըստ տոկոսների """

    return (count_type * 100)/(number_of_cycles*length_password)


def counter_of_identical_symbols(string1, string2):
    """Ֆունկցիան վերադարձնում է string1 ի մեջ եղած են սիմվոլների քանակը, որոնք
    կան string2 ի մեջ"""

    result = []
    for i in string2:
        if i in string1:
            result.append(i)

    return len(result)


def probability_character_in_password(argument):
    """Ֆունկցիան ստուգում է իրեն փոխանցած արգումենտի 19 ից մեծ 31 ից փոքր
    լինելը"""

    if 30 >= argument >= 20:
        return True
    return False


@pytest.mark.parametrize("num", [1, 4, 7])
def test_argument_greater_than_seven(num):
    """Ֆունկցիան ստուգում է password մոդուլը 8 ից փոքր բնական թվերի համար"""

    try:
        generate_password(num)
    except ValueError as desc_name:
        assert str(desc_name) == "ֆունկցիաին փոխանցած թիվը պետք է " \
                                 "մեծ լինի {} ից".format(MIN_LENGTH_PASSWORD)
    else:
        pytest.fail("Սպասվում էր ValueError {} թվի համար, բայց ֆունկցիան "
                    "աշխատեց նորմալ".format(num))


@pytest.mark.parametrize('len_password', [8, 9, 35, 36])
def test_str_in_password(len_password):
    """Ֆունկցիան ստուգում է գախտնաբառի մեջ հատուկ սիմվոլների, թվերի, " \
    մեծատառերի, և փոքրատառերի առկայուտյունը """

    password = generate_password(len_password)

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


@pytest.mark.parametrize("argument", ["string", "16", 7.3, True])
def test_for_string_argument(argument):
    """Ֆունկցիան ստուգում է password մոդուլի աշխատանքը ոչ
    բնական թվերի դեպքում"""

    try:
        generate_password(argument)
    except TypeError as desc_name:
        assert str(desc_name) == "Ֆունկցիան աշխատում է բնական թվի համար. "\
               "'{}'-ը չի համարվում բնական թիվ".format(argument)
    else:
        pytest.fail("ֆունկցիան պետք է կանչեր TypeError <<{}>> արգումենտի "
                    "համար, քանի որ այն աշխատում է 7 ից մեծ բնական թվերի "
                    "համար".format(argument))


@pytest.mark.parametrize("number", [15, 45, 59])
def test_for_len_arguments(number):
    """Ֆունկցիան ստուգում է password_generator մոդուլին փոխանցած թվի և հետ
    վերադարձրած գաղտնաբառի երկարության հավասար լինելը"""

    assert len(generate_password(number)) == number, "ֆունկցիաին փոխանցած "\
           "թիվը պետք է հավասար լիներ գաղտնաբառի երկարությանը"


@pytest.mark.parametrize("symbols", [LOWERS, UPPERS, INTEGERS, SPEC_SYMBOLS])
def test_for_check_random_password(symbols):
    """Ֆունկցիան ստուգում է գաղտնաբառի random լինելը"""

    symbol_count = 0

    number_of_cycles = 100
    length_password = 12

    for _ in range(number_of_cycles):

        password = generate_password(length_password)
        symbol_count += counter_of_identical_symbols(symbols, password)

    symbol_percent = interest_calculator(symbol_count, number_of_cycles,
                                         length_password)
    assert probability_character_in_password(symbol_percent), "Փոքրատառերի "\
           "քանակը պետք է կազմեր ընդհանուր սիմվոլների քանակի 0.2 ից 0.3 մասը,"\
           " բայց կազմեց {} մասը".format("%.2f" % round(symbol_percent/100, 2))
