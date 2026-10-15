# 1. SINGLE INHERITANCE

class Parent:
    def func1(self):
        print("This function is in parent class.")


class Child(Parent):
    def func2(self):
        print("This function is in child class.")


# Creating an object
print(" SINGLE INHERITANCE ")

obj = Child()
obj.func1()
obj.func2()


# 2. MULTILEVEL INHERITANCE

class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

    # Getter
    def get_grandfathername(self):
        return self.grandfathername

    # Setter
    def set_grandfathername(self, name):
        self.grandfathername = name


class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        super().__init__(grandfathername)
        self.fathername = fathername

    # Getter
    def get_fathername(self):
        return self.fathername

    # Setter
    def set_fathername(self, name):
        self.fathername = name


class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        super().__init__(fathername, grandfathername)
        self.sonname = sonname

    # Getter
    def get_sonname(self):
        return self.sonname

    # Setter
    def set_sonname(self, name):
        self.sonname = name

    def print_name(self):
        print("Grandfather name:", self.get_grandfathername())
        print("Father name:", self.get_fathername())
        print("Son name:", self.get_sonname())


# Creating an object
print("\n MULTILEVEL INHERITANCE ")

s1 = Son("Prince", "Rampal", "Lal mani")

s1.print_name()

# Testing setter methods
print("\nAfter changing the names:")

s1.set_grandfathername("Ralph")
s1.set_fathername("Ronaldo")
s1.set_sonname("Miguel")

s1.print_name()


# 3. HIERARCHICAL INHERITANCE

class Parent2:
    def __init__(self, name):
        self.name = name

    # Getter
    def get_name(self):
        return self.name

    # Setter
    def set_name(self, name):
        self.name = name

    def func1(self):
        print("This function is in parent class.")


class Child1(Parent2):
    def func2(self):
        print("This function is in child 1.")


class Child2(Parent2):
    def func3(self):
        print("This function is in child 2.")


# Creating objects
print("\n HIERARCHICAL INHERITANCE ")

object1 = Child1("Child One")
object2 = Child2("Child Two")

# Calling methods from Child1
object1.func1()
object1.func2()
print("Name:", object1.get_name())

# Calling methods from Child2
object2.func1()
object2.func3()
print("Name:", object2.get_name())

# Testing a setter method
print("\nAfter changing Child1's name:")

object1.set_name("Angelo")
print("Name:", object1.get_name())
