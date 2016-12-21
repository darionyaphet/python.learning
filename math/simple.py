
# Return an accurate floating point sum of values in the iterable. 
# Avoids loss of precision by tracking multiple intermediate partial sums:
array = [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]
print(sum(array))
from math import fsum
print(fsum(array))


from math import exp, expm1
print(exp(1e-5) - 1)
