**What is Unit Testing?**

Unit Testing is the first level of software testing where the smallest testable parts of a software are tested. This is used to validate that each unit of the software performs as designed.

**Method:**

White Box Testing method is used for Unit testing.

Python has inbuilt module unittest

Documentation: https://docs.python.org/3/library/unittest.html

## Naming Convention for unittest

Naming convention #1

```python
projectname
|
 --main.py
|
 --test_filename.py
```

example:

```python
projectname
|
 --main.py
|
 --test_case.py
|
 --test_num.py
```

It’s a convention   we need to follow to write the  test_filename is needed while writing the test.

### Naming convention #2

```python
projectname
|
 --main.py
|
 --filename_test.py
```

example:

```python
projectname
|
 --main.py
|
 --case_test.py
| 
 --num.py
|
 --num_test.py
```

It’s a convention   we need to follow to write the  filename_test.py is needed while writing the test.

### importing the unittest

```python
import unittest
```

- first import unittest (inbuit in python).
- Next import the module or method or python  file you need to test in unittesting

### importing the modules

```python
from <modules> import <method name to test> 
```

example:

```python
import unittest
from circles import circle_area
```

Next we need to define a class which need to start with Test followed class name.

```python
class Testclassname(unittest.TestCase):
		def test_method(self):
				# testing
```

creates a test class inherits from unittest from unittest.TestCase.

And method also follows with test_method name these are the conventions.

for the unittest module to identify these methods as tests and run them, these name should start with test_ for methods and Test for classes.

The test class in the unittest module provides useful assertion methods to check if the function under test return the expected values.

# assert statement

The assert keyword lets you debug ,test if a condition in your code returns True, if not, the
program will raise an AssertionError than can be written by ourselves.

syntax:

```python
assert condition,'Error message'
```

ex-1

```python
assert 1>0  # true
assert 1<0 #output AssertionError
```

```python
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-2-2d19dbe67b58> in <module>
----> 1 assert 1 < 0

AssertionError:
```

Notice that in the last row of the error message there isn't an actual message after `AssertionError:`. That's because the user should pass this message. Here's how:

```python
n = 0
assert 1 < n, 'The Condition is False'
```

```python
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-3-e335e3eb84ff> in <module>
      1 n = 0
----> 2 assert 1 < n, 'The Condition is False'

AssertionError: The Condition is False
```

So, the basic syntax for using `assert` is the following:

```python
assert <condition being tested>, <error message to be displayed>
```

`TestCase` class also provides several of its own assert methods that work just like the `assert` statement but for specific types of assertions.

For instance, the `assertEqual` takes two elements and tests if they are equal to each other while `assertNotEqual` tests if the elements are different. Also, the `assertTrue` method takes one element and tests if it's true while `assertFalse` tests if it's false.

Here's a list of the most commonly used assert methods in the `TestCase` class, provided by the official `unittest` documentation:

| Method | Checks that |
| --- | --- |
| assertEqual(a, b) | a == b |
| assertNotEqual(a, b) | a != b |
| assertTrue(x) | bool(x) is True |
| assertFalse(x) | bool(x) is False |
| assertIs(a, b) | a is b |
| assertIsNot(a, b) | a is not b |
| assertIsNone(x) | x is None |
| assertIsNotNone(x) | x is not None |
| assertIn(a, b) | a in b |
| assertNotIn(a, b) | a not in b |
| assertIsInstance(a, b) | isinstance(a, b) |
| assertNotIsInstance(a, b) | not isinstance(a, b) |

It's important to say that all assert methods in the `TestCase` class also take a `msg` argument that is used as an error message in case the test fails.

# Implementing Unit Tests

So let's implement a simple set of unit tests. First of all, we need to have some code to test. For that, let's consider the following `Calculations` class that is inside the `my_calculations.py` file inside the `tests` directory:

```python
# project/code/my_calculations.py

class Calculations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a + self.b

    def get_difference(self):
        return self.a - self.b

    def get_product(self):
        return self.a * self.b

    def get_quotient(self):
        return self.a / self.b
```

This is a very simple class that takes two numbers and has four methods to add, subtract, multiply and divide the first number by the second one and return the result.

So now we want to test the methods inside this class. For that, we need to create a class based on the `TestCase` class and this class will contain methods that perform the tests.

Let's say we have the following folder structure:

```python
project/
│
├── code/
│   ├── __init__.py
│   └── my_calculations
│
└── tests.py
```

```python
# project/test.py

import unittest
from code.my_calculations import Calculations

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong.')

if __name__ == '__main__':
    unittest.main()
```

The code above tests the `get_sum` method of the `Calculations` class. To achieve that, we had to do the following:

1. Import both `unittests` and the `Calculations` class
2. Instantiate an object if the `Calculations` class
3. Create the `TestCalculations` class and the `test_sum` method inside it

Notice that we use `assertEqual` to assert if the output of `get_sum` is equal to 10. We also have a message set for the case of failure. Finally, when we run this script, `unittest.main()` runs the test. This is the output we get:

```python
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
OK
```

For instance, if we change the expected value from 10 to, let's say, 11, the test would fail and we'd have this output:

```python
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".\my_test.py", line 9, in test_sum
    self.assertEqual(calculation.get_sum(), 11, 'The sum is wrong.')
AssertionError: 10 != 11 : The sum is wrong.
----------------------------------------------------------------------
Ran 1 test in 0.001s
```

Notice that the `The sum is wrong.` message is there as expected.

Following the same logic, we have the code below that tests all four methods in the `Calculations` class:

```python
import unittest
from code.my_calculations import Calculations

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong.')

    def test_diff(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_difference(), 6, 'The difference is wrong.')

    def test_product(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_product(), 16, 'The product is wrong.')

    def test_quotient(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_quotient(), 4, 'The quotient is wrong.')

if __name__ == '__main__':
    unittest.main()
```

And all the tests ran:

```python
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s
OK
```

By the way, it isn't an accident that all the methods' names start with the word `test`. This is a convention we use so that `unittest` can identify the tests it's supposed to run. For instance, the following code runs only three tests:

```python
import unittest
from code.my_calculations import Calculations

class TestCalculations(unittest.TestCase):

    def not_a_test_sum(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong.')

    def test_diff(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_difference(), 6, 'The difference is wrong.')

    def test_product(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_product(), 16, 'The product is wrong.')

    def test_quotient(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_quotient(), 4, 'The quotient is wrong.')

if __name__ == '__main__':
    unittest.main()
```

```python
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s
OK
```

The output says that three tests ran. Notice that the first method is called `not_a_test_sum`, and that's why it wasn't executed.

### The `setUp` Method

Now that we understand the basics of unit testing with the `unittest` module, let's optimize our code a bit. You probably have noticed that inside each test we initialized an object of the `Calculations` class, which will be tested. However, we can avoid that by creating a `setUp` method.

The `TestCase` class already has a `setUp` method that runs before each test. So what we'll do when creating a new one is actually overwrite the default method with our own. This is the code with this new method implemented:

```python
import unittest
from code.my_calculations import Calculations

class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.calculation = Calculations(8, 2)

    def test_sum(self):
        self.assertEqual(self.calculation.get_sum(), 10, 'The sum is wrong.')

    def test_diff(self):
        self.assertEqual(self.calculation.get_difference(), 6, 'The difference is wrong.')

    def test_product(self):
        self.assertEqual(self.calculation.get_product(), 16, 'The product is wrong.')

    def test_quotient(self):
        self.assertEqual(self.calculation.get_quotient(), 4, 'The quotient is wrong.')

if __name__ == '__main__':
    unittest.main()
```

This means that the `calculations` object will be initialized before each test is run. Another option is to use `setUpClass` instead. The idea is the same with the only difference being that this method will run only once and not before each test. This is how this method is implemented:

```python
@classmethod
def setUpClass(self):
    self.calculation = Calculations(8, 2)
```

# Running Tests from the Command-Line

In the previous section, we saw that it's possible to run the tests with the `unittest.main()` inside `.py` file. However, another very useful way to run tests is calling `unittest` directly from the command line.

Using the command-line interface to run unit tests can improve your productivity because it allows you to run multiple files at once:

```python
>>>pyhon -m unittest
```

The line above will run the discovery mode in `unittest` that will look for the tests inside the current directory.

However, for the tests to run, we have to follow some naming conventions: the name of each file containing tests has to start with `test`, and all the tests have to be methods of class based on the `TestCase` class. As we said earlier, the names of all these methods have to start with the word `test`. Finally, the directory must be an importable module, which means it should contain an `init.py` file.

Let's say we have the following `tests` directory:

```python
tests/
├── init.py
├── test.py
└── test_str.py
```

The `test_str.py` file contains the following tests that were taken from an example in the unittest documentation:

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

If we want to run the tests in both files, we can use the following line:

```python
>>>python -m unittest -v
```

The `-v` makes the output a bit more verbose, which can be useful when running several tests at once:

```python
test_diff (teste.test.TestCalculations) ... ok
test_product (teste.test.TestCalculations) ... ok
test_quotient (teste.test.TestCalculations) ... ok
test_sum (teste.test.TestCalculations) ... ok
test_isupper (teste.test_str.TestStringMethods) ... ok
test_split (teste.test_str.TestStringMethods) ... ok
test_upper (teste.test_str.TestStringMethods) ... ok
----------------------------------------------------------------------
Ran 7 tests in 0.002s
OK
```

We can also specify a single file to be run:

```python
>>>python -m unittest -v tests.test
```

In the line above, `tests.test` ensures that only the tests.py file will run. Using the same logic, we specify the test class and even a single method that we want to run:

```python
>>>python -m unittest -v tests.test.TestCalculations.test_diff
```

The line above will run only the `test_diff` method, as we can see in the output:

```python
test_diff (teste.test.TestCalculations) ... ok
----------------------------------------------------------------------
Ran 1 test in 0.000s
OK
```

To run these tests, we should run unittest as the main module, using the following command:

```bash
$ python -m unittest <module-name>.py
```

or

```python
python -m unittest
```

or

```python
python -m unittest -v foldername.filename
```

ex:

```python
python -m unittest -v code.num.py
```

or

```python
python -m unittest -v foldername.filename.classname.methodname
```

to know more about the assertion methods 

in repl shell

>>> import unittest

>>>help(unittest.TestCase.assertSetEqual)
