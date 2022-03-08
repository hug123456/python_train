import pytest




def test_01():
    print("用例01")
    assert 1 == 1


def test_02(login_02):  #开始调用model 作用域范围
    print("用例02")
    assert 1 == 3


class TestLogin():
    def test_1(self):
        print("用例1")
        assert 1 == 3

    def test_2(self):
        print("用例2")

    def test_3(self):
        print("用例3")


@pytest.mark.usefixtures('logout01')
def test_03():
    print("用例03")
    assert 1 == 2

#
