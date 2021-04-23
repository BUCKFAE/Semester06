"""Tests the functions in main.py"""

from main import prodZ, divZ

def test_math():

    for i in range(-10, 10):
        for j in range(-10, 10):
            assert prodZ(i, j) == i * j
            assert divZ(i, j) == i // j if j != 0 else True