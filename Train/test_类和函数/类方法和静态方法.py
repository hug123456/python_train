class Parement():

    ha="我是类属性"

    # def __init__(self):
    #     self.name = 'hgq'
    #     self.age = 18
    #     # sex = "男"

    def test01(self):
        print("this is parement normal function")

    @classmethod
    def test02(cls):
        print("this is parement  classmethod %s" % cls.ha)

    @staticmethod
    def test03():
        print("this is parement staticmethod")


print("类直接调用方法")
# Parement.test01()   #TypeError: test01() missing 1 required positional argument: 'self'
# Parement.test02()
# Parement.test03()


##  ************************************************************ 类方法和静态方法  类都可以直接调用, 但是类不能直接调用实例方法test01(),self没有传参






print("对象调用方法")

# resp = Parement()
#
# resp.test01()
# resp.test02()
# resp.test03()
##  ************************************************************* 类方法和静态方法  对象都可以直接调用



#继承Parement类 -----------------------------------------------------------------------------------------------------------


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


print("result of p.averag(1,5)")
print(Son.averag(1, 5))
print("result of p.static_method()")
print(Son.static_method())        #子类的实例继承了父类的static_method静态方法，调用该方法，还是调用的父类的方法和类属性。
print("result of p.class_method()")
print(Son.class_method())         # 子类的实例继承了父类的class_method类方法，调用该方法，调用的是子类的方法和子类的类属性。

#
# 子类的实例继承了父类的static_method静态方法，调用该方法，还是调用的父类的方法和类属性。
# ***子类的实例继承了父类的class_method类方法，调用该方法，调用的是子类的方法和子类的类属性。













