
pairs = {'key0':0, 'key1':1, 'key2':2, 'key3':3, 'key4':4}
print({value:key for key,value in pairs.iteritems()})
print(dict((value,key) for key,value in pairs.iteritems()))

'''to process duplicate key'''
from collections import defaultdict
pairs = {'key':0, 'key_':0, 'key2':2, 'key3':3, 'key4':4}
entry = defaultdict(list)
for key,val in pairs.iteritems():
    entry[val].append(key)
print(entry)

