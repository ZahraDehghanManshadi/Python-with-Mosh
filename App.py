# %%
age = 22
if 18 <= age < 65:
    print("Eligible")
# %%
age = 25
if 18 <= age < 30:
    print("university student")
else:
    print("no")

# %%
age = 23
message = "university student" if 18 <= age < 30 else "no"
print(message)
# %%
for number in range(3):
    print("sending a message", number + 1, (number + 1) * ".")
for number in range(1, 4):
    print("sending a message", number + 1, (number + 1) * ".")
for number in range(1, 10, 2):
    print("sending a message", number + 1, (number + 1) * ".")
# %% For..Else
successful = 0  # change 0 or 1
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
# %% Nested Loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
# %% Iterables nosqa
print(type(5))
print(type(range(5)))
for i in [1, 2, 4]:
    print(i)
for i in "python":
    print(i)
# range, list and string are iterable objects
# %% While
command = ""
# if the user types andy kind of quit it stops the program: QUIT, Quit , ...
while command.lower() != "quit":
    command = input(">")
    print("Echo", command)

# %% Infinite Loops
while True:
    command = input(">")
    print("Echo", command)
    if command.lower() == "quit":
        break
# %%
count = 0
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        count += 1
print(f"There are {count} even numbers between 1 and 10")

# %% Task func.


def greet(first, last):  # Not Optional Arguments
    print(f"Hi there {first} {last}")


greet("Zah", "Deh")
# %% Return func.


def get_greeting(name):
    return f"Hi{name}"


message = get_greeting("Zah")
file = open("content.txt", "w")
file.write(message)
# %% Using "Keyword Arguments" When Calling a Function


def increment(number, by):
    return number + by


print(increment(4, by=1))  # we can write "by =" to make code more readable

# %% Default Arguments can be optional, they come after required parameters


def increment(number, by=1):
    return number + by


print(increment(2))  # 3
print(increment(2, 5))  # 7

# %% xarg, multiply arguments (x), using *, it is a tuple


def multiply(*numbers):
    print(numbers)  # extra line
    total = 1
    for number in numbers:
        print(number)  # extra line
        total *= number
    return total


print("start")
print(multiply(2, 3, 7, 6))

# %% xxarg, used to define dictionaries


def save_user(**user):
    print(user)


save_user(id=1, name="john", age=22)

# %% scope, local vs global
message = "a"


def greet(name):
    global message  # better avoid defining a global variable in a function
    message = "b"


greet("Mosh")
print(message)
# %% Shortcuts:
# Fn + End: move cursor to the end of the line
# Fn + Home: move cursor to the beginning of the line
# ctrl + Fn + End: move cursor to the end of the file
# ctrl + Fn + Home: move cursor to the beginning of the file
# Alt + Up and Down arrows: move selected lines up and down
# Alt + Shift + Down arrow: Duplicates selected lines
# ctrl + /: Comment and uncomment selected lines
# Type a few letters from beginning of a command or any letters just in sequence: Autocompletes commands
# ctrl + F2: change all similar words to a new word
# ctrl + k   Ctrl + 0 : fold
# ctrl + k   ctrl + j : unfold


# %%


def fizz_buzz(input):
    if input % 15 == 0:
        return 'FizzBuzz'
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(15))
print(fizz_buzz(8))
print(fizz_buzz(9))
print(fizz_buzz(10))

# %% Section 4: DATA STRUCTURES

# %% Lists
letters = ["a", "b", "c"]
matrix = [[1, 2], [3, 4]]
zeros = [0]*5
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World")
print(chars)
print(len(chars))
# %% Accessing items
letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters[0:3])
print(letters)


numbers = list(range(20))
print(numbers)
print(numbers[::2])  # فقط اعداد زوج را چاپ میکند
print(numbers[::-1])  # ترتیب چاپ را برعکس میکند
# %% List Unpacking
numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]
# a better way: unpacking lists
first, second, third = numbers  # باید تعداد رعایت شود.
# packing lists: درصورتی که تعداد اجزای لیست بیشتر باشد، می توان از * استفاده کرد.
first, *others = numbers
print(first)
print(others)
# like here:
# def multiply(*numbers):
# *numbers is a pack of parameters combined to a list

# %%
# if we care only about first and last items:
numbers = [1, 4, 4, 4, 6]
first, *others, last = numbers
print(first, last)
print(others)


# %%
