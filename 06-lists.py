# There are Four collection data types
# List, Tuple, Set, Dictionary


# List is a collection which is ordered and changeable. Allows duplicate members.
mylist = ['apple', 'banana', 'mango', 'grape']
print('mylist = ', mylist)
print(mylist[1])
mylist[1] = 'orange'
print('mylist[1] = "orange"', mylist)
for x in mylist:
    print(x)

print('length: ', len(mylist))
mylist.append('banana')
print('append(banana) = ', mylist)
mylist.insert(1, 'xxxxx')
print('insert(1, xxxxx = ', mylist)
mylist.remove('xxxxx')
print('remove(xxxxx) = ', mylist)
mylist.pop()
print('pop() = ', mylist)
del mylist[3]
print('del mylist[3] = ', mylist)
mylist.clear()
print('mylist.clear() = ', mylist)
myNewlist = ['apple', 'banana', 'mango', 'grape']
mylist = myNewlist.copy()
print('mylist = myNewlist.copy()', mylist)
mylist.clear()
print('mylist = ', mylist)
mylist = list(myNewlist)
print('mylist = list(myNewlist) = ', mylist)

mylist.reverse()
print('mylist.reverse() = ', mylist)
mylist.sort()
print('mylist.sort() = ', mylist)
