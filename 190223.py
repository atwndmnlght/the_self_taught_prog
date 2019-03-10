import re
line = "The ghost that says boo haunts tho loo"
m = re.findall(".oo", line, re.IGNORECASE)
print(m)

s = "h t t p s : / / p y p i . p y t h o n . o r g"
s = s.replace(" ", "",3)
print(s)
