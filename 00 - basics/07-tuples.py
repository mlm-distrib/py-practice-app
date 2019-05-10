# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(mytuple[1])

for x in mytuple:
    print(x)

print('length: ', len(mytuple))
mytuple = tuple(('AAA', 'BBB', 'CCC', 'BBB'))
print(mytuple)
print('BBB apear', mytuple.count('BBB'), 'times')
print('Display index value of CCC is', mytuple.index('CCC'))
