def test_001(logout01,logout02):
    print("用例001")


class TestLogin:
    def test_1(self):
        print("用例1")

    def test_2(self, login):# 开始调用class 作用域范围
        print("用例2")

    def test_3(self):
        print("用例3")

    def test_4(self):
        print("用例4")

def test_002():
    print("用例002")



# ** 测试类下面只有一些测试方法使用了fixture函数名，这样的话，fixture只在该class下第一个使用fixture函数的测试用例位置开始算，后面所有的测试用例执行前只执行一次。而该位置之前的测试用例就不管
