# %% xarg, multiply arguments (x), using *, it is a tuple


def multiply(*numbers):
    print(numbers)  # extra line
    total = 1
    for number in numbers:
        print(number)  # extra line
        total *= number
        return total


print("start")
print(multiply(2, 3, 1))
# %%
