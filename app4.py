# %% CLASSES
# Class: A blueprint for creating new objects (Human)
# Objects: An instance of a class (John, David, Elena, ...)


class Point:
    # Class attribute is shared among all objects of this class, we can change it from outside the class def, too
    default_color = "Red"

    def __init__(self, x, y):  # Instance method needs a specific object
        self.x = x
        self.y = y

    @classmethod      # decorator   # Class method does not need a specific object
    def zeros(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()
point.z = 3
point.draw()

point2 = Point(4, 5)
point2.draw()

print(point2.default_color)  # Calling a class attribute in an object level
print(Point.default_color)  # Calling a class attribute in a class level

point = Point(0, 0)
# instead we can use a class method :a method in class level, not an instance method
point = Point.zeros()
point.draw()

# %% Magic Methods (can search in web)
# __name__ : we do not directly call them, they execute automatically depending on how we use our objects and calasses
# built in magic method of __str__ does something and we want to iprove it in this class


class Point:

    def __init__(self, x, y):  # The constructor
        self.x = x
        self.y = y

    # New str magic method: so that if we print(point) we get a string like: (1, 2)
    def __str__(self):
        return f"({self.x}, {self.y})"
    # By default, "=="" checks the memory addresses. -> we use __eq__

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point)
# %% Compare Objects
point = Point(1, 2)
other = Point(3, 4)
if point == other:  # By default, "=="" checks the memory addresses. -> we use __eq__
    print("yes")
else:
    print("no")

if point > other:  # define __gt__
    print("point")
else:
    print("other")

print(point + other)  # It is a true and false expression --> answer: False or True


#                     A GREAT EXAMPLE

# %% Making Custom Container (a new data structure)


class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):  # tag is a key here
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()

# __add__ magic method
# normal dictionaries are case sensitive -> we want to take care of case sensitivity
cloud.add("Python")  # Python with upper case
cloud.add("python")  # python with lower case
cloud.add("C++")
print(cloud.tags)

# We can get an item by its key (the number of clouds with this tag (python))
# __getitem__ magic method is only for reading the value not chaging them
cloud["python"]

# __setitem__ magic method is used to change values
cloud["JavaScript"] = 3
print(cloud.tags)

# __len__ magic method , to see the num of items in an object
len(cloud)  # Because it is a container, we can get number of items in this container


# __iter__ magic method to iterate over item tags
for t in cloud.tags:
    print(cloud.tags[t])

# %% Private Members (of Attributes)


# to hide an attribute outside the class def block
# to exclude access to an attribute to a class def block
# we replace attributes name with __name, all over the class def block
# in this example: tags -->   __tags  (by putting the cursor on the word "tags" and pressing F2)
# as a result we don't have the access either to cloud.tags["PYTHON"] or to cloud.__tags["PYTHON"]


######################### the class changes to:#####################################################
# class TagCloud:
#     def __init__(self):
#         self.__tags = {}

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):  # tag is a key here
#         return self.__tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.__tags)

#     def __iter__(self):
#         return iter(self.__tags)

# Althogh this private member is still accessible from outside
# it shows all the attributes in this class. Here: {'_TagCloud__tags':{}}
print(TagCloud.__dict__)
# we can still access to this attributs with this name: "_TagCloud__tags"
# %% Properties
# when we need to have control over our attributes

# in this example, the price can be negative!


class Produ:
    def __init__(self, price):
        self.price = price

# but it is not desirable, so we define two methods, set and get :


class Produc:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


produc = Produc(-50)  # it raises an error correctly


# it works properly but it is messy -> we use propoerties
# Propertes sit infront of an attribute and allows us to get and set the value of that attribute
# %% example for properties

class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    price = property(get_price, set_price)


product = Product(10)
print(product.price)

# product.price = -2  # rises an error
# int(product.price)

# %%
# we can change get_price and set_price to private methods with adding: __
# but it is still messy. So we use another way to define our properties:
# we use a decorator: @propert for the first method, and chage its name to an ideal name like "price"
# then we use another decorator: @ for the second method and change its name to ""


class Product1:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):  # it will automatically make a property obj called price
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    # price = property(get_price, set_price)   # we don't need this line anymore


product = Product1(10)
print(product.price)

product = Product1(-10)  # It rises an error as we desire
print(product.price)


# %%
