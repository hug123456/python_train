# -*- coding: utf-8 -*

import threading


class Test():
    def __init__(self):
        self.num = 0

    def add(self):
        print("add获得锁")
        # lock.acquire()
        for i in range(0, 1000):
            self.num += 2

        print("add释放锁")
        # lock.release()

    def delete(self):
        print("delete获得锁")
        # lock.acquire()
        for i in range(0, 1000):
            self.num -= 1

        print("delete 释放锁")
        # lock.release()


thread_list = []
# caozuo
train = Test()
# lock = threading.Lock()
print("创建线程")
thread1 = threading.Thread(target=train.delete)
thread2 = threading.Thread(target=train.add)
thread_list.append(thread1)
thread_list.append(thread2)
for th in thread_list:
    th.start()


print("开启线程")
# thread1.start()
# thread2.start()

print("等待子线程完成，也可以叫做主线程阻塞")
print('The final balance is: {}'.format(train.num))

thread1.join()
thread2.join()

# print('The final balance is: {}'.format(train.num))






