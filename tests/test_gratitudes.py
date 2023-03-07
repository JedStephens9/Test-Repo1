from lib.gratitudes import *

def test_gratitudes_returns_no_additional_string_if_one_not_given():
    gratitudes = Gratitudes()
    gratitudes.add ("")
    assert gratitudes.format() == "Be grateful for: "

def test_gratitudes_returns_one_additional_string_if_one_given():
    gratitudes = Gratitudes()
    gratitudes.add ("beer")
    assert gratitudes.format() == "Be grateful for: beer"

def test_gratitudes_returns_two_additional_string_if_two_given():
    gratitudes = Gratitudes()
    gratitudes.add ("beer")
    gratitudes.add ("chips")
    assert gratitudes.format() == "Be grateful for: beer, chips"