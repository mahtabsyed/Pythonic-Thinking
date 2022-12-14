d = {"matthew": "blue", "rachel": "green", "raymond": "red", "mahtab": "cyan"}

# Looping over dictionary keys
# Indices of a list are same as keys of a dictionary
for k in d:
    print(k)

print("------")
# If you wish to mutate a dictionary then you can loop over a copy of the keys
# https://bobbyhadz.com/blog/python-runtimeerror-dictionary-changed-size-during-iteration
for k in d.copy():
    if k.startswith("r"):
        d.pop(k, None)
print("------")

for k in d:
    print(k)

print("------")

# Looping over a dictionary keys and vakues
for k in d:
    print(k, "-->", d[k])
print("------")

# Better way
for k, v in d.items():
    print(k, "-->", v)
print("------")

# Construct a dictionary from pairs
country = ["France", "Australia", "USA"]
capital = ["Paris", "Canberra", "Washington DC"]
d = dict(zip(country, capital))
print(d)
print("------")

# Counting with dictionaries
# Simple way
colors = ["red", "green", "blue", "green", "blue", "green", "blue", "blue"]
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
print(d)
print("------")


# Better way
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1

print(d)
print("------")

# Modern way using defaultdict
from collections import defaultdict

d = defaultdict(int)
for color in colors:
    d[color] += 1
print(d)
print("------")

# Grouping with dictionaries
# Group by length of the names, or first char of a name
names = [
    "raymond",
    "rachel",
    "matthew",
    "roger",
    "betty",
    "melissa",
    "judith",
    "mahtab",
    "charlie",
    "chloe",
]

d = {}
for name in names:
    # Just change the key to group by other condition
    # key = len(name)
    key = name[0]
    # key = name[-1]
    if key not in d:
        d[key] = []
    d[key].append(name)

print(d)
print("------")

#  With d.setdefault
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)

print(d)
print("------")

#  With defaultdict
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)

print(d)
print("------")


# dictionary popitem() which is atomic (no locks needed between threads)
d = {"matthew": "blue", "rachel": "green", "raymond": "red", "mahtab": "cyan"}
# The popitem() method removes the item that was last inserted into the dictionary.
# In versions before 3.7, the popitem() method removes a random item.
# The removed item is the return value of the popitem() method, as a tuple
print("dict is now ", d)
while d:
    key, value = d.popitem()
    print(key, "-->", value)
print("dict is now ", d)
print("------")


# Linking dictionaries
# dictionary with default values
"""
defaults = {"color": "red", "user": "guest"}
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user")
parser.add_argument("-c", "--color")
namespace = parser.parse_args([])
command_line_args = {k: v for k, v in cars(namespace).items() if v}

d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)

# much better way
d = ChainMap(command_line_args, os.environ, defaults)
"""
