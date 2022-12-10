# %%
# Inheritance

# abc is module, ABC is class, abstractmethod is func
from collections import namedtuple
from abc import ABC, abstractmethod
from sys import ps2


class Animal:

    def __init__(self):
        self.age = 1

    # It does almost the same thing as the upper line. But they are different.
    # The upper line's value generates later: when an object is defined.
    # If we print(m.age), the answer will be 1.
    age = 6

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub


class Mammal(Animal):
    def walk(self):
        print("walk")


class fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(m.age)  # It -> prints "1".

# %% The Object Class: the parent for every class.
print(isinstance(m, Mammal))  # True
print(isinstance(m, Animal))  # True
print(isinstance(m, object))  # True
print(issubclass(Mammal, Animal))  # True
# %% Method Overriding: When we redefine a method in a child class, it replaces the method in the parent class (2 methods with the same name).
# We also can maintain the parent's method, by using "super().MethodName()"


class Animal1:

    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal1(Animal1):

    def __init__(self):    # We redefined __init__ in Animal with a new __init__ in Mammal

        # Here we can add super command to maintain parent's __init__ method features
        super().__init__()

        self.weight = 20   # So the age does not get value, instead the weight does

    def walk(self):
        print("walk")


m = Mammal1()
# without super().__init__() -> AttributeError: 'Mammal1' object has no attribute 'age'
print(m.age)
print(m.weight)  # -> 20

# What if we want to keep the parent __init__ method, and also add some features to it in child's __init__ method:
# We use the command super, "super().__init__()" in the child's __init__ method, to get access to the parent class


# %% Multi-level Inheritance: like Animal -> Bird -> Chicken
# Do not try to use it, because it adds complexity to your program. It can cause problems: Animal class(eat method) -> Bird class(fly method) -> Chicken class(a bird that does not fly!)
# %% Multiple Inheritance
# It also can make problems, and we probably should avoid it.

class Person:
    def greet(self):
        print("Greet Person")


class Employee:
    def greet(self):
        print("Greet Employee")


class Manager(Person, Employee):
    pass


# Which greet does it execute: the first class in paranthesis (Here: Person)
m = Manager()
m.greet()

# If we have two small classes that have certainly nothing in common, it can be OK to use them as multiple base classes
# The FlyFish class is a good example of Multiple Inheritance, Because the Flyer and Swimmer classes are small classes and they certainly have nothing in common


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass

# Multiple Inheritance:


class FlyingFish(Flyer, Swimmer):
    pass


# %% A Good Example of Inheritance


# we do not have a built in invalid operator error in python, so we build one:
class InvalidOperationError(Exception):  # always inherits from Exception class
    pass


class Stream:
    def __init__(self):
        self.opened = False  # opened Flag

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a stream.")


# %% Abstract Base Classes: 1- They are not ready to use (half-baked) they are just common codes to reuse in different classes.
# problem 1- We should not be able to make an instance of them.
# problem 2- We need independent read methods for each child class: read method is common in childs, with different actions and the same name. We should define read method in every other child of Stream class, independently.
# solution: using an ABC (Abstract Base Class)
# in previous example, we want to make Stream class an abstract base class.


# do it every time: we import:
# from abc import ABC, abstractmethod


class Stream1(ABC):
    def __init__(self):
        self.opened = False  # opened Flag

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    # We have different read methods in each child of Stream.
    @abstractmethod
    def read(self):
        pass


class FileStream1(Stream1):
    def read(self):
        print("Reading data from a file.")


class NetworkStream1(Stream1):
    def read(self):
        print("Reading data from a stream.")


class MemoryStream1(Stream1):
    # while we do not define read method, we can not instantiate (make an instance of) this class
    pass
    # So we define read, unless this class is also considered as an abstract class

    def read(self):
        print("Reading from memory.")

# problem 1 is solved
# sream = Stream()  # Instantiate Error: We can not make an instance of an abstract class


# %% Plymorphism is used to make UIs
# We can draw objects from deffernt classes, the specific way we want to draw that object, with the same command
# from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(control):  # a function to draw everything, no matter the type
    control.draw()  # calls draw method for whatever object control is, and it references to draw methods in deffernet classes according to the tye of object


ddl = DropDownList()
draw(ddl)

tb = TextBox()
draw(tb)


def draw_whatever(controls):
    for control in controls:
        control.draw()


draw_whatever([ddl, tb])  # This is the way we build UIs


# %% Duck Typing
# in the last example, we can even remove ABC (UIControl), as long as the draw method exists in both TextBox and DropDownList classes, they are considered as UIControls (a class with draw func)

class TextBox1():
    def draw(self):
        print("TextBox")


class DropDownList1():
    def draw(self):
        print("DropDownList")


def draw(control):  # a function to draw everything, no matter the type
    control.draw()  # calls draw method for whatever object control is, and it references to draw methods in deffernet classes according to the tye of object


ddl = DropDownList1()
draw(ddl)

tb = TextBox1()
draw(tb)


# %% Extending Built-in Types
class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text)
print(text.lower())  # str methods
print(text.duplicate())

# %%


class TrackableList(list):
    pass
    # Extending a method from the base class

    def append(self, objcet):
        print("Append Called")
        super().append(object)


tl = TrackableList()
tl.append("7")
print(tl)


# %% Data class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)

# without __eq__ metod:
print(p1 == p2)
# ->False because they are stored in 2 defferent loations in memory

# id: returns the memory address of a variable
print(id(p1))
print(id(p2))

#  %% Named Tuples instead of classes
# But redefining __eq__ and other methods like that is tedious
# A better way: When we have casses that have only data and no action, we might better use namedtuple instead of classes.
# Unlike regular tuples, named tuples have attributes: (print(p1.x)). But they are stil immutable. (can not be changed)
# Using named tuples instead of casses, we can simply compare p1 and p2, without defining methods,


# Always: from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)  # Use keys for clarity
p2 = Point(x=1, y=2)
print(p1 == p2)  # -> True

# attributes are accessible:
print(p1.x, p1.y)

# immutable
# p2.x = 10 #-> AttributeError: can't set attribute
# solution: defining new tuples
p1 = Point(x=10, y=2)
print(p1, p2)


# %% Creating Modules
