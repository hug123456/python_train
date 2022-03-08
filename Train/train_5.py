# def generate():
#     i = 0
#     while i < 5:
#         print("我在这。。")
#         xx = yield i  # 注意，python程序，碰到=，都是先从右往左执行
#         print(xx)
#         i += 1
#
# g = generate()
# # g.send(None)  # <==> next(g) 第一次启动，执行到yield i（此时i=0），挂起任务，主程序继续往下执行
# #
# # g.send("lalala")
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.send('gmy'))
# # 生成器 迭代器的一种
# ha = (i for i in range(18))
# print(type(ha))
# 生成器


# import asyncio
#
#
# async def work(x):  # 通过async关键字定义一个协程
#     for _ in range(3):
#         print('Work {} is running ..'.format(x))
#
#
# coroutine_1 = work(1)  #------ 协程是一个对象，不能直接运行  -------
#
# # 方式一：
# loop = asyncio.get_event_loop()  # 创建一个事件循环
# result = loop.run_until_complete(coroutine_1)  # 将协程对象加入到事件循环中，并执行
# print(result)  # 协程对象
# asyncio.run(coroutine_1)

# task = loop.create_task(coroutine_1)
# print(task)
# # asyncio.run(task)
# loop.run_until_complete(task)
# print(task)

# 并发运行任务的案例

import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")  # python3.7新语法，了解一波
        await asyncio.sleep(1)  # await后面是 可等待对象
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

    return f"Task {name}: Finished!"


async def main():
    # Schedule three calls *concurrently*:
    results = await asyncio.gather(  # results包含所有任务的返回结果，是一个列表，按执行顺序返回结果
        factorial("A", 2),  # 协程，会自动调度为任务
        factorial("B", 3),
        factorial("C", 4),
    )
    print(results)


asyncio.run(main())  # 协程的嵌套，后面有详解

#



