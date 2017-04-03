# fstring427
Python 3.6 f-string sympathy (partial compatibility) module for Python 2.7
See https://www.python.org/dev/peps/pep-0498/ for the specification for _Literal String Interpolation_.


## Example from PEP-0498

```
>>> import datetime
>>> name = 'Fred'
>>> age = 50
>>> anniversary = datetime.date(1991, 10, 12)
>>> f'My name is {name}, my age next year is {age+1}, my anniversary is {anniversary:%A, %B %d, %Y}.'
'My name is Fred, my age next year is 51, my anniversary is Saturday, October 12, 1991.'
>>> f'He said his name is {name!r}.'
"He said his name is 'Fred'."
```

## Sympathetic output from fstring427

```
>>> from fstring427.fstring import Fmt as f
>>> import datetime
>>> name = 'Fred'
>>> age = 50
>>> anniversary = datetime.date(1991,10,12)
>>> str(f('My name is {name}, my age next year is {age+1}, my anniversary is {anniversary:%A, %B %d, %Y}.'))
'My name is Fred, my age next year is 51, my anniversary is Saturday, October 12, 1991.'
>>>  f('He said his name is {name!r}')()
"He said his name is 'Fred'"
```

Note the major differences:

* `f` is a class, not a string type
* `f()` evaluates the string
* str() of a instance of `f` also evaluates the string

The underlying implementation is a subclass of the Python 2.7 Format class, and depends on internals. Obviously fragile
 and probably non-portable, but still serves my purpose.

 ## `printf()`, a convenience function

 ```
 >>> printf('He said his name is {name!r}')
 He said his name is 'Fred'
 ```

 which has the additional convenience of a temporary scope for kwargs

```
 >>> printf('He said his name is {name!r}', name="Sam")
He said his name is 'Sam'
```

## Major incompatibilities:

Python 3.6 f-strings were carefully designed, and cover edge cases that .format() does not, see
https://mail.python.org/pipermail/python-ideas/2015-July/034726.html

fstring427 was implemented on top of .format() and shares the underlying implementation of lookups. If .format()
can't handle a `{field}`, fstring427 will evaluate field as a Python expression in the proper scope.
In practice this means that:

```
a = 10
d = {'a': 'string', 10: 'int'}
printf("{d[a]")
```

prints `string` (Python 2.7 .format() behavior) instead of `int` (Python 3.6 f-string behavior). I've found this a small price to pay
in my 2.7 code to get cleaner printing and string formatting.

_Copyright 2017, Smartvid.io_
