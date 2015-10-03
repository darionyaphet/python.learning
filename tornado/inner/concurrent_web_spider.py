import HTMLParser
import time
import urlparse
from datetime import timedelta

from tornado import httpclient, gen, ioloop, queues

base_url = 'http://www.tornadoweb.org/en/stable/'
concurrency = 10




if __name__ == '__main__' :
    import logging
    logging.basicConfig()

    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(main)
