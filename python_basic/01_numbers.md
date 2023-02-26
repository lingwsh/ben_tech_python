

## Basic python type explaination
In Python, there are several built-in data types that can be used to store values, including:

1. Numbers: used to store numeric values. There are two types of numbers in Python: integers (int) and floating-point numbers (float).

2. Strings: used to store sequences of characters. Strings are enclosed in quotation marks, either single or double.

3. Lists: used to store an ordered collection of items, which can be of different types. Lists are defined using square brackets.

4. Tuples: similar to lists, but tuples are immutable, meaning their elements cannot be changed once they are assigned. Tuples are defined using parentheses.

5. Dictionaries: used to store key-value pairs. Dictionaries are defined using curly braces {}.

6. Sets: used to store unordered collections of unique elements. Sets are defined using curly braces {} with elements separated by commas.

7. Boolean: used to store the values True or False.

These data types form the basic building blocks of any Python program and are used to represent and manipulate different types of data.

## List of the basic Python data types:

1. int
2. float
3. str
4. list
5. tuple
6. dictionary
7. set
8. bool

## Introduce python numbers
In Python, there are two main types of numbers: integers (int) and floating-point numbers (float).

Integers are whole numbers, such as 1, 2, 3, and so on. They can be positive, negative, or zero, and are used to represent countable values.

Floating-point numbers are numbers with a decimal point, such as 3.14, 1.23, and so on. They are used to represent real-world values that can have fractional parts.

Both integers and floating-point numbers can be used in mathematical operations, such as addition, subtraction, multiplication, division, and more.

In Python, you can perform various arithmetic operations on numbers, such as addition, subtraction, multiplication, division, and more. For example:

```# Addition
print(2 + 3)  # Output: 5

# Subtraction
print(5 - 2)  # Output: 3

# Multiplication
print(2 * 3)  # Output: 6

# Division
print(6 / 2)  # Output: 3.0
```
In addition to basic arithmetic operations, Python also supports more advanced mathematical operations, such as exponentiation, square roots, logarithms, and more, using functions from the math module.


## Why int / int, the result is float

In Python 3, division of two integers results in a floating-point number even if the result is a whole number. This behavior was introduced to align with the behavior of other programming languages and to provide a more consistent behavior for division operations in Python.

In earlier versions of Python (Python 2), division of two integers resulted in an integer if the result was a whole number, and a floating-point number if the result was not a whole number. This behavior was considered inconsistent and was changed in Python 3 to always return a floating-point number.

For example, in Python 3:

```print(5 / 2)  # Output: 2.5```

If you want the result of a division operation to be an integer, you can use the // operator, which performs integer division and rounds down to the nearest whole number:

```print(5 // 2)  # Output: 2```