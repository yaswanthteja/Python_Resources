## lamdba functions
**A lambda function in Python is a small, anonymous function that is defined using the `lambda` keyword.** 

Lambda functions are also known as anonymous functions or lambda expressions. 

They are typically used for short, simple operations that can be defined in a single line of code.

The basic syntax of a lambda function is as follows:

```python

lambda arguments: expression

```

`lambda inputs : return value`

- **`lambda`** is the keyword that defines the lambda function.
- **`arguments`** are the input parameters to the function.
- **`expression`** is a single expression that is evaluated and returned as the result of the function.

Lambda functions are often used in scenarios where a small, throwaway function is needed for a short operation, such as when passing a function as an argument to another function like **`map()`**, **`filter()`**, or **`sorted()`**.

Here are some examples of lambda functions:

1. **Simple Addition:**
    
    ```python
    
    add = lambda x, y: x + y
    result = add(3, 5)
    print(result)  # Output: 8
    
    ```
    
2. **Sorting a List of Tuples:**
    
    ```python
    
    points = [(1, 3), (2, 1), (0, 5)]
    points_sorted = sorted(points, key=lambda point: point[1])
    print(points_sorted)  # Output: [(2, 1), (1, 3), (0, 5)]
    
    ```
    
3. **Filtering a List:**
    
    ```python
    
    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)  # Output: [2, 4, 6]
    
    ```
    
4. **Mapping a List:**
    
    ```python
    
    numbers = [1, 2, 3, 4, 5]
    doubled_numbers = list(map(lambda x: x * 2, numbers))
    print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]
    
    ```
    

It's important to note that while lambda functions are convenient for simple operations, they are not meant for complex logic. For more complex functions, it's recommended to define a regular named function using the **`def`** keyword for better readability and maintainability. Lambda functions are typically used for short and one-off tasks where brevity is more important than having a named function.
