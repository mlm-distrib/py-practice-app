
# print by index
a = "Hello, World"
print(a[1])

# index with range
print(a[2:5])

# strip() removed whitespace from Begin & End
b = "           Hello, World              "
print(b.strip())

# len() get length of the string
print(len(a))

# lower() for string lower case and upper() for upper case
print(a.lower())
print(a.upper())

# replace() method for string replace
print(a.replace('l', 'k'))

# split() method splits string to substrings
print(a.split(','))

# command-line string input
print("Enter your name")
x = input()
print("Hello, ", x)
