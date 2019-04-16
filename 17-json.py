import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# JSON string, you can parse it by using the json.loads() method
y = json.loads(x)

print(y.keys())
print(y['city'])

# Convert from Python to JSON

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)

print(y)

# Convert Python objects into JSON strings

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
