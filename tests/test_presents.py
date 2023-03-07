import pytest   
from lib.presents import Present

def test_presents_wrap_and_unwrap():
    present = Present()
    present.wrap(20)
    assert present.unwrap() == 20

def test_unwrap_present_not_wrapped():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_wrap_present_already_wrapped():
    present = Present()
    present.wrap(25)
    with pytest.raises(Exception) as e:
        present.wrap(10)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_wrapped_present_retains_value():
    present = Present()
    present.wrap(205)
    with pytest.raises(Exception) as e:
        present.wrap(50)
    assert present.unwrap() == 205
    