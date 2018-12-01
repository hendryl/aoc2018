import pytest
from calibrate import calibrate, calibrateSame

def test_calibrate():
    assert calibrate('+1, +1, +1') == 3
    assert calibrate('+1, +1, -2') == 0
    assert calibrate('-1, -2, -3') == -6
    assert calibrate('-100, +1000') == 900
    assert calibrate('-100') == -100

def test_calibratesame():
    assert calibrateSame('+1, -1') == 0
    assert calibrateSame('+3, +3, +4, -2, -4') == 10
    assert calibrateSame('-6, +3, +8, +5, -6') == 5
    assert calibrateSame('+7, +7, -2, -7, -4') == 14