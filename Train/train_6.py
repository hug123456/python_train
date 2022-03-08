import threading
import time

#
# def get_thread_name():
#     t = threading.current_thread()
#     return t.name
#
# def print_time(delay):
#     """Define a function for the thread."""
#     thread_name=get_thread_name()
#     count = 0
#     while count < 8:
#         time.sleep(delay)
#         count += 1
#         print("%s:%s" % (thread_name, time.ctime(time.time())))
#
# t1 = threading.Thread(target=print_time, args=(1,))
# t2 = threading.Thread(target=print_time, args=(2,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# def sum_demo(x, y):
#     for _ in range(2):
#         x += 1
#         y += 1
#         result = x + y
#         print(result)
#     return result
#
# if __name__ == '__main__':
#     result = sum_demo(1, 1)
#     print(result)

# ha = list()
# resp = ["h", "g", "q"]
# haxi = [ha.append(i) for i in resp]
# print(haxi)

#
# def train(ha, *args, haxi=None):
#     print(ha, args, haxi)
#
#
# train(1, 2, 3, 4, 5, haxi="lihai")
#
# d={"a":6,"b":9}
#
# def train01(a, b):
#     a, b = b, a
#     print("train01  a is %s, b is %s" % (a, b))
#
#
# a = 2
# b = 6
# train01(a, b)
# print("a is %s, b is %s" % (a, b))
#
# def train02(dw):
#     dw["a"], dw["b"] = dw["b"], dw["a"]
#     print("train02函数外，a元素的值是", dw['a'], "；b元素的值是", dw['b'])
#
# train02(d)
# print("train02函数外，a元素的值是", d['a'], "；b元素的值是", d['b'])
# 浅拷贝 和 深拷贝 的概念
# 浅拷贝 和 深拷贝 的概念


# dict_a = {key: value for key in 'python' for value in "python"}
# print(dict_a)
# # key value
# resp1 = [1, 2, 3, 4, 5]
# resp2 = ["hgq", "gmy", "dwq"]
# print(zip(resp1,resp2))
# respha={"name":"hgq","age":18}
# print(*respha)
# true or false hgq age
# 生成器 和
# x = [1, 2, 3, 4, 5]
# print(type(x))
# print(1 in x)
# print(2 not in x)
# for i in x:
#     print(i)
# Y = iter(x)
# print(Y)
# print(next(Y))
# print(next)
# class Test(object):
#     def __init__(self, array):
#         self.x = array
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.x):
#             value = self.x[self.index]
#             self.index = self.index + 1
#
#         else:
#             raise StopIteration
#         return value
# it = Test([1,2,3,4,5])
# print(type(it))
# print(it.__next__())
# print(it.__iter__())
# __和  __test__   方法

# 手写一个迭代器 建普利司通array
# def Train(array):
#     for i in array:
#         yield i
#
# ha = Train([11,22,33,44])
# print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# print(type(ha))
# print(next(ha))
# print(iter(ha))
# print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# xi = (i for i in range(10))# 生成器表达式
# print(xi)


# y = [1,2,3,4,5]
# print(next(y))

# class CS():
#     cls_val = 1
#
#     def __init__(self):
#         self.name = 10
#
#
# bb = CS()
# print(bb.__dict__)
# bb.cls_val= 99
# print(bb.__dict__)
# print(CS.__dict__)
# print(CS.cls_val)
#实例属性 和 类属性


# class Desc(object):
#
#       def __get__(self, instance, owner):
#           print("__get__...")
#           print("self : \t\t", self)
#           print("instance : \t", instance)
#           print("owner : \t", owner)
#           print('='*40, "\n")
#
#      def __set__(self, instance, value):
#          print('__set__...')
#          print("self : \t\t", self)
#          print("instance : \t", instance)
#          print("value : \t", value)
#          print('='*40, "\n")
#
#
#  class TestDesc(object):
#      x = Desc()

# get event loop corotuin  task future asyncio/await

# def generate():
#     i = 0
#     while i < 5:
#         print("我在这。。")
#         xx = yield i  # 注意，python程序，碰到=，都是先从右往左执行
#         print(xx)
#         i += 1
#
# g = generate()
# print(g.__next__())
# print(g.__next__())

# 执行None
import asyncio
from functools import partial
# async def test_01():
#     for i in range(8):
#         print(i)
# ha = test_01()
# loop = asyncio.get_event_loop()
# result = loop.run_until_complete(ha)
# print(result)
# print(type(ha))
# event loop  run until complete  携程对象是不容易调用 None






async def work(x):  # 通过async关键字定义一个协程
    for i in range(3):
        print('Work {} is running ..'.format(x))
    return i
def call_back(future):
    print("Callback: {}".format(future.result()))

# future
# renwuhuidiaohansh
#   call_back()
coroutine_1 = work(1)  # 协程是一个对象，不能直接运行


# 方式一：
loop = asyncio.get_event_loop()  # 创建一个事件循环
task = loop.create_task(coroutine_1) # 携程对象
# print(task)
task.add_done_callback(call_back)
result = loop.run_until_complete(task)  # 将协程对象加入到事件循环中，并执行
print(result)


# 携程对象调用 回调函数  future.resuult()
# print(task)  # return await gather gather gather gather
# print(isinstance(task, asyncio.Future))
# def func(a,b):
#     return a + b
#
# result1=func(1,2)
#
# new_func = partial(func,1)
# result2 = new_func(2)
#
# print(result1, result2)

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")  # python3.7新语法，了解一波
        await asyncio.sleep(1)  # await后面是 可等待对象
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

    return f"Task {name}: Finished!"

#

async def main():
    # Schedule three calls *concurrently*:
    results = await asyncio.gather(  # results包含所有任务的返回结果，是一个列表，按执行顺序返回结果
        factorial("A", 2),  # 协程，会自动调度为任务
        factorial("B", 3),
        factorial("C", 4),
    )
    print(results)


asyncio.run(main())  # 协程的嵌套，后面有详解
#await pip 先进后出 gather result  GIL 垃圾回收  一遍 遍历 一边计算  yield  result fanhuijieguo
#asyncio  main pr










