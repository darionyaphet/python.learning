numbers = [1,2,3,4,5]

print [x**2 for x in numbers]

print [x**2 for x in numbers if x%2]

print dict([(x,x**2) for x in numbers])

print [(x,y) for x in range(10) if x%2 if x>3 for y in range(10) if y>7 if y!=8]

def power(x):
    return x**2

print [power(x) for x in numbers]

print [x*y for x in range(3) for y in range(5) ]


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

print matrix
print [[row[i] for row in matrix] for i in range(4)]
