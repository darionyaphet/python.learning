import json

my = {
  "firstname":"darion",
  "lastname":"yaphet",
  "age":25
}

'''Python Object <==> JSON Object'''
my_str = json.dumps(my)
print(my_str)

my_json = json.loads(my_str)
print(my_json)


'''Reading & Writing Files'''
with open('json.data','w') as json_file:
    json.dump(my,json_file)

with open('json.data','r') as json_file:
    reading_json = json.load(json_file)
    print(reading_json)
