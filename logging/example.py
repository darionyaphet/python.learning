
'''
    http://www.cnblogs.com/dkblog/archive/2011/08/26/2155018.html
'''

import logging

logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='log.out',
        filemode='w')


console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
