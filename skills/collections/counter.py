'''
The collections library is, like, the best thing ever. Stackoverflow turned me on to ordered dicts early on, but I kept
using a snippet to create dicts to count occurrences of results in my code. One of these days, I'll figure out a use for
collections.deque.
'''

from collections import Counter
from random import randrange
import pprint

counter = Counter()
for index in range(1024):
    randon_number = randrange(10)
    counter[randon_number]+=1

for index in range(10):
    print(index,counter[index])
