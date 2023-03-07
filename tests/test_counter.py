from lib.counter import *

def test_counter_initially_reports_zero():
    counter = Counter()
    assert counter.report() == 'Counted to 0 so far.'

def test_counter_adds_a_Single_number_to_the_count():
    counter = Counter()
    counter.add(5)
    assert counter.report() == 'Counted to 5 so far.'

def test_counter_multiple_numbers_to_the_count():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    assert counter.report() == 'Counted to 8 so far.'

def test_counter_pos_and_neg_numbers_to_the_count():
    counter = Counter()
    counter.add(5)
    counter.add(-3)
    assert counter.report() == 'Counted to 2 so far.'

def test_counter_neg_and_neg_numbers_to_the_count():
    counter = Counter()
    counter.add(-5)
    counter.add(-3)
    assert counter.report() == 'Counted to -8 so far.'