import functools

'''
    functools : Higher-order functions and operations on callable objects
    functions that act on or return other functions.
    In general, any callable object can be treated as a function for the purposes of this module.
'''

'''
    functools.reduce
    same function as reduce()

'''


'''
    functools.partial

'''
from operator import add
print add(1,2) #3
add1 = functools.partial(add,1)
print add1(10) #11


'''
    functools.update_wrapper

'''


'''
    functools.wraps
'''

'''
    
'''
