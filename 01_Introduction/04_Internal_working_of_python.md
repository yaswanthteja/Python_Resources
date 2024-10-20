# Internal Working Of Python

![1729342662948](image/Internal_working_of_python/1729342662948.jpg)

### **1. Source Code**

When you write a Python script, it’s human-readable text. This source code is the starting point for everything.

Your Python source code, written in a `.py` file, is human-readable. This code defines what your program does, specifying variables, functions, loops, and so on.

### **2. Compilation to Bytecode (compiler)**

When you run a Python program, the first step is to compile the source code to bytecode. This is done by the Python interpreter:

* **Syntax Check** : Ensures there are no syntax errors.
* **Compilation** : Translates the high-level source code into bytecode, a lower-level, platform-independent representation. This bytecode typically resides in `.pyc` files within the `__pycache__` directory.
  **Compiler** : Python uses an interpreter, but it first compiles your source code into a lower-level form known as bytecode.
* **Tokenizing** : Breaks down your code into small pieces called tokens (like keywords, operators, identifiers).
* **Parsing** : Analyzes the tokens to ensure they follow Python's syntax rules.
* **Control Flow Graph (CFG)** : Represents all paths that might be traversed through a program during its execution.
* **Bytecode Generation** : Converts the parsed tokens into bytecode, a set of instructions for the Python Virtual Machine (PVM).

---

Let’s deep dive this

 **Python Compiler** : Even though Python is known as an interpreted language, it does have a compilation step. Here’s the breakdown:

* **Tokenization** :
  Breaks down your code into small pieces called tokens (like keywords, operators, identifiers).

1. **Source Code** : Starts with your written code.
2. **Tokenizer (Lexer)** : This breaks the source code into smaller pieces called tokens, like keywords (`for`, `if`), operators (`+`, ``), identifiers (variable names), and literals (like numbers or strings).
3. **Parsing** :Analyzes the tokens to ensure they follow Python's syntax rules.
4. **Syntax Analysis** : The parser takes these tokens and checks them against Python's grammar rules.
5. **Parse Tree** : Builds a tree structure from the tokens, representing the grammatical structure of the code.
6. **Semantic Analysis** : Ensures the code makes sense in terms of data types, scope, and other context-specific rules.
7. **Control Flow Graph (CFG)** : Represents all paths that might be traversed through a program during its execution.
   a. **Control Flow Graph** : Represents all possible paths that might be taken through the code during execution.
   b. **Nodes and Edges** : Each node represents a basic block of code, and edges represent the flow of control from one block to another.
8. **Bytecode Generation** :  **Converts the parsed tokens into bytecode, a set of instructions for the Python Virtual Machine (PVM).**
   The bytecode is a more compact, lower level representation of your source code, optimized for execution. It’s platform-independent, meaning it can be run on any system with a compatible PVM.
   a. **Bytecode** : The parsed code is converted into bytecode, a lower-level, platform-independent representation.
   b. **Instruction Set** : This bytecode is a set of instructions that the Python Virtual Machine (PVM) can execute. Bytecode is stored in `.pyc` files in the `__pycache__` directory to speed up future executions.

### **3. Loading Bytecode (Byte code)**

After compilation, the Python Virtual Machine loads the bytecode:

* **Reading from Cache** : If the bytecode has been previously compiled and hasn’t changed, it’s read from the cache (`__pycache__`) (mostly visible when we imported the code) .This speeds up execution by skipping the compilation step.
* The bytecode is loaded into memory, ready to be executed.
  The bytecode is then executed by the PVM, interpreting the instructions to perform the program’s tasks.

### **4. Execution by PVM (PVM)**

The PVM now interprets and executes the bytecode:

* **Instruction Execution** : The PVM reads each bytecode instruction and executes it. Each instruction corresponds to a specific operation, like loading a value, performing arithmetic, or calling a function.
* **Memory Management** : Manages allocation and deallocation of memory for variables and objects. **Memory Management in Python** :

  1. **Reference Counting** : Python keeps track of how many references there are to an object in memory. When the reference count drops to zero, the memory occupied by the object can be reclaimed.
  2. **Object Allocation** : Python objects (like integers, strings, lists) are created in memory when the code is run.
  3. **Garbage Collection** : Python has a garbage collector that helps manage memory by deallocating memory that is no longer in use (i.e., objects with a reference count of zero).
  4. **Memory Pooling** : Python uses pools of memory to allocate small objects more efficiently. This pooling helps reduce the overhead of frequently allocating and deallocating small chunks of memory.
  5. **Memory Optimization** : Python applies various optimizations to minimize memory usage, such as:

     * The PVM performs various runtime optimizations to improve efficiency, such as just-in-time (JIT) compilation in some implementations (like PyPy).
     * Reusing small integers and interned strings.
     * Efficiently managing data structures (e.g., tuples, lists, dictionaries).

     Examples :

     ***Bytecode Caching**
     The PVM caches compiled bytecode to avoid recompiling the source code every time. This speeds up subsequent runs.

     ***Constant Folding**
     This involves simplifying constant expressions at compile time rather than runtime. For example,`3 * 2` might be precomputed to `6`.

So, in summary: the PVM is like an orchestra conductor, seamlessly turning the bytecode into actions that your computer can execute. The beautiful thing about it is that Python code, thanks to the PVM, is portable and can run on different platforms without modification.
