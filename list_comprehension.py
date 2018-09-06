#python3

# List comprehension is an elegant way to define and create list in Python. These lists have often the qualities of sets, 
# but are not in all cases sets. List comprehension is a complete substitute for the lambda function as well as the 
# functions map(), filter() and reduce().

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius]
print(Fahrenheit)
# [102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]

# The following list comprehension creates the Pythagorean triplets:
triples = [ (x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2+y**2 == z**2]
print(triples)
# [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (10, 24, 26), (12, 16, 20), 
# (15, 20, 25), (20, 21, 29)]

# Cross product of two sets:
colors = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
colored_things = [ (x,y) for x in colors for y in things if not (x=="blue" and y=="tree") ]
print(colored_things)
# [('red', 'house'), ('red', 'car'), ('red', 'tree'), ('green', 'house'), ('green', 'car'), ('green', 'tree'), 
# ('yellow', 'house'), ('yellow', 'car'), ('yellow', 'tree'), ('blue', 'house'), ('blue', 'car')]


### Generator Comprehension ###
# Generator comprehension were introduced in Python 2.6. They are simple a generator expression with a parenthesis 
# - round brackets - around it. Otherwise, the syntax and the way of working is like list comprehension, but a 
# generator comprehension returns a generator instead of a list.

x = ( x**2 for x in range(20))
print(x)
# at 0xb7307aa4>
x = list(x)
print(x)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]


nonprimes = [j for i in range(2,8) for j in range(i*2, 100, i)]
# i = [2,3,4,5,6,7]
# j = [4,6,8,10...98], [9,12,15...99], [16,20,24,28...96], [25,30,35,40...95], [36,42,48,54....96], [49,56,63,70....98]
primes = [x for x in range(1,100) if x not in nonprimes]
print(primes)
# [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#Doing the long way!
def append_to_array(num, max, array):
    for i in range(num*2,max,num):
        array.append(i)
    return array
def only_primes(array, max):
    prime_array = []
    for i in range(1,max):
        if i not in array:
            prime_array.append(i)
    return prime_array
def get_all_primes(max):
    array = []
    for j in range(2,8):
        append_to_array(j, max, array)
    return only_primes(array, max)

print(get_all_primes(100))

# adding some Lambda and Filter() to do the same job.
the_primes = filter(lambda x: x not in nonprimes, [x for x in range(1,100)])
print(the_primes)

### Set Comprehension ###
# A set comprenhension is similar to a list comprehension, but returns a set and not a list. Syntactically, we use curly 
# brackets instead of square brackets to create a set. Set comprehension is the right functionality to solve our problem 
# from the previous subsection. We are able to create the set of non primes without doublets.

# The number 8 was chosen because I choose the highest number to 100. For higher numbers, you need to take the sqrt of 
# that number and use it.
from math import sqrt
n = 100
sqrt_n = int(sqrt(n))
no_primes = {j for i in range(2,sqrt_n) for j in range(i*2, n, i)}
primes = {x for x in range(1,n) if x not in no_primes}
print(primes)