'''yesterday'''
import datetime
yesterday = datetime.date.today() - datetime.timedelta(days=1)
print 'yesterday : '+str(yesterday)
