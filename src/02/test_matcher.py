import pytest
from matcher import count, checksum, findDifference, compare

def test_count():
    assert count('abcdef') == (False, False)
    assert count('bababc') == (True, True)
    assert count('abbcde') == (True, False)
    assert count('abcccd') == (False, True)
    assert count('aabcdd') == (True, False)
    assert count('abcdee') == (True, False)
    assert count('ababab') == (False, True)

def test_checksum():
    assert checksum(['abcdef',
'bababc',
'abbcde',
'abcccd',
'aabcdd',
'abcdee',
'ababab']) == 12

def test_findDifference():
    assert findDifference('abcde', 'fghij') == (2, [0,1])
    assert findDifference('fghij', 'fguij') == (1, [2])

def test_compare():
    assert compare([
        'abcde',
        'fghij',
        'klmno',
        'pqrst',
        'fguij',
        'axcye',
        'wvxyz',
    ]) == 'fgij'