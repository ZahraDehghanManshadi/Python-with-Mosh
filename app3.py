# %% Exceptoins: Terminates execution of a program
from timeit import timeit
numbers = [1, 2]
print(numbers[3])  # IndexError: list index out of range

# %%
age = int(input("Age: "))  # if input = a -> ValueError
# %% Handling the exceptions -> so that the program does not crash while executing
# Solution:
try:
    age = int(input("Age: "))
except ValueError:  # or "except ValueError as ex:"
    print("You didn't enter a valid age.")
    # print(ex, type(ex)) ..... ex: shows the false input & type(ex): is ValueError
else:  # optional, executes if no exceptions happen
    print("No exceptions were thrown.")

# %% more than one Exceptions:
try:
    age = int(input("Age: "))
    xfactor = 10 / age  # new line
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:  # new exception
    print("Age cannot be 0.")
else:
    print("No exceptions were thrown.")


# %% if the action for several errors was similar:
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):  # Several errors
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")

# %% Cleaning Up: Releasing external resources (like files) so that others programs can open them
# we do that using "finally:" it executes anyway (wether an exception happens or not)

try:
    file = open("app1.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):  # Several errors
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    file.close()

# %% Except Block:
try:
    ...
except ValueError:  # or other error(s):
    ...
else:  # executes if no exceptions occur
    ...
finally:  # executes anyway, to release external resources (files)
    ...
# %% Release external resources without finally
# The "with ... as" Statement automatically releases resources by calling close() func.

try:
    with open("app1.py") as file:
        # instead of open, we use with ... as -> we don't need finally clause to release resources
        # calling a file by with statememnt, automatically calls file.__exit
        print("File opened.")

    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):  # Several errors
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")

# %% Raising (throwing) Exceptions
# it is not recommended to raise an exception as it is costly.


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

# %% Cost of Raising Exceptions: execution time is high
code1 = """
def calculate_xfactor1(age):
    if age <= 0:
        raise ValueError("Error: Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor1(-1)
except ValueError as error:
    pass
"""

# a better solution for previous problem, without raising an exception
code2 = """
def calculate_xfactor1(age):
    if age <= 0:
       return None
    return 10 / age

x_factor = calculate_xfactor1(-1)
if x_factor == None:
    pass
"""
print("time of code 1: ", timeit(code1, number=10000))
print("time of code 2: ", timeit(code2, number=10000))

# if the iterations are not a lot, we may raise exceptions if we really have to
