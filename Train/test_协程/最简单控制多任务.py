import asyncio

async def coroutine_example(name):
    print('正在执行name:', name)
    await asyncio.sleep(1)
    print('执行完毕name:', name)

loop = asyncio.get_event_loop()

tasks = [coroutine_example('Zarten_' + str(i)) for i in range(3)]
wait_coro = asyncio.wait(tasks)
print(wait_coro)
loop.run_until_complete(wait_coro)


