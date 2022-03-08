def outer(a):
    b = 10
    c = [a]
    def inner():
        # nonlocal b
        # 内函数中想修改闭包变量
        # 方法1 nonlocal关键字声明
        # nonlocal  b
        b += 1
        # 方法二，把闭包变量修改成可变数据类型 比如列表
        c[0] += 1

        print(c[0])
        print(b)
    return  inner
ha = outer(5)
ha()

#  问题自己提出自己解答 pytest.