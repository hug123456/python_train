#!/usr/bin/python
# -*- coding:utf-8 -*-
#

# class MyMetaClass(type):
#     def __call__(cls, *args, **kwargs):
#         print('--自动触发元类当中的__call__方法---')
#         print("cls is %s" % cls)
#         #调用__new__产生一个空对象obj
#         obj = cls.__new__(cls)
#         print(obj)
#         print(obj.__dict__)   #此时名称空间为空.
#         #调用__init__初始化这个对象.
#         cls.__init__(obj,*args,**kwargs)
#         #返回初始化的对象
#         print(obj.__dict__)
#
#         return obj
#
#
#
# class Person(object, metaclass=MyMetaClass):  # 这一行: Person = MyMetaClass('Person',(object,),{...})
#
#     country = 'China'
#
#     def __init__(self, name, age):
#         print('-----Person--init-----')
#         self.name = name
#         self.age = age
#
#     def tell_info(self):
#         print('%s 的年龄是:%s' % (self.name, self.age))
#
#     def __new__(cls, *args, **kwargs):
#         print('---------new--------')
#         print("cls is %s " % cls)
#         return super().__new__(cls)

#dia object



# print(callable(Person))
# person = Person('wtt',25)   #Person这个类之所以可以被调用,肯定是因为造出Person的类：MyMetaClass当中含有__call__方法.
# print(person)
# print(MyMetaClass.__dict__)


# list_num = ['a', 'a', 'b', 'b', 'c', 'd']
# list_num1=[1,2,3,4,5,6]
# a=0
# for i in range(1,len(list_num)):
#     print(i-a)
#     print(i-a-1)
#     print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#     if list_num[i-a] == list_num[i-a-1]:
#         list_num.pop(i-a)
#         a += 1
# print(list_num)

# for i in range(len(list_num1)):
#     for j in range(i+1,len(list_num1)):
#         print('%s + %s = %s' % (list_num1[i],list_num1[j],list_num1[i]+list_num1[j]))


# def longestCommonPrefix(strs):
#     char = ""
#     #对列表进行排序
#     strs.sort(key=len)
#     #处理一些特殊情况
#     if len(strs) == 0 or strs[0]=="":
#         return char
#     #循环次数依据最短字符串来遍历
#     for i in range(len(strs[0])):
#         list1 = []
#         #与strs中的字符串逐个比较
#         for j in range(len(strs)):
#             if strs[0][i] == strs[j][i]:
#                 list1.append(strs[0][i])
#         print(list1)
#         #如果次数为列表长度，说明列表中的字符串都含有对应的字符
#         if len(list1) == len(strs):
#             char += strs[0][i]
#         else:
#             break
#     return char
# ha = longestCommonPrefix(['abc','abjing','abmnb'])
# print(ha)
#
#
# ha = ['abcd','abjdng','abmdb']
# char1=''
#
# ha.sort(key=len)
# for i in range(len(ha[0])):
#     new_list=[]
#     for j in range(len(ha)):
#         if ha[0][i] == ha[j][i]:
#             new_list.append(ha[0][i])
#     if len(new_list) == len(ha):
#         char1 += ha[0][i]
#     else:
#         break
#         #终止循环 终止循环
# print(char1)



#找出他们功能相同的数目
#最长公共前缀

#print(char)

def test(a=[]):
    print(a)
test(a=["1","2"])







