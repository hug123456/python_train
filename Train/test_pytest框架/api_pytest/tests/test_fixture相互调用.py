class TestLogin:
    def test_1(self, login03):
        print("直接使用第二层fixture,返回值为{}".format(login03))

    def test_2(self, account):
        print("只调用account fixture,返回值为{}".format(account))

# 1.即使fixture之间支持相互调用，但普通函数直接使用fixture是不支持的，一定是在测试函数内调用才会逐级调用生效
# 2.有多层fixture调用时，最先执行的是最后一层fixture，而不是先执行传入测试函数的fixture
# 3.上层fixture的值不会自动return,这里就类似函数相互调用一样的逻辑

