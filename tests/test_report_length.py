from lib.report_length import *

def six_letter_word():
    result = report_length("snazzy")
    assert result == 6

def five_letter_word():
    result = report_length("house")
    assert result == 5

def ten_letter_word():
    result = report_length("pizzicatos")
    assert result == 10