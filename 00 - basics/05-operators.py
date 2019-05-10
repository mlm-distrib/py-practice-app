# Operators
# Arithmetic operators
x = 10
y = 5

print('#### Arithmetic ####')
print('addition   :', x+y)
print('subtraction:', x-y)
print('multiply   :', x*y)
print('division   :', x/y)
print('modulus    :', x % y)
print('exponential:', x**y)
print('floor division:', x//y)
print('')
# Assignment operators
x = 15
print('### Assignment operators')
x += 3
print('+= operator:', x)
x -= 3
print('-= operator:', x)
x *= 3
print('*= operator:', x)
x /= 3
print('/= operator:', x)
x %= 3
print('%= operator:', x)
x //= 3
print('//= operator:', x)
x **= 3
print('**= operator:', x)
x = 5
x &= 3
print('&= operator:', x)
x = 5
x |= 3
print('|= operator:', x)
x = 5
x ^= 3
print('^= operator:', x)
print('')
# Comparison operators
print('### Comparison operators')
x = 4
y = 4
if x == y:
    print(x, y, '== operator: are equal')

y = 5
if x != y:
    print(x, y, '!= operator: are not equal')

if y > x:
    print(x, y, '> operator: y greater than x')

if x < y:
    print(x, y, '< operator: x lesser than y')

y = 4
if x >= y:
    print(x, y, '>= operator: x greater than or equal to y')

if x <= y:
    print(x, y, '<= operator: x lesser than or equal to y')
print('')
# Logical operators
print('### Logical operators')
y = 5
if x < y and y > 4:
    print(x, y, 'and operator: x less than y and y greater than 4')

if x == y or y > 4:
    print(x, y, 'or operator: x equals y or y greater than 4')

if not(x >= y and y > 5):
    print(x, y, 'not operator: x greater than y and y greater than 5')
print('')
# Identity operators
print('### Identity operators')
y = 4
if x is y:
    print(x, y, 'is operator: return true when x, y variables are same ')
y = 5
if x is not y:
    print(x, y, 'is not operator: return true when x, y variables are not same ')
print('')
# Membership operators
print('### Membership operators')
a = ['apple', 'banana', 'mango', 'grapes']
b = 'mango'
if b in a:
    print('in operator    : ', b, 'is available in the array', a)
b = 'orange'
if b not in a:
    print('not in operator: ', b, 'is not available in the array', a)
print('')
# Bitwise operators
print('### Bitwise operators')
a = 60
b = 13
c = 0

c = a & b
print(a, b, '& operator: Value of c is: ', c)
c = a | b
print(a, b, '| operator: Value of c is: ', c)
c = a ^ b
print(a, b, '^ operator: Value of c is: ', c)
c = ~ a
print(a, b, '~ operator: Value of c is: ', c)
c = a << 2
print(a, b, '<< operator: Value of c is: ', c)
c = a >> 2
print(a, b, '>> operator: Value of c is: ', c)
