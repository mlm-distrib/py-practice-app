# create functions using def keyword


def my_func():
    print('my function called')


def my_function(params="defaultParam"):
    print('my function called wih parameter', params)


def multiply_function(i=0, j=0):
    return i * j


def tri_recursion(k):
    if(k > 0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0

    return result


my_func()
my_function(["param1", "param2"])
my_function()
x = multiply_function(2, 5)
print(x)

print('## recursive functions')
tri_recursion(6)
