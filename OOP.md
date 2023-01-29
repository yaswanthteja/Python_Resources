

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






### 13. What kinds of variables are there in Python?
Ans: 
The following 2 categories of variables are initializable and modifiable within the class.

  - Instance Variable
  - Class Variable / Static Variable
### 14. What in Python is an instance variable?
Ans: Variables that are specific to an instance of an object are defined in the class; other instances cannot access these variables. The self arguments and the class function Object() { [native code] } method define and initialise instance variables. We may use the self keyword to specify instance variables in the init method. Class variables are less often used than instance variables.

### 15. What exactly is a static variable or class variable?
Ans: All instances of the class have access to the class variables. Class variables are declared at the beginning of the Python class. Changes to one class variable have an impact on the class variable of the other instance. Class variables can also be accessed outside of a class; to do so, use the class name and class variable name.

### 16. What Python function is new?
Ans: The new method produces a class object. It will employ in order to manage the production of a fresh instance of the class. Memory is set aside for the item. An object's instance variables require memory to store them. When an object is created, this method will be invoked. A type can be sent as the first parameter to the new method, which then returns a fresh instance of that type. The creation of a new instance will be managed by the new method. The new method gives the calling class its new instance back.

### 17. What in Python is init?
Ans: Python classes have an init function and function Object() { [native code] }. Following memory allocation from the new method, this method is automatically invoked. The init method is present in all classes.

### 18. What various sorts of Python methods are there?
Ans: The class has three distinct kinds of methods. All of the class activities are carried out with these techniques.
- Instance Methods
- Class Methods
- Static Methods
### 19. What does Python's instance method mean?
Ans: Methods known as instance methods operate on a class's instance variables. The memory address is crucial information that the instance method needs to know, and it can be found out thanks to its first parameter, self. Using the self. variable name within the self method, we can quickly retrieve instance variables.

### 20. What do Python class methods do?
Ans: A class method is a method that operates on static and class variables. The @classmethod decorator must be used to create a method that is a member of a class. Cls, which refers to the class itself, is the input argument for the class method.

### 21. What do Python's static methods mean?
Ans: When processing that relates to a class but does not need the class or any of its instances is needed, the static method is utilised.

### 22. What does Python's Nested Class mean?
Ans: A class is referred to be an inner class or nested class if it is declared inside another class. The code may become more object-oriented by using inner classes. Although it is possible to specify more than one inner class in a class, doing so is not advised.

### 23. What does Python's inheritance mean?
Ans: The new class must be derived from the existing class through inheritance. The current class's variables and methods can be accessed in the new class through inheritance. In Python, every class is descended from the object class. The object class becomes the superclass when a Python class is created on the inside. Code accessibility is inheritance's key benefit.

### 24. What kinds of inheritance are there in Python?
Ans: The four main forms of inheritance are listed below.

Inheritance gives the power to a class to access all attributes and methods of another class. It aids in code reusability and helps the developer to maintain applications without redundant code. The class inheriting from another class is a child class or also called a derived class. The class from which a child class derives the members are called parent class or superclass.

- Single Inheritance
- Multi-level Inheritance
- Hierarchical Inheritance
- Multiple Inheritance
- 
### 25. What in Python Is a Single Inheritance?
Ans: Single inheritance is the process through which a class derives from a single base or parent class. The child class has access by default to the base class's function Object() { [native code] } function.
![image](https://user-images.githubusercontent.com/93423367/215339614-3b8fa090-c08d-4bf4-a3d8-514b82763e00.png)
```
# Parent class
class ParentClass:
    def par_func(self):
         print("I am parent class function")

# Child class
class ChildClass(ParentClass):
    def child_func(self):
         print("I am child class function")

# Driver code
obj1 = ChildClass()
obj1.par_func()
obj1.child_func()

```

### 26. What does Python's function Object() { [native code] } overriding mean?
Ans: The child class cannot access the function Object() { [native code] } of a parent class if we write constructors in both classes. Only the child class function Object() { [native code] } is available in this situation; the parent class function Object() { [native code] } is no longer used. When the current function Object() { [native code] } has to be changed, function Object() { [native code] } overriding is utilised.
```
class University:
  def __init__(self):
    self.name = 'Yele University'
    print("You are in University Class Constructor")
 
class College (University):
  def __init__(self):
    self.name = 'Yale School of Medicine'
    print('You are in college Class Constructor')
 
  def show(self):
    print('College class instance method:',self.name)
 
college = College()
college.show()
```
### 27. What does Python's Super Method mean?
Ans: If we write a function Object() { [native code] } for each class, the child class cannot use the function Object() { [native code] } from the parent class. The child class function Object() { [native code] } takes the place of the parent class function Object() { [native code] } in this scenario. The super function must be used if we wish to access the function Object() { [native code] } of the parent class.
```
class University:
  def __init__(self):
    self.name = 'Yele University'
    print("You are in University Class Constructor")
   
  def disp(self):
    print('You are in University class disp method')
 
class College (University):
  def __init__(self):
    super().__init__()
    self.name = 'Yale School of Medicine'
    print('You are in college Class Constructor')
 
  def show(self):
    print('College class instance method:',self.name)
 
college = College()
college.show()
college.disp()
```
### 28. What does Python's multi-level inheritance mean?

Ans: The class inherits a feature from another derived class via multi-level inheritance (Child Class). The class under Multi-Level Inheritance derives a different child class. The University class inherits from the College class in the example below, and the Student class inherits from the College class. The Student class in this sort of inheritance has access to the variables and methods from the University and College classes.

 The members of the parent class, A, are inherited by child class which is then inherited by another child class, B. The features of the base class and the derived class are further inherited into the new derived class, C. Here, A is the grandfather class of class C.
![image](https://user-images.githubusercontent.com/93423367/215339714-cb246104-695b-4a88-bae6-378f80afe8d1.png)



```
# Parent class
class A:
   def __init__(self, a_name):
       self.a_name = a_name
   
# Intermediate class
class B(A):
   def __init__(self, b_name, a_name):
       self.b_name = b_name
       # invoke constructor of class A
       A.__init__(self, a_name)

# Child class
class C(B):
   def __init__(self,c_name, b_name, a_name):
       self.c_name = c_name
       # invoke constructor of class B
       B.__init__(self, b_name, a_name)
       
   def display_names(self):
       print("A name : ", self.a_name)
       print("B name : ", self.b_name)
       print("C name : ", self.c_name)

#  Driver code
obj1 = C('child', 'intermediate', 'parent')
print(obj1.a_name)
obj1.display_names()


```


  ```
  def __init__(self):
    self.name = 'Yele University'
    print("You are in University Class Constructor")
   
  def disp(self):
    print('You are in University class disp method')
 
class College (University):
  def __init__(self):
    self.name = 'Yale School of Medicine'
    print('You are in college Class Constructor')
 
  def show(self):
    print('College class instance method:',self.name)
 
class Student(College):
  def __init__(self):
    self.name='Martin'
    print('You are in student Class Constructor')
 
  def view(self):
    print('Student class instance method:',self.name)
 
student = Student()
student.view()
student.show()
student.disp()
```
### 29. What does Python's hierarchical inheritance mean?



Ans: We may inherit a class from many classes via hierarchical inheritance. The MedicalCollege and LawCollege classes in the example below have inherited the University Base/Parent class. Both of the child classes may now access the parent class's variables and methods.



When a parent class is derived by more than one child class, it is called hierarchical inheritance.
![image](https://user-images.githubusercontent.com/93423367/215339797-6321cb5b-eca9-4c9f-b9b0-58a3de4c5d41.png)

```
class University:
  def __init__(self):
    self.name = 'Yele University'
    print("You are in University Class Constructor")
   
  def disp(self):
    print('You are in University class disp method')
 
class MedicalCollege (University):
  def __init__(self):
    self.name = 'Yale School of Medicine'
    print('You are in Medical college Class Constructor')
 
  def show(self):
    print('Medical College class instance method:',self.name)
 
class LawCollege (University):
  def __init__(self):
    self.name = 'Yale Law School'
    print('You are in Law college Class Constructor')
 
  def view(self):
    print('Law College class instance method:',self.name) 
 
lawcollege = LawCollege()
lawcollege.view()
lawcollege.disp()
 
medicalcollege = MedicalCollege()
medicalcollege.show()
medicalcollege.disp()
```

### 30. What does Python's Multiple Inheritance mean?
Ans: Many Inheritance is the term used when a class inherits from multiple classes. The workings of numerous inheritances are seen in the example presented below.

 This is achieved when one child class derives members from more than one parent class. All features of parent classes are inherited in the child class.
 ![image](https://user-images.githubusercontent.com/93423367/215339865-cbcc2a26-7e28-462d-ba13-0140da0ac9be.png)

```
# Parent class1
class Parent1:
   def parent1_func(self):
       print("Hi I am first Parent")

# Parent class2
class Parent2:
   def parent2_func(self):
       print("Hi I am second Parent")

# Child class
class Child(Parent1, Parent2):
   def child_func(self):
       self.parent1_func()
       self.parent2_func()

# Driver's code
obj1 = Child()
obj1.child_func()
```
 
```
class Father:
  def __init__(self):
    print('You are in Father Class Constructor')
   
  def disp(self):
    print("Father Class instance Method")
         
class Mother:
  def __init__(self):
    print("You are in Mother Class Constructor")
   
  def show(self):
    print("Mother Class instance Method")
         
class Son(Father, Mother):
    def __init__(self):
        print("You are in Son Class Constructor")
   
    def view(self):
        print("Son Class Instance Method")
         
         
son = Son()
son.view()
son.show()
son.disp()
```
### 31. What does Python's MRO (Method Resolution Order) mean?
Ans:
Method Resolution Order is referred to as MRO.
A class inherits from many classes under multiple inheritance.
If we attempt to access a method by building an object from the child class, the methods of the child class are first searched for the method.
If the method is not found in the child class, the inheritance classes are searched from left to right.
The display method is present in both the Father and Mother classes in the example presented below.
In MRO, methods and variables are searched from left to right because while conducting inheritance, father class is written first and mother class is written afterwards.
After the kid class, the father class's factors and research methodologies are prioritised in

```
class Father:
  def __init__(self):
    print('You are in Father Class Constructor')
   
  def show(self):
    print("Father Class instance Method")
         
class Mother:
  def __init__(self):
    print("You are in Mother Class Constructor")
   
  def show(self):
    print("Mother Class instance Method")
         
class Son(Father, Mother):
    def __init__(self):
        print("You are in Son Class Constructor")
     
son = Son()
son.show() 
```
