Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> print(__builtins__.__doc__)
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> a = 10
>>> a
10
>>> a * a
100
>>> b=1.89
>>> b
1.89
>>> b * b
3.5721
>>> c = p

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    c = p
NameError: name 'p' is not defined
>>> c = 'P'
>>> c
'P'
>>> vars()
{'a': 10, 'c': 'P', 'b': 1.89, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> c * c

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    c * c
TypeError: can't multiply sequence by non-int of type 'str'
>>> type(a)
<type 'int'>
>>> type(b)
<type 'float'>
>>> type(c)
<type 'str'>
>>> 
