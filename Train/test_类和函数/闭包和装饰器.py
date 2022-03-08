# ***************************************************************
# /1 闭包条件
# 　　     1 在一个外函数中定义了一个内函数。
#
#         2 内函数里运用了外函数的临时变量。
#
#         3 并且外函数的返回值是内函数的引用。


# **********************************************************************

def train01(ha):
    def train_01(name):
        ha(name)
        print("guo ming yue cai shi zui bang de %s" % name)

    return train_01

def train(ha):
    def train_02(name):
        ha(name)
        print("guo ming yue cai shi zui bang de %s" % name)

    return train_02

# test = train(test)
@train01
@train   #=test = train(test)
def test(name):
    print("huang guo qing shi zui bang de %s" % name)

test("mgy")


# ************************************************************************ 闭包中内函数修改外函数局部变量
def outer(a):
    b = 10
    c = [a]
    def inner():
        nonlocal b
        # 内函数中想修改闭包变量
        # 方法1 nonlocal关键字声明
        b += 1
        # 方法二，把闭包变量修改成可变数据类型 比如列表
        c[0] += 1

        print(c[0])
        print(b)
    return  inner
ha = outer(5)
ha()
#这个是修改外部函数变量 ，




def outer_outer(flag=0):

    def outer(ha):

        def inner(a,b):
            ha(a,b)

            if flag:
                print("huang guo qing shi zui bang de")

        return inner
    return outer


@outer_outer(2)
def test_train(a,b):
    print("wo shi zui bang de %s" % (a+b))
test_train(2,2)

# 是不能太他们使用




# 列表 可变类型




