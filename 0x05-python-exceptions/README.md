0x05. Python - Exceptions


Exception handling is a programming construct that allows you to handleruntime errors in a controlled manner. By using exception handling, youcan catch and respond to exceptions, preventing your program from crashing abruptly.


The try-except Block

The primary mechanism for handling exceptions in Python is the try-except block. It allows you to write code that might raise an exception within the try block, and if an exception occurs, it is caught and handledwithin the except block.

GENERAL SYNTAX:

try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception


Multiple Exception Handling

Python allows you to handle multiple exceptions using multiple except clauses. This allows you to specify different exception types and handle them separately.

SYNTAX:

try:
    # Code that might raise an exception
except ExceptionType1:
    # Code to handle ExceptionType1
except ExceptionType2:
    # Code to handle ExceptionType2


Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
What’s the difference between errors and exceptions
What are exceptions and how to use them
When do we need to use exceptions
How to correctly handle an exception
What’s the purpose of catching exceptions
How to raise a builtin exception
When do we need to implement a clean-up action after an exception