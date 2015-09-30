import sys

mod = __import__('folder.print_thread', fromlist=['print_threading'])
klass = getattr(mod, 'print_threading')
instance = klass('a')
instance.start()
