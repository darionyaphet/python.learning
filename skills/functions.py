def power(x):
    return x**2

def add(x,y):
    return x+y

def even(x):
    return x%2==0

numbers = range(3,6)
print numbers

print map(power , numbers)
print reduce(add , numbers)
print filter(even , numbers)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

print zip(*matrix)
