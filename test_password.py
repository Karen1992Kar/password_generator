#!/usr/bin/env pytest

"""
aaa
"""

import pytest
from password import password


@pytest.mark.parametrize("num", [1,2,3,4,5,6,7])
def test_argument_greater_than_seven(num):
    """aaaa"""

    try:
        password(num)
    except ValueError as desc_name:
        assert str(desc_name) == "ֆունկցիաին փոխանցած թիվը պետք է մեծ լինի 7 ից"
    else:
        pytest.fail("Սպասվում էր ValueError {} թվի համար, բայց ֆունկցիան "
                    "աշխատեց նորմալ".format(num))
