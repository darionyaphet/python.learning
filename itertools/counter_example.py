'''
http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652563762&idx=2&sn=a1f2db851cc8b7086abfd7d11c168ac9&scene=23&srcid=0617E4lHVpcd4aowYJSqJvW9#rd
'''

from itertools import count

for index in count(10):
    if index > 20 : break 
    else : print index

print '*****'*10

from itertools import islice

for index in islice(count(10), 5):
    print index

print '*****'*10

from itertools import cycle

count = 0
for index in cycle('ABC'):
    if count > 7: break
    print index 
    count += 1

print '*****'*10

polys = ['triangle', 'square', 'pentagon', 'rectangle']

iterator = cycle(polys)

print next(iterator)
print next(iterator)
print next(iterator)
print next(iterator)

print '*****'*10

from itertools import repeat

iterator = repeat(5, 5)

print next(iterator)
print next(iterator)
print next(iterator)
print next(iterator)
print next(iterator)

print '*****'*10

#from itertools import accumulate

#print list(accumulate(range(10)))

import operator

#print list(accumulate(range(1, 5), operator.mul))

print '*****'*10

from itertools import chain

numbers = list(range(5))
cmd     = ['ls' ,'/tmp']

print list(chain(['foo', 'bar'], cmd, numbers))
print list(chain.from_iterable([cmd, numbers]))

print '*****'*10

from itertools import compress

letters = 'ABCDEFG'
bools = [True, False, True, True, False]

print list(compress(letters, bools))

print '*****'*10

from itertools import dropwhile

print list(dropwhile(lambda x: x<5, [1,4,6,4,1]))

def less_than_five(x):return x < 5

print list(dropwhile(less_than_five, [1,4,6,4,1]))

print '*****'*10

#from itertools import filterfalse

#def greater_than_five(x): return x > 5 

#print list(filterfalse(greater_than_five, [6, 7, 8, 9, 1, 2, 3, 10]))

print '*****'*10

from itertools import groupby

vehicles = [('Ford', 'Taurus'), ('Dodge', 'Durango'),
            ('Chevrolet', 'Cobalt'), ('Ford', 'F150'),
            ('Dodge', 'Charger'), ('Ford', 'GT')]
 
sorted_vehicles = sorted(vehicles)

for key,group in groupby(sorted_vehicles, lambda make: make[0]):
  for make,model in group:
    print '{model} is made by {make}'.format(model=model, make=make)


print '*****'*10

from itertools import starmap

def add(a, b): return a+b  

for item in starmap(add, [(2,3), (4,5)]):
    print item 


print '*****'*10

from itertools import takewhile

print list(takewhile(lambda x: x<5, [1,4,6,4,1]))

print '*****'*10

from itertools import tee

iter1, iter2 = tee('ABCD')
for item in iter1:
    print item

print '*****'*10

#from itertools import zip_longest

#for item in zip_longest('ABCD','XYZ',fillvalue='BLANK'):
#    print item 

print '*****'*10

from itertools import combinations

print list(combinations('XYZ',2))

print '*****'*10

from itertools import combinations_with_replacement 

print list(combinations_with_replacement('XYZ', 2))

print '*****'*10

from itertools import product

arrays = [(-1,1), (-3,3), (-5,5)]

print list(product(*arrays))

print '*****'*10

from itertools import permutations

for item in permutations('XYZ', 2):
    print ''.join(item)
