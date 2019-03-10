import re

line = "I love $"
m = re.findall("\\$", line, re.IGNORECASE)
print(m)

l = "The ghost that says boo haunts the loo"
m = re.findall(".*oo", l, re.IGNORECASE)
print(m)
