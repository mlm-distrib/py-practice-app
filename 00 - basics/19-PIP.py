# Before you import install camelcase package
# command to install => pip install camelcase

import camelcase

c = camelcase.CamelCase()

txt = "my name is evelyn junelle"

print(c.hump(txt))
