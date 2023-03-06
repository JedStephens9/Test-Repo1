from lib.report_length import *

def test_six_letter_word():
    result = report_length("snazzy")
    assert result == "This string was 6 characters long."

def test_five_letter_word():
    result = report_length("house")
    assert result == "This string was 5 characters long."

def test_ten_letter_word():
    result = report_length("pizzicatos")
    assert result == "This string was 10 characters long."
    