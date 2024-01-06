# Learning the basics

### Assignments and Variables

When we store data in a mamory location we have created a variable.

variable > operator > value
a = 2
or
a = 1+3 (a will evaulate as 4)

Variable names must start with an underscore or letter and **snake_case** is recommended.

#### keywords

The following are built in keywords and must not be used as variables:

False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield

### Data Types

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

#### Assignment

Assign a value to a variable using the = for assignment

#### Determining type

Use the command print(type(variable)) to see what data type a variable is.

`>>> a = 678
>>> print(a)
678
>>> print(type(a))
<class 'int'>
>>> b = 2.3454
>>> print (type(b))
<class 'float'>
>>>`

#### Floating Point Errors

>>> a = 0.1 + 0.3 + 0.6
>>> print(a)
1.0
>>> a = 0.1 + 0.1 + 0.1
>>> print(a)
0.30000000000000004
>>>

Unfortunately, most decimal fractions cannot be represented exactly as binary fractions. A consequence is that, in general, the decimal floating-point numbers you enter are only approximated by the binary floating-point numbers actually stored in the machine.

#### Strings

Strings are sequences of characters surrounded by quotes. You can use either single or double quotes to demark the start and end of the sentence. In this way, you can include a single quote mark as a character. 
“This is a string” 
‘This is also a string’ 
“This is a string with an internal quote mark of one type, which doesn’t count as a quote”
Strings are immutable, that means you cannot change the string

#### The None keyword

The None keyword is used to define a null value or no value, it is a data type

>>> a = None
>>> print (type(a))
<class 'NoneType'>
>>>

#### Booleans

True and False are used for testing conditions. Any number which is not 0 evaluates as True.

>>> a = True
>>> print(a)
True
>>>

#### Dynamic Typing

Python uses dynamic typing, unlike many other languages. We can change the value in a variable.

>>> dog = 2
>>> print(dog)
2
>>> dog = "mutt"
>>> print(dog)
mutt
>>>

### Arithmetic Operators

### Comparison Operators

### Logical and Boolean Operators

### Coding with operators

### Coding with Strings

#### String Interpolation

We can concatenate strings using + to give text and a variable.





See exercises_01 folder


