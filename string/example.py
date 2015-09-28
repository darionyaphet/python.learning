
'''JSON String --> dict'''
'''SimpleJSON https://pypi.python.org/pypi/simplejson/'''
import simplejson

json_string = '''{"name": "darion.yaphet","sex": "male","age": 25}'''
json_dict   = simplejson.loads(json_string) 
print(json_dict)
print(simplejson.dumps(json_dict))
