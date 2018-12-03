import pytest
from overlap import separate, claim, findOverlapCountInClaims

def test_separate():
    assert separate('#123 @ 3,2: 5x4') == {
        "id": '#123',
        "origin": (3, 2),
        "area": (5, 4)
    }

def test_claim():
    assert claim('#123 @ 3,2: 2x3') == {
        (3,2): 1,
        (3,3): 1,
        (3,4): 1,
        (4,2): 1,
        (4,3): 1,
        (4,4): 1,
    }

    assert claim('#123 @ 8,2: 7x1') == {
        (8,2): 1,
        (9,2): 1,
        (10,2): 1,
        (11,2): 1,
        (12,2): 1,
        (13,2): 1,
        (14,2): 1,
    }

def test_findOverlapCountInClaims():
    assert findOverlapCountInClaims([
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2'
    ]) == 4
