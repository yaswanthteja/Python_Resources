## Full Pyramid

```
for i in range(5):
  for s in range(-6,-i):
    print("", end =" ")
  for j in range(i+1):
    print("*",end =" ")
  print()
  
  
  
  
#output

        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
```

## Inverted Full Pyramid


```
for i in range(5):
  for s in range(i):
    print(" ",end="")  #end with no space 
  for j in range (i,5):
    print("*",end=" ")
  print()

#output 


* * * * * 
 * * * * 
  * * * 
   * * 
    * 




```





## Half Pyramid

```

for i in range(5):
  for j in range(i+1):
    print("*",end="")
  print()
  
  

#output
*
**
***
****
*****
```

## Inverted half Pyramid

```
for i in range(5):
  for j in range(i,5):
    print("*",end="")
  print()


#output


*****
****
***
**
*


```

## Number Patterns

```
num=1
for i in range(5):
  for j in range(i+1):
    print(num ,end=" ")
    num = num+1
  print()


#Output
1 
2 3
4 5 6 
7 8 9 10 
11 12 13 14 15 


------ ----- 2 ------ -- ---


num=1
for i in range(5):
  for j in range(i+1):
    print(num,end=" ")
    num= num+1
  num=1
  print()


#Output

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

--------  3  ---------


for i in range(5):
  num=1
  for j in range (5,i,-1):
    print(num,end=" ")
    num=num+1
  print()


#Output
1 2 3 4 5 
1 2 3 4
1 2 3
1 2 
1 

```


