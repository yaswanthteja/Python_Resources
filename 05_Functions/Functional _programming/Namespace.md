
## Namespace
Namespace is a container that holds a set of identifiers (names) and their corresponding objects (values). It provides a way to organize and manage the names used in a program, preventing naming conflicts and providing a scope for variables and other identifiers.

There are several types of namespaces in Python:

1. built-in namespace —→ starts when ever idle or python  opens
2. module/global name space ———> starts  at run time
3. local name space ———>used for  functions & methods
4. Enclosed namespace ———> used for nested

1. **Local Namespace (Local Scope):**
    - A local namespace is associated with a specific function or method.
    - It contains the local variables and parameters defined within that function.
    - The local namespace is created when the function is called and is destroyed when the function exits.
    
    Example:
    
    ```python
    
    def my_function(x):
        local_variable = x
        print(local_variable)
    
    ```
    
2. **Global Namespace (Global Scope):**
    - The global namespace contains names defined at the top level of a module or script.
    - It includes global variables and functions.
    - The global namespace is created when the module is imported or when the script is executed, and it persists throughout the lifetime of the program.
    
    Example:
    
    ```python
    
    global_variable = 42
    
    def my_function():
        print(global_variable)
    
    ```
    
3. **Built-in Namespace:**
    - The built-in namespace contains names that are built into the Python language and are always available.
    - It includes built-in functions, exceptions, and constants.
    - Names in the built-in namespace can be accessed without importing any modules.
    
    Example:
    
    ```python
    
    result = len([1, 2, 3])
    
    ```
    
4. **Module Namespace:**
    - Each module in Python has its own namespace.
    - It contains the names defined within the module, including functions, variables, and classes.
    - Module namespaces help organize code and avoid naming conflicts between modules.
    
    Example:
    
    ```python
    
    # module.py
    module_variable = 10
    
    def module_function():
        print(module_variable)
    
    ```
    
5. **Class Namespace:**
    - Each class in Python has its own namespace.
    - It contains the names defined within the class, including attributes and methods.
    - Class namespaces help encapsulate the behavior of objects and avoid naming conflicts between classes.
    
    Example:
    
    ```python
    
    class MyClass:
        class_variable = 20
    
        def __init__(self):
            self.instance_variable = 30
    
    ```
    

Namespaces provide a way to organize code, encapsulate functionality, and manage the scope of identifiers in Python programs. Understanding namespaces is crucial for avoiding naming conflicts and writing modular and maintainable code.

## LEGB(local,enclosed,global,built-in)

LEGB is an acronym that represents the order in which Python looks for names (identifiers) when they are referenced in code. It stands for Local, Enclosing, Global, and Built-in, which are the four nested scopes or namespaces that Python searches to resolve the reference to a name.

Here's a brief overview of each scope:

1. **Local (L):**
    - The local scope refers to the innermost scope, typically associated with a function or method.
    - It contains local variables and parameters defined within the function.
    - The local scope is created when the function is called and is destroyed when the function exits.
2. **Enclosing (E):**
    - The enclosing scope refers to the scope of the containing function if the current scope is inside a nested function.
    - It captures the local scope of the enclosing function.
    - This scope is relevant when dealing with nested functions.
3. **Global (G):**
    - The global scope refers to the top-level scope of a module or script.
    - It contains global variables and functions defined at the module level.
    - The global scope is created when the module is imported or when the script is executed and persists throughout the program.
4. **Built-in (B):**
    - The built-in scope refers to the scope containing built-in names that are always available.
    - It includes built-in functions, exceptions, and constants.
    - Names in the built-in scope can be accessed without importing any modules.

When a name is referenced in code, Python searches for the name in the following order: local, enclosing, global, and built-in. If the name is found in one of these scopes, the search stops, and the corresponding value is used. If the name is not found in any of the scopes, a **`NameError`** is raised.

Understanding the LEGB rule is crucial for resolving variable names and avoiding naming conflicts in Python programs. It helps programmers write clear and unambiguous code by specifying the order in which different scopes are searched.

```python
# Global scope
global_variable = "I am global"

def outer_function():
    # Enclosing scope
    enclosing_variable = "I am in the enclosing scope"

    def inner_function():
        # Local scope
        local_variable = "I am in the local scope"
        print(local_variable)
        print(enclosing_variable)
        print(global_variable)

    inner_function()

# Call the outer function
outer_function()
```

In this example:

- **`global_variable`** is in the global scope.
- **`outer_function`** defines **`enclosing_variable`** in its local scope.
- **`inner_function`** defines **`local_variable`** in its local scope.

When **`inner_function`** is called from within **`outer_function`**, Python follows the LEGB rule:

1. **Local (L):** It first looks for **`local_variable`** in its own local scope. It finds it and prints its value.
2. **Enclosing (E):** If the variable is not found in the local scope, Python looks in the enclosing scope of **`outer_function`**. It finds **`enclosing_variable`** and prints its value.
3. **Global (G):** If the variable is not found in the enclosing scope, Python looks in the global scope. It finds **`global_variable`** and prints its value.
4. **Built-in (B):** If the variable is not found in the global scope, Python looks in the built-in scope for built-in names.

The output of running this code would be:

```python

I am in the local scope
I am in the enclosing scope
I am global

```

This demonstrates how Python searches for variables in different scopes based on the LEGB rule.
