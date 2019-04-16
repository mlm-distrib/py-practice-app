import platform
import mymodule as mymod
from mymodule import person1

mymod.greetings("Paul")
a = mymod.person1["age"]
print(a)

## Built in modules

x = platform.system()
print(x)

x = dir(platform)
print(x)
print('')
print(person1.keys())
print(person1["name"])
