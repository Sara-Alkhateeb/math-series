import pytest
from series.series import fibonacci , lucas , sum_series



def  test_fibonacci_zero ():
   actual= fibonacci(0)
   excepted = 0
   assert actual == excepted

def  test_fibonacci_one ():
   actual= fibonacci(1)
   excepted = 1
   assert actual == excepted

def  test_fibonacci_two ():
   actual= fibonacci(2)
   excepted = 1
   assert actual == excepted

def  test_lucas_zero ():
   actual= lucas(0)
   excepted = 2
   assert actual == excepted

def  test_lucas_one ():
   actual= lucas(1)
   excepted = 1
   assert actual == excepted

def  test_lucas_two ():
   actual= lucas(2)
   excepted = 3
   assert actual == excepted

def test_sum_series():
    actual=sum_series(3,3,3)
    expected=4
    assert actual == expected

def test_sum_series_one():
    actual=sum_series(1,2)
    expected=1
    assert actual == expected

def test_sum_series_two():
    actual=sum_series(2)
    expected=1
    assert actual == expected



