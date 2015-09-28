from Queue import Queue
from threading import Thread

class Worker(Thread):

    def __init__(self,tasks):
        Thread.__init__(self)
        self._tasks = tasks
        self_daemon = True
        self.start()

    def run(self):
        while True:
            function ,args ,kargs = self._tasks.get()
            try:
                function(*args,**kargs)
            except Exception, e:
                print(e)

            self._tasks.task_done()

class ThreadPool:

    def __init__(self,num_threads):
        self._tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self._tasks)

    def add_task(self,function,*args,**kargs):
        self._tasks.put((function,args,kargs))

    def wait_completion(self):
        self._tasks.join()

if __name__ == '__main__':
    from random import randrang
    delays = [randrange(1, 10) for i in range(100)]

    from time import sleep
    def wait_delay(d):
        print 'sleep for (%d) sec'%d
        sleep(d)

    pool = ThreadPool(13)

    for index,d in enumerate(delays):
        print('%.2f%c' % ((float(i)/float(len(delays)))*100.0,'%'))
        pool.add_task(wait_delay,d)

    pool.wait_completion()
