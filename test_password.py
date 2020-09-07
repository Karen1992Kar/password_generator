#!/usr/bin/env pytest

"""

"""
import random
import string
import pytest
from password import password_generator


@pytest.mark.parametrize("num", [1,2,3,4,5,6,7])
def test_argument_greater_than_seven(num):
    """ֆունկցիան ստուգում է password մոդուլը 8 ից փոքր բնական թվերի համար"""

    try:
        password_generator(num)
    except ValueError as desc_name:
        assert str(desc_name) == "ֆունկցիաին փոխանցած թիվը պետք է մեծ լինի 7 ից"
    else:
        pytest.fail("Սպասվում էր ValueError {} թվի համար, բայց ֆունկցիան "
                    "աշխատեց նորմալ".format(num))


@pytest.mark.parametrize('len_password', [8,9,25,30])
@pytest.mark.parametrize('type_simbols', [string.punctuation,\
                          str(list(range(0, 10))), string.ascii_letters[:26],\
                          string.ascii_letters[26:]])
def test_str_in_password(len_password, type_simbols):
    """Ֆունկցիան ստուգում է գախտնաբառի մեջ հատուկ սիմվոլների ի առկայուտյունը """

    assert set(password_generator(len_password)).intersection(type_simbols), "գաղտնաբառը "\
           "պետք է բարունակեր {} սիմվոլներից մեկը, բայց չի " \
           "բարունակում".format(type_simbols)

