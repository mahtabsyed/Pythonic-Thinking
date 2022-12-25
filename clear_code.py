# Positional arguments and indices are nice. Its convenient for computer.
# Keywords and names are better. This is how humans think.

# Clarify function calls with keyword arguments
# twitter_search("@obama", False, 20, True)
# twitter_search("@obama", retweets=False, numtweets=20, popular=True)

# Clarify multiple return values with named tuples
# doctest.testmod()
# (0, 4)

# doctest.testmod()
# TestResults = namedtuple("TestResults", ["failed", "attempted"])
# TestResults(failed=0, attempted=4)

# Named Tuple is a subclass of Tuple
from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple("Student", ["name", "age", "DOB"])

# Adding values
S = Student("Nandini", "19", "25/Jan/1997")

print(f"Student is {S}")
# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)
print("------")

# Unpacking sequences
# There are three basic sequence types: lists, tuples, and range objects
p = ["Raymond", "Hettinger", 0x30, "python@example.com"]
fname = p[0]
lname = p[1]
age = p[2]
email = p[3]
print("A way - ", fname, lname, age, email)
print("------")
fname, lname, age, email = p
print("Better way - ", fname, lname, age, email)
print("------")

# Tuple packing and unpacking
# Dont underestimate the advantages of updating state variables at the same time
# It elimintaes erros due to out of order updates
# It allows high-level thinking: chunking
