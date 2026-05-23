# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
print("Hello")
print('Hello')

# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assign String to a Variable
a = "Hello"
print(a)

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of unicode characters.
# Square brackets can be used to access elements of the string.
a = "Hello, World!"
print("Character at position 1:", a[1])

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
print("Looping through 'banana':")
for x in "banana":
  print(x)

# String Length
# To get the length of a string, use the len() function.
a = "Hello, World!"
print("Length of string:", len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("Is 'free' in txt?", "free" in txt)

# Use it in an if statement:
if "free" in txt:
  print("Yes, 'free' is present.")

# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("Is 'expensive' not in txt?", "expensive" not in txt)

# Use it in an if statement:
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
