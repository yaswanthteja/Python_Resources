

###  What Is Object-Oriented Programming in Python?
Object-oriented programming is a programming paradigm that provides a means of structuring programs so that properties and behaviors are bundled into individual objects.



### 1. Python uses access specifiers, right?

Ans: Access specifiers like private, public, protected, etc.
promotional ad for article skills
are not used by Python. But it doesn't get this information from any variables. By using a single (protected) or double underscore (private) as a prefix to the variable names, it mimics the behaviour of variables. The variables that don't have an underscore before them are public by default.

### 2. Can a parent class be called without first creating an instance of it?

Ans: Yes, it is feasible if the base class is a static method or if additional child classes instantiate the base class.

### 3. How do you make a Python class that is empty?
Ans: A class that is empty has no defined members. By employing the pass keyword, it is made (the pass command does nothing in python). Outside of the class, we can produce objects for this class.

### 4. Explain the differences between override and new modifiers.
Ans: The base class function is not to be utilised; instead, the new modifier instructs the compiler to use the new implementation. When overriding a base class function inside a child class, the Override modifier is helpful.

### 5. Why do we finalise?
Ans: Before the trash collection function is called, unmanaged resources are released and cleaned up using the finalise method. Tasks involving memory management are facilitated by this.

### 6. What does Python's init function do?
Ans: The Java constructors and the init method both function identically. As soon as an object is created, the method is called. When an object is first created, it is helpful for initialising any characteristics or default behaviours.

### 7. How can you determine whether a class is a subclass of another class?
Ans: This is accomplished by utilising a Python function called issubclass(). The function returns true or false depending on if a class is a child of another class, indicating whether it is.

### 8. What is a Class in python?
Ans: Even the class is an object. The purpose of classes is to produce class objects. The characteristics (state) and behaviour of class objects (variables). We may create class variables to hold information that is available in each instance object. Metaclass type is used while creating classes.

### 9. How do you make a Python class that is empty?
Ans: A class with no declared code is said to be empty. The pass keyword is inserted into the class to create an empty class. Python allows us to construct an object of the empty class.

### 10. What does a class object or instance mean?
Ans: A class type variable or class instance is an object. A class object must be generated in order to use a class. Allocate RAM to hold the contents of the class variable when you create a class instance. Data from the class's instance variable is transferred to the object or instance when a class object is created. Each class object or instance is distinct. Class objects have attributes and capabilities. Functions are the actions carried out by the object or instance, whereas properties are its qualities.

### 11. How Can an Object Be Created?
Ans: The heap allocates a block of memory for the stud object (refer below example). The Student class's memory allocation is determined by the variables and methods of the object. The variables and methods provided in the object of the Student class determine how much memory the object requires. The class's new function manages the object's memory allocation. Following the memory allocation in which the instance variables are declared, the new method invokes the init method. The returned value is the memory address assigned to the Stud object. Self is used to pass the object's or instance's memory location.

### 12. A class function Object() { [native code] }: What does it do?
Ans: Python has a unique kind of procedure called a function Object() { [native code] } that is used to set up the class' instance variables. The class's function Object() { [native code] }, often known as the default method, is the init method. The init method is automatically invoked when memory has been allocated by the new function. It is possible to declare instance variables using this function Object() { [native code] } method. The function Object() { [native code] } is executed for each instance if a class generates two.


