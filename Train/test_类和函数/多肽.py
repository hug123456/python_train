# 闭包函数条件 外函数定义内函数 ，外函数应用了内函数。外函数定义了内函数


def outer_outer(flag=0):
    x,y = 666, 888
    def outer(ha):
        z = 666888
        def inner(a, b):

            ha(a, b)
            if flag:
                print("qi shi  huang guo qing ni cai shi zui bang de  %s" % flag)
            xi = x + 1
            print(xi)
            hx = z + 1
            print(hx)

        return inner
    return outer
# return

@outer_outer(2)
def test(a,b):
    print("guo ming yue shi zui bangde %s" % (a+b))

# test(2,4)




def outer01(func):
    m = 999999
    def inner01(f,g):
        nonlocal  m
        func(f,g)
        print("this is inner func")
        m = m + 1
        print(m)

    return inner01


@outer01
def train(num1,num2):
    print("this is train %s" % (num1 + num2))

train(1,2)

# ****************************************************************************: 总结：一个接口,多种实现
# 多肽 不同的类，相同的函数 不同的类， 相同的类
class Test():
    def ha(self):
        print("wo  shi Test ha")

class Train():
    def ha(self):
        print("wo shi Train ha")

class Td():
    def ha(self):
        print("wo shi Td ha")


def Tp(func):
    func.ha()


test = Test()
train = Train()
td = Td()
Tp(td)

# 多肽 id  value type id value type id value

# 单例模式










