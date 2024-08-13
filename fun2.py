

getattr():
This function returns the value of a named attribute of an object. If the attribute is not found, it can return a default value if specified.


class MyClass:
    def __init__(self):
        self.attribute = 'Hello, World!'

obj = MyClass()
print(getattr(obj, 'attribute'))  # Output: Hello, World!
print(getattr(obj, 'non_existing_attr', 'Default Value'))  # Output: Default Value

globals():
This function returns a dictionary representing the current global symbol table.

x = 10
y = 20

def print_globals():
    print(globals())

print_globals()
# Output: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at ...>, '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, 'x': 10, 'y': 20, 'print_globals': <function print_globals at ...>, ...}
hasattr():
This function checks if an object has a named attribute.


class MyClass:
    def __init__(self):
        self.attribute = 'Hello'

obj = MyClass()
print(hasattr(obj, 'attribute'))  # Output: True
print(hasattr(obj, 'non_existing_attr'))  # Output: False


hash():
This function returns the hash value of an object. Hashable objects include numbers, strings, and tuples (containing only hashable types).


a = 'hello'
b = (1, 2, 3)
print(hash(a))  # Output: A hash value (e.g., 1395966031385867664)
print(hash(b))  # Output: A hash value (e.g., 2528502973977326415)


help():
This function invokes the built-in help system and provides information about objects. You can pass it a module, class, function, or even an object.


help(print)  # This will provide documentation about the print function


hex():
This function converts an integer to a hexadecimal string.


num = 255
print(hex(num))  # Output: '0xff'


id():
This function returns the identity (memory address) of an object.


a = 'hello'
print(id(a))  # Output: Memory address of the object (e.g., 140354387429824)


input():
This function reads a line from input and returns it as a string.


user_input = input("Enter something: ")
print(f'You entered: {user_input}')
# If you type 'Python' and press Enter, the output will be: You entered: Python



