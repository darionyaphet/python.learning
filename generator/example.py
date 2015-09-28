
'''
    http://www.jb51.net/article/70366.htm
'''

def print_my_name():
    print 'Darion.J.Yaphet'

print_my_name()


def my_info(func):
    def wrapper(*args,**params):
        print 1024
        return func(*args,**params)
    return wrapper

@my_info
def print_my_info():
    print 'Darion.J.Yaphet'

print_my_info()

def more_info(name):
    def my_info(func):
        def wrapper(*args, **params):
            print name+'\t'+str(1024)
            return func(*args, **params)
        return wrapper
    return my_info

@more_info('Lucien')
def print_more_info():
    print 'Darion.J.Yaphet'

print_more_info()
