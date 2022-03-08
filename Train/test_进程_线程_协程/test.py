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

T1 = ThreadPoolExecutor(max_workers=1)
future1 = T1.submit(action, 50)
# future2 =T1.submit(action, 100)
print("代表future1代表任务是否结束 %s" % future1.done())

print("代表future1任务的结果%s" % future1.result())
T1.shutdown()


# shutdown
