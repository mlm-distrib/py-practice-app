import re

txt = "This is a string message"
x = re.search("^This.*message$", txt)
if x:
    print('Matched')
else:
    print('Not matched')


y = re.findall('is', txt)
print('total match count', len(y))

y = re.search(r"\s", txt)
print('first whitespace starts at', y.start())

y = re.split(r"\s", txt)
print(y)
# find replace
y = re.sub(r'\s', '-', txt)
print(y)

# find replace by count
y = re.sub('-', '_', y, 2)
print(y)
