
## globals() & locals() function
symbol table: It is a data structure which contains all necessary  information about global space of the program

### global()

globals() returns a dictionary of current global symbol table.

Syntax:

```python
globals()
```

ex:

```python
a=10
def demo():
	print('hello')
print(globals())
```

output:

```python
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001FDF5DC4350>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\python_programs\\main.py', '__cached__': None, 'a': 10, 'demo': <function demo at 0x000001FDF5F38900>}
```

```python
a=10
def demo():
	print('hello')
	globals()['a']=10000

demo()
print(a)
```

```python
hello
10000
```

## locals()

**`locals()`** is a built-in function that returns a dictionary containing the current local symbol table. The local symbol table is a namespace containing the names of local variables, which includes variables defined in the current function and any variables passed as arguments.

```python
a=10
def demo():
	print('hello')
	b=100
	print(locals())
demo()
```

```python
hello
{'b': 100}
```

```python
a=10
def demo():
	print('hello')
	b=100
	print(locals()['b'])
demo()
```

```python
hello
100
```
