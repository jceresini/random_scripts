import pytest

from abbrev_v1 import abbreviate as ab1
from abbrev_v2 import abbreviate as ab2
from abbrev_v3 import abbreviate as ab3
from abbrev_v4 import abbreviate as ab4

def abbrev_count(in_str):
    l = len(in_str)
    return ((l + 1) * (l / 2)) + 1
    
@pytest.mark.parametrize(
    "in_str",
    [
        ("abcde"),
        ("localization"),
        ("internationalization"),
        ("foo"),
    ]
)
def test_abbreviations_good(in_str: str):

    expected_count = abbrev_count(in_str)
    v1 = ab1(in_str)
    v2 = ab2(in_str)
    v3 = ab3(in_str)
    v4 = ab4(in_str)
    assert len(v1) == expected_count == len(v2) == len(v3) == len(v4)

def test_abbreviations_bad():
    with pytest.raises(ValueError):
        ab1("abcde", 7)
