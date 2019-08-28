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

        
'''
Beware of what you pass in as patch.
Be sure to pass in the mock_{method} first then other args to the test function

@patch() doesn't require importing the object before patching.
@patch.object() does require importing before patching. 
-> @patch.object is easier to use if you already have a reference to the object.

'''
@patch('lib.donald_trump.randint')
def test_patch_func_from_submodule(mock_randint, president):
    mock_randint.return_value = 3
    assert president.check_enemies() == 3
    
    
'''
Use call_count to verify how many times a mock function should be called.
Remember, call_count for a mock function is cumulative. If you want to 
test different cases use parametrized test data
'''
@patch.object(trump.Twitter, 'publish_msg', return_value=None)
def test_patch_func_call_count(mock_publish_msg, president):
    president.publish_message("short")
    assert mock_publish_msg.call_count == 1
    president.publish_message("looooooooooooooonoooooooooooooooooog")
    assert mock_publish_msg.call_count == 3  #fails due to the above reason

    
'''
Sometimes it could be useful to mock patch a class attribute,
Beware of how you use the return value to access attribute of class
'''    
@patch('lib.donald_trump.Twitter')
def test_platform_followers(mock_twitter):
    mock_twitter.return_value.platform_followers.return_value = 20
    fakePres = trump.Donald_Trump(0)
    assert fakePres.platform.platform_followers() == 20


'''
It actually does not matter what name give the patched function
as long as it is in order or used with correct name reference
'''
@pytest.mark.parametrize('numEnemies, expPlatform', [(4,'Twitter'), (12,'Facebook'), (16,'Instagram')])
@patch.object(trump.Donald_Trump, 'check_enemies')
def test_check_new_stance(mock_func, numEnemies, expPlatform, president):
    mock_func.return_value = numEnemies
    president.switch_platform()
    assert str(president.platform) == expPlatform

    
'''
Sometimes it is better to set test parameters by reference
'''
test_data_max_enemies = [
    (trump.maxEnemyThresh - 1, False),
    (trump.maxEnemyThresh    , False),
    (trump.maxEnemyThresh + 1, True)
]

@pytest.mark.parametrize('numEnemies, expected', test_data_max_enemies)
@patch.object(trump.Donald_Trump, 'check_enemies')
def test_has_too_many_enemies(mock_check_enemies, numEnemies, expected, president):
    mock_check_enemies.return_value = numEnemies
    assert president.has_too_many_enemies() == expected
    
    
'''
Brief note on mock.side_effect
'''
# def test_side_effect_1():
# def test_side_effect_2():
# def test_side_effect_3():    