import threading

class print_threading(threading.Thread):

    def __init__(self,info):
        threading.Thread.__init__(self)
        self._info = info

    def run(self):
        print(self._info)
