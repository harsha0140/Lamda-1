### Lambda ###

# Lambdas are one line functions. They are also known as anonymous functions in some other languages. 
# You might want to use lambdas when you don't want to use a function twice on a program. They are just 
# like normal functions and even behave like them.

# Lambda function can take any number of arguments, but can only have one expression. They are mainly 
# used in combination with the functions filter(), map() and reduce().

x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

### Map ###
# r = map(func, seq)
# The first argument `func` is the name of a function and the second a sequence (e.g. a list) seq. `map()` 
# applies the function `func` to all the elements of the sequence `seq`. It returns a new list with the elements 
# changed by `func`.

def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5,39)

F = map(fahrenheit, temp)
C = map(celsius, F)

### Combined ###
Celsius = [39.2, 36.5, 37.3, 37.8]
F = map(lambda a: (float(9)/5)*a + 32, Celsius)
print(F)
# [102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]
C = map(lambda b: (float(5)/9)*(b-32), F)
print(C)
# [39.200000000000003, 36.5, 37.300000000000004, 37.799999999999997]

# map() can be applied to more than one list. The lists have to have the same length.
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
h = map(lambda x,y:x+y, a,b)
print(h)
# [18,14,14,14]
i = map(lambda x,y,z: x+y+z, a,b,c)
print(i)
# [17,10,19,23]

### Filter ###
# The function filter(function, list) offers an elegant way to filter out all the elements of a list, for which 
# the function `function` returns True.
# The function filter(f,l) needs a function f as its first argument. f returns a Boolean value, i.e. either True 
# or False. This function will be applied to every element of the list `l`. Only if f returns True will the element 
# of the list be included in the result list.

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x : x%2, fib)
print(result)
# [1,1,3,5,13,21,55]
result = filter(lambda x: x%2==0, fib)
print(result)
# [0,2,8,34]

### Reduce ###
# The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value.
# If seq = [s1, s2, s3, ..., sn], calling reduce(func, seq) works like this:
#  * At first the first two elements of seq will be applied to func, i.e. func(s1,s2) The list on which reduce() works looks 
#    now like this: [ func(s1, s2), s3, ..., sn]
#  * In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1,s2),s3)
#    The list looks like this now: [ func(func(s1, s2),s3), ... , sn]
#  * Continue like this until just one element is left and return this element as the result of reduce()

R = reduce(lambda x,y: x+y, [47,11,42,13])
print(R)

f = reduce(lambda x,y: x if x>y else y, [48,11,42,102,13])
print(f)

s = reduce(lambda x,y: x+y, range(1,101))
print(s)