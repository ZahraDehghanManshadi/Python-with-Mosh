# %%
# 9- PYTHON STANDARD LIBRARIES


# 2- Working with Paths

import json
import csv
from asyncore import read
from zipfile import ZipFile
import shutil
from time import ctime  # creation time
from pathlib import Path
# .... from pathlib import path
# %% Defining Paths:
# 1-
path = Path("C:\\Program Files\\Microsft")

# 2- using raw string --> only one back slash
path = Path(r"C:\Program Files\Microsoft")
# %%
# 3- current folder
path = Path()

# 4- relative referencing
path = Path("ecommerce/__init__.py")
# %%
# 5- combine paths and strings
path = Path() / Path("ecommerce")
path = Path() / "ecommerce" / "__init__."
# %%
# 6- home directory of the current user
path = Path.home()


# %% Working with Paths:

path = Path("ecommerce/__init__.py")
# %%
# path methods:
path.exists()
path.is_file()
path.is_dir()
# %%
# path attributes:
print(path.name)  # name with extention
print(path.stem)  # name without extention
print(path.suffix)  # only the extention
print(path.parent)  # the parent folder: ecommerce
# %%
# methods to create new paths (The file doesn't exist. We only create path):
new_path = path.with_name("new_file.txt")
print(new_path)  # relative value of this path
print(new_path.absolute())  # absolute value of this path
# .with_suffix: changes the file's suffix or extention
new_file = new_path.with_suffix(".py")
print(new_path)


# %% 3- Working with Directories

# ... from pathlib import Path
path = Path("ecommerce")
# iterdir() returns all the files and directories in this path
print(path.iterdir())
# as it is a generator object (iterative), we use for to iterate it:

for p in path.iterdir():
    print(p)

# a better way is to use list comprehension expression:
paths = [p for p in path.iterdir()]
print(paths)
# if we want to filter files, we only want to see directories:
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

# %%
# ... from pathlib import Path
path = Path("ecommerce")

# in the above method we can not search with a pattern or recursively, so we uses .glob():
# we only need files with the pattern "*.py" :
py_files = [p for p in path.glob("*.py")]
print(py_files)

# Recursive search: search in the current directory and all its children, using .rglob():
rec_py_files = [p for p in path.rglob("*.py")]
print(rec_py_files)
# another way for recursive search is using this pattern for glob:.glob("**/*.py")
rec_py_files = [p for p in path.glob("**/*.py")]
print(rec_py_files)

# %% 4- Working with Files

# ... from pathlib import Path
path = Path("ecommerce/__init__.py")

# path.exists()
# path.rename("init.txt")
# path.unlink() # deletes the file

print(path.stat())  # returns information ablut this file

# to see the time the way that is understood by human:
# .... from time import ctime # creation time
print(ctime(path.stat().st_ctime))  # it shows: Sun - 14 Aug ...

# content of the files:
path.read_bytes()  # returns content of the file as binary object
path.read_text()  # returns content of the filw as sting
# it is similar to "with open("__init__.py", "r")" as file:" . It also needs closing.
# write in the files:
# path.write_bytes(" ")
# path.write_text(" ")

# %%
# copy a file to a different location
# ... from pathlib import Path

source = Path("ecommerce/__init__.py")
target = Path()/"__init__.py"

target.write_text(source.read_text())
# it is tidious --> we import shutil module:

# ... import shutil
shutil.copy(source, target)

# this way is cleaner and easier than using a path object


#  %% 5- Working with Zip-Files
# ... from pathlib import Path
# ... from zipfile import ZipFile
# w for write   # Doesn't need close. (as we used "with... as zip")
with ZipFile("ecommerce.zip", "w") as zip:
    # searches recursively for all children of ecommerce
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)  # write all these paths to zip

with ZipFile("ecommerce.zip") as zip:  # Don't want to write --> no "w"
    print(zip.namelist())
    info = zip.getinfo("ecommerce/__init__.py")  # information about a file
    print(info.file_size)  # real size
    print(info.compress_size)  # size after compression
    # makes the extract filder of this zip with name "extract"
    zip.extractall("ecommerce_extract")

# %% 6- Working with CSV-Files
# ... import csv

# make and write in a csv-file using a csv.writer
with open("data.csv", "w") as file:
    writer = csv.writer(file)  # needs file as input, can't accept path
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow(["1000", "a", "5"])
    writer.writerow(["1001", "b", "10"])

# read a csv-file using a csv.reader
with open("data.csv") as file:
    reader = csv.reader(file)  # needs file as input, can't accept path
    # print(list(reader))
    for row in reader:  # reader is an iterative object
        print(row)


# %% 7- Working with JSON Files

# making and writing in json files
# ... import json

# ... from pathlib import Path

movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Kindergarten Cop", "year": 1993}
]

data = json.dumps(movies)
print(data)
Path("movies.json").write_text(data)

# %% reading data from json-files

# ... import json

# ... from pathlib import Path

# jaon_data is a string that includes data from movies
json_data = Path("movies.json").read_text()
print(json_data)
# making an array of dictionaries from this string:
movies = json.loads(json_data)
print(movies)

# now python considers this data as an array of dictionaries, and we can access all items by indexing
print(movies[0])
print(movies[0]["title"])
# %%
