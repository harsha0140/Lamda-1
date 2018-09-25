# https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python

"""
A Staticmethod is a method that knows nothing about the class or instance it was called on. It just gets the arguments that 
were passed, no implicit first argument. The functions could be wrtten into a basic module function instead of using 
staticmethod but it's a way of putting a function into a class (because it logically belongs there), while indicating that 
it does not require access to the class.
This function is nothing more than a function defined inside a class. It is callable without instantiating the class first. 
It's definition is immutable via inheritance.

A Classmethod, on the other hand, is a method that gets passed the class it was called on, or the class of the instance it 
was called on, as first argument. This is useful when you want the method to be a factory for the class: since it gets the 
actual class it was called on as first argument, you can always instantiate the right class, even when sunclasses are 
involved.
This function also callable without instantiating the class, but its definition follows Subclass, not Parent class, via 
inheritance. That's because the first argument for @classmethos function must always be cls (class).
"""

class A(object):
    def foo(self, x):
        print "executing foo(%s,%s)"%(self,x)
    
    @classmethod
    def class_foo(cls, x):
        print "executing class_foo(%s,%s)"%(cls,x)
    
    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x

a=A()

# Below is the usual way an object instance calls a method. The object instance, `a`, is implicitly passed as the first 
# argument.
print "a.foo(1): "
a.foo(1)
# executing foo(<__main__.A object at 0xb7dbef0c>,1)

# With classmethods, the class of the object instance is implicitly passed as the first argument instead of `self`.
print "a.class_foo(1): "
a.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)

# You can also call `class_foo` using the class. In fact, if you define something to be a classmethod, it is probably 
# because you intend to call it from the class rather than from a class instance.

# `A.foo(1)` would have raised a TypeError, but `A.class_foo(1)` works just fine.
print "A.class_foo(1): "
A.class_foo(1)
# executing class_foo(<class '__main__.A',1)

print "-" * 5, "staticmethod", "-" * 5

# With staticmethods, neither `self` (the object instance) nor `cls` (the class) is implicitly passed as the first 
# argument. They behave like plain functions except that you can call them from an instance or the class:

print 'a.static_foo(1): '
a.static_foo(1)
# executing static_foo(1)

print 'A.static_foo(1): '
A.static_foo('hi')
#executing static_foo(hi)

# Staticmethods are used to group functions which have some logical connection with a class to the class.

# `foo` is just a function, but you call `a.foo` you dont just get the function, you get a "partially applied" version of 
# the function with the object instance `a` bound as the first argument to the function. `foo` expects 2 argumnents, while 
# `a.foo` only expects 1 argument.

# `a` is bound to `foo`. That is what is meant by the term "bound" below:
print 'a.foo: ', a.foo 
# <bound method A.foo of <__main__.A object at 0xb7d52f0c>>

# With `a.class_foo`, `a` is not bound to `class_foo`, rather the class `A` is bound to `class_foo`.
print 'a.class_foo: ', a.class_foo
# <bound  method type.class_foo of <class '__main__.A'>>

#Here, with a staticmethod, even though it is a method, `a.static_foo` just returns a good 'ole function with no arguments 
# bound. `static_foo` expects 1 argument, and `a.static_foo` expects 1 argument too.
print(a.static_foo)
# <function static_foo at 0xb7d478cc>
# And of course the same thing happens when you call `static_foo` with the class `A` instead.
print 'A.static_foo: ', A.static_foo
# <function static_foo at 0xb7d478cc>

print "-" * 5, "classmethod", "-" * 5

# `classmethod` is a descriptor, wrapping a function, and you can call the resulting object on a class or (equivalently) an 
# instance thereof:

class x(object):
    def c1(*args): print 'c1', args
    c1 = classmethod(c1)
    @classmethod
    def c2(*args): print 'c2', args

inst = x()

print "x.c1(): "
x.c1()
# c1 (<class '__main__.x'>,)

print "x.c2(): "
x.c2()
# c2 (<class '__main__.x'>,)

print "inst.c1(): "
inst.c1()
# c1 (<class '__main__.x'>,)

print "inst.c2(): "
inst.c2()
# c2 (<class '__main__.x'>,)

# As you see, whether you define it directly or with decorator syntax, and whether you call it on the class or the instance,
#  the `classmethod` always receives the class as its first argument.

# One of the main uses of classmethod is to define "alternative constructors":

print "-" * 5, "alternative constructors", "-" * 5

class y(object):
    def __init__(self, astring):
        self.s = astring
    @classmethod
    def fromlist(cls, alist):
        x = cls('')
        x.s = ','.join(str(s) for s in alist)
        return x
    def __repr__(self):
        return 'y(%r)' % self.s

y1 = y('xx')
print 'y1: ', y1
# y('xx')

y2 = y.fromlist(range(3))
print 'y2: ', y2
# y('0,1,2')

# Now if you subclass `y`, the classmethod keeps working:

class k(y):
    def __repr__(self):
        return 'k(%r)' % self.s.upper()

k1 = k.fromlist(['za','bu'])
print 'k1: ', k1
# k('ZA,BU')

