import time


DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

'''current time stamp'''
current_timestamp = time.time()
print('current timestamp : '+str(current_timestamp))

'''current time string'''
current_datetime = time.strftime(DATE_FORMAT,time.localtime(current_timestamp))
print(current_datetime)

'''yesterday'''
import datetime
yesterday = datetime.date.today() - datetime.timedelta(days=1)
#print 'yesterday : '+str(yesterday)



