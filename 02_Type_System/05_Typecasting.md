# Type casting

We can convert one type value to another type. This conversion is called Typecasting or 
Type coersion.
The following are various inbuilt functions for type casting.
1. int()
2. float()
3. complex()
4. bool()
5. str()

# 1.int():
We can use this function to convert values from other types to int
Eg:
```
 >>> int(123.987) 
 123 
 >>> int(10+5j) 
 TypeError: can't convert complex to int 
 >>> int(True) 
 1 
 >>> int(False) 
 0 
 >>> int("10") 
 10 
 >>> int("10.5") 
 ValueError: invalid literal for int() with base 10: '10.5' 
 >>> int("ten") 
 ValueError: invalid literal for int() with base 10: 'ten' 
 >>> int("0B1111") 
 ValueError: invalid literal for int() with base 10: '0B1111' 
```
Note:
1. We can convert from any type to int except complex type.
2. If we want to convert str type to int type, compulsary str should contain only integral 
value and should be specified in base-10


# 2. float():
We can use float() function to convert other type values to float type.
```
 >>> float(10) 
 10.0 
 >>> float(10+5j) 
 TypeError: can't convert complex to float 
 >>> float(True) 
 1.0 
 >>> float(False) 
 0.0 
 >>> float("10") 
 10.0 
 >>> float("10.5") 
 10.5 
 >>> float("ten") 
 ValueError: could not convert string to float: 'ten' 
 >>> float("0B1111") 
 ValueError: could not convert string to float: '0B1111' 
```
Note:
1. We can convert any type value to float type except complex type.
2. Whenever we are trying to convert str type to float type compulsary str should be either integral or floating point literal and should be specified only in base-10.

# 3. complex():
We can use complex() function to convert other types to complex type.

## Form-1: complex(x)
We can use this function to convert x into complex number with real part x and imaginary 
part 0.

Eg: 

```
 complex(10)==>10+0j 
 complex(10.5)===>10.5+0j 
 complex(True)==>1+0j 
 complex(False)==>0j 
 complex("10")==>10+0j 
 complex("10.5")==>10.5+0j 
 complex("ten") 
 ValueError: complex() arg is a malformed string 
```
## Form-2: complex(x,y)
We can use this method to convert x and y into complex number such that x will be real 
part and y will be imaginary part.

Eg: 

```
complex(10,-2)==>10-2j
complex(True,False)==>1+0j
```
# 4. bool():
We can use this function to convert other type values to bool type.

Eg: 

```
 bool(0)==>False 
 bool(1)==>True 
 bool(10)===>True 
 bool(10.5)===>True 
 bool(0.178)==>True 
 bool(0.0)==>False 
 bool(10-2j)==>True 
 bool(0+1.5j)==>True 
 bool(0+0j)==>False 
 bool("True")==>True 
 bool("False")==>True 
 bool("")==>False
```

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/1ad03a89-675c-4726-932e-03b2007dc8bd)

 
 # 5. str():
We can use this method to convert other type values to str type

Eg:
```
 >>> str(10) 
 '10' 
 >>> str(10.5) 
 '10.5' 
 >>> str(10+5j) 
 '(10+5j)' 
 >>> str(True) 
 'True'
``` 
