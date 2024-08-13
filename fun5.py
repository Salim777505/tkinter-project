

1. print()
Prints the given object to the console.


print("Hello, world!")  # Output: Hello, world!
print(42)              # Output: 42
print([1, 2, 3])       # Output: [1, 2, 3]



2. property()
Returns a property attribute for a class. This is typically used in conjunction with getter, setter, and deleter methods.


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

p = Person("Alice")
print(p.name)    # Output: Alice
p.name = "Bob"
print(p.name)    # Output: Bob
del p.name
3. range()
Returns a sequence of integers.


for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4


4. repr()
Returns a printable representation of an object, useful for debugging.


x = [1, 2, 3]
print(repr(x))  # Output: [1, 2, 3]


5. reversed()
Returns an iterator that accesses the given sequence in the reverse order.


seq = [1, 2, 3]
for item in reversed(seq):
    print(item)
# Output:
# 3
# 2
# 1


6. round()
Rounds a number to a specified number of decimal places.


print(round(3.14159, 2))  # Output: 3.14
print(round(3.14159))     # Output: 3


7. set()
Constructs and returns a set from the given iterable.


s = set([1, 2, 2, 3])
print(s)  # Output: {1, 2, 3}


8. setattr()
Sets the value of an attribute of an object.


class MyClass:
    pass

obj = MyClass()
setattr(obj, 'attribute', 42)
print(obj.attribute)  # Output: 42


