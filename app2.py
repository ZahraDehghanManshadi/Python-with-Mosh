# %% Dictionaries : Like lists, but indices are names (keys) instead of numbers (in lists)
from pprint import pprint
from sys import getsizeof
from sys
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)  # same thing with a better syntax
# dict()
# list()
# tuple()
# set()

point["x"] = 10  # modify
point["z"] = 20  # add
print(point)

# %% if a key does not exist:
# print(point["a"]) # an error occurs

# solution 1: using if
if "a" in point:
    print(point["a"])  # else prints nothing

# solution 2: get func
print(point.get("a"))  # else returns "None"
print(point.get("a", 0))  # else returns "0"

# delete an item
del point["x"]
print(point)
# %% Loop over Dictionaries
point = dict(x=1, y=2, z=20)

# only keys
for x in point:  # returns keys
    print(x)

for key in point:
    print(key, point[key])


# keys and values
print(point.items())  # dict.items() is an iterative variable
for x in point.items():  # keys and values
    print(x)

# unpacking dicts:
for key, value in point.items():
    print(key, value)
# %% Dictionary Comprehension
values = []
for x in range(5):
    values.append(x*2)
print(values)

# doing the same thing with lists comprehension:
#[expression for item in items]
values_list = [x*2 for x in range(5)]
print(values_list)

# for sets we replace [] with {}
values_set = {x*2 for x in range(5)}
print(values_set)

# for dictionaries: dict = {key:value for item in items}
values_dict = {x: x * 2 for x in range(5)}
print(values_dict)

# %% Generator Object (minimum use of memory, for very large data)
values = [x*2 for x in range(10)]  # this is a list
for x in values:
    print(x)

# To convert a list to a generator expression: We use () instead of []
values = (x*2 for x in range(10))
print(values)  # values is a generator object, it is iterable and it can not be printed
for x in values:
    print(x)

# %% Using generator objects leads much less memory consumption

 # to see the occupied memory size of an object:
values = (x*2 for x in range(1000))
print("memory size of gen1:", getsizeof(values))

values = (x*2 for x in range(100000))
print("memory size of gen2:", getsizeof(values))

values = [x*2 for x in range(100000)]
print("memory size of list2;", getsizeof(values))
# %% Unpacking Operator (unpacks any iritable): [an "*" before variable's name] passes the arbitrary arguments to functions
numbers = [1, 2, 3]
print("list:", numbers)
# what if we do not want [, ,]? like:
print("simple print:", 1, 2, 3)

# solution:
print("unpacking operator:", *numbers)

# another application of unpacking operator: Creating Lists
list = [*range(5), *"HelloWorld"]
print(list)
# another example
first = [1, 2, 3]
second = [4, 5]
mix = [*first, *second, "g", *"kitty"]
print(mix)
# Unpack Dictionaries with {} and **
first = {"x": 1, "y": 2}
second = {"y": 20, "z": 30}  # first "y" will be deleted
combined = {**first, **second, "z": 400}  # unpack dics with {**}
print(combined)

# %% Exercise : find the most repeated character
sentence = "This is a common interview question"
char_count = {}
for ch in sentence:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1
print(char_count)

# %%
# to print more pretty, we import pprint func
pprint(char_count, width=1)

# dictionaries like sets are not ordered objects -> we put items in a list of tuples to sort them
print(char_count.items())  # we use items() to convert a dic to a list of tuples
sorted_char_count = sorted(
    char_count.items(),
    key=lambda kv: kv[1],
    reverse=True)
print(sorted_char_count)
print(f"The answer is {sorted_char_count [0]}")

# %%
