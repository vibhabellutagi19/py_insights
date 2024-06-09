# Input and Output in Python

In Python, input and output (I/O) operations are fundamental for interacting with the user and external systems. Let's break down how these operations work internally.

### Output Formatting

#### Ways of writing values:
  - Expression statements 
  - the print() function. 
  - write() method of file objects; the standard output file can be referenced as `sys.stdout`

#### The `print()` function:
- All `non-keyword arguments` are converted to strings like `str()` does and written to the stream, separated by sep and followed by end. Both sep and end must be strings; they can also be None, which means to use the default values.
- Internally, `print()` works by:
  - Converting its arguments to strings.
  - Writing the resulting string to `sys.stdout`.
  - Flushing the output buffer if needed to ensure that the text appears on the screen immediately.