# %% 8- MODULES
# 1- calling a module
from ecommerce.shopping import sale
import sys
from ecommerce.shopping.sale import calc_shipping, calc_shipp
import ecommerce.shopping.sale as sale
sale.calc_shipping()
sale.calc_shipp()
# %%
# or calling the module this way:
# ..... from ecommerce.sale import calc_shipping, calc_shipp
calc_shipping()
calc_shipp()


# %%
# ..... import sys
# 2- pycache folder is the compiled version of modules we use in entry (main) file
# 3- Module Search Path (when module is in another directory)
# all of the directories that it searches to find the modules we are callig
print(sys.path)
# %%
# 4- Packages
# ordering sub-directories (like ecommerce)
# if we add __init__.py to the folder, it becomes a package (container of some modules)

# 5- Sub-packeges (folders in packages)
# They need __init__.py , too

# %%
# 6- Intra-package Referencing (see sale.py module)

# 7- The "dir" function
print(dir(sale))  # shows every method and function in sale
print(sale.__name__)  # ecommerce.shopping.sale
print(sale.__package__)  # ecommerce.shopping
print(sale.__file__)  # path to this file

# %%
# 8- Executing Modules as Scripts
# to quickly access the other files:press "ctrl + p"
# write commands in modules (other than functions, variables, ...)
# %%
