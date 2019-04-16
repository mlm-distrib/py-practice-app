

class my_class:
    x = 5


print(my_class)
y = my_class()
print(y.x)

# self parameter is a reference to the current instance of the class


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def mynamefunc(self):
        print('My name is', self.name)


p = person("Andy", "24")
print(p.name)
print(p.age)
print(p.mynamefunc())


# set value of age

p.age = "40"
# print(p.age)
# delete age
del p.age
# print(p.age)
# del object
del p


# inheritance
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    pass


class Teacher(Person):
    def __init__(self, firstname, lastname, joinyear):
        Person.__init__(self, firstname, lastname)
        self.joinedyear = joinyear
        # Use the Person class to create an object, and then execute the printname method:


print('## inheritance ')
x = Person("John", "Doe")
x.printname()

x = Student("Mike", "Tyson")
x.printname()

x = Teacher("Don", "Abraov", 2019)
x.printname()
print(x.joinedyear)
