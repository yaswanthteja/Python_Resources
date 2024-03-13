NumPy

The NumPy library is the core library for scientific computing in Python. It provides a  high-performance multidimensional array object and tools for working with these arrays.  

Use the following import convention:  
```
 import numpy as np
```


### Creating Arrays 

```
 a = np.array([1,2,3])
 b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
 c = np.array([[(1.5,2,3), (4,5,6)],[(3,2,1), (4,5,6)]], dtype = float)
```

```
import numpy as np

# 1D array
arr1d = np.array([1, 2, 3, 4, 5])

# 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# Array filled with zeros
zeros_arr = np.zeros((2, 3))

# Array filled with ones
ones_arr = np.ones((3, 2))

# Array filled with a range of values
range_arr = np.arange(0, 10, 2)

# Random array
rand_arr = np.random.rand(2, 3)

```

### Array Operations:

```
# Element-wise arithmetic operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
add_arr = arr1 + arr2
sub_arr = arr1 - arr2
mul_arr = arr1 * arr2
div_arr = arr1 / arr2

# Matrix multiplication
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
mat_mul = np.dot(mat1, mat2)

# Broadcasting
arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10
broadcasted = arr + scalar


```

### Indexing and Slicing:

```
# Indexing
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])   # Accessing first element
print(arr[-1])  # Accessing last element

# Slicing
arr = np.array([1, 2, 3, 4, 5])
print(arr[1:4])  # Slicing from index 1 to 3 (exclusive)

```



### Random Number Generation:

```
# Generate random numbers
rand_int = np.random.randint(1, 10)        # Random integer between 1 and 10
rand_float = np.random.random()            # Random float between 0 and 1
rand_arr = np.random.randn(2, 3)           # Random array from standard normal distribution


```

### File I/O:

```
# Saving and loading arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
np.save('my_array.npy', arr)         # Save array to file
loaded_arr = np.load('my_array.npy')  # Load array from file

```


