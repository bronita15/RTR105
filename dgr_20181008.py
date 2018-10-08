Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> type(32)
<type 'int'>
>>> max('Hello world')
'w'
>>> min('Hello world')
' '
>>> len('Hello world')
11
>>> int('32')
32
>>> int('Hello')

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int('Hello')
ValueError: invalid literal for int() with base 10: 'Hello'
>>> int(3.99999)
3
>>> int(-2.3)
-2
>>> float(32)
32.0
>>> float('3.14159')
3.14159
>>> float(3.14159)
3.14159
>>> str(32)
'32'
>>> str(3.1547528)
'3.1547528'
>>> import math
>>> print(math)
<module 'math' (built-in)>
>>> ratio = signal_power / noise_power

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    ratio = signal_power / noise_power
NameError: name 'signal_power' is not defined
>>> decibels = 10* math.log10(ratio)

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    decibels = 10* math.log10(ratio)
NameError: name 'ratio' is not defined
>>> import random
>>> for i in range (10):
	x = random.random()
	print(x)

	
0.749464762704
0.81635772071
0.421979179824
0.620068069837
0.424387628514
0.54709010212
0.488278223494
0.326441867906
0.681449384966
0.799050059738
>>> 
