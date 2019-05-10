

# Lamda function
# syntax: lambda arguments : expression

def x(a): return a + 10


def y(a, b): return a*b


print(x(5))
print(y(2, 4))

# use lambda as an anonymous function inside another function


def my_func(n):
    return lambda a: a * n


my_doubler = my_func(2)
my_tripler = my_func(3)
print('doubler =>', my_doubler(11))
print('tripler =>', my_tripler(11))
