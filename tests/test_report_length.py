from lib.report_length import *

def test_six_letter_word():
    result = report_length("snazzy")
    assert result == 6

def test_five_letter_word():
    result = report_length("house")
    assert result == 5

def test_ten_letter_word():
    result = report_length("pizzicatos")
    assert result == 10
    