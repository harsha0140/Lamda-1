### Generators ###
"""
Generators look like functions, but there is both a syntactical and a sematic difference. Instead of return 
statements, you will find inside of the body of a generator only yield statements, i.e. one or more yield statements.

Another important feature of generators is that the local variables and the execution start is automatically saved 
between calls. This is necessary, because unlike an ordinary function successive calls to a generator function don't 
start execution at the beginning of the function. Instead, the new call to a generator function will resume execution 
right after the tield statement in the code, where the last call exited.

If there is a return statement in the code of a generator, the execution will stop with a `StopIteration exception` 
error if this code is executed by the Python interpreter.

Everthing what can be done with a generator can be implemented with a class based iterator as well. But the crucial 
advantage of generators consists in automatically creating the methods __iter__() and next(). Generators provide a 
very near way of producing data which is huge or infinite.
"""

def city_generators():
    yield("Konstanz")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")

x = city_generators()
print(x.next())
print("Second City: ", x.next())
print("Third City: ", x.next())
print("Fourth City: ", x.next())
# print("Fifth City?: ", x.next())

"""
Thought at first sight the yield statement looks like the return statement of a function, we can see in this example 
that there is a big difference. If we had a return statement instead of a yield in the previous example, it would be 
a function. But this function would always return "Konstanz" and never any of the other cities.
"""

def fib(n):
    # Fibonacci numbers generator
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): return
        yield a
        a, b = b, a+b
        counter += 1

f = fib(10)
print(f.next())
print(f.next())
print(f.next())
print(f.next())
print(f.next())
print(f.next())
print(f.next())
# print(f)
# for x in f:
#     print(x)
# print

"""
Recursive Generators to get permutations
A permutation is a rearrangement of the elements of an ordered list. Every arrangement of n elements is called a 
permutation. The number of permutations on a set of n elements is given by n!.
n! = n*(n-1)*(n-2)...2*1
"""
def permutations(items):
    n = len(items)
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i]+items[i+1:]):
                yield [items[i]] + cc

for p in permutations(['r','e','d']): print ''.join(p)
for p in permutations(list('game')): print ''.join(p)
