#!/usr/bin/env pytest

"""
Մոդուլը թեստավորում է password_generator մոդուլը
"""

import string
import pytest
from password_generator import generator_password

# TODO: use string module's property/functions
LOWERS = string.ascii_lowercase
UPPERS = string.ascii_uppercase
SPEC_SIMBOLS = string.punctuation
INTS = string.digits


@pytest.mark.parametrize("num", [1,4,7])
def test_argument_greater_than_seven(num):
    """ֆունկցիան ստուգում է password մոդուլը 8 ից փոքր բնական թվերի համար"""

    try:
        generator_password(num)
    except ValueError as desc_name:
        assert str(desc_name) == "ֆունկցիաին փոխանցած թիվը պետք է մեծ լինի 7 ից"
    else:
        pytest.fail("Սպասվում էր ValueError {} թվի համար, բայց ֆունկցիան "
                    "աշխատեց նորմալ".format(num))


@pytest.mark.parametrize('len_password', [8, 9, 35, 36])
def test_str_in_password(len_password):
    """Ֆունկցիան ստուգում է գախտնաբառի մեջ հատուկ սիմվոլների, թվերի, " \
    մեծատառերի, և փոքրատառերի առկայուտյունը """

    password = generator_password(len_password)

    assert set(password).intersection(LOWERS), "գաղտնաբառը "\
        "պետք է բարունակեր {} սիմվոլներից մեկը, բայց չի " \
        "բարունակում".format(LOWERS)

    assert set(password).intersection(UPPERS), "գաղտնաբառը "\
        "պետք է բարունակեր {} սիմվոլներից մեկը, բայց չի " \
        "բարունակում".format(UPPERS)

    assert set(password).intersection(SPEC_SIMBOLS), "գաղտնաբառը "\
        "պետք է բարունակեր {} սիմվոլներից մեկը, բայց չի " \
        "բարունակում".format(SPEC_SIMBOLS)

    assert set(password).intersection(INTS), "գաղտնաբառը "\
        "պետք է բարունակեր {} սիմվոլներից մեկը, բայց չի " \
        "բարունակում".format(INTS)


@pytest.mark.parametrize("argument", ["string", "16", 7.3, True])
def test_for_string_argument(argument):
    """Ֆունկցիան ստուգում է password մոդուլի աշխատանքը ոչ
    բնական թվերի դեպքում"""

    try:
        generator_password(argument)
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

    assert len(generator_password(number)) == number, "ֆունկցիաին փոխանցած "\
           "թիվը պետք է հավասար լիներ գաղտնաբառի երկարությանը"
