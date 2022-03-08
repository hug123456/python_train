#!/usr/bin/python
# -*- coding:utf-8 -*-


#python utf-8 -*-

#GIL  同一时刻只有一个线程进行
#死锁  一个占用  一个等待

import time
import threading
#
# def mop_floor():
#     print("我要拖地")
#     time.sleep(3)
#     print("底托完了")
#
# def heat_up_water():
#     print("我要浇水")
#     time.sleep(3)
#     print("水浇完了")
#
# start_time = time.time()
# heat_up_water()
# mop_floor()
# end_time= time.time()
# print("总共耗时 %s" % (end_time-start_time))
#
# t1 = threading.Thread(target=mop_floor)
# t2 = threading.Thread(target=heat_up_water)

# t1.run()
# t2.run()

# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# t1 t2 join join heat_up_wate

# end_time = time.time()
#
# print("消耗多少时间 %s" % (end_time - start_time))

s = "   fly me   to   the moon  "
print(id(s))
# print(s.strip())
ha=s.strip()
print(id(ha))
print(ha)
l=ha.split(" ")
print(l)

# print(type(s.strip()))
#
li1=[1,2,3,4,5]
li2=[6,7,8]
print(id(li1))
li1.extend(li2)
print(id(li1))
print(li1)
print(li1 + li2)


# print(li1)
# li1.pop(0)
# print(li1)
# ha=s.split(' ')
# print(ha)
# for i in s[::-1]:
#     if i != " ":
#         length_world = len(i)
#         print(length_world)
#         break







