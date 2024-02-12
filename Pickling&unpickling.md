# Pickling & unpickling

Pickling and unpickling are processes in Python that allow you to serialize (convert to a byte stream) and deserialize (convert from a byte stream) objects. This is commonly used for data persistence, storage, and communication between processes or systems.

Python objects are converted into byte stream is called serialization (pickling).

When byte stream are converted into python objects are called deserialization (unpickling).

**Pickling:**

- Pickling is the process of converting a Python object into a byte stream.
- It is also known as Serialization or Marshalling or Flattening
- Use:- To transfer python objects from one server /system/ application into another.
- Pickled file has any extension
- The **`pickle`** module in Python provides the **`dump()`** function for pickling an object to a file-like object (e.g., a file or a **`BytesIO`** object).

```python
import pickle
```

We have 4 functions present in pickle module.

1. dump() :- python objects —→byte-streams(store into file)
2. load():-  byte streams  ——→  python objects(read from file)
3. dumps(): - python  objects —→byte-streams
4. loads():-  byte streams  ——→  python objects

dump() performs —→ pickling

load() performs ——> un pickling

loads(), dumps() is used when we don’t want to store byte stream into file.

example:

```python
import pickle
data=['Yash',98.2,22]

#pickling
byte=pickle.dumps(data)
print(byte) #pickled representation

# unpickling
data1=pickle.loads(byte)
print(data1)   # ['Yash',98.2,22]
```

output-

```python
b'\x80\x04\x95\x17\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x04Yash\x94G@X\x8c\xcc\xcc\xcc\xcc\xcdK\x16e.'
['Yash', 98.2, 22]
```

Example of pickling:

```python

import pickle

# Object to pickle
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Pickle the object to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

```

In this example, the dictionary **`data`** is pickled to a file named 'data.pkl'.

**Disadvantages:**

- It is advisable not to unpickle data received from an untrusted sources as they may have security threats.
- pickle module has no way to identify these threats or malicious data.

**Unpickling:**

- Unpickling is the process of converting a byte stream back into a Python object.
- The **`pickle`** module provides the **`load()`** function for unpickling an object from a file-like object.

Example of unpickling:

```python

import pickle

# Unpickle the object from a file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)

```

In this example, the pickled data in 'data.pkl' is unpickled back into a Python object, and **`loaded_data`** will contain the original dictionary.

It's important to note that the **`pickle`** module is Python-specific, and the pickled data may not be compatible with other programming languages. If cross-language compatibility is needed, you might consider using other serialization formats like JSON.

**Security Note:**

- Be cautious when unpickling data from an untrusted source, as it could execute arbitrary code. Only unpickle data from trusted sources to avoid security risks.

The **`pickle`** module also provides functions like **`dumps()`** and **`loads()`** for pickling and unpickling in-memory byte streams without the need for external files.

example:

```python
project
|
-student.py
|
-pickling.py
|
-unpickling.py
|
----
```

student.py

```python
class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    
    def display(self):
        print(f'nameis {self.name} \n,roll no is {self.rollno}\n,marks is {self.marks}')
```

pickling.py

```python
import student
import pickle

f=open('data.pkl','wb')
n=int(input("Enter a number of employees: "))
for i in range(n):
    name=input('Enter a name: ')
    rollno=int(input('Enter the roll no: '))
    marks=float(input('Enter  your marks: '))
    obj=student.Student(name,rollno,marks)
    pickle.dump(obj,f)  # pickling
    
print('Object stored success')
```

unpickling.py

```python
import pickle

f1=open('data.pkl','rb')

while True:
    try:
        obj=pickle.load(f1)
        print(obj)
        obj.display()
    except EOFError:
        print('All the data picklied')
        break
f1.close()
```

