
# Tuple Data Structure

1. Tuple is exactly same as List except that it is immutable. i.e once we creates Tuple 
object,we cannot perform any changes in that object.
Hence Tuple is Read Only version of List.
2. If our data is fixed and never changes then we should go for Tuple.
3. Insertion Order is preserved
4. Duplicates are allowed
5. Heterogeneous objects are allowed.
6. We can preserve insertion order and we can differentiate duplicate objects by using 
index. Hence index will play very important role in Tuple also.
Tuple support both +ve and -ve index. +ve index means forward direction(from left to 
right) and -ve index means backward direction(from right to left)
7. We can represent Tuple elements within Parenthesis and with comma seperator.
 Parenethesis are optional but recommended to use.

Example:

 ```
t=10,20,30,40 
print(t) 
print(type(t)) 

Output
(10, 20, 30, 40) 
<class 'tuple'> 

t=() 
print(type(t)) # tuple 
 ```

Note: We have to take special care about single valued tuple.compulsary the value 
should ends with comma,otherwise it is not treated as tuple.

Eg:

```

t=(10) 
print(t) 
print(type(t)) 

Output 
10 
<class 'int'> 
```
```
# Q. Which of the following are valid tuples?
 t=()
 t=10,20,30,40
 t=10
 t=10,
 t=(10)
 t=(10,)
 t=(10,20,30,40)
```
## Tuple creation:

###  1. t=()
 creation of empty tuple
### 2. t=(10,)
 t=10,
 creation of single valued tuple ,parenthesis are optional,should ends with comma
### 3. t=10,20,30
 t=(10,20,30)
 creation of multi values tuples & parenthesis are optional
### 4. By using tuple() function:

```
list=[10,20,30] 
t=tuple(list) 
print(t) 

t=tuple(range(10,20,2)) 
print(t) 

```

## Accessing elements of tuple:

We can access either by index or by slice operator

```
1. By using index:

t=(10,20,30,40,50,60) 
print(t[0]) #10 
print(t[-1]) #60 
print(t[100]) IndexError: tuple index out of range 

2.By using slice operator:

t=(10,20,30,40,50,60) 
print(t[2:5]) 
print(t[2:100]) 
print(t[::2]) 

Output
(30, 40, 50) 
(30, 40, 50, 60) 
(10, 30, 50) 
```
## Tuple vs immutability:
Once we creates tuple,we cannot change its content.
Hence tuple objects are immutable.
 
Eg:
```
t=(10,20,30,40)
t[1]=70 TypeError: 'tuple' object does not support item assignment
```

## Important functions of Tuple:
## 1. len()
 To return number of elements present in the tuple
 Eg:
 ```
 t=(10,20,30,40)
 print(len(t)) #4
```
## 2. count()
 To return number of occurrences of given element in the tuple
 Eg:
 ```
 t=(10,20,10,10,20)
 print(t.count(10)) #3
 ```
## 3. index()
 returns index of first occurrence of the given element.
 If the specified element is not available then we will get ValueError.
 Eg:
 ```
 t=(10,20,10,10,20)
 print(t.index(10)) #0
 print(t.index(30)) ValueError: tuple.index(x): x not in tuple
 ```
## 4. sorted()
 To sort elements based on default natural sorting order
 ```
t=(40,10,30,20) 
t1=sorted(t) 
print(t1) 
print(t) 

Output
[10, 20, 30, 40] 
(40, 10, 30, 20) 
```
We can sort according to reverse of default natural sorting order as follows
```
t1=sorted(t,reverse=True)
print(t1) [40, 30, 20, 10]
```

## 5. min() and max() functions:
These functions return min and max values according to default natural sorting order.
Eg:

```
1. t=(40,10,30,20) 
2. print(min(t)) #10 
3. print(max(t)) #40 
6. cmp():
```
- It compares the elements of both tuples.
- If both tuples are equal then returns 0
- If the first tuple is less than second tuple then it returns -1
- If the first tuple is greater than second tuple then it returns +1
 Eg:
```
t1=(10,20,30) 
t2=(40,50,60) 
t3=(10,20,30) 
print(cmp(t1,t2)) # -1 
print(cmp(t1,t3)) # 0 
print(cmp(t2,t3)) # +1 
```
Note: cmp() function is available only in Python2 but not in Python 3



## Tuple Packing and Unpacking:
We can create a tuple by packing a group of variables.

Eg:
```
a=10
b=20
c=30
d=40
t=a,b,c,d
print(t) #(10, 20, 30, 40)
```

Here a,b,c,d are packed into a tuple t. This is nothing but tuple packing.

- Tuple unpacking is the reverse process of tuple packing
We can unpack a tuple and assign its values to different variables
Eg:

```
t=(10,20,30,40) 
a,b,c,d=t 
print("a=",a,"b=",b,"c=",c,"d=",d) 

Output
a= 10 b= 20 c= 30 d= 40 
```
- `Note`: 

At the time of tuple unpacking the number of variables and number of values 
should be same. ,otherwise we will get ValueError.
Eg:
```
t=(10,20,30,40)
a,b,c=t #ValueError: too many values to unpack (expected 3)
```


