# %% Python Standard Library


# %% 1- Path

from pathlib import Path

# %% How to make a path object
# To get rid of extra \ signs, we use raw string
Path("C:\\Program Files\\Microsoft")
# the same path with raw string:
Path(r"C:\Program Files\Microsoft")
# Relative paths:
Path("ecommerce\__init__.py")
# Combine paths:
Path() / Path("ecommerce")
# Combine a path and a string:
Path() / "ecommerce" / "__init__.py"
# home directory of a current user-> using home() method:
Path.home()

# %% Path Methods
from pathlib import Path
path = Path()
# path.exists()
# path.is_file()
# path.is_dir()
print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path = path.with_name("test.py")
# print(path)
# path = path.with_name(".txt")
# print(path)
# %%
