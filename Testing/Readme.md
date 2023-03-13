
# Python Unit Testing

Unit tests are segments of code written to test other pieces of code, typically a single function or method, that we refer to as a unit. They are a very important part of the software development process, as they help to ensure that code works as intended and catch bugs early on. 

the writing of unit tests in Python, from understanding the assert statement to using a framework designed specifically for this kind of task — and following Python unit testing best practices.

Python has two main frameworks to make unit testing easier: unittest and PyTest. The first one has been part of Python’s standard library since Python 2.1 and that’s the one we’re focused on in this article.

To follow along with the unit test tutorial, you don’t need any advanced knowledge, but we do expect you to have a basic understanding of how Python functions and classes work.

## The assert Statement 
The assert statement is a built-in statement in Python used to, as the name says, assert if a given condition is true or not. If the condition is true, nothing happens, but if it’s not true, an error is raised. Although, at first, it may look like the try and except clauses, they are completely different, and assert should not be used for error handling but for debugging and testing reasons.

As an example, the condition in the line below is true and, therefore, it does not output or return anything:

assert 1 > 0
However, if we change this condition so it becomes false, we get an AssertionError:
```
assert 1 < 0
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-2-2d19dbe67b58> in <module>
----> 1 assert 1 < 0
```
AssertionError:
Notice that in the last row of the error message there isn’t an actual message after AssertionError:. That’s because the user should pass this message. Here’s how:
```
n = 0
assert 1 < n, 'The Condition is False'
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-3-e335e3eb84ff> in <module>
      1 n = 0
----> 2 assert 1 < n, 'The Condition is False'
```

AssertionError: The Condition is False
So, the basic syntax for using assert is the following:

assert <condition being tested>, <error message to be displayed>
assert is very simple to use. Understanding it is critical for testing purposes, as we’ll see in the following sections.



  The unittest Module
The unittest module is a framework designed to make our lives easier when it comes to testing code. The module works based on some important object-oriented concepts, and that’s why you need to understand the basics of classes and methods in Python.

A test case is considered a single unit of testing, and it’s represented by the TestCase class. Among the numerous tools provided by unittest that allow us to test code, this class is one of the most important ones. It’s used as a base class to create our own test cases that enable us to run multiple tests at once.

Although we’ve seen the importance of the Python assert statement in the last section, it won’t be used here. That’s because the TestCase class also provides several of its own assert methods that work just like the assert statement but for specific types of assertions.

For instance, the assertEqual takes two elements and tests if they are equal to each other while assertNotEqual tests if the elements are different. Also, the assertTrue method takes one element and tests if it’s true while assertFalse tests if it’s false.

Here’s a list of the most commonly used assert methods in the TestCase class, provided by the official unittest documentation:

###  Method	               `Checks that`
- assertEqual(a, b)     	a == b
- assertNotEqual(a, b)   	a != b
- assertTrue(x)	         bool(x) is True
- assertFalse(x)	       bool(x) is False
- assertIs(a, b)        	a is b
- assertIsNot(a, b)	    a is not b
- assertIsNone(x)       	x is None
- assertIsNotNone(x)   	x is not None
- assertIn(a, b)	      a in b
- assertNotIn(a, b)	   a not in b
- assertIsInstance(a, b)  	isinstance(a, b)
- assertNotIsInstance(a, b)	 not isinstance(a, b)
It’s important to say that all assert methods in the TestCase class also take a msg argument that is used as an error message in case the test fails.

## Implementing Unit Tests
So let’s implement a simple set of unit tests. First of all, we need to have some code to test. For that, let’s consider the following Calculations class that is inside the my_calculations.py file inside the tests directory:

  ```
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

So now we want to test the methods inside this class. For that, we need to create a class based on the TestCase class and this class will contain methods that perform the tests.

Let’s say we have the following folder structure:
```
project/
│
├── code/
│   ├── __initII.py
│   └── my_calculations
│
└── tests.py
# project/test.py
```
```
import unittest
from code.my_calculations import Calculations

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong.')

if __name__ == '__main__':
    unittest.main()
```
  
  The code above tests the get_sum method of the Calculations class. To achieve that, we had to do the following:

1.Import both unittests and the Calculations class
2.Instantiate an object if the Calculations class
3.Create the TestCalculations class and the test_sum method inside it
Notice that we use assertEqual to assert if the output of get_sum is equal to 10. We also have a message set for the case of failure. Finally, when we run this script, unittest.main() runs the test. This is the output we get:

  ```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
OK
For instance, if we change the expected value from 10 to, let’s say, 11, the test would fail and we’d have this output:
  
  ```
  
  ```
  ----------------------------------------------------------------------
Traceback (most recent call last):
  File ".\my_test.py", line 9, in test_sum
    self.assertEqual(calculation.get_sum(), 11, 'The sum is wrong.')
AssertionError: 10 != 11 : The sum is wrong.
----------------------------------------------------------------------
Ran 1 test in 0.001s
  
  ```
  
  Notice that the The sum is wrong. message is there as expected.

Following the same logic, we have the code below that tests all four methods in the Calculations class:
```
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
 ``` 
  And all the tests ran:

....
----------------------------------------------------------------------
Ran 4 tests in 0.001s
OK
  
```  
By the way, it isn’t an accident that all the methods’ names start with the word test. This is a convention we use so that unittest can identify the tests it’s supposed to run. For instance, the following code runs only three tests:
  
 ``` 
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
```
----------------------------------------------------------------------
Ran 3 tests in 0.001s
OK
  ```
The output says that three tests ran. Notice that the first method is called not_a_test_sum, and that’s why it wasn’t executed.  
  
  ## The setUp Method
Now that we understand the basics of unit testing with the unittest module, let’s optimize our code a bit. You probably have noticed that inside each test we initialized an object of the Calculations class, which will be tested. However, we can avoid that by creating a setUp method.

The TestCase class already has a setUp method that runs before each test. So what we’ll do when creating a new one is actually overwrite the default method with our own. This is the code with this new method implemented:
```
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
This means that the calculations object will be initialized before each test is run. Another option is to use setUpClass instead. The idea is the same with the only difference being that this method will run only once and not before each test. This is how this method is implemented:
```
@classmethod
def setUpClass(self):
    self.calculation = Calculations(8, 2)
```
  
  
##   Running Tests from the Command-Line
In the previous section, we saw that it’s possible to run the tests with the unittest.main() inside .py file. However, another very useful way to run tests is calling unittest directly from the command line.

Using the command-line interface to run unit tests can improve your productivity because it allows you to run multiple files at once:
```
>>>pyhon -m unittest
  
```
The line above will run the discovery mode in unittest that will look for the tests inside the current directory. 

However, for the tests to run, we have to follow some naming conventions: the name of each file containing tests has to start with test, and all the tests have to be methods of class based on the TestCase class. As we said earlier, the names of all these methods have to start with the word test. Finally, the directory must be an importable module, which means it should contain an init.py file.

Let’s say we have the following tests directory:
```
tests/
├── init.py
├── test.py
└── test_str.py
```
The test_str.py file contains the following tests that were taken from an example in the unittest documentation:
```
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
```
>>>python -m unittest -v
```
The -v makes the output a bit more verbose, which can be useful when running several tests at once:
```
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
```
>>>python -m unittest -v tests.test
 ```
In the line above, tests.test ensures that only the tests.py file will run. Using the same logic, we specify the test class and even a single method that we want to run:
```
>>>python -m unittest -v tests.test.TestCalculations.test_diff
```
The line above will run only the test_diff method, as we can see in the output:
```
test_diff (teste.test.TestCalculations) ... ok
----------------------------------------------------------------------
Ran 1 test in 0.000s
OK
``` 
  
  
  
  
