import redis

client = redis.Redis(host='127.0.0.1', port=6379, db=0)

'''Redis Config Infos'''
info = client.info()
for key in info:
  print "%s : %s" % (key,info[key])

'''Redis DataBase Size'''
print 'DataBase Size : '+ client.dbsize()


