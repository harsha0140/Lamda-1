class Person(object):

    def __init__(self, first, last, age):
        self._firstname = first
        self._lastname = last
        self._age = age

    """
    # Getter method
    def Name(self):
        return self._firstname + " " + self._lastname
    """

    # Generate a `string casting` for our classes and we can simply print out instances. This makes a leaner design.
    def __str__(self):
        return self._firstname + " " + self._lastname + ", " + str(self._age)


# Employee inherits from Person
class Employee(Person):

    def __init__(self, first, last, age, staffnum):
        # The __init__methof of Person class is explicitly invoked.
        # Person.__init__(self, first, last)
        # Instead we can use super instead.
        super(Employee, self).__init__(first, last, age)
        self._staffnum = staffnum

    """
    def GetEmployee(self):
        return self.Name() + ", " + self._staffnum
    """
    """
    def __str__(self):
        return self._firstname + " " + self._lastname + ", " + self._staffnum
    """

    # Method `Overriding` is an object-oriented programming feature that allows a subclass to provide a different implemetation of a method that is already defined by its superclass or by one of its superclasses. The implementation in the subclass overrides the implementation of the superclass by providing a method with the same name, same parameters or signature, and same return type as the method of the parent class.

    # `Overloading` is the ability to define the same method, with the same name but with a different number of arguments and types. It's the ability of one function to perform different tasks, depending on the number of parameters or the types of the parameters.
    def __str__(self):
        return super(Employee, self).__str__() + ", " + self._staffnum

x = Person("Marge", "Simpson", 28)
y = Employee("Homer", "Simpson", 36, "1007")

print(x)
print(y)

# print(x.Name())
# print(y.GetEmployee())