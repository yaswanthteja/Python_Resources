| Category | Operator | Description | Example |
| --- | --- | --- | --- |
| Arithmetic | + | Addition | 5 + 3 |
|  | - | Subtraction | 10 - 4 |
|  | * | Multiplication | 3 * 4 |
|  | / | Division | 15 / 3 |
|  | // | Floor Division | 15 // 2 |
|  | % | Modulus | 15 % 2 |
|  | ** | Exponentiation | 2 ** 3 |
| Comparison | == | Equal to | 5 == 5 |
|  | != | Not equal to | 5 != 3 |
|  | > | Greater than | 8 > 6 |
|  | < | Less than | 4 < 7 |
|  | >= | Greater than or equal to | 5 >= 5 |
|  | <= | Less than or equal to | 3 <= 5 |
| Logical | and | Logical AND | True and False |
|  | or | Logical OR | True or False |
|  | not | Logical NOT | not True |
| Assignment | = | Assignment | x = 10 |
|  | += | Addition Assignment | x += 5 |
|  | -= | Subtraction Assignment | x -= 3 |
|  | *= | Multiplication Assignment | x *= 2 |
|  | /= | Division Assignment | x /= 4 |
| Identity | is | Identity | x is y |
|  | is not | Not Identity | x is not y |
| Membership | in | Membership | 5 in [1, 2, 3, 4, 5] |
|  | not in | Not Membership | 8 not in [1, 2, 3, 4, 5] |

Example:

```python
# Arithmetic Operators
num1 = 10
num2 = 3
addition_result = num1 + num2
subtraction_result = num1 - num2
multiplication_result = num1 * num2
division_result = num1 / num2
floor_division_result = num1 // num2
modulus_result = num1 % num2
exponentiation_result = num1 ** num2

# Comparison Operators
equal_check = num1 == num2
not_equal_check = num1 != num2
greater_than_check = num1 > num2
less_than_check = num1 < num2
greater_than_equal_check = num1 >= num2
less_than_equal_check = num1 <= num2

# Logical Operators
logical_and_result = (num1 > 5) and (num2 < 8)
logical_or_result = (num1 > 5) or (num2 < 2)
logical_not_result = not (num1 == 10)

# Assignment Operators
assignment_variable = 5
assignment_variable += 3
assignment_variable -= 2
assignment_variable *= 4
assignment_variable /= 2

# Identity Operators
identity_check = (num1 is num2)
not_identity_check = (num1 is not num2)

# Membership Operators
membership_check = (num1 in [1, 2, 3, 4, 5])
not_membership_check = (num2 not in [1, 2, 3, 4, 5])

# Displaying Results
print("Arithmetic Results:")
print("Addition:", addition_result)
print("Subtraction:", subtraction_result)
print("Multiplication:", multiplication_result)
print("Division:", division_result)
print("Floor Division:", floor_division_result)
print("Modulus:", modulus_result)
print("Exponentiation:", exponentiation_result)

print("\nComparison Results:")
print("Equal Check:", equal_check)
print("Not Equal Check:", not_equal_check)
print("Greater Than Check:", greater_than_check)
print("Less Than Check:", less_than_check)
print("Greater Than Equal Check:", greater_than_equal_check)
print("Less Than Equal Check:", less_than_equal_check)

print("\nLogical Results:")
print("Logical AND:", logical_and_result)
print("Logical OR:", logical_or_result)
print("Logical NOT:", logical_not_result)

print("\nAssignment Results:")
print("Assignment Variable:", assignment_variable)

print("\nIdentity Results:")
print("Identity Check:", identity_check)
print("Not Identity Check:", not_identity_check)

print("\nMembership Results:")
print("Membership Check:", membership_check)
print("Not Membership Check:", not_membership_check)
```

```python
Arithmetic Results:
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Floor Division: 3
Modulus: 1
Exponentiation: 1000

Comparison Results:
Equal Check: False
Not Equal Check: True
Greater Than Check: True
Less Than Check: False
Greater Than Equal Check: True
Less Than Equal Check: False

Logical Results:
Logical AND: True
Logical OR: True
Logical NOT: False

Assignment Results:
Assignment Variable: 12.0

Identity Results:
Identity Check: False
Not Identity Check: True

Membership Results:
Membership Check: False
Not Membership Check: False
```
