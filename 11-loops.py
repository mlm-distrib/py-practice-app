
# There are two primitive loop commands
# while loop
# for loop

print('##### While loop ######')

i = 1
while i < 6:
    print(i)
    i += 1

print('##### while with break at 3')

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print('##### while with continue at 4')

i = 0
while i < 6:
    i += 1
    if i == 4:
        continue
    print(i)


print('##### For loop ######')

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string
print('# iterate list')
fruits = ['apple', 'banana', 'mango', 'orange']

for fruit in fruits:
    print('fruit:', fruit)
print('# iterate string')
a = 'banana'
for x in a:
    print(x)
print('# break when fruit is mango')
for fruit in fruits:
    print('fruit:', fruit)
    if fruit == 'mango':
        break

print('# break when fruit is mango')
for fruit in fruits:
    if fruit == 'mango':
        break
    print('fruit:', fruit)

print('using range()')
for i in range(6):
    print(i)

print('using range(x,y) ~ starts from x but ends at y ~ 0 is the index')
for i in range(2, 6):
    print(i)

print('using range(x, y, increament) ~ where incremental sequence is 2')
for i in range(1, 10, 2):
    print(i)


print('else in for loop')
for i in range(6):
    print(i)
else:
    print('Finished Finally!')

print('nested for loop')
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
for x in adj:
    for y in fruits:
        print(x, y)
