

abs() - Returns the absolute value of a number.


number = -7
result = abs(number)
print(result)  # Output: 7


all() - Returns True if all elements in an iterable are true.


values = [True, True, True]
result = all(values)
print(result)  # Output: True

values = [True, False, True]
result = all(values)
print(result)  # Output: False


any() - Returns True if any element of an iterable is true.


values = [False, False, True]
result = any(values)
print(result)  # Output: True

values = [False, False, False]
result = any(values)
print(result)  # Output: False


ascii() - Returns a string containing a printable representation of an object, but with non-ASCII characters escaped.


text = 'Hello,'
result = ascii(text)
print(result)  # Output: 'Hello, \u4e16\u754c'
bin() - Converts an integer to a binary string.


number = 10
result = bin(number)
print(result)  # Output: '0b1010'


bool() - Converts a value to a boolean.


value = 0
result = bool(value)
print(result)  # Output: False

value = 1
result = bool(value)
print(result)  # Output: True


bytearray() - Returns a mutable array of bytes.


byte_arr = bytearray([65, 66, 67])
print(byte_arr)  # Output: bytearray(b'ABC')

byte_arr[0] = 90
print(byte_arr)  # Output: bytearray(b'ZBC')


bytes() - Returns an immutable bytes object.


byte_obj = bytes([65, 66, 67])
print(byte_obj)  # Output: b'ABC'

# byte_obj[0] = 90  # This would raise a TypeError because bytes objects are immutable




