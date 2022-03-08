
# -*- coding: utf-8 -*

import threading


class Account:
    def __init__(self):
        self.balance = 0

    def add(self, lock):
        # 获得锁
        print("获得锁add")
        lock.acquire()
        for i in range(0, 100000):
            self.balance += 1
        # 释放锁
        print("add balance %s" % self.balance)
        print("获得锁add")
        lock.release()

    def delete(self, lock):
        # 获得锁
        print("获得锁delete")
        lock.acquire()
        for i in range(0, 100000):
            self.balance -= 1
            # 释放锁
        print("delete balance %s" % self.balance)
        print("释放锁delete")
        lock.release()


if __name__ == "__main__":
    account = Account()
    lock = threading.Lock()
    # 创建线程
    print("创建线程")
    thread_add = threading.Thread(target=account.add, args=(lock,), name='Add')
    thread_delete = threading.Thread(target=account.delete, args=(lock,), name='Delete')

    # 启动线程
    print("启动线程")
    thread_add.start()
    thread_delete.start()

    # 等待线程结束
    print("等待子线程结束")
    thread_add.join()
    thread_delete.join()

    print('The final balance is: {}'.format(account.balance))