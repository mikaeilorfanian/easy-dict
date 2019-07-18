# easy-dict: eye-friendly Python `dict`
`easy-dict` makes working with Python `dict` objects easier by letting you type less to achieve more.   
It supports:   
- dot notation for accessing values, i.e. `obj.a.b` instead of `obj['a']['b']`
- nested `dict` and `list` structures
- iteration over keys e.g. `[e for e in easy_dict]`
- nice string representation for debugging and `print`ing
- eye-friendly way of getting the first element of a `list`, e.g. `my_list.first` instead of my_list[0] 

This library is a very thin layer around `dict` objects and it's been used in production systems without adding much memory or CPU overhead. To minimize bugs and avoid using magic the data-structures in this library don't inherit from or depend on the internal implementation details of Python's built-in objects.      
# How to use it
`easy-dict`'s main object is `EasyAccessDict`:   
```python
from easy_dict import EasyAccessDict
regular_dict = {'a': 'b'}
easy_dict = EasyAccessDict(regular_dict)
```
By default `EasyAccessDict` creates a `deepcopy` of your dict, but you can disable that to gain some performance:    
`easy_dict = EasyAccessDict(regular_dict, make_copy=False)`
### Important Note   
As the class name `EasyAccessDict` suggests, you *should not make changes* to instances of it as this feature isn't supported and has undefined behavior:   
```python
>>> regular_dict = {'a': 1, 'b': {'c': 2}}
>>> easy_dict = EasyAccessDict(regular_dict)
>>> easy_dict.b.c = 3
>>> assert easy_dict.b.c == 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```
## Accessing data
To access data in an `EasyAccessDict` use the dot notation like how objects are accessed in JavaScript:   
```python
from easy_dict import EasyAccessDict
regular_dict = {'a': 'b'}
easy_dict = EasyAccessDict(regular_dict)
easy_dict.a  == regular_dict['a']
```
If you access a non-existing key, you'll get an error:   
```python
>>> easy_dict.b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "easy_dict.py", line 34, in __getattr__
    raise EasyDictError('No attr/key called "{}"'.format(attribute_name))
easy_dict.EasyDictError: No attr/key called "b"
```
## Nested `dict` structures
`EasyAccessDict` also works with nested `dict` structures by automatically converting them to `EasyAccessDict` instances:   
```python
regular_dict = {'a': 1, 'b': {'c': 2}}
easy_dict = EasyAccessDict(regular_dict)
easy_dict.b.c  == regular_dict['b']['c']
```
## Iteration
An `EasyAccessDict` instance supports the `iterable` protocol for looping over its attributes:   
```python
regular_dict = {'a': 1, 'b': {'c': 2}}
easy_dict = EasyAccessDict(regular_dict)
assert [e for e in easy_dict] == ['a', 'b']
assert [e for e in easy_dict.b] == ['c']
```
## Access using the `get` method
Some `dict` keys (e.g. `{1: '1'}`) cannot be used in dot notation. In such cases you can use the `get` method which mirrors the behavior of `dict.get`:   
```python
regular_dict = {1: '1'}
easy_dict = EasyAccessDict(regular_dict)
assert regular_dict[1] == easy_dict.get(1)

easy_dict.get(2, default=2)  # returns the provided default value
``` 
## Debugging (printing `EasyAccessDict` objects)
`EasyAccessDict` instances are `print` and `repr` friendly and show the original data fed to them:      
```python
>>> regular_dict = {'a': 1}
>>> easy_dict = EasyAccessDict(regular_dict)
>>> print(easy_dict)
{'a': 1}
```
## bonus: first element in lists
There's a nice little feature of `EasyAccesDict` objects which allows you to access the first element of `list` objects without having to use `[0]`:   
```python
regular_dict = {'a': [{'d': 2}]}
easy_dict = EasyAccessDict(regular_dict)
easy_dict.a.first.d  == regular_dict['a'][0]['d']
``` 
# Please hack on It
The source code is pretty small - 60 lines in just 1 Python module - and it's well-tested. To reduce complexity and magic, I've use some advanced feature of the language which make the code pleasant to the eye. I invite you to read the source and let me know what you think! Also, create GitHub issues with suggestions for improvements if you're in a creative mood :)
## How to hack on it
First, the dependencies:    
`pip install -r requirements-dev.txt`   
Then, make changes and add tests - using `pytest` patterns and idioms - to make sure you get the behavior you intended. Finally run the tests:    
`pytest`