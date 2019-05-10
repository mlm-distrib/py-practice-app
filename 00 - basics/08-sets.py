
# Set is a collection which is unordered and unindexed. No duplicate members.
myset = {"apple", "banana", "mango"}
print(myset)

for x in myset:
    print(x)
print('')
print('Is banana in myset?', "banana" in myset)

myset.add('orange')
print(myset)
myset.update(["pineapple", "orange", "grapes"])
print(myset)
print('length is', len(myset))
myset.remove("orange")
print(myset)
myset.discard("mango")
print(myset)
myset.pop()
print(myset)
myset.clear()
print(myset)
myset = set(("AAA", "BBB", "CCC"))
print(myset)
