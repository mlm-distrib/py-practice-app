import datetime

x = datetime.datetime.now()
print(x)
print(x.year,  x.month, x.day)
print(x.strftime("%A"))

# create date object
x = datetime.datetime(2020, 5, 17)
print(x)

print(x.strftime("%B"))
