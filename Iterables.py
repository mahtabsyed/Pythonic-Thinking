# Acknowledgements:
# Raymond Hettinger - https://www.youtube.com/watch?v=OSGv2VnC0go&ab_channel=NextDayVideo

# Replace traditional index manipulation with Pthon's core looping idioms
# Learn advanced techniques with for-else clauses and two argument form of iter()
# Improve your craftmanship and aim for clean, fast, idiomatic Python code

# for in python is not same as for in C, its houdl be called for each as it iterates over an iterable
# range in python 3 uses iterable
for i in range(5):
    print(i)

print("-----")

# Looping over a collection
colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)

print("-----")

# Loop backwards
for color in reversed(colors):
    print(color)

print("-----")

# Looping over a collection and indices
for i, color in enumerate(colors):
    print(i, "-->", colors[i])

print("-----")


# Looping over two collections, zip in python3 now returns an iterator
names = ["raymond", "rachel", "matthew"]
for name, color in zip(names, colors):
    print(name, "-->", color)

print("-----")

# Looping in sorted order
for color in sorted(colors):
    print(color)
print("-----")

for color in sorted(colors, reverse=True):
    print(color)

print("-----")


# Custom sort order
print(sorted(colors, key=len))
print("-----")
