import pytest
from unittest.mock import *
from mock import patch

import lib.trump_util as tutil
import lib.donald_trump as trump


'''
The fixture allows setup and teardown of many test functions (pass in arg)
-> adding (scope='module') will run setup and tear down each once before
   and after all test methods, which you may want for continuous behavioral testing

Just setup method:
@pytest.fixture(scope='module')
def db():
    db = myDB()
    db.connect('test_data.json')
    return db

If you also need teardown method, use yield:
@pytest.fixture(scope='module')
def db():
    db = myDB()
    db.connect('test_data.json')
    yield db # setup part until here
    db.close() # teardown part after each test is run
'''
@pytest.fixture #(scope='module')
def president():
    pres = trump.Donald_Trump()
    print("created donald")
    yield pres
    del pres
    print("deleted donald")
    

'''
By passing the setup method, we can reuse the same class object
initialization to avoid repeating setup in the beginning of each test method.
This is especially useful for testing against database methods
'''
def test_fixture_initialization(president):
    assert president.enemies == 0
    assert str(president.platform) == 'Twitter'
    
    
'''
Normally, you cannot mock patch an attribute that is created at runtime (a.k.a during __init__)
In this case you could use the context manager to mock __init__.

Beware! You can create non-existing attributes in the original class,
-> use spec, autospec, or spec-set to perform a check
'''
def test_create_mock_class():
    # Context manager to mock dynamically created attributes (e.g. self.attr in __init__)
    with patch.object(trump.Donald_Trump, "__init__", lambda x, y, z: None):
        fakePres = trump.Donald_Trump(None, None)
        fakePres.notAttribute = 100
        assert fakePres.notAttribute == 100
        fakePres.enemies = 10
        assert fakePres.enemies > 9











