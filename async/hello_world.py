#coding=utf-8

'''
    asyncio的编程模型就是一个消息循环。
    从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
'''

import asyncio

#@asyncio.coroutine把一个generator标记为coroutine类型
@asyncio.coroutine
def hello():
    print('Hello World ~')
    # 异步调用asyncio.sleep(1)
    # yield from可以调用另一个generator
    r = yield from asyncio.sleep(1)
    print("Hello again!")


#获取EventLoop:
loop = asyncio.get_event_loop()

#执行coroutine
loop.run_until_complete(hello())
loop.close()
