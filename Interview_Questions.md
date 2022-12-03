
# 1.Write a code to reverse a number
```
num = int(input("Enter the Number:"))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print("The Given number is {} and Reverse is {}".format(temp, reverse))
```
# 2 Write code Check if the given string is Palindrome or not
```
#take user input
String1 = input('Enter the String :')
#initialize string and save reverse of 1st string
String2 = String1[::-1]
#check if both matches
if String1 == String2:
    print('String is palindromic')
else:
    print('Strings is not palindromic')
```

# 3.Write code to check a String is palindrome or not?
```
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
  
```
