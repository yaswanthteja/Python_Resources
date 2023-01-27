### 1. What is Python? What are the benefits of using Python?

Ans: Python is a programming language with objects, modules, threads, exceptions and automatic memory management. The benefits of pythons are that it is simple and easy, portable, extensible, build-in data structure and it is an open source.





### 2. What is PEP 8?
Ans: PEP 8 is a coding convention, a set of recommendation, about how to write your Python code more readable.




### 3. What is pickling and unpickling?

Ans: Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using dump function, this process is called pickling. While the process of retrieving original Python objects from the stored string representation is called unpickling.





### 4. How Python is interpreted?

Ans: Python language is an interpreted language. Python program runs directly from the source code. It converts the source code that is written by the programmer into an intermediate language, which is again translated into machine language that has to be executed.




### 5. How memory is managed in Python?

Ans: Python memory is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have an access to this private heap and interpreter takes care of this Python private heap.
The allocation of Python heap space for Python objects is done by Python memory manager. The core API gives access to some tools for the programmer to code.
Python also have an inbuilt garbage collector, which recycle all the unused memory and frees the memory and makes it available to the heap space.



### 6. What are the tools that help to find bugs or perform static analysis?

Ans: PyChecker is a static analysis tool that detects the bugs in Python source code and warns about the style and complexity of the bug. Pylint is another tool that verifies whether the module meets the coding standard.

 

 

### 7. What are Python decorators?

Ans: A Python decorator is a specific change that we make in Python syntax to alter functions easily.




### 8. What is the difference between list and tuple?
Ans: The difference between list and tuple is that list is mutable while tuple is not. Tuple can be hashed for e.g as a key for dictionaries.




### 9. How are arguments passed by value or by reference?
Ans: Everything in Python is an object and all variables hold references to the objects. The references values are according to the functions; as a result you cannot change the value of the references. However, you can change the objects if it is mutable.





### 10. What is Dict and List comprehensions are?
Ans: They are syntax constructions to ease the creation of a Dictionary or List based on existing iterable.




### 11. What are the built-in type does python provides?
Ans: There are mutable and Immutable types of Pythons built in types Mutable built-in types
List Sets
Dictionaries Immutable built-in types
Strings Tuples Numbers



### 12. What is namespace in Python?
Ans: In Python, every name introduced has a place where it lives and can be hooked for. This is known as namespace. It is like a box where a variable name is mapped to the object placed. Whenever the variable is searched out, this box will be searched, to get corresponding object.





### 13. What is lambda in Python?
Ans: It is a single expression anonymous function often used as In-line function.






### 14. Why lambda forms in python does not have statements?
Ans: A lambda form in python does not have statements as it is used to make new function object and then return them at runtime.



### 15. What is pass in Python?
Ans: Pass means, no-operation Python statement, or in other words it is a place holder in compound statement, where there should be a blank left and nothing has to be written there.





### 16. In Python what are iterators?
Ans: In Python, iterators are used to iterate a group of elements, containers like list.



### 17. What is unit test in Python?
Ans: A unit testing framework in Python is known as unittest. It supports sharing of setups, automation testing, shutdown code for tests, aggregation of tests into collections etc.




### 18. In Python what is slicing?
Ans: A mechanism to select a range of items from sequence types like list, tuple, strings etc. is known as slicing.



### 19. What are generators in Python?
Ans: The way of implementing iterators are known as generators. It is a normal function except that it yields expression in the function.



### 20. What is docstring in Python?
Ans: A Python documentation string is known as docstring, it is a way of documenting Python functions, modules and classes.




### 21. How can you copy an object in Python?
Ans: To copy an object in Python, you can try copy.copy () or copy.deepcopy() for the general case. You cannot copy all objects but most of them.



### 22. What is negative index in Python?
Ans: Python sequences can be index in positive and negative numbers. For positive index, 0 is the first index, 1 is the second index and so forth. For negative index, (-1) is the last index and (-2) is the second last index and so forth.



### 23. How you can convert a number to a string?
Ans: In order to convert a number into a string, use the inbuilt function str(). If you want a octal or hexadecimal representation, use the inbuilt function oct() or hex().




### 24. What is the difference between Xrange and range?
Ans: Xrange returns the xrange object while range returns the list, and uses the same memory and no matter what the range size is.




### 25. What is module and package in Python?
Ans: In Python, module is the way to structure program. Each Python program file is a module, which imports other modules like objects and attributes.
The folder of Python program is a package of modules. A package can have modules or subfolders.




### 26. Mention what are the rules for local and global variables in Python?
Ans: Local variables: If a variable is assigned a new value anywhere within the function’s body, it’s assumed to be local.

Global variables: Those variables that are only referenced inside a function are implicitly global.





### 27. How can you share global variables across modules?
Ans: To share global variables across modules within a single program, create a special module. Import the config module in all modules of your application. The module will be available as a global variable across modules.






### 28. Explain how can you make a Python Script executable on Unix?To make a Python Script executable on Unix, you need to do two things,
Ans: Script file’s mode must be executable and
the first line must begin with # ( #!/usr/local/bin/python)






### 29. Explain how to delete a file in Python?
Ans: By using a command os.remove (filename) or os.unlink(filename)





### 30. Explain how can you generate random numbers in Python?
Ans: To generate random numbers in Python, you need to import command as import random
random.random()
This returns a random floating point number in the range [0,1)






### 31. Explain how can you access a module written in Python from C?
Ans: You can access a module written in Python from C by following method, Module = =PyImport_ImportModule(“”);






### 32. Mention the use of // operator in Python?
Ans: It is a Floor Divisionoperator , which is used for dividing two operands with the result as quotient showing only digits before the decimal point. For instance, 10//5 = 2 and 10.0//5.0 = 2.0.




### 33. Mention five benefits of using Python?
Ans: Python comprises of a huge standard library for most Internet platforms like Email, HTML, etc.
Python does not require explicit memory management as the interpreter itself allocates the memory to new variables and free them automatically
Provide easy readability due to use of square brackets Easy-to-learn for beginners
Having the built-in data types saves programming time and effort from declaring variables






### 34. Mention the use of the split function in Python?
Ans: The use of the split function in Python is that it breaks a string into shorter strings using the defined separator. It gives a list of all words present in the string.







### 35. Explain what is Flask & its benefits?
Ans: Flask is a web micro framework for Python based on “Werkzeug, Jinja 2 and good intentions” BSD licensed. Werkzeug and jingja are two of its dependencies.


Flask is part of the micro-framework. Which means it will have little to no dependencies on external libraries. It makes the framework light while there is little dependency to update and less security bugs.





### 36. Mention what is the difference between Django, Pyramid, and Flask?
Ans: Flask is a “micro framework” primarily build for a small application with simpler requirements. In flask, you have to use external libraries. Flask is ready to use.
Pyramid are build for larger applications. It provides flexibility and lets the developer use the right tools for their project. The developer can choose the database, URL structure, templating style and more. Pyramid is heavy configurable.

Like Pyramid, Django can also used for larger applications. It includes an ORM.






### 37. Mention what is Flask-WTF and what are their features?
Ans: Flask-WTF offers simple integration with WTForms. Features include for Flask WTF are
Integration with wtforms Secure form with csrf token Global csrf protection Internationalization integration Recaptcha supporting
File upload that works with Flask Uploads






### 38. Explain what is the common way for the Flask script to work?
Ans: The common way for the flask script to work is…
Either it should be the import path for your application Or the path to a Python file






### 39. Explain how you can access sessions in Flask?
Ans: A session basically allows you to remember information from one request to another. In a flask, it uses a signed cookie so the user can look at the session contents and modify. The user can modify the session if only it has the secret key Flask.secret_key.


### 40. Is Flask an MVC model and if yes give an example showing MVC pattern for your application?
Ans: Basically, Flask is a minimalistic framework which behaves same as MVC framework. So MVC is a perfect fit for Flask, and the pattern for MVC we will consider for the following example

```
from flask import Flaskapp = Flask(_name_)
@app.route(“/”)

def hello():

   return “Hello World”

app.run(debug = True)

In this code your,
Configuration part will be
from flask import Flask

app = Flask(_name_)

View part will be
@app.route(“/”)

def hello():

   return “Hello World”

While you model or main part will be
app.run(debug = True)

``` 




### 41. What type of a language is python? Interpreted or Compiled?

Ans: Beginner’s Answer:

Python is an interpreted, interactive, object­oriented programming language.

Expert Answer:

Python is an interpreted language, as opposed to a compiled one, though the
distinction can be blurry because of the presence of the bytecode compiler. This means
that source files can be run directly without explicitly creating an executable which is
then run.



### 42. What do you mean by python being an “interpreted language”? (Continues from previous question)
Ans: An interpreted language​is a programming language​for which most of its
implementations execute instructions directly, without previously compiling a program
into machine­language​instructions. In context of Python, it means that Python program
runs directly from the source code.






### 43. What is python’s standard way of identifying a block of code?
Ans: Indentation.







### 44. Please provide an example implementation of a function called “my_func” that returns the square of a given variable “x”. (Continues from previous question)
Ans:
defmy_func(x):
returnx**2







### 45. Is python statically typed or dynamically typed?
Ans: ​Dynamic.
In a statically typed language, the type of variables must be known (and usually
declared) at the point at which it is used. Attempting to use it will be an error. In a
dynamically typed language, objects still have a type, but it is determined at runtime.
You are free to bind names (variables) to different objects with a different type. So long
as you only perform operations valid for the type the interpreter doesn’t care what type
they actually are.





### 46. Is python strongly typed or weakly typed language?
Ans: ​Strong.
In a weakly typed language a compiler / interpreter will sometimes change the
type of a variable. For example, in some languages (like JavaScript) you can add
strings to numbers ‘x’ + 3 becomes ‘x3’. This can be a problem because if you have
made a mistake in your program, instead of raising an exception execution will continue
but your variables now have wrong and unexpected values. In a strongly typed
language (like Python) you can’t perform operations inappropriate to the type of the
object ­ attempting to add numbers to strings will fail. Problems like these are easier to
diagnose because the exception is raised at the point where the error occurs rather than
at some other, potentially far removed, place.







### 47. Create a unicode string in python with the string “This is a test string”?
Ans: some_variable=u’Thisisateststring’
Or
some_variable=u”Thisisateststring”







### 48. What is the python syntax for switch case statements?
Ans: Python doesn’t support switch­case statements. You can use if­else statements
for this purpose.










### 49. What is a lambda statement? Provide an example.
Ans: A lambda statement is used to create new function objects and then return them at
runtime. Example:
my_func=lambdax:x**2
creates a function called my_func that returns the square of the argument
passed.








### 50.What are the rules for local and global variables in Python?
Ans: If a variable is defined outside function then it is implicitly global​. If variable is
assigned new value inside the function means it is local​. If we want to make it global we

need to explicitly define it as global. Variable referenced inside the function are implicit
global​


 ### 51 What is the difference between a list and a tuple? When should you use each?
A list is a mutable data structure while a tuple is an immutable one.
A mutable object in Python has the ability to change its values.

Lists are dynamic: you can add items to them or override and remove existing ones.
Tuples are fixed-size: they don’t have an appendor an extendmethod. You cannot remove items from them either.
Both tuples and lists support indexing and allow using the inoperator to check for existing elements in them.

→ There are some situations where I think tuples might be useful.

If you declare a collection of items that you know will never change or that you will loop over only without changing its values, use tuples.
If you look for performance, tuples are faster than lists since they’re read-only structures. If you don’t need write operations, consider using tuples.
Tuples can make your code safer if you want to prevent accidentally writing data that doesn’t need to be changed.
Here’s a code sample that show how tuples differ from lists.

```
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[1] = 100
>>> print(numbers)
[1, 100, 3, 4, 5]

>>> names = ("john", "joe", "alice")
>>> names[0] = "bob")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-25012ce34a87> in <module>
----> 1 names[0] = "bob"

TypeError: 'tuple' object does not support item assignment
```

### 52 What is the difference between multiprocessing and multithreading? When should you use each?
Multiprocessing and Multithreading are programming paradigms that aim to speed up your code.

When you use multiprocessing, you parallelize your computation over processes. Processes are independent and don’t communicate with each other: they don’t share the same memory area and have strict isolation between. In terms of applications, multiprocessing is suited for CPU-intensive workloads. It does, however, have a large memory footprint that is proportional to the number of processes.

On the other hand, in multithreaded applications, threads live inside a single process. Consequently, they share the same memory area: they can modify the same variables and can interfere with one another. While processes are strictly executed in parallel, only one thread is executed at a given point in time in Python, and this is due to the Global Interpreter Lock (GIL). Multithreading is suited to IO-bound applications such as web scraping or fetching data from a database.

### 53 What is the difference between a module, a package, and a library?
A module is simply a Python file that’s intended to be imported into scripts or other modules. It contains functions, classes, and global variables.

A package is a collection of modules that are grouped together inside a folder to provide consistent functionality. Packages can be imported just like modules. They usually have an __init__.pyfile in them that tells the Python interpreter to process them as such.

A library is a collection of packages.

### 53 Are function arguments passed by reference or by value?
All function arguments are passed by reference in Python: this means that if you pass a parameter to a function, the function gets a reference to that same object.

If the object is mutable and the function changes it, the parameter will mutate in the outer scope of the function. Let’s see an example:

```
>>> def append_number(numbers):
        numbers.append(5)

>>> numbers = [1, 2, 3, 4]
>>> print(f"before: {numbers}"
[1, 2, 3, 4]

>>> append_number(numbers)
>>> numbers
[1, 2, 3, 4, 5]
```



### 54 What is namespace in Python?
In Python, a namespace is a system that assigns a unique name to each and every object. A variable or a method might be considered an object. Python has its own namespace, which is kept in the form of a Python dictionary. Let’s look at a directory-file system structure in a computer as an example. It should go without saying that a file with the same name might be found in numerous folders. However, by supplying the absolute path of the file, one may be routed to it if desired.

A namespace is essentially a technique for ensuring that all of the names in a programme are distinct and may be used interchangeably. You may already be aware that everything in Python is an object, including strings, lists, functions, and so on. Another notable thing is that Python uses dictionaries to implement namespaces. A name-to-object mapping exists, with the names serving as keys and the objects serving as values. The same name can be used by many namespaces, each mapping it to a distinct object. Here are a few namespace examples:

Local Namespace: This namespace stores the local names of functions. This namespace is created when a function is invoked and only lives till the function returns.

Global Namespace: Names from various imported modules that you are utilizing in a project are stored in this namespace. It’s formed when the module is added to the project and lasts till the script is completed.

Built-in Namespace: This namespace contains the names of built-in functions and exceptions.

## 55 How is memory managed in Python?
This is one of the most commonly asked python interview questions

Memory management in python comprises a private heap containing all objects and data structure. The heap is managed by the interpreter and the programmer does not have access to it at all. The Python memory manager does all the memory allocation. Moreover, there is an inbuilt garbage collector that recycles and frees memory for the heap space.

## 56 How do you delete a file in Python?
Files can be deleted in Python by using the command os.remove (filename) or os.unlink(filename)


## 57 What are Python decorators?
Decorators are functions that take another function as an argument to modify its behavior without changing the function itself. These are useful when we want to dynamically increase the functionality of a function without changing it.

Here is an example:
```
def smart_divide(func):
    def inner(a, b):
        print("Dividing", a, "by", b)
        if b == 0:
            print("Make sure Denominator is not zero")
            return
return func(a, b)
    return inner
@smart_divide
def divide(a, b):
    print(a/b)
divide(1,0)
```
Here smart_divide is a decorator function that is used to add functionality to simple divide function.


## 58 What is Scope Resolution in Python?
The variable’s accessibility is defined in python according to the location of the variable declaration, called the scope of variables in python. Scope Resolution refers to the order in which these variables are looked for a name to variable matching. Following is the scope defined in python for variable declaration.

a. Local scope – The variable declared inside a loop, the function body is accessible only within that function or loop.

b. Global scope – The variable is declared outside any other code at the topmost level and is accessible everywhere.

c. Enclosing scope – The variable is declared inside an enclosing function, accessible only within that enclosing function.

d. Built-in Scope – The variable declared inside the inbuilt functions of various modules of python has the built-in scope and is accessible only within that particular module.

The scope resolution for any variable is made in java in a particular order, and that order is

Local Scope -> enclosing scope -> global scope -> built-in scope

## 59 What do you mean by Python literals?
A literal is a simple and direct form of expressing a value. Literals reflect the primitive type options available in that language. Integers, floating-point numbers, Booleans, and character strings are some of the most common forms of literal. Python supports the following literals:

Literals in Python relate to the data that is kept in a variable or constant. There are several types of literals present in Python

String Literals: It’s a sequence of characters wrapped in a set of codes. Depending on the number of quotations used, there can be single, double, or triple strings. Single characters enclosed by single or double quotations are known as character literals.

Numeric Literals: These are unchangeable numbers that may be divided into three types: integer, float, and complex.

Boolean Literals: True or False, which signify ‘1’ and ‘0,’ respectively, can be assigned to them.

Special Literals: It’s used to categorize fields that have not been generated. ‘None’ is the value that is used to represent it.

String literals: “halo” , ‘12345’
Int literals: 0,1,2,-1,-2
Long literals: 89675L
Float literals: 3.14
Complex literals: 12j
Boolean literals: True or False
Special literals: None
Unicode literals: u”hello”
List literals: [], [5, 6, 7]
Tuple literals: (), (9,), (8, 9, 0)
Dict literals: {}, {‘x’:1}
Set literals: {8, 9, 10}

## 60 Are Arguments in Python Passed by Value or by Reference?
Arguments are passed in python by a reference. This means that any changes made within a function are reflected in the original object.

Consider two sets of code shown below:
![image](https://user-images.githubusercontent.com/93423367/215160015-8ccda4f9-830e-4de5-b2cf-bdd70accc90b.png)

In the first example, we only assigned a value to one element of ‘l’, so the output is [3, 2, 3, 4].

In the second example, we have created a whole new object for ‘l’. But, the values [3, 2, 3, 4] doesn’t show up in the output as it is outside the definition of the function.


## 61 How Do You Use Print() Without the Newline?
The solution to this depends on the Python version you are using. 

Python v2

>>print(“Hi. ”),

>>print(“How are you?”)

Output: Hi. How are you?

Python v3

>>print(“Hi”,end=“ ”)

>>print(“How are you?”)

Output: Hi. How are you?


## 62 Is Python Object-oriented or Functional Programming?
Python is considered a multi-paradigm language.

Python follows the object-oriented paradigm 

Python allows the creation of objects and their manipulation through specific methods 
It supports most of the features of OOPS such as inheritance and polymorphism
Python follows the functional programming paradigm

Functions may be used as the first-class object 
Python supports Lambda functions which are characteristic of the functional paradigm 

## 63 What Are *args and *kwargs?
*args 

It is used in a function prototype to accept a varying number of arguments.
It's an iterable object. 
Usage - def fun(*args)
*kwargs 

It is used in a function prototype to accept the varying number of keyworded arguments.
It's an iterable object
Usage - def fun(**kwargs):
fun(colour=”red”.units=2)

## 64 “in Python, Functions Are First-class Objects.” What Do You Infer from This?
It means that a function can be treated just like an object. You can assign them to variables, or pass them as arguments to other functions. You can even return them from other functions.


## 65 What Is the Output Of: Print(__name__)? Justify Your Answer.
__name__ is a special variable that holds the name of the current module. Program execution starts from main or code with 0 indentations. Thus, __name__ has a value __main__ in the above case. If the file is imported from another module, __name__ holds the name of this module.
