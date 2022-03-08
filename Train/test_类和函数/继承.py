# coding:utf-8
class Foo(object):
    X = 1
    Y = 2

    @staticmethod
    def averag(*mixes):  # "父类中的静态方法"
        return sum(mixes) / 2

    @staticmethod
    def static_method():  # "父类中的静态方法"
        print("父类中的静态方法")
        return Foo.averag(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls):  # 父类中的类方法
        print("父类中的类方法")
        print(cls.X, cls.Y)
        return cls.averag(cls.X, cls.Y)


class Son(Foo):
    X = 3
    Y = 5

    @staticmethod
    def averag(*mixes):  # "子类中重载了父类的静态方法"
        print("子类中重载了父类的静态方法")
        return sum(mixes) / 3


# print("result of p.averag(1,5)")
# print(Son.averag(1, 5))
# print("result of p.static_method()")
# print(Son.static_method())        #子类的实例继承了父类的static_method静态方法，调用该方法，还是调用的父类的方法和类属性。
# print("result of p.class_method()")
# print(Son.class_method())         # 子类的实例继承了父类的class_method类方法，调用该方法，调用的是子类的方法和子类的类属性。

#
# 子类的实例继承了父类的static_method静态方法，调用该方法，还是调用的父类的方法和类属性。
# 子类的实例继承了父类的class_method类方法，调用该方法，调用的是子类的方法和子类的类属性。


# ---------------------------------------------------- 多继承的方法 --------------------------------------------------------
class Gramparent():

    def train03(self):
        print("this is Gramparent")


class Parent():
    name="hgq"
    age=18

    def __init__(self,sex):
        self.sex = sex

    def train01(self):
        print("this is paremt train01")

    def train02(self):
        print("this is paremet train02")


class Child(Parent):
    name = "gmy"
    age="10"

    def __init__(self, sex):
        super().__init__(sex)

    def train01(self):
        super(Child, self).train02()
        print("this is child train01")

    # def train02(self):
    #     print("this is child train02")


# response = Child("男")
# response.train01()

class Son(Gramparent,Child):
    def __init__(self,sex):
        super().__init__(sex)

    def train01(self):
        super().train02()
        print("this is Son train02")

resp = Son("男")
resp.train01()
print(Son.__mro__)   ## ** mro 私有方法 可以查询继承的顺序
