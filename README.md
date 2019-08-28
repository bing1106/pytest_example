# Welcome to pytest_example
Learn to build your Python unit tests with this fun example using Pytest. DisclaimerL this exercise is not politically motivated or holds any bias again specific individuals.

[Pytest](https://docs.pytest.org/en/latest/) and the Python built-in [Unittest](https://docs.python.org/3/library/unittest.html) are great tools to write your test suites and help you scale up your code base with a peace of mind. This out-of-box tutorial will cover the basic elements commonly used in building unit tests to help you get started.

***Before running the example, install pytest.***
```
pip install pytest
```

The __init__.py files in each sub folders makes Python treat directories containing it as modules. Furthermore, this is the first file to be loaded in a module, so you can use it to execute code that you want to run each time a module is loaded, or specify the submodules to be exported.

Go ahead and start the example by running the following at the top of the directory:
```
pytest .\test\ -v
```
The -v arg will list a detailed view of the tests run. Note that the test files in ```\test``` either has test as prefix or suffix. This tells pytest to look for these files and run the tests.

Test methods in each file should also begin with test_ as prefix. i.e. ```def test_some_fund():```


### Extra Side Notes 

shortcut to run all tests
py.test  /  py.test -v

-v verbose, more details on which functions pass/failed
pytest test_xx.py -v

run single test only ina  test file
pytest test_module.py::test_myFunc

run specific named type tests (e.g. with add in the test name)
pytest -v -k "add"
(to run add types and product types) pytest -v -k "add or product"
(can also specify more keywords that must appear in functions) pytest -v -k "add and string"

Use -x for exit on assertion failure
pytest -v -x

Tolerate only 2 failures at most
pytest -v --maxfail=2

-q quiet mode, print minimal information
-s you can print out extra embedded print statements


### Mark

##### To categorize your tests
@pytest.mark.numbers on top of certain functions allow you to run these functions with
pytest -v -m numbers

##### Use skip to skip certain test functions
@pytest.mark.skip(reason="do not run this test right now")

##### Skip test function if differen Python version
import sys
@pytest.mark.skipif(sys.version_info > (2, 7), reason="does not support Python version greater than 2.7")
