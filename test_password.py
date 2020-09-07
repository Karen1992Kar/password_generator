#!/usr/bin/env pytest

"""

"""
import random
import string
import pytest
from password import password_generator

# TODO: use string module's property/functions
lowers = string.ascii_lowercase
uppers = string.ascii_uppercase
spec_simbols = string.punctuation
ints = string.digits


@pytest.mark.parametrize("num", [1,4,7])
def test_argument_greater_than_seven(num):
    """ֆունկցիան ստուգում է password մոդուլը 8 ից փոքր բնական թվերի համար"""

    try:
        password_generator(num)
    except ValueError as desc_name:
        assert str(desc_name) == "ֆունկցիաին փոխանցած թիվը պետք է մեծ լինի 7 ից"
    else:
        pytest.fail("Սպասվում էր ValueError {} թվի համար, բայց ֆունկցիան "
                    "աշխատեց նորմալ".format(num))


@pytest.mark.parametrize('len_password', [8, 9, 35, 36])
def test_str_in_password(len_password):
    """Ֆունկցիան ստուգում է գախտնաբառի մեջ հատուկ սիմվոլների, տվերի, " \
    մեծատառերի, և փոքրատառերի առկայուտյունը """

    password = password_generator(len_password)

    assert set(password).intersection(lowers), "գաղտնաբառը "\
        "պետք է բարունակեր {} սիմվոլներից մեկը, բայց չի " \
        "բարունակում".format(lowers)

    assert set(password).intersection(uppers), "գաղտնաբառը "\
        "պետք է բարունակեր {} սիմվոլներից մեկը, բայց չի " \
        "բարունակում".format(uppers)

    assert set(password).intersection(spec_simbols), "գաղտնաբառը "\
        "պետք է բարունակեր {} սիմվոլներից մեկը, բայց չի " \
        "բարունակում".format(spec_simbols)

    assert set(password).intersection(ints), "գաղտնաբառը "\
        "պետք է բարունակեր {} սիմվոլներից մեկը, բայց չի " \
        "բարունակում".format(ints)


@pytest.mark.parametrize("argument", ["string", "16"])
def test_for_string_argument(argument):
    """Ֆունկցիան ստուգում է password մոդուլի աշխատանքը ոչ
    բնական թվերի դեպքում"""

    try:
        password_generator(argument)
    except TypeError as desc_name:
        assert str(desc_name) == "Ֆունկցիան աշխատում է բնական թվի համար. "\
               "'{}'-ը չի համարվում բնական թիվ".format(argument)
    else:
        pytest.fail("ֆունկցիան պետք է կանչեր TypeError <<{}>> արգումենտի "
                    "համար".format(argument))


def test_for_len_arguments():
    











