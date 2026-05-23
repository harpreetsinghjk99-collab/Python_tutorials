# Built-in Data Types
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:
# Text Type:      str
# Numeric Types:  int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type:   dict
# Set Types:      set, frozenset
# Boolean Type:   bool
# Binary Types:   bytes, bytearray, memoryview
# None Type:      NoneType

# Getting the Data Type
# You can get the data type of any object by using the type() function:
x = 5
print(type(x))

# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:
x_str = "Hello World" # str
x_int = 20 # int
x_float = 20.5 # float
x_complex = 1j # complex
x_list = ["apple", "banana", "cherry"] # list
x_tuple = ("apple", "banana", "cherry") # tuple
x_range = range(6) # range
x_dict = {"name" : "John", "age" : 36} # dict
x_set = {"apple", "banana", "cherry"} # set
x_frozenset = frozenset({"apple", "banana", "cherry"}) # frozenset
x_bool = True # bool
x_bytes = b"Hello" # bytes
x_bytearray = bytearray(5) # bytearray
x_memoryview = memoryview(bytes(5)) # memoryview
x_none = None # NoneType

print(type(x_str))
print(type(x_int))
print(type(x_float))
print(type(x_complex))
print(type(x_list))
print(type(x_tuple))
print(type(x_range))
print(type(x_dict))
print(type(x_set))
print(type(x_frozenset))
print(type(x_bool))
print(type(x_bytes))
print(type(x_bytearray))
print(type(x_memoryview))
print(type(x_none))

# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:
x_str_c = str("Hello World")
x_int_c = int(20)
x_float_c = float(20.5)
x_complex_c = complex(1j)
x_list_c = list(("apple", "banana", "cherry"))
x_tuple_c = tuple(("apple", "banana", "cherry"))
x_range_c = range(6)
x_dict_c = dict(name="John", age=36)
x_set_c = set(("apple", "banana", "cherry"))
x_frozenset_c = frozenset(("apple", "banana", "cherry"))
x_bool_c = bool(5)
x_bytes_c = bytes(5)
x_bytearray_c = bytearray(5)
x_memoryview_c = memoryview(bytes(5))
