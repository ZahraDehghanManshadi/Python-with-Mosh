# %% Creating Modules
# we made a new file (sales) and we want to import some functions from sales
from sales import calc_shipping

# first way:
import sales
sales.calc_shipping
print("1")

# %%
# another way:
# from sales import calc_shipping
calc_shipping()
print("2")

# %%
