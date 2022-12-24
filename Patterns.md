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



