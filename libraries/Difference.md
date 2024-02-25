
## Differences Between Python Modules, Packages, Libraries, and Frameworks


If you are new to Python, you might be confused about all its libraries, packages, modules, and frameworks, But mostly all will think  that there are some pieces of code in it.

But what’s the difference between them? 
I’ll try to explain the difference between Python modules, packages, libraries, and frameworks.

Before getting to it let me give you  a basic idea about

## What is python?

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. With its high-level built-in data structures,  Python's simple, easy-to-learn syntax emphasizes readability and therefore reduces the cost of program maintenance.

Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms and can be freely distributed.

#  Why do we use these Modules, Packages, Libraries, and Frameworks?

 Real-world programs are complex. Even a simple snake  game  would require lots of code if you programmed everything from scratch. To simplify the process and make it more effective, developers leverage 
- **modular programming** – a method of breaking large coding tasks into smaller and more manageable subtasks. This is why Python has so many modules, packages, libraries, and frameworks.



## Python Modules

- **A module is a bunch of related code saved in a file with the extension .py**. 
- You may choose to define functions, classes, or variables in a module. It’s also fine to include runnable code in modules.
- If you want your code to be well organized, it’s a good idea to start by grouping related code.


- For example, let’s define a function to welcome Messages for visitors of your website or blog 
 

```python
def welcome_message(blog):
  print("Thank you for Visiting to our " +Blog+ " Blog. You will get all the details in   the blog.")

```
To have this function stored in the module welcome, we save this code in a file named welcome.py.


If we want to use this code in our application, we first need to import the respective module using the import statement. Then, we’ll be ready to use a function defined in this module by calling that function with the module.function() syntax:

```Python
import welcome
welcome.welcome_message (“dev blog”)
Output
"Thank you for Visiting our  dev blog. You will get all the details in  the blog
```

It’s common to have many different items defined within the same module. So, you may want to import only one specific function rather than the entire module. For that, you can use the following syntax:

```python
from welcome import welcome_message
```

If you have some experience with Python, you’ve likely used modules.  For example, you may have used the: 

- [re](https://docs.python.org/3/library/re.html): module to detect and parse regular expressions in Python
- [date&time](https://docs.python.org/3/library/datetime.html): module to manipulate date and time data.
- [random](https://docs.python.org/3/library/random.html): module to generate pseudo-random number generators for various distributions.


## We have numerous benefits using modules in your Python code

- **Improved development process**.
Python modules help you focus on one small portion of a task rather than an entire problem. This simplifies the development process and makes it less prone to errors. Furthermore, modules are usually written in a way that minimizes interdependency. Thus, it’s more viable for a team of several programmers to work on the same application.

- The functionality you define in one module can be used in different parts of an application, minimizing duplicate code.
- **Separate namespaces**.  With Python modules, you can define separate namespaces to avoid collisions between identifiers in different parts of your application.


## **Python Packages**


When developing a large application, you may end up with many different modules that are difficult to manage. In such a case, you’ll benefit from grouping and organizing your modules. That’s when packages come into play.

- **Python packages are a directory of a collection of modules**. Packages allow the hierarchical structure of the module namespace. 

- Just like we organize our files on a hard drive into folders and sub-folders, we can organize our modules into packages and sub-packages.

- To be considered a package (or subpackage), a directory must contain a file named **__init__.py**. 

- This file usually includes the initialization code for the corresponding package.

For example, we can have the following package my_model with modules related to our data science project:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xx7o4okmcc26s5xexrsu.png)
 
We can import specific modules from this package using the dot notation. For example, to import the dataset module from the above package, we can use one of the following code snippets:

```python
import my_model.training.dataset
```

(or)

```python
from my_model.training import dataset
```

Next, we may choose to import only the **load_dataset()** function from our **dataset.py** module. Either of the following options will do the job:

```python
import my_model.training.dataset.load_dataset()
```

(or)

```python
from my_model.training.dataset import load_dataset()
```

There are a lot of built-in and open-source Python packages that you are probably already using.

- [Numpy](https://numpy.org/) :is the fundamental Python package for scientific computing.
- [pandas](https://pandas.pydata.org/): is a Python package for fast and efficient processing of tabular data, time series, matrix data, etc.
- [pytest](https://pypi.org/project/pytest/) : provides a variety of modules to test new code, including small unit tests or complex functional tests.

As your application grows larger and uses many different modules, Python packages become a crucial component for optimizing your code structure.

## Python Libraries

- A library is an umbrella term referring to a reusable chunk of code. Usually, a Python **library contains a collection of related modules and packages**.
- Actually, this term is often used interchangeably with “Python package” because packages can also contain modules and other packages (sub-packages). 
- However, it is often assumed that **while a package is a collection of modules, a library is a collection of packages**.

Oftentimes, developers create Python libraries to share reusable code with the community. To eliminate the need for writing code from scratch, they create a set of useful functions related to the same area.

There are thousands of useful libraries available today. I’ll give just a few examples:

- [Matplotlib](https://matplotlib.org/) : library is a standard library for generating data visualizations in Python. It supports building basic two-dimensional graphs as well as more complex animated and interactive visualizations.

- [Pytorch](https://pytorch.org/) : is an open-source deep-learning library built by Facebook’s AI Research lab to implement advanced neural networks and cutting-edge research ideas in industry and academia.
- [Pygame](https://pypi.org/project/pygame/) :provides developers with tons of convenient features and tools to make game development a more intuitive task.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): is a very popular Python library for getting data from the web. The modules and packages inside this library help extract useful information from HTML and XML files.
- [Requests](https://docs.python-requests.org/en/master/) :  is a part of a large collection of libraries designed to make Python HTTP requests simpler. The library offers an intuitive JSON method that helps you avoid manually adding query strings to your URLs.

- [missingno](https://github.com/ResidentMario/missingno) :is very handy for handling missing data points. It provides informative visualizations about the missing values in a dataframe, helping data scientists to spot areas with missing data. It is just one of the many great Python libraries for data cleaning.


## Python Frameworks


- Similar to libraries, Python frameworks are a collection of modules and packages that help programmers to fast-track the development process.
- However, frameworks are usually more complex than libraries. 
- Also, while libraries contain packages that perform specific operations, **frameworks contain the basic flow and architecture of the application**.



If you COMPARE APPLICATION DEVELOPMENT TO HOUSE CONSTRUCTION, Python frameworks provide all the essential building blocks like the foundation, walls, windows, and roof. 
Then, the developers build their application around this foundation by adding functionalities comparable to a house’s alarm system, furniture, appliances, etc.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/comghquo3ywh5z3415fj.png)
 

For a better understanding, let’s review several popular frameworks:

- [Django ](https://www.djangoproject.com/)is a Python framework for building web applications with less coding. With all the necessary features included by default, developers can focus on their applications rather than dealing with routine processes.

- [Flask ](https://flask.palletsprojects.com/en/2.0.x/)is a web development framework that is known for its lightweight and modular design. It has many out-of-the-box features and is easily adaptable to specific requirements. 

- [Bottle](https://bottlepy.org/docs/dev/)is another lightweight framework for web development that was originally meant for building APIs. Its unique features are that it has no dependencies other than the [Python Standard Library](https://docs.python.org/3/library/) and it implements everything in a single source file.

Python frameworks allow programmers to streamline the web development process by providing a necessary foundation while still being flexible. No wonder that top applications – including Netflix, Airbnb, Reddit, and Udemy – leverage the benefits of Python frameworks.





