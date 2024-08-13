

1. int()
The int() function converts a number or a string into an integer.


# From a number
num = int(5.67)  # Converts float to integer
print(num)  # Output: 5

# From a string
num_str = int("123")  # Converts string to integer
print(num_str)  # Output: 123

# With base
num_base = int("1010", 2)  # Converts binary string to integer
print(num_base)  # Output: 10


2. isinstance()
The isinstance() function checks if an object is an instance of a specified class or a tuple of classes.


# Checking if an object is an instance of a class
x = 10
print(isinstance(x, int))  # Output: True

# Checking if an object is an instance of multiple classes
y = "Hello"
print(isinstance(y, (int, str)))  # Output: True


3. issubclass()
The issubclass() function checks if a class is a subclass of another class or a tuple of classes.


class Animal:
    pass

class Dog(Animal):
    pass

# Checking if Dog is a subclass of Animal
print(issubclass(Dog, Animal))  # Output: True

# Checking against multiple classes
print(issubclass(Dog, (Animal, str)))  # Output: True


4. iter()
The iter() function returns an iterator object from an iterable.


# From a list
my_list = [1, 2, 3]
list_iter = iter(my_list)

# Using the iterator
print(next(list_iter))  # Output: 1
print(next(list_iter))  # Output: 2
print(next(list_iter))  # Output: 3


5. len()
The len() function returns the length (number of items) of an object.


# Length of a list
my_list = [1, 2, 3, 4]
print(len(my_list))  # Output: 4

# Length of a string
my_string = "Hello"
print(len(my_string))  # Output:

6. list()
The list() function creates a list from an iterable.


# From a string
str_to_list = list("hello")  # Converts string to list of characters
print(str_to_list)  # Output: ['h', 'e', 'l', 'l', 'o']

# From a tuple
tuple_to_list = list((1, 2, 3))
print(tuple_to_list)  # Output: [1, 2, 3]


7. locals()
The locals() function returns a dictionary of the current local symbol table.


def my_function():
    a = 10
    b = 20
    local_vars = locals()  # Get local variables
    print(local_vars)  # Output: {'a': 10, 'b': 20}

my_function()
8. map()
The map() function applies a function to all items in an iterable and returns an iterator.


# Function to apply
def square(x):
    return x * x

# Iterable
numbers = [1, 2, 3, 4]

# Using map
squared_numbers = map(square, numbers)

# Convert map object to list
print(list(squared_numbers))  # Output: [1, 4, 9, 16]

