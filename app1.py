# %% looping over lists
from array import array
from collections import deque
Word = ["a", "b", "c"]
for letter in Word:
    print(letter)

# %% enumerate functions returns a tuple of item's index and its value
Word = ["a", "b", "c"]
for letter in enumerate(Word):
    print(letter)
    print(letter[0], letter[1])


# a better way: by tuple (just like lists) unpacking, by using () instead of []
Word = ["a", "b", "c"]
items = (0, "a")  # tuple: () instead of []
index, letter = items  # unpacking tuple
for index, letter in enumerate(Word):
    print(index, letter)
# %% Add an item to the list
# Add
letters = ["a", "b", "c"]
letters.append("d")  # end of the list
letters.insert(0, "-")
print(letters)
# Remove
letters.pop()  # the last
print(letters)

letters.pop(0)  # with index
print(letters)

letters.remove("b")  # removes the first "b" in the list
print(letters)

# delete a range of a statement
letters = ["a", "b", "c", "d", "e"]
del letters[0:3]
print(letters)

# clear all the list
letters.clear()
print(letters)

# %% Finding iterms
letters = ["a", "b", "c"]
print(letters.index("c"))

# if the object doesn't exist in the list, an error occurs
# to prevent the error we use if
if "d" in letters:
    print(letters.index("d"))

# we use the "count() func." to count the number of an item in a list
print(letters.count("d"))
# %% Sorting lists
numbers = [3, 51, 2, 7, 9]
numbers.sort()  # sorts numbers, changes main list
numbers.sort(reverse=True)

# %% sorting without overwriting the main list
numbers = [3, 51, 2, 7, 9]
print(sorted(numbers))  # makes a "new list" that is sorted
print(numbers)  # main list
print(sorted(numbers, reverse=True))
# %% Sorting tuples
items = [           # (product, price)
    ("P1", 10),
    ("p2", 9),
    ("p3", 13)
]
items.sort()  # doesnt work, so we def a func


def sort_item_by(item):  # مقداری که قراره بر اساسش سرت کنیم میده. اینجا= قیمت که ایندکس 1 هست
    return item[1]


items.sort(key=sort_item_by)
print(items)
# %% Lambda Functions: lambda parameters:expression

items = [           # (product, price)
    ("P1", 10),
    ("p2", 9),
    ("p3", 13)
]

items.sort(key=lambda item: item[1])
print(items)
# %% Map Function: takes a function and an iterable

items = [           # (product, price)
    ("P1", 10),
    ("p2", 9),
    ("p3", 13)
]
prices = []
for item in items:
    prices.append(item[1])
print(prices)

# a better way, is using map func:
prices = []
prices = list(map(lambda item: item[1], items))
print(prices)
# %% Filter Function (like map func. takes a function (with a logical value) and an iterable)
items = [           # (product, price)
    ("P1", 10),
    ("p2", 9),
    ("p3", 13)
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
# %% List Comprehensions instead of map or filter  [expression for i in I] or [expression1 for i in I if expression2]
items = [           # (product, price)
    ("P1", 10),
    ("p2", 9),
    ("p3", 13)
]

prices = list(map(lambda item: item[1], items))
# List Comprehension = [expression for item in items]
prices = [item[1] for item in items]
print(prices)


filtered = (list(filter(lambda item: item[1] >= 10, items)))
filtered = [item for item in items if item[1] >= 10]
print(filtered)

# %% Zip func: combine 2 lists as a tuple
# convert list1=[1, 2, 3] and list2=[10, 20, 30]
# like this: combined=[(1,10), (2,20), (3,30)]

list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip(list1, list2)))
print(list(zip("abc", list1, list2)))

# %% Stack (Last In First Out - LIFO)
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
# print(last)
# print(browsing_session)
if browsing_session:
    print("redirect", browsing_session[-1])
else:
    print("no more options")
# %% Swap in Python
x = 10
y = 11
x, y = y, x  # because we are assigning a tuple and unpacking it
print(f"x = {x}, y = {y}")
a, b = 1, 2
# %% Set : a collection with no duplicates. مجموعه
# sets are unordered, without indices, unlike lists and ...
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)
# define a set with {}, add, remove and len
second = {1, 4}
second.add(5)
second.remove(1)
print(second)
len(second)

# operators on sets اجتماع- اشتراک- تفریق و اجتماع اختصاصی
first = {1, 2, 3, 4}
second = {1, 5}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)  # exclusive or


# %% Queues (FIFO): we need to define a deque to use queue
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")

# %% Tuples : a read only list, can not add, remove, modify
# used to prevent accidental changes to variables
point = (1, 2)
point = 1, 2  # like the line above
point = (1, 2) + (3, 4)
point = (1, 2) * 3
# convert a list to a tuple
point = tuple("Hello World")
point = tuple([1, 2, 3])
# point[0:2]  # tuples are ordered
x, y, z = point
if 10 in point:
    print("exists")

# %% Arrays take less amount of memory and perform faster than lists
# all objects must have the same type like signed int
# first parameter is a type code :"i" for a signed integer
numbers = array("i", [1, 2, 3])
numbers.pop()
numbers.remove(1)
# impossible to chage object's type like: numbers[0] = 1.2

# %%
