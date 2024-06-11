# Input and Output in Python

In Python, input and output (I/O) operations are fundamental for interacting with the user and external systems. Let's break down how these operations work internally.

## Output

### Ways of writing values:
  - Expression statements 
  - the print() function. 
  - write() method of file objects; the standard output file can be referenced as `sys.stdout`

### The `print()` function:
- All `non-keyword arguments` are converted to strings like `str()` does and written to the stream, separated by sep and followed by end. Both sep and end must be strings; they can also be None, which means to use the default values.
- Internally, `print()` works by:
  - Converting its arguments to strings.
  - Writing the resulting string to `sys.stdout`.
  - Flushing the output buffer if needed to ensure that the text appears on the screen immediately.

### Output Formatting
1. To use `Formatted string literals` (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}.

```python
name = "John"
age = 25
print(f"Hello, {name}. You are {age}.")
```

An optional format specifier can follow the expression. This allows greater control over how the value is formatted. The following example rounds pi to three places after the decimal:

```python
import math
print(f"The value of pi is approximately {math.pi:.3f}.")
```

Passing an interger after the `:` will cause that field to be a `minimum number of characters wide`. This is useful for making columns line up.

```python
name = {'John': 25, 'Jane': 30, 'Doe': 35}
for name, age in name.items():
    print(f'{name:10} ==> {age:10}')

# Output
# John       ==>         25
# Jane       ==>         30
# Doe        ==>         35
```

Other modifiers can be used to convert the value before it is formatted. `'!a'` applies `ascii()`, `'!s'` applies `str()`, and `'!r'` applies `repr()`:


```python

animals = 'eels'
print(f'My hovercraft is full of {animals}.')

# Output
# My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.')

# Output
# My hovercraft is full of 'eels'.
```

The `=` specifier can be used to expand an expression to the text of the expression, an equal sign, then the representation of the evaluated expression:

```python
animals = 'eels'
print(f'{animals=}.')
# Output
# animals='eels'.
```

see more about self documenting expressions [here](https://docs.python.org/3.10/whatsnew/3.8.html#bpo-36817-whatsnew)

2. Using the `str.format()` method:

```python
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"
```

The brackets and characters within them (called format fields) are replaced with the objects passed into the `str.format()` method. A number in the brackets can be used to refer to the position of the object passed into the str.format() method.

### Reading and Writing to files

1. Read from a file: `open()`
- open() returns a file object, and is most commonly used with two positional arguments and one keyword argument: 

```python 
f = open(filename, mode, encoding=None)
```

arguments:
- The first argument is a string containing the `filename`. 
- The second argument is another string containing a few characters describing the way in which the file will be used. `mode` can be 
  - 'r' when the file will only be read
  - 'w' for only writing (an existing file with the same name will be erased)
  - 'a' opens the file for appending; any data written to the file is automatically added to the end. 
  - 'r+' opens the file for both reading and writing. 
  - The mode argument is optional; 'r' will be assumed if it’s omitted.

#### Good practice 

>> It is `good practice` to use the with keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than writing equivalent try-finally blocks:

