import pytest
import mock
from unittest.mock import *
import numpy as np

import lib.trump_util as tutil


'''
Test functions have prefixes of test_
Without the prefix, the function is just a regular one
'''
def not_a_test():
    print("This will not be run by pytest")

    
'''
This function will be run by pytest due to the test_ prefix
However, it will only print the message with -v (verbose option)
'''
def test_print_something():
    print("This will be run by pytest")
    
    
'''
Simple assertion statements to check results
'''
def test_assertion_statements():
    assert True == True
    assert 3 != 55
    assert pytest.approx(1.0000000009) == 1
    assert 1.0000000009 == 1  # fails
    
    
'''
Simple way to test a function
'''
def test_add_two_num():
    assert tutil.add_two_num(20, 10) == 30
    assert tutil.add_two_num(-11, 2) == -9
    

'''
Better way to test larger functions would be to parametrize test data.
The parametrized fields must be given to the test function as args
'''
test_data_concat_two_strings = [
    ("Hello ", "world!", "Hello world!"),
    ("Make Taiwan", " great again!", "Make Taiwan great again!"),
    ("I miss ", "President Obama", "I miss President Obama"),
    ("I", "am happy", "I am happy"),
    ("Winnie th", "e Pooh", "Winnie the Pooh")
]
    
@pytest.mark.parametrize('testStr0, testStr1, expected', test_data_concat_two_strings)    
def test_concat_two_strings(testStr0, testStr1, expected):
    assert tutil.concat_two_strings(testStr0, testStr1) == expected
    

'''
Patch can be used to force behaviors of functions or attributes
Note that since in trump_util, numpy is imported as np,
we have to use the imported name np to patch instead of numpy
'''
@patch.object(tutil.np, 'absolute', return_value=10)
def test_calc_abs(mock_absolute):
    assert tutil.calc_abs(-3) == 10
    
    
'''
Another way to patch with return value inside context manager
'''
def test_calc_abs_2():
    # regular behavior
    assert tutil.calc_abs(-6) == 6
    assert tutil.calc_abs(34) == 34
    # declare return value in header
    with patch.object(tutil.np, 'absolute', return_value=100):
        assert tutil.calc_abs(-3) == 100
    # assign return value on the fly
    with patch.object(tutil.np, 'absolute'):
        tutil.np.absolute.return_value = -6
        assert tutil.calc_abs(18) == -6
        tutil.np.absolute.return_value = 15
        assert tutil.calc_abs(-15) == 15
    