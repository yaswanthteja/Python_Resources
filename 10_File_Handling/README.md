## Table of Contents

1. Overview
2. Opening and Closing Files
3. Understanding Text and Binary Files
4. Specifying the Character Encoding
5. Choosing the Line Ending
6. Exploring the Different File Modes
7. Reading and Writing Text Files in Python
8. Reading and Writing CSV Data
9. Summary



- Understand the difference between text  and binary files
- Learn about character encodings and line endings
- Work with file objects in Python
- Read and write character data in various file modes
- Use open() , Path. open() , and the with statement
- Take advantage of the csv module to manipulate CSV data




## What is File?

- files are named locations on disk to store information
- They are used to store data permanently.
- Data is stored in non-volatile memory.
- We can retrieve data whenever required.

## Types of files?

### Text files:-

Stores data in the form of characters. It is used to store data and strings.
  examples: txt, json

### Binary files:-

 Stores data in the form of bytes(group of 8 bits)

example : music, videos, pdf

## What is file handling?

File handling means:-

- Opening a file.
- Performing some operations on it.
- Closing a file

example

we need  to  store  the data inside a txt file given by the user as input:

```python
age=input('Enter your age:')
f=open("data.txt",'w') #location of the file
f.write(age)
f.close()
```

To read the above data  we use the below code

```python
f=open("data.txt",'r')
print(f.read())
f.close()
```

How to open the file??

Python provides an inbuilt function `open()`  to open a file.

`Syntax`

```python
f=open('filename with path',mode='r',buffering,encoding=None,
         errors=None,newline=None,closefd=True)
```

syntax

```python
f=open('filename',mode='r')
```

**`open()`** function in Python, which is used to open files in different modes. Below is an explanation of each parameter in the syntax:

- **`filename with path`**: This parameter specifies the name and location (path) of the file you want to open. It should be a string representing the file's path on the file system.

- **`mode`**: This parameter indicates the mode in which the file will be opened. It is an optional parameter, and if not provided, it defaults to read mode ('r'). The mode parameter can take the following values:

- **`'r'`**: **Read mode** (default). The file will be opened for reading.
- **`'w'`**: **Write mode.** The file will be opened for writing. If the file already exists, its contents will be truncated. If the file does not exist, a new file will be created.
- **`'a'`**: **Append mode**. The file will be opened for writing, but data will be appended to the end of the file instead of overwriting its contents. If the file does not exist, a new file will be created.
- **`'b'`**: **Binary mode.** This mode is used when working with binary files.
- **`'t'`**: **Text mode** (default). This mode is used when working with text files. Text mode handles encoding and decoding automatically.
- **`'x'`**: **Exclusive creation mode**. This mode is used to create a new file but raises an error if the file already exists.

- **`buffering`**: This parameter is an optional integer value that specifies the buffering policy. If not provided, it defaults to the system default buffering. A value of 0 means no buffering, 1 means line buffering, and any other positive value represents the buffer size in bytes.
- In main memory there is a buffer memory  which is temporary memory which divides data into n chunks for processing.
    - Positive Integer value used to set buffer size for file.
    • In text mode, buffer size should be 1 or more than 1.
    • In binary mode, buffer size can be 0.
    • Default size:- 4096 - 8192 bytes

- **`encoding`**: This parameter is an optional string that specifies the character encoding to be used when reading or writing a text file. If not provided, the system default encoding will be used.

- Encoding type used to decode and encode file.
• Should be used in text mode only.
• Default value depends on OS.
• For windows cp1252 or we can use utf-8

- **`errors`**: This parameter is an optional string that specifies how encoding and decoding errors should be handled when reading or writing a text file. If not provided, it defaults to 'strict', which raises an exception on error. Other possible values include 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace', and more.
    - Represents how encoding and decoding errors are to be
    handled.
    • Cannot be used in binary mode.
    • Some standard values are :- strict, ignore, replace etc.

- **`newline`**: This parameter is an optional string used to specify the line ending used when reading or writing text files. If not provided, the system default line ending will be used.
- it can be \n,\r,\r\n.

- **`closefd`**: This parameter is an optional boolean value that determines whether the file descriptor (fd) should be closed after the file is opened. If not provided, it defaults to True, meaning the file descriptor will be closed.

Example:

```python
# Opening a file in read mode with custom encoding and line ending
with open("example.txt", mode="r", encoding="utf-8", newline="\n") as file:
    content = file.read()
    print(content)
```

we open a file named "example.txt" in read mode with a specific encoding (UTF-8) and newline character (LF, **`\n`**). The **`with`** statement ensures that the file is automatically closed after reading its content.

# Closing a file

After  performing operations we have to close a file.

`close()` : function used to close s file.

syntax:

```python
file_handler.close()
```

### what happens when we close a file?

file object is deleted from memory and file id no more accessible unless we open it again.

### what happens when we do not  close a file?

After program execution, python garbage collector will destroy file object and closes file automatically.

note: Don’t rely on garbage collector

```python
# Accessing file object variables
f=open('hello.txt',mode='w',encoding='utf-8')
print("Encoding is ",f.encoding)
print("mode is ",f.mode)
print("name is ",f.name)
```

### file object methods:

1. readable()
2. writable()

### readable()

- This method is used to check whether file is readable or not.
True:- if file is readable.
False:- if file is not readable.

```python
f=open('hello.txt',mode='r',encoding='utf-8')
print(f.readable())
print(f.writable())
f.close()

output:
True
False
```

### writable()

- This method is used to check whether file is writable or not.
True:- if file is writable.
False:- if file is not writable.

```python
f=open('hello.txt',mode='w',encoding='utf-8')
print(f.readable())
print(f.writable())
f.close()

output:
False
True
```

if we want to read and write the file we use w+

```python
f=open('hello.txt',mode='w+',encoding='utf-8')
print(f.readable())
print(f.writable())
f.close()

output:

True
True
```

### How to check File a Exist or Not Exist in directory  using python .

```python
f=open("new.txt")

f.close()

output:
Traceback (most recent call last):
  File "f:\courses\Python\ModulesAndPackages\file.py", line 2, in <module>
    f=open("new.txt")
      ^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'new.txt'
```

### Check file exist or not?

`isfile()`:-

This method is used to check file exist or not.

This method belongs to path module which is sub-
module of os module.

Syntax:

```python
import os
os.path.isfile("filename")
```

here it returns boolean value

```python
import os
print(os.path.isfile("hello.txt"))

output:

true
```

```python
import os

if os.path.isfile("hell.txt"):
    f=open("hello.txt")
    # operations on that file
    f.close()
else:
     print("File not exist")
```

```python
import os

filename=input("Enter the file name: ")
if os.path.isfile(filename):
    f=open(filename)
    # operations on that file
    f.close()
else:
     print("File not exist")

```

# ways of closing files:

In python there is no gaurantee that the close() is going to close the file. so there are 3 ways we  can close the file.

- Normal way
- Using exception handling
- with statement

### Normal  way

```python
f=open("filename",mode="r")
# operations  
f.close()
```

if exceptions stop the flow of program  then the close()  will never executed and your file also not close.

### Using exception handling

```python
try:
    f=open("filename",mode="r")
    # operations
finally:
    f.close()
```

here finally block always executed  if exception occurs or not.

### with statement

with statement close the file 

syntax:

```python
with open("filename",mode="r") as f:
   # operations
```

example:

```python
with open("filename",mode="r") as f:
   # operations
   data=f.read()
   print(data)
```

# Modes of opening file:

when you open a file for operations, you have to specify mode. 

mode specifies the purpose of opening file. There are two types of modes:-

1. Text modes
2. Binary modes.

### Text mode:

- when you open a file in text modes, python treats it's content as "str" type.
- When you get data from a text mode file, python first decodes the raw bytes using either a platform dependent encoding or specified encoding.

Text mode is used when dealing with plain text files, such as .txt files, .csv files, etc., where the data is in human-readable form and encoded using a character encoding (e.g., UTF-8, ASCII).

To specify text mode, you can use the following modes when opening a file:

- **`'r'`**: Read mode (default).
- **`'w'`**: Write mode.
- **`'a'`**: Append mode.
- **`'x'`**: Exclusive creation mode.
- **`'r+'`**: Open for reading and then writing.
- **`'w+'`**: Open for  writing and then reading .
- **`'a+'`**: Open for appending and then writing.

Example of opening a file in text mode for reading:

```python
with open('example.txt', mode='r') as file:
    content = file.read()
    print(content)
```

### Binary mode

- When you open a file for binary mode, python uses the data without any encoding. Binary mode file reflects the raw data directly in the file.
- Python treats file contents as "bytes" type. These modes are used while dealing with non-text files like images, audios, videos etc.

Binary mode is used when working with files that contain non-textual data, such as images, audio files, video files, etc. These files are stored as a sequence of bytes, and reading or writing them requires binary mode.

To specify binary mode, you can use the following modes when opening a file:

- **`'rb'`**: Read mode in binary.
- **`'wb'`**: Write mode in binary.
- **`'ab'`**: Append mode in binary.
- **`'xb'`**: Exclusive creation mode in binary.
- **`'rb+'`**: Open for reading and then writing  in binary.
- **`'wb+'`**: Open for  writing and then reading  in binary .
- **`'ab+'`**: Open for appending and then writing in binary.

Example of opening a file in binary mode for reading:

```python
with open('example.bin', mode='rb') as file:
    data = file.read()
    print(data)
```

# Reading data from file:

To read content of file, we have following three methods:-

- read()
- readline()
- readlines()

**`read()`**: This method reads the entire content of the file and **returns it as a single string.**

Example:

```python
with open('example.txt', 'r') as file:
    content = file.read() # here you can specify size file.read(20)
    print(content)
```

**`readline()`**: This method reads a single line from the file and **returns it as a string**. It moves the file pointer to the beginning of the next line.

syntax:

```python
file_object.readline(size)
# size:- number of characters to read from line
```

Example:

```python
with open('example.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1)
    print(line2)
```

**`readlines()`**: This method reads all the lines from the file and **returns them as a list of strings**. Each element of the list represents a line from the file, including the newline character at the end of each line.

syntax:

```python
file_object.readlines()
```

Example:

```python
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)
```

example:

```python
f=open("hello.txt",mode="r")
data=f.readlines()

for i in data:
   print(i)
f.close()
```

It's essential to choose the appropriate method based on your specific requirements. If you want to read the entire content of the file as a single string, use **`read()`**. If you need to process the file line by line, use **`readline()`**. If you want to read all the lines and store them in a list, use **`readlines()`**.

# How to read the file using the for loop:

```python
f=open("hello.txt",mode="r")
for i in f:
   print(i)
f.close()

output:
kil
                   #here spaces occurs by /n
bill 

pandey
```

To remove spaces

```python
f=open("hello.txt",mode="r")
for i in f:
   print(i,end="")
f.close()

output:

kil
bill 
pandey

```

# tell() and seek()

**`tell()`** and **`seek()`** methods are used in file handling to determine the current position (offset) of the file pointer and to move the file pointer to a specified position, respectively.

1. **`tell()`**: This method returns the current position of the file pointer in the file. The position is represented as the number of bytes from the beginning of the file.
2. position starts from 0. it is just like indexing in string.

syntax:

```python
file_object.tell()
```

Example:

```python
with open('example.txt', 'r') as file:
    content = file.read(10)  # Read the first 10 bytes of the file
    position = file.tell()   # Get the current position of the file pointer
    print("Content:", content)
    print("Current Position:", position)
```

```python
with open('hello.txt', 'r') as file:
    content = file.read(10)  # Read the first 10 bytes of the file
    position = file.tell()   # Get the current position of the file pointer
    print("Content:", content)
    print("Current Position:", position)

Output:
Content: kill
mull

Current Position: 12
```

`seek()`

This method is used to move the file pointer to a specified position within the file. It takes two arguments: the offset (number of bytes) from the reference point and the reference point itself. The reference point can take three values:

- 0: The beginning of the file (default).
- 1: The current position of the file pointer.
- 2: The end of the file.

Example:

```python
with open('example.txt', 'r') as file:
    content = file.read()     # Read the entire file
    print("Content:", content)

    file.seek(0, 0)           # Move the file pointer to the beginning
    line = file.readline()    # Read the first line from the beginning
    print("First Line:", line)

    file.seek(10, 1)          # Move the file pointer 10 bytes from the current position
    line = file.readline()    # Read the next line after skipping 10 bytes
    print("Next Line:", line)

    file.seek(-15, 2)         # Move the file pointer 15 bytes before the end of the file
    line = file.readline()    # Read the last line by moving backwards from the end
    print("Last Line:", line)
```

example:

```python
f=open("hello.txt",mode='r')
print(f.tell())
print(f.read(2))
f.seek(0)
print(f.read())
f.close()

output:

0
ki
kill
mull
null
bill
```

The **`tell()`** and **`seek()`** methods are useful for working with large files or when you need to read or write data from specific positions in a file. By combining these methods with other file reading and writing methods, you can efficiently manage file operations based on your requirements.

# Find number of characters, words and lines in file

```python
f=open("hello.txt",mode='r')
number_of_words=0
number_of_chars=0
number_of_lines=0

for line in f:
    number_of_lines+=1
    line=line.strip("\n") # removes \n
    number_of_chars+=len(line)
    list1=line.split()
    number_of_words+=len(list1)
#this for loop runs upto empty line
f.close()

print("Number of words: ",number_of_words)
print("Number of chars: ",number_of_chars)
print("Number of lines: ",number_of_lines)

output:

Number of words:  6
Number of chars:  36
Number of lines:  3
```

# Writing Data to a text file using :

- 'W' mode:-
• It opens the file to write only.
• It overwrites the data in a file.
• If a file doesn't exist ,it creates a new file and write into it.
- The file pointer exists at the beginning of file.

- Mainly,two methods are used for writing data in file:-
1. write()
2. writelines()

syntax

```python
file_obj.write(data in string format)
```

1. **`write()`**:
The **`write()`** method is used to write a string to the file. It takes a single argument, which is the string data that you want to write. If the file is opened in text mode, the data is expected to be a string, and if the file is opened in binary mode, the data should be bytes.

Syntax:

```python
with open("filename.txt", "w") as file:
    file.write("This is a line of text.")
```

In this example, we open the file "filename.txt" in write mode ("w") and use the **`write()`** method to write the string "This is a line of text." to the file.

**`writelines()`**:

The **`writelines()`** method is used to write multiple lines of data to the file. It takes a sequence (e.g., list or tuple) of strings as its argument. Each string in the sequence represents a line of data to be written to the file.

Syntax:

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("filename.txt", "w") as file:
    file.writelines(lines)
```

In this example, we open the file "filename.txt" in write mode ("w") and use the **`writelines()`** method to write the list of lines to the file.

It's important to note that the **`write()`** method overwrites the existing content of the file, and the **`writelines()`** method writes the lines as they are, including any newline characters ("\n") you include in the data.

example:

```python
lines = ["python \n", " is a\n", "programming language\n"]
with open("hello.txt", "w") as file:
    file.writelines(lines)

Output:
hello.txt file 

python 
 is a
programming language
```

# Copy content of one file to another file

```python
f1=open("source.txt",mode='r',encoding='utf-8')
f2=open("target.txt",mode='w',encoding='utf-8')
data=f1.readlines()
for line in data:
    f2.write(line)
f1.close()
f2.close()

Output
from the source the data copied to target
```

```python
def copy_file(source_file, destination_file):
    try:
        # Open the source file in read mode
        with open(source_file, "r") as source:
            # Read the content of the source file
            content = source.read()

        # Open the destination file in write mode
        with open(destination_file, "w") as destination:
            # Write the content to the destination file
            destination.write(content)

        print(f"Content from '{source_file}' copied to '{destination_file}' successfully.")

    except FileNotFoundError:
        print("One of the files does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
copy_file("source.txt", "destination.txt")
```

# X mode  prevent Data loss while writing

## Xmode:-

Used to write data in file.
Note:- It writes only in a new file.

the "x" mode, also known as "exclusive creation" mode, is a file opening mode that helps prevent data loss while writing to a file. It is designed to create a new file, but it raises a **`FileExistsError`** if the file already exists, ensuring that existing data is not accidentally overwritten.

When you use the "x" mode to open a file, Python will attempt to create the file, and if the file already exists, it will raise an exception. This makes it useful when you want to create a new file and ensure that no other file with the same name exists.

Here's an example of using the "x" mode:

```python
try:
    with open("new_file.txt", "x") as file:
        file.write("This is a new file.")
    print("File created and data written successfully.")
except FileExistsError:
    print("File 'new_file.txt' already exists. Cannot overwrite.")
except Exception as e:
    print(f"An error occurred: {e}")
```

In this example, we attempt to open a file named "new_file.txt" in "x" mode. If the file doesn't exist, Python will create it and write the specified data into it. If the file already exists, the **`FileExistsError`** exception will be caught, and the code will print a message indicating that the file cannot be overwritten.

Using the "x" mode can be helpful when you want to ensure that you don't accidentally overwrite important data while writing to a new file. It's a safe way to create new files without risking data loss.

```python
data="yaswanth teja"

f=open("one.txt",mode='x')
f.write(data)
f.close()

Output

here we have two posibilities if there is no file then it creates a new file and copys the data to it.
 
if already the file exists: error 

Traceback (most recent call last):
  File "f:\courses\Python\file.py", line 3, in <module>
    f=open("one.txt",mode='x')
      ^^^^^^^^^^^^^^^^^^^^^^^^
FileExistsError: [Errno 17] File exists: 'one.txt'
```

# Merging multiple files

```python
import os

files=[]
merged_data=""
while True:
    f_name=input("Enter the file name:")
    files.append(f_name)
    ans=input("Want to add another file? (y/n):").lower()
    if ans!='y':
        break
for file in files:
    filename=file+'.txt'
    if os.path.isfile(filename):
        f=open(filename,mode='r',encoding='utf=8')
        merged_data=merged_data+f.read()+'\n'
        f.close()
print(merged_data)

with open(input("Enter final file name: ")+'.txt',mode='x',encoding='utf-8') as f:
    f.write(merged_data)
    print("merging is done !!")

Output:

Enter the file name:file 
Want to add another file? (y/n):y
Enter the file name:file1
Want to add another file? (y/n):y
Enter the file name:file2
Want to add another file? (y/n):n

Enter final file name: final
merging is done !!
```

```python
def merge_files(output_file, input_files):
    try:
        with open(output_file, "w") as output:
            for file_name in input_files:
                with open(file_name, "r") as input_file:
                    content = input_file.read()
                    output.write(content)

        print("Files merged successfully.")

    except FileNotFoundError:
        print("One of the input files does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_files = ["file1.txt", "file2.txt", "file3.txt"]
output_file = "merged_output.txt"
merge_files(output_file, input_files)
```

the **`merge_files()`** function takes two arguments: **`output_file`** (the name of the file where the merged content will be written) and **`input_files`** (a list containing the names of input files to be merged).

The function iterates through each input file in the **`input_files`** list, reads its content using the **`read()`** method, and writes the content to the output file using the **`write()`** method. This process repeats for each input file, effectively merging the contents of all the input files into the output file.

Make sure to replace the file names in the **`input_files`** list with the names of the files you want to merge. Also, provide a valid **`output_file`** name where the merged content should be saved.

Remember that this approach is suitable for merging small to moderately sized files. For very large files or a large number of files, you may want to consider reading and writing the files in chunks to handle memory efficiently.

To merge multiple Excel files in Python,

```python
import pandas as pd

def merge_excel_files(output_file, input_files):
    try:
        # Create an empty list to store DataFrames from each file
        dataframes = []

        # Read each Excel file and store its DataFrame in the list
        for file_name in input_files:
            df = pd.read_excel(file_name)
            dataframes.append(df)

        # Concatenate all DataFrames into a single DataFrame
        merged_df = pd.concat(dataframes, ignore_index=True)

        # Write the merged DataFrame to a new Excel file
        merged_df.to_excel(output_file, index=False)

        print("Excel files merged successfully.")

    except FileNotFoundError:
        print("One of the input files does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_files = ["file1.xlsx", "file2.xlsx", "file3.xlsx"]
output_file = "merged_output.xlsx"
merge_excel_files(output_file, input_files)
```

the **`merge_excel_files()`** function takes two arguments: **`output_file`** (the name of the file where the merged content will be saved) and **`input_files`** (a list containing the names of Excel files to be merged).

The function reads each Excel file using **`pd.read_excel()`**, stores each DataFrame in a list (**`dataframes`**), and then uses **`pd.concat()`** to concatenate all the DataFrames into a single DataFrame (**`merged_df`**). Finally, the merged DataFrame is written to a new Excel file using the **`to_excel()`** method.

Please ensure that all the input Excel files have the same structure (same column names and order) to avoid any issues during concatenation. Also, make sure that the columns in the output file are appropriate for your use case.

Pandas provides many options and features to customize the merging process further, such as handling missing values, selecting specific columns, etc. You can refer to the pandas documentation for more information on data manipulation with DataFrames.

# rename files

```python
import os

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' renamed to '{new_name}' successfully.")
    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
old_file_name = "old_file.txt"
new_file_name = "new_file.txt"
rename_file(old_file_name, new_file_name)
```

the **`rename_file()`** function takes two arguments: **`old_name`** (the current name of the file) and **`new_name`** (the desired new name of the file). The function uses **`os.rename()`** to rename the file. If the file with the old name exists, it will be renamed to the new name. If the file does not exist, a **`FileNotFoundError`** will be raised.

Please note that the **`os.rename()`** function will not overwrite an existing file with the new name. If a file with the new name already exists, it will raise an error. To avoid overwriting files, you can check if the new name is available before renaming the file.

```python
import os

def rename_file(old_name, new_name):
    if not os.path.exists(old_name):
        print(f"The file '{old_name}' does not exist.")
    elif os.path.exists(new_name):
        print(f"A file with the name '{new_name}' already exists.")
    else:
        try:
            os.rename(old_name, new_name)
            print(f"File '{old_name}' renamed to '{new_name}' successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage
old_file_name = "old_file.txt"
new_file_name = "new_file.txt"
rename_file(old_file_name, new_file_name)
```

we added checks for the existence of the old file and the absence of a file with the new name before renaming the file. This way, you can handle potential issues and ensure a smooth renaming process.

```python
import os
path=input("Enter the path: ")   # in python \ need to convert to /
path=path.replace('\\','/')
print(path)

# rename(old_name,new_name)

def main():
    i=1
    for filename in os.listdir(path):
        new_name=path+"car"+str(i)+'.jpg'
        old_name=path+filename
        os.rename(old_name,new_name)
        i+=1

main()

```

# Reading and Writing CSV Data

To read and write CSV (Comma-Separated Values) data in Python, you can use the built-in **`csv`** module. The **`csv`** module provides functions for working with CSV files in an easy and efficient way.

Let's go through reading and writing CSV data step-by-step:

## **Reading CSV Data:**

1. Import the **`csv`** module:

```python
import csv
```

1. Use **`csv.reader`** to read data from the CSV file:

```python
def read_csv_file(file_name):
    try:
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
read_csv_file("data.csv")
```

we define a function **`read_csv_file()`** that takes the CSV file's name as input. The function opens the file using **`open()`** and reads its content using **`csv.reader()`**. Each row of the CSV file is returned as a list, and the function prints each row.

## **Writing CSV Data:**

1. Import the **`csv`** module:

```python
import csv
```

1. Use **`csv.writer`** to write data to the CSV file:

```python
def write_csv_file(file_name, data):
    try:
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                writer.writerow(row)

        print(f"Data written to '{file_name}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
data_to_write = [
    ["Name", "Age", "City"],
    ["John", 28, "New York"],
    ["Alice", 24, "London"],
    ["Bob", 32, "Paris"]
]
write_csv_file("output.csv", data_to_write)
```

we define a function **`write_csv_file()`** that takes the CSV file's name and the data to be written as input. The function opens the file using **`open()`** in write mode ('w') and writes the data using **`csv.writer()`** and **`writerow()`**.

Make sure to replace **`data.csv`** with the name of your input CSV file and **`output.csv`** with the desired name for the output CSV file.

## **Reading CSV Data using pandas:**

To read CSV data using pandas, you can use the **`pd.read_csv()`** function.

```python
import pandas as pd

def read_csv_file(file_name):
    try:
        df = pd.read_csv(file_name)
        print(df)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
read_csv_file("data.csv")
```

the **`read_csv_file()`** function takes the CSV file's name as input. The function uses **`pd.read_csv()`** to read the CSV file and store it as a pandas DataFrame. The entire DataFrame is then printed to display the content.

## **Writing CSV Data using pandas:**

To write CSV data using pandas, you can use the **`pd.to_csv()`** function.

```python
import pandas as pd

def write_csv_file(file_name, data):
    try:
        df = pd.DataFrame(data)
        df.to_csv(file_name, index=False)
        print(f"Data written to '{file_name}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
data_to_write = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [28, 24, 32],
    "City": ["New York", "London", "Paris"]
}
write_csv_file("output.csv", data_to_write)
```

the **`write_csv_file()`** function takes the CSV file's name and the data to be written as input. The function converts the data to a pandas DataFrame using **`pd.DataFrame()`**. It then uses **`pd.to_csv()`** to write the DataFrame to the CSV file. The **`index=False`** argument is used to exclude writing the DataFrame index as a separate column in the CSV file.

Pandas provide many options and parameters for customizing the reading and writing of CSV files, such as specifying the delimiter, handling missing values, selecting specific columns, and more. You can refer to the pandas documentation for further details on how to work with CSV data using pandas.


