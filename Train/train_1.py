#!/usr/bin/python
# -*- coding:utf-8 -*-
# class Test(object):
#     def __new__(cls, *args, **kwargs):
#         print("cls is  %s" % cls)
#         print("这是 new method %s" % object.__new__(cls))
#         return object.__new__(cls)
#
#     def __init__(self, name):
#         self.name = name
#
#     # def __new__(cls):
#     #     print("这是 new method %s" % object.__new__(cls))
#     #     return object.__new__(cls)
#
#     def ha(self):
#         print("wo shi zui bang %s" % self.name)
#
#     def xi(self):
#         print("wo shi  da shuai ge")
#
# res=Test("huang")
# res.ha()
#
# class Studnet(Test):
#     def __init__(self, name):
#         super(Studnet, self).__init__(name)
#
#     def aoli(self):
#         pass
#     def xi(self):
#         print("wo shi da mei nv")
#
# response=Studnet("meili")
# response.xi()
#多肽  不同类目统一函数名字

# class Test2(object):
#     def __new__(cls, *args, **kwargs):
#         print("-------111-------")
#         print("cls is %s" % cls)
#         print("return result is %s" % object.__new__(cls))
#         print(object.__new__(cls).__dict__)#这个对象没有任何属性
#         return object.__new__(cls)
#
#     def __init__(self,name,age):
#         print("-------222-------")
#         print("self is %s" % self)
#         self.name = name
#         self.age = age
#
#
#     def test(self):
#         print("my name is %s" % self.name)
#
#     def __call__(self):
#         print("age is %s" % self.age)
#         print("-------333-------")

# ha1=Test2("gmy",18)
# ha1.test()
# ha1()
#产生类的方式

#type str tuple dict

# country = "china"
# def __init__(self,name,age):
#     self.name = name
#     self.age = age
#
# def tell(self):
#     print("%s 年龄是：%s" % (self.name, self.age))
#
# Person = type("Person",(object,),{"__init__":__init__,"country":country,"tell":tell})
#
# print(Person.__dict__)
# print(Person.country)

#自定义原理  __dict__


# class Person(object):
#     color = "yellow"
#
#     def think(self):
#         self.color = "black"
#         print("i am a %s" % self.color)
#
# class Chinese(Person):
#     pass
#
# hs= Chinese()
# print(hs.color)
#类对象  直接调用  color

#
# class Test():
#     age=18
#
#     def __new__(cls, *args, **kwargs):
#         print(cls)
#         #<class '__main__.Test'>
#         print(object.__new__(cls))
#         print(object.__new__(cls).__dict__)
#         return object.__new__(cls)
#
#
#     def __init__(self, name):
#         print(self)
#         self.name = name
#
#     def name_test(self):
#         print("name test is %s" % self.name)
#
#     def __call__(self, lihai):
#
#         print("__call__ method is %s" % lihai)
#         #__call__ method is <__main__.Test object at 0x00000129F6BA0FD0>
#
# ha=Test("huang")
# ha.name_test()
# name test
# print(Test.name_test())
# print(Test.age)
# print(ha.name)
# lei he duixiang doukeyidiao yong
# ha.name_test()
# ha("ai li ge")
# print(Test.age)
# print(ha.age)
# print(Test.name_test())

# print(Test.__dict__)
# print(ha.__dict__)
# class MyMeta(type):
#     def __call__(cls, *args, **kwargs):
#         print("MyMeta __call__ method cls is %s" % cls)
#         obj=cls.__new__(cls, *args, **kwargs)
#         print("MyMeta obj method is %s" % obj)
#         cls.__init__(obj, *args, **kwargs)
#         return obj
#
# class Student(object, metaclass=MyMeta):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __new__(cls, *args, **kwargs):
#         obj = super().__new__(cls)
#         print("Student cls method is %s" % cls)
#         return obj
#
# response = Student("huang",88)
# print(response)
#
#
# class MyMeta(type):
#     def __call__(cls, *args, **kwargs):
#         obj = cls.__new__(cls,*args,**kwargs)
#         cls.__init__(obj,*args,**kwargs)
#
#         #这个对象本来构造并初始化完毕了,但是我们不立即进行返回,而是进行进一步的操作:
#         obj.__dict__ = {'_%s__%s'%(cls.__name__,key):value for key,value in obj.__dict__.items()}
#         #
#         print("############### %s" %  obj.__dict__)
#         #  _类名__属性的名字
#
#         return obj
#
#
# class Student(object,metaclass=MyMeta):
#     country = 'China'
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def tell_info(self):
#         print('%s的姓名是:%s'%(self.name,self.age))
#
#
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls)
#
#
#
# student = Student('wtt',25)
# print(student.__dict__)
# print(student._Student__name,student._Student__age)
# print(Student.name)
#  封装  继承  多肽  oop 面向对象变成  地址  和  指针有关系 age Execute.py
# print(Student.name)
#
# class Btest(object):
#     def __new__(cls, *args, **kwargs):
#         if object.__new__(cls) == None:
#             objc = object.__new__(cls)
#         return objc
#
#     def __init__(self, name):
#         self.name = name
#
#     def a_test(self):
#         print("ha %s" % self.name)
#
# ha = Btest("guo")
# print(id(ha))

#
# class Person(type):
#     def __call__(cls, *args, **kwargs):
#         print("1")
#         print("Person cls %s" % cls )
#         obj = cls.__new__(cls, *args, **kwargs)
#         print("Person obj %s" % obj)
#         print("8")
#         cls.__init__(obj, *args, **kwargs)
#         return obj

# return obj **kwargs  return print print kwargs kwargs Person kwargs
# return obj kwargs return print kwargs kwargs person kwargs
# obj kwargs return print kwargs kwargs person kwargs
#
#
# class Googperson(object, metaclass=Person):# Goodperson =  Person("Goodperson",(object,),{......})
#     def __new__(cls, *args, **kwargs):
#         print("1.1")
#
#         return object.__new__(cls)
#
#     def __init__(self, name, age):
#         print("8.1")
#         self.name = name
#         self.age = age
#
#     def test(self):
#         print("my name is %s" % self.name)
#
# ha=Googperson("name",18)

# #
# class Person(type):
#     def __call__(cls, *args, **kwargs):
#         obj = cls.__new__(cls, *args, **kwargs)
#         cls.__init__(obj, *args, **kwargs)
#         return obj
#
#
# class Badperson(object,metaclass=Person):
#     def __new__(cls, *args, **kwargs):
#         return object.__new__(cls)
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def test_a(self):
#         print("my name is %s, age is %s" % (self.name, self.age))
#
# response_a = Badperson("huang",18)
# response_a.test_a()

#pip install apt-get
# pip install apt-get 'huang'
# class School(object):
#     def __init__(self, name):
#         self.name = name
#
#     def test_b(self):
#         print("% ao li ge" % self.name)
#
# class Teacher(School):
#     def  __init__(self, name, age):
#         super(Teacher, self).__init__(name)
#         self.age = age
#
#     def test_c(self):
#         super().test_b()
#         print("ao li ge ge  %s" % self.age)
# response_c = Teacher("huang",18)
# response_c.test_c()


# JIESHIQI  RESPONSE_C.TEST_C() Teacher huang 18

# Techer huang 18 Teacher "huang 18 self.age huang 18"

# li = [1, 2, 3, 4, 5]
#
# print(id(li))
#
# li.append("ha")
#
# print(li)
#
# print(id(li))
#
# print(enumerate(li))
#
# for i, v in enumerate(li):
#     print(i, v)


# print(enumerate(li))

# li = [1, 2, 3, 4, 5]
# print(li[1:4])
# class A():
#     def __init__(self,name):
#         self.name = name
#
#     def test(self, age):
#         print("my name is %s" % age)
#     @staticmethod
#     def test_2():
#         print("he is good boys")
#
#     @classmethod
#     def test_3(cls):
#         print("hs is bad girls")


# class Apple(object):
#     def get_apple(self, n):
#         print("apple: %s,%s" % (self, n))
#
#     @classmethod
#     def get_class_apple(cls, n):
#         print("apple: %s,%s" % (cls, n))
#
#     @staticmethod
#     def get_static_apple(n):
#         print("apple: %s" % n)
#
#     @staticmethod
#     def get_static_apple_2(m):
#         Apple.get_static_apple(m)
#
#
# res=Apple()
# Apple.get_apple(res,22)
# Apple.get_static_apple("hgq")
# Apple.get_class_apple("gmy")
# res.get_apple(555)
# res.get_class_apple(666)
# res.get_static_apple(777)
# res.get_static_apple_2("ha")
import time


# def get_time(func):
#     def wrapper():
#         startTime = time.time()
#         func()
#         endTime = time.time()
#         print("spend %f" % (endTime-startTime))
#
#     return wrapper
#
#
# @get_time# myfunc = get_time(myfunc)
# def myfunc():
#     print("start")
#     time.sleep(0.8)
#     print("end")
#
# myfunc()
# def test(haxi):
#     def train_test(didi):
#         print("wo shi zui%s  bang de %s" % (haxi, didi))
#     return train_test
#
# ha = test("hgq")
# # print(ha)
# # ha("dalao")
# print(ha.__dict__)
# print(ha.__doc__)

class Pare():
    _xixi = 'xixixixinizuibang'
    def xiaoji(self):
        print("wo shi zui bang de")

    def daya(self):
        print("bu ni shi zui cha de")

    def only_fun(self):
        print("wo ben lai jiu shi zui bang de")

        # 普通方法

    def _test1(self):
        self.__test2()
        print("普通方法_test1方法")

        # 私有方法

    def __test2(self):
        print("私有方法__test2方法")


class Child(Pare):
    __haxi = 'nizuibang'
    haha = 'wozuibang'
    def test(self):
        print(self.__dict__)
        super().xiaoji()
        print("test one function")

    def daya(self):
        print("haha test two function")

    def __test3(self):
        print("私有方法__test3方法")
# resp = Child()
# resp._test1()
# print(resp._Child__haxi)
# print(resp.__haxi)
# resp.__test3()
# resp.__test2()
# resp._Child__test3()
# print(Child.__dict__)
li = {"name":"hgq","name":"gmy"}
print(li)

# print(resp._xixi)

# resp.test()
# resp.daya()
# resp.only_fun()
#XX.daya() 方法  only func
# print(resp.haha)
# print(Child.haha)
# print(Child.__haxi)
# print(resp._Child__haxi)
class Test(object):
    # 普通方法
    def test(self):
        print("普通方法test")

    # 普通方法
    def _test1(self):
        self.__test2()
        print("普通方法_test1方法")

    # 私有方法
    def __test2(self):
        print("私有方法__test2方法")
# t = Test()
# t._test1()





























