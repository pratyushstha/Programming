Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello world")
Hello world
a = 20
b = "Hello world"
c = 'Thank you'
#a is integer, b and c are strings
type(a)
<class 'int'>
#"class" int
#type()--> data type of variables
>>> #dir()--> returns methods/attrabutes available to the object
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> #OR
>>> dir(b)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> d = b.upper()
>>> print(d)
HELLO WORLD
>>> x = 2.5
>>> type(x)
<class 'float'>
>>> #print()---> Write Operations
>>> print(a, b, c)
20 Hello world Thank you
>>> #comma gives space
>>> print("The value of a =", a)
The value of a = 20
>>> print("x ="x, "y ="y, "z ="z)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("x =", x, "y = ", y, "z =", z)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print("x =", x, "y = ", y, "z =", z)
NameError: name 'y' is not defined
>>> print("a =", x, "b = ", y, "c =", z)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print("a =", x, "b = ", y, "c =", z)
NameError: name 'y' is not defined
>>> print(f"x={x})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"x={x}")
...       
x=2.5
