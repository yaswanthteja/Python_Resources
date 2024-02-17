
# 1. Write a code to reverse a number

```python
# Write a code to reverse a number

# Taking input from the user
num = int(input("Enter the Number:"))

# Storing the original number in a temporary variable
temp = num

# Initializing a variable to store the reversed number
reverse = 0

# Reversing the number using a loop
while num > 0:
    # Finding the remainder when the number is divided by 10
    remainder = num % 10
    
    # Adding the remainder to the reversed number after shifting it one place to the left
    reverse = (reverse * 10) + remainder
    
    # Removing the last digit from the original number
    num = num // 10
# Printing the original and reversed numbers
print("The Given number is {} and Reverse is {}".format(temp, reverse))

```

```python
Enter the Number: 1023
The Given number is 1023 and Reverse is 3201
```

Explanation of the code:

The program starts by taking an integer input from the user using the input() function and converting it to an integer using int().

The original input number is stored in the variable temp for later reference.

The variable reverse is initialized to store the reversed number. It starts with a value of 0.

The program uses a while loop to reverse the number:

Inside the loop, the remainder of the number when divided by 10 is calculated using the modulus operator %. This remainder is the last digit of the number.
The reverse number is updated by shifting it one place to the left (multiplying by 10) and adding the current remainder.
The last digit is removed from the original number using integer division num // 10.
The loop continues until the original number becomes 0, meaning all its digits have been reversed.

Finally, the program prints out the original number (temp) and the reversed number (reverse) using the format() method to insert the values into the output string.

When you run the program, it will take a number as input, reverse it, and display both the original and reversed numbers.

# 2. Write the code to find the Fibonacci series upto the nth term.

```python
# fibanoci Series

n=int(input("Enter your number:"))
first=0
second=1
for i in range(n):
	print(first)
	temp=first
	first=second
	second=temp+second

Output:
Enter your number:10
0
1
1
2
3
5
8
13
21
34
```

# 3. Fibanocci Series using recursion

```python

def fibanocci(n):
	  assert n>=0 and int(n)==n,'The fibanocci number must be positive' 
    if n in [0,1]:
        return n
    else:
        return fibanocci(n-1)+fibanocci(n-2)

print(fibanocci(8))

Output
21
```

# 4. Write code Check if the given string is Palindrome or not

```python
# Write code Check if the given string is Palindrome or not

#take user input
String1 = input('Enter the String :')
#initialize string and save reverse of 1st string
String2 = String1[::-1]
#check if both matches
if String1 == String2:
    print('String is palindromic')
else:
    print('Strings is not palindromic')

output:

Enter your String:malayalam
It is palindrome
```

```python
# Write code to check a String is palindrome or not?

# function which return reverse of a string

def isPalindrome(s): 
  return s == s[::-1]

# Driver code 
s = "malayalam"
ans = isPalindrome(s)

if ans: 
  print("Yes") 
else: 
  print("No")

Output:
Yes
```

```python
def palindrome(s):
	return s==s[::-1]
s=input("Enter a string: ")
r=palindrome(s)
if r:
	print("It is palindrome")
else:
	print("It is Not Palindrome")
```

# 5. Factorial (3 ways)

### Using Recursion function

### n!  =n*(n-1)

5! =5*4*3*2*1=120

```python
def factorial(n):
    # Check if n is a non-negative integer using an assertion
    assert n >= 0 and int(n) == n, "The Number must be positive"

    # Base case: If n is 0 or 1, return 1
    if n in [0, 1]:
        return 1
    else:
        # Recursive case: Calculate factorial by multiplying n with factorial of (n-1)
        return n * factorial(n - 1)

# Example usage: Calculate the factorial of 5
print(factorial(8))
```

```python
40320
```

Explanation:

1. The **`factorial`** function takes a single argument, **`n`**, which represents the integer for which we want to calculate the factorial.
2. There's an assertion at the beginning of the function to check whether **`n`** is a non-negative integer. The assertion ensures that the function is called with a valid input, and it raises an error with the specified message if **`n`** doesn't meet the criteria.
3. The base case of the recursion is when **`n`** is 0 or 1. In these cases, the function returns 1, as the factorial of 0 and 1 is defined as 1.
4. For values of **`n`** greater than 1, the function uses recursion to calculate the factorial. It multiplies **`n`** with the factorial of **`(n-1)`**.
5. The recursion continues until **`n`** reaches either 0 or 1, at which point it starts returning values, ultimately leading to the calculation of the factorial of the original input.
6. The example usage at the end demonstrates how to call the **`factorial`** function with an input of 5 and print the result, which should be 120 (5!).

When you run this code with **`factorial(5)`**, it will calculate and print the factorial of 5, which is 120.

## Using Inbuilt Function

### math.factorial()

```python
import math
n=int(input("Enter a number: "))
result=math.factorial(n)
print(f"The factorial of {n} is {result} ")
```

```python
Enter a number: 5
The factorial of 5 is 120
```

## Using for  loop

```python
# Taking input from the user
n = int(input("Enter a number:"))

# Initializing a variable to store the factorial result
result = 1

# Loop to calculate the factorial
for i in range(n, 0, -1):
    result = result * i

# Printing the result
print(f" The given number is {n} and the result is {result}")
```

```python
Enter a number:5
 The given number is 5 and the result is 120
```

Here's an explanation of each part:

1. The user is prompted to enter a number, which is read as an integer using **`int(input())`** and stored in the variable **`n`**.
2. The variable **`result`** is initialized to 1. This variable will be used to accumulate the factorial value.
3. The **`for`** loop is used to calculate the factorial. It starts from **`n`** and goes down to 1 (inclusive) with a step of -1. In other words, it iterates through the numbers from **`n`** down to 1.
4. Inside the loop, **`result`** is updated by multiplying it with the current value of **`i`**. This effectively calculates the factorial as it iterates through the numbers.
5. After the loop completes, the program prints the original input number (**`n`**) and the calculated factorial result.

When you run this program, it will ask you to input a number, and then it will calculate and display the factorial of that number.

## 6. Prime numbers

What is a prime number in math?

A prime number is **a number that can only be divided by itself and 1 without remainders**.

 What are the prime numbers from 1 to 100? 

The prime numbers from 1 to 100 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.


```python
# Taking input for the lower and upper interval
lower = int(input("Enter a lower interval number: "))
upper = int(input("Enter an upper interval number: "))

# Loop through numbers in the given interval
for num in range(lower, upper + 1):
    if num > 1:  # Prime numbers are greater than 1
        for i in range(2, num):
            if (num % i) == 0:
                break  # If num is divisible by any number in this range, it's not prime
        else:
            print(num)
```

Explanation of the code:

1.  enter two numbers: the lower and upper bounds of the interval.
2. A **`for`** loop iterates through each number in the specified interval, from **`lower`** to **`upper`** (inclusive).
3. Inside the loop, there's a check to ensure that **`num`** is greater than 1 because prime numbers are defined as greater than 1.
4. Then, there's another nested **`for`** loop that iterates from 2 to **`num - 1`**. This inner loop is used to check if **`num`** is divisible by any number in that range.
5. If **`num`** is divisible by any number in the inner loop (i.e., if **`num % i == 0`** for any **`i`**), it means **`num`** is not a prime number. In this case, the loop is terminated using **`break`**.
6. If the inner loop completes without finding any divisors for **`num`**, it means **`num`** is not divisible by any number other than 1 and itself, making it a prime number. In this case, it is printed.

So, when you run this program, it will ask you to enter a lower and upper interval, and then it will print all the prime numbers within that interval.

What is a prime number in math?

A prime number is **a number that can only be divided by itself and 1 without remainders**.

 What are the prime numbers from 1 to 100? 

The prime numbers from 1 to 100 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.

```python
num = int(input("Enter any positive number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
```

Here's how the code works:

1.   input a positive number, which is stored in the variable **`num`**.
2. The code checks if **`num`** is greater than 1. Prime numbers are defined as greater than 1, so this check is necessary.
3. If **`num`** is greater than 1, a **`for`** loop is used to iterate through numbers from 2 to **`num - 1`**.
4. Inside the loop, it checks if **`num`** is divisible by any of these numbers (**`(num % i) == 0`**). If it is, it means that **`num`** is not a prime number, and it prints a message stating that it's not prime. Then, it breaks out of the loop.
5. If the loop completes without finding any divisors for **`num`**, it means **`num`** is not divisible by any number other than 1 and itself, making it a prime number. In this case, it prints a message stating that it's a prime number.
6. If **`num`** is less than or equal to 1, it prints a message stating that it's not a prime number.

This corrected code will correctly determine whether the input number is prime or not and print the appropriate message.

## 7. Leap Year

```python
def check_leap(year):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

year = int(input("Enter your year: "))
check_leap(year)
```

```python
Enter your year: 2000
2000 is a leap year
```

Explanation of the code:

1. The **`check_leap`** function takes a **`year`** as input and checks if it's a leap year.
2. It uses a condition to determine leap years:
    - A year is a leap year if it's divisible by 400, OR
    - A year is a leap year if it's not divisible by 100 and is divisible by 4.
3. Depending on the result of the condition, it prints whether the given year is a leap year or not.
4. In the main program, the user is prompted to input a year.
5. The **`check_leap`** function is called with the user's input year, and it prints the result directly.

## 8. Separate the characters from given string

```python
def separate_char(input_string):
    characters = list(input_string)
    return characters

input_string = input("Enter a string: ")
result = separate_char(input_string)

print("The separate characters are:")
for char in result:
    print(char)
```

```python
Enter a string: Python
The separate characters are:
P
y
t
h
o
n
```

1. The **`separate_char`** function takes an **`input_string`** as input and converts it into a list of characters using the **`list()`** function. It then returns this list.
2. The user is prompted to enter a string, which is stored in the **`input_string`** variable.
3. The **`separate_char`** function is called with the **`input_string`**, and the result (a list of characters) is stored in the **`result`** variable.
4. The code then prints "The separate characters are:" to indicate the start of the character list.
5. Using a **`for`** loop, it iterates through each character in the **`result`** list and prints each character individually.

## 9. Write a program to convert temperature from Celsius to Fahrenheit. (Type casting)

```python
# Input temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit using the conversion formula
fahrenheit = (celsius * 9/5) + 32

# Print the result
print("Temperature in Fahrenheit:", fahrenheit)
```

1. The input is read as a floating-point number and stored in the variable **`celsius`**.
2. The code then uses the formula **`(celsius * 9/5) + 32`** to convert the temperature from Celsius to Fahrenheit. In this formula, you multiply the Celsius temperature by 9/5 (or 1.8) and then add 32.
3. The converted temperature in Fahrenheit is stored in the variable **`fahrenheit`**.
4. Finally, the program prints the result, displaying the temperature in Fahrenheit.

When you run this program, it will ask you to input a temperature in degrees Celsius, and it will then calculate and display the equivalent temperature in degrees Fahrenheit.

## 10.  Convert Fahrenheit to Celsius

```python
# Input temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius using the conversion formula
celsius = (fahrenheit - 32) * 5/9

# Print the result
print("Temperature in Celsius:", celsius)
```

1. The input is read as a floating-point number and stored in the variable **`fahrenheit`**.
2. The code then uses the formula **`(fahrenheit - 32) * 5/9`** to convert the temperature from Fahrenheit to Celsius. In this formula, you subtract 32 from the Fahrenheit temperature and then multiply the result by 5/9.
3. The converted temperature in Celsius is stored in the variable **`celsius`**.
4. Finally, the program prints the result, displaying the temperature in Celsius.

When you run this program, it will ask you to input a temperature in degrees Fahrenheit, and it will then calculate and display the equivalent temperature in degrees Celsius.

### 11. : Take a positive integer input and tell if it is even or odd

```python
# Taking positive integer input from the user
number = int(input("Enter a positive integer: "))
 
# Checking if the number is even or odd
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```

By using ternary operator

```python
# Taking input number from the user
number = int(input("Enter a number: "))
 
# Checking if the number is odd or even using a ternary operator
result = "Odd" if number % 2 != 0 else "Even"
 
# Printing the result
print("The number is", result)
```

```python
Enter a number: 2
The number is Even
```

### 12 .  If cost price and selling price of an item is input through the keyboard, write a program to determine whether the seller has made profit or incurred loss or no profit no loss. Also determine how much profit he
made or loss he incurred

```python
# Taking cost price and selling price input from the user
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))
 
# Calculating profit/loss
profit = selling_price - cost_price
profit_percentage = (profit / cost_price) * 100
 
# Checking profit/loss and providing output
if profit > 0:
    print("\nThe seller has made a profit of", profit, "units.")
    print("Profit percentage:", profit_percentage, "%")
elif profit < 0: 
    print("\nThe seller has incurred a loss of", abs(profit), "units.")
    print("Loss percentage:", abs(profit_percentage), "%")
else:
    print("\nIt's neither loss nor profit")
```

### 13. whether a given number is a perfect number or not.

```python
# Perfect

num=int(input('Enter a number: '))
result=0
for i in range(1,num):
	if num%i==0:
		result=result+i
if result==num:
	print('It is a perfect number: ')
else:
	print('It is not a perfect number:')
```

A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).

Here's a breakdown of your code:

1. You take user input to get an integer number **`num`**.
2. You initialize a variable **`result`** to 0. This variable will be used to store the sum of the proper divisors.
3. You iterate through a range of numbers from 1 to **`num - 1`** (excluding **`num`** itself).
4. Inside the loop, you check if **`num`** is divisible by the current number **`i`**. If it is, you add **`i`** to the **`result`**. This calculates the sum of the proper divisors of **`num`**.
5. After the loop, you check if **`result`** is equal to **`num`**. If they are equal, you print that it's a perfect number; otherwise, you print that it's not a perfect number.

Your code correctly identifies whether the input number is a perfect number or not. Perfect numbers include examples like 6 (1 + 2 + 3 = 6) and 28 (1 + 2 + 4 + 7 + 14 = 28). If the sum of the divisors equals the number itself, it's considered perfect.

## 14. Star programs

```python
for i in range(5):
	print((i+1)*'*')
```

```python
*
**
***
****
*****
```

## 15. Armstrong number upto n

```python
for num in range(1001):
    i = num
    result = 0
    n = len(str(num))

    while i != 0:
        digit = i % 10
        result = result + digit ** n
        i = i // 10

    if num == result:
        print(num)
```

```python
0
1
2
3
4
5
6
7
8
9
153
370
371
407
```

Here's a step-by-step explanation of the code:

1. **`for num in range(1001):`**: This is a loop that iterates through numbers from 0 to 1000. It assigns each number to the variable **`num`** for further processing.
2. **`num = i`**: The current number being checked is stored in the variable **`num`**. The variable **`i`** is the loop variable, which iterates through the numbers in the range.
3. **`result = 0`**: This variable is used to calculate the sum of the digits raised to the power of **`n`**, where **`n`** is the number of digits in the current number **`num`**.
4. **`n = len(str(i))`**: This line calculates the number of digits in the current number **`num`** by converting it to a string, and then measuring the length of that string. This value is stored in the variable **`n`**.
5. **`while i != 0:`**: This is a while loop that continues until the current number **`i`** becomes 0. It processes each digit in the number from right to left.
6. **`digit = i % 10`**: This line extracts the last digit of the number **`i`** by taking the remainder when dividing by 10.
7. **`result = result + digit ** n`**: The code raises the extracted **`digit`** to the power of **`n`** and adds it to the **`result`**. This is accumulating the sum of the digits raised to the power of the number of digits.
8. **`i = i // 10`**: This line removes the last digit from the number **`i`** by integer division (//) by 10. This effectively moves to the next digit to the left in the number.
9. **`if num == result:`**: After processing all the digits of the number, the code checks if **`num`** (the original number) is equal to **`result`** (the calculated sum of digits raised to the power of **`n`**). If they are equal, it means the number is an Armstrong number.
10. **`print(num)`**: If the number is an Armstrong number, it is printed to the console

```python
def is_armstrong_number(number):
    # Convert the number to a string to find the number of digits
    num_str = str(number)
    
    # Find the number of digits
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return armstrong_sum == number

# Example usage:
user_input = int(input("Enter a number: "))
if is_armstrong_number(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")
```

```python
Enter a number: 153
153 is an Armstrong number.
```

## 16. Reverse a list using Two pointer approach

```python
# Two  pointer approach 
# time complexity: O(n)
# space Complexity: O(1)

# Two Pointer approach to reverse a list
def reverse_list(list1):
    # Initialize two pointers: low and high
    low, high = 0, len(list1) - 1

    # Loop until the low pointer is less than the high pointer
    while low < high:
        # Swap the elements at the low and high positions
        list1[low], list1[high] = list1[high], list1[low]

        # Increment the low pointer by 1
        low += 1

        # Decrement the high pointer by 1
        high -= 1

    # Return the reversed list
    return list1

# Driver code
list1 = [2, 5, 7, 11, 10]
list2 = [3, 5, 9, 8, 10]

# Call the reverse_list function for both lists
reversed_list1 = reverse_list(list1)
reversed_list2 = reverse_list(list2)

# Print the reversed lists
print(reversed_list1)  # Output: [10, 11, 7, 5, 2]
print(reversed_list2)  # Output: [10, 8, 9, 5, 3]
```

```python
[10, 11, 7, 5, 2]
[10, 8, 9, 5, 3]
```

- **`low`** and **`high`** are two pointers that are initially set to the beginning and end of the list, respectively.
- The **`while`** loop continues until **`low`** is less than **`high`**.
- Inside the loop, the elements at positions **`low`** and **`high`** are swapped using tuple packing and unpacking.
- The **`low`** pointer is incremented by 1, and the **`high`** pointer is decremented by 1 in each iteration.
- The loop continues until **`low`** becomes greater than or equal to **`high`**, ensuring that the list is fully reversed.
- The function returns the reversed list.

The Two-Pointer approach is an efficient way to reverse a list in-place and has a time complexity of O(n), where n is the number of elements in the list. It operates with a space complexity of O(1) since it doesn't use any additional memory.

## 17. Reverse a list by custom index using Two pointer approach

```python
#
def sort_list(list1,start,end):
	# check the indices
	if start<0 and end>=len(list1):
		return 'Invalid index'
	while start<end:
		#  # Swap the elements at the start and end positions
		list1[start],list1[end]=list1[end],list1[start]
		# Increment the start index
		start+=1
		# Decrement the end index
		end-=1
	return list1

# # Define a list
list1=[2,3,5,6,9,7]

# calling and printing the function with custom arguments
print(sort_list(list1,1,3))
```

```python
[2, 6, 5, 3, 9, 7]
```

## 18.  Create a function that accepts a list of numbers and returns the sum of all the even numbers in a list.

Example

list1 = [2, 5, 8, 91]

output = 2+8 = 10

```python
def sum_even_numbers(numbers):
    # Initialize a variable to store the sum
    even_sum = 0
    
    # Loop through the list of numbers
    for num in numbers:
        # Check if the number is even
        if num % 2 == 0:
            # Add the even number to the sum
            even_sum += num
    
    return even_sum

# Test the function with the given list
list1 = [2, 5, 8, 91]
result = sum_even_numbers(list1)
print("Sum of even numbers:", result)  # Output: Sum of even numbers: 10
```

## 19 .Two-Pointer approach to find a pair of elements in a sorted list that sums up to zero

```python
arr = [-9, -4, -1, 1, 4, 8, 11]
left = 0
right = len(arr) - 1

while left < right:
    # Calculate the sum of elements at the left and right pointers
    total = arr[left] + arr[right]

    if total == 0:
        # If the sum is zero, print the pair and break out of the loop
        print("Pair found:", arr[left], arr[right])
        break
    elif total < 0:
        # If the sum is negative, move the left pointer to the right
        left += 1
    else:
        # If the sum is positive, move the right pointer to the left
        right -= 1
```

- **`left`** and **`right`** are two pointers initially set to the beginning and end of the sorted list, respectively.
- The **`while`** loop continues until the **`left`** pointer is less than the **`right`** pointer, ensuring that all possible pairs are checked.
- In each iteration, the code calculates the sum of the elements at the **`left`** and **`right`** pointers.
- If the sum is zero, it means a pair of elements that sum up to zero has been found, and their values are printed.
- If the sum is negative, the **`left`** pointer is moved to the right to explore larger values.
- If the sum is positive, the **`right`** pointer is moved to the left to explore smaller values.
- The loop continues until a pair is found (sum is zero) or until the pointers meet or cross.

This Two-Pointer approach efficiently finds a pair of elements in the sorted list that adds up to zero with a time complexity of O(n), where n is the number of elements in the list, and it uses O(1) extra space. It's a common approach for solving problems like finding pairs with a specific sum in sorted arrays.

## 20 . Addition of two numbers with out + operator

```python
x=20
y=30
while y!=0:
    temp=x&y
    x=x^y
    y=temp<<1
print(x)
```

1. It initializes variables **`x`** and **`y`** with integer values.
2. It enters a **`while`** loop that continues until **`y`** becomes zero.
3. Inside the loop:
    - It calculates the bitwise AND of **`x`** and **`y`** and stores it in the variable **`temp`**.
    - It calculates the bitwise XOR of **`x`** and **`y`** and updates the value of **`x`**.
    - It calculates **`y`** shifted left by one position (**`temp << 1`**) and updates the value of **`y`**.
4. When **`y`** becomes zero, the loop exits, and it prints the value of **`x`**.

## 21 . Power the numbers with out power operator(**)

```python
def power(base,exponent):
    result=1
    while exponent>0:
        result*=base
        exponent-=1
    return result
print (power(2,3))
```

1. t defines a function named **`power`** that takes two parameters: **`base`** and **`exponent`**.
2. It initializes a variable **`result`** to 1. This variable will hold the result of the exponentiation operation.
3. It enters a **`while`** loop that continues as long as the **`exponent`** is greater than 0.
4. Inside the loop:
    - It multiplies the **`result`** by the **`base`** and updates the value of **`result`**.
    - It decrements the value of **`exponent`** by 1.
5. When the **`exponent`** becomes 0 or negative, the loop exits.
6. It returns the final value of **`result`**, which represents the result of **`base`** raised to the power of **`exponent`**.
7. It calls the **`power`** function with arguments **`2`** and **`3`**, printing the result.

The output of this code will be **`8`**, which is the result of **`2`** raised to the power of **`3`**.
