# Casting in python is done using constructor function

# int()
# float()
# str()


x = 1
y = 2.8
z = "3"

print(type(x), x)
print(type(y), y)
print(type(z), z)

x = int(x)  # int to int
y = int(y)  # float to int
z = int(z)  # string to int
print('')
print('casting to int.......')
print(type(x), x)
print(type(y), y)
print(type(z), z)

# floats
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.6")
print('')
print('casting to float.......')
print(type(x), x)
print(type(y), y)
print(type(z), z)
print(type(w), w)


x = str(1)
y = str(2.8)
z = str("3")
w = str("4.6")
print('')
print('casting to string.......')
print(type(x), x)
print(type(y), y)
print(type(z), z)
print(type(w), w)
