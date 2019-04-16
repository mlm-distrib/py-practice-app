# if - elif - else statement

a = 200
b = 100

if b > a:
    print(b, 'is greated than', a)
elif a == b:
    print(a, 'is equal to', b)
else:
    print(a, 'is greated than', b)

# one line if statement
if a > b:
    print('one line if statement')


# short hand if
print('b is greater') if a < b else print('a is greater')
