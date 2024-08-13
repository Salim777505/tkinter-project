
1. slice()
The slice() function creates a slice object that can be used to specify how to slice sequences.


# Create a slice object
s = slice(1, 5, 2)

# Use the slice object to slice a list
my_list = [10, 20, 30, 40, 50]
sliced_list = my_list[s]
print(sliced_list)  # Output: [20, 40]
2. sorted()
The sorted() function returns a new sorted list from the elements of any iterable.

# Sort a list of numbers
numbers = [4, 1, 7, 3, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 3, 4, 7, 9]

# Sort a list of strings
words = ['banana', 'apple', 'cherry']
sorted_words = sorted(words)
print(sorted_words)  # Output: ['apple', 'banana', 'cherry']
3. staticmethod()
The staticmethod() decorator transforms a method into a static method, which doesn’t receive an implicit first argument (i.e., it doesn’t get self or cls).


class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Call the static method without creating an instance
result = MathUtils.add(5, 3)
print(result)  # Output: 8


4. str()
The str() function returns the string representation of an object.


# Convert an integer to a string
num = 123
num_str = str(num)
print(num_str)  # Output: '123'

# Convert a list to a string
my_list = [1, 2, 3]
list_str = str(my_list)
print(list_str)  # Output: '[1, 2, 3]'


5. sum()
The sum() function adds up the items of an iterable.


# Sum a list of numbers
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # Output: 15

# Sum with a starting value
total_with_start = sum(numbers, 10)
print(total_with_start)  # Output: 25



6. super()
The super() function returns a proxy object that allows you to call methods from a parent class.


class Parent:
    def __init__(self):
        self.value = 'parent'

    def show(self):
        print(self.value)

class Child(Parent):
    def __init__(self):
        super().__init__()  # Call the parent class constructor
        self.value = 'child'

# Create an instance of Child
child = Child()
child.show()  # Output: 'child'


7. tuple()
The tuple() function returns a tuple object.


# Convert a list to a tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

# Create a tuple directly
another_tuple = (4, 5, 6)
print(another_tuple)  # Output: (4, 5, 6)



8. type()
The type() function returns the type of an object.

# Get the type of an integer
print(type(123))  # Output: <class 'int'>

# Get the type of a string
print(type("hello"))  # Output: <class 'str'>

# Get the type of a custom class instance
class MyClass:
    pass

obj = MyClass()
print(type(obj))  # Output: <class '__main__.MyClass'>
