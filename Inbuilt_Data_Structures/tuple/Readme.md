## What is tuple in python?

A tuple is a built-in ordered data structure in python and it is used to store a collection of items like integer, float, string, list, dictionary, set, etc in one variable.

**NOTE:** Once a tuple is created you can not update or modify it because the tuple is immutable.

## Why do we use tuple?

If we compare the list with tuple then yes list has much more flexibility **but tuple is much faster than the list and this is the primary reason to use a tuple.**

second reason sometimes we don’t need to update our data and that time tuple is the best choice to use instead of a list.

## Create tuple in python

To create a tuple in python write comma-separated values inside the parenthesis (small brackets).

**Example:**

```python
t1 = (1,3,5,7,'saurabh',5.3) # create a tuple
print(t1)
```

**Output:**

```markup
(1, 3, 5, 7, 'saurabh', 5.3)
```

## Access elements of tuple

You can access elements of a tuple by using indexing.

Indexing starts from **0** (ZERO) and ends at **len(tuple) – 1**.

**Example:**

```python
t1 = (1,3,5,7,'allinpython',5.3)

# access 1 ----> index value of 1 is 0

print(t1[0])

# access allinpython ---> index value of allinpython is 4

print(t1[4])

# access last elements of tuple
print(t1[-1])
```

**Output:**

```markup
1
allinpython
5.3
```

| t1 (values) | positive index values | negative index values |
| --- | --- | --- |
| 1 | 0 | -6 |
| 3 | 1 | -5 |
| 5 | 2 | -4 |
| 7 | 3 | -3 |
| allinpython | 4 | -2 |
| 5.3 | 5 | -1 |

## Loop in tuple

### Iterate in a tuple using while-loop

**Example:**

```python
t2 = (45,45.6,23,67,12.1)

i = 0
while i< len(t2):
    print(t2[i])
    i+=1
```

**Output:**

```markup
45
45.6
23
67
12.1
```

### Iterate in a tuple using for-loop

```python
t2 = ('harsh',201,21,'football')
for i in t2:
    print(i)
```

**Output:**

```markup
harsh
201
21
football
```

## Tuple with one element



To create a tuple with a single element put a comma after your value otherwise it is not considered a tuple element.

**Example:**

```python
t3 = (2)
print(t3)
print(type(t3)) #---> return int not tuple

t3 = (2,)
print(t3)
print(type(t3)) #---> return tuple
```

**Output:**

```markup
2
<class 'int'>
(2,)
<class 'tuple'>
```

## Tuple without parenthesis

To create a tuple without using parenthesis write a comma-separated value after assigning your variable.

**Example:**

```python
guitars = 'yamaha','bataon rouge','taylor'
print(guitars)
print(type(guitars))
```

**Output:**

```markup
('yamaha', 'bataon rouge', 'taylor')
<class 'tuple'>
```

## Tuple unpacking

Tuple unpacking means you can store every element of a tuple in different-different variables.

**Example:**

```python
# create a tuple
guitarists = ('moneti jamal', 'eddie van der meer','andrew foy')

# tuple unpacking

guitarists_1,guitarists_2, guitarists_3 = guitarists

print(guitarists_1)
print(guitarists_3)
```

**Output:**

```markup
moneti jamal
andrew foy
```

**NOTE:** If the number of variables is less or more than the value present inside a tuple then it will give an error.

## Methods of tuple

there are only two methods used in the tuple.

1. .count() method
2. .index() method

### .count()method

count() method counts the number of times a specified value presents in the tuple.

**Example:**

```python
t2 = (45,45.6,23,67,12.1,23,45.6,23)

count1 = t2.count(23)
print(count1)

count2 = t2.count(45.6)
print(count2)
```

**Output:**

```markup
3
2
```

### .index() method

index() method returns index value of specified element.

**Example:**

```python
guitars = ('yamaha','bataon rouge','taylor')

index_1 = guitars.index('bataon rouge')
print(index_1)
```

**Output:**

```markup
1
```

## List inside a tuple

list present inside a tuple is act like a normal list which means you can update or delete elements of the list (you can use every methods of the list like .pop(), .append(), etc.,).

**Example:**

```python
t4 = (4,7,3,['rocky','yashin','malik'])

print(t4)

# access list present inside tuple
print(t4[3])

# delete last eleemnt of list
t4[3].pop()
print(t4)

# add in list
t4[3].append('roja')

print(t4)

# clear list
t4[3].clear()

print(t4)
```

**Output:**

```markup
(4, 7, 3, ['rocky', 'yashin', 'malik'])
['rocky', 'yashin', 'malik']
(4, 7, 3, ['rocky', 'yashin'])
(4, 7, 3, ['rocky', 'yashin', 'roja'])
(4, 7, 3, [])
```

## Function returns two values in the form of a tuple

**Example:**

```python
def func(a,b):
    add1 = a+b
    mul1 = a*b
    return add1,mul1

print(func(3,5))

add1, mul1 = func(2,7)  #tuple unpacking

print(add1)
print(mul1)
```

**Output:**

```markup
(8, 15)
9
14
```

## Create a tuple with range function

**Example:**

```python
nums = tuple(range(1,11))
print(nums)
```

**Output:**

```markup
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
```

### WAP to count no of students with grade "A" in the following tuple

```python
tup=('C','D','A','A','B','B','A')
print(tup.count('A'))
```
