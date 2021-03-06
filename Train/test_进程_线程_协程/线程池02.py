from concurrent.futures import ThreadPoolExecutor
import threading
import time
# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum
# 创建一个包含2条线程的线程池
pool = ThreadPoolExecutor(max_workers=2)
# 向线程池提交一个task, 50会作为action()函数的参数
future1 = pool.submit(action, 50)
# 向线程池再提交一个task, 100会作为action()函数的参数
future2 = pool.submit(action, 100)
# 判断future1代表的任务是否结束
print("判断future1代表的任务是否结束 %s" % future1.done())
time.sleep(3)
# 判断future2代表的任务是否结束
print("判断future2代表的任务是否结束%s" % future2.done())
# 查看future1代表的任务返回的结果
print("查看future1代表的任务返回的结果%s" % future1.result())
# 查看future2代表的任务返回的结果
print("查看future2代表的任务返回的结果%s" % future2.result())
# 关闭线程池
pool.shutdown()

# 关闭线程池 result 返回的结果是否结束



# *************************************************************************总结
"""
上面程序中，第 12 行代码创建了一个包含两个线程的线程池，接下来的两行代码只要将 action() 函数提交（submit）给线程池，该线程池就会负责启动线程来执行 action() 函数。这种启动线程的方法既优雅，又具有更高的效率。

当程序把 action() 函数提交给线程池时，submit() 方法会返回该任务所对应的 Future 对象，程序立即判断 futurel 的 done() 方法，该方法将会返回 False（表明此时该任务还未完成）。接下来主程序暂停 3 秒，然后判断 future2 的 done() 方法，如果此时该任务已经完成，那么该方法将会返回 True。

程序最后通过 Future 的 result() 方法来获取两个异步任务返回的结果
"""



