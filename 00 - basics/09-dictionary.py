# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
mydict = {
    "brand": "Suzuki",
    "model": "Gixxer SF Fi ABS",
    "year": 2018
}
print(mydict)
x = mydict["model"]
print("mydict[key]:", x)

x = mydict.get("year")
print("mydict.get(key):", x)

mydict["year"] = 2017
print(mydict)

for x in mydict:
    print('key:', x, '- value', mydict[x])

if "model" in mydict:
    print("model present in mydict")

print('Length:', len(mydict))

mydict.pop("year")
print('pop year', mydict)

mydict["year"] = 2017
print('add new key year with value', mydict)

mydict.popitem()
print("mydict.popitem() removes last item", mydict)
