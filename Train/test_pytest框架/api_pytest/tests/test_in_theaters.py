import requests
import yaml
import os
import pytest
import sys

sys.path.append("D:\\测试开发\\Test\\test_pytest框架\\api_pytest")

from utils.commlib import get_test_data



file_path = os.path.join(os.path.dirname(__file__))
# def get_test_data(test_data_path):
#     case = []  # 存储测试用例名称
#     http = []  # 存储请求对象
#     expected = []  # 存储预期结果
#     with open(test_data_path,'r+',encoding='utf-8') as f:
#         dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
#         test = dat['tests']
#         for td in test:
#             case.append(td.get('case', ''))
#             http.append(td.get('http', {}))
#             expected.append(td.get('expected', {}))
#     parameters = zip(case, http, expected)
#     return case, parameters

cases, parameters = get_test_data(file_path + "\\..\\data\\test_in_theaters.yaml")
list_params=list(parameters)
#

# 测试fixture 作用域范围class 必须传conftest 文件 login  从 test_2  开始执行log ，test_3 就不会再执行了
class TestLogin:
    def test_1(self):
        print("log用例1")

    def test_2(self, login):
        print("log用例2")

    def test_3(self, login):
        print("log用例3")

    def test_4(self):
        print("log用例4")





class Testtrain01():
    def test01(self):
        print("this is test01")
        assert 1==1

# api utils utils tests data config data data t
class TestInTheaters(object):

    def test02(self):
        print("this is test02")
        assert 1 == 1


    @pytest.mark.parametrize("case,http,expected", list(list_params), ids=cases)
    def test_in_theaters(self, case, http, expected,env):
        # print(list(list_params))
        # print(type(list_params))
        # host = "https://www.baidu.com/"
        # path = "/v2/movie/in_theaters"
        # params = {"apikey": "0df993c66c0c636e29ecbb5344252a4a",
        #           "start": 0,
        #           "count": 10
        #           }
        # headers = {
        #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        # }
        response = requests.request(http["method"],
                             url=env["host"]["baidu"],
                             headers=http["headers"])


        # response = requests.request("GET", url=host, headers=headers)

        print("我看看走到这里位置代码了吗test_in_theaters")

        assert response.status_code == expected['response']["status_code"]

    # def test04(self):
    #     print("this is test04")
    #     assert 1==1

    def test03(self):
        print("this is test03")
        assert 1 == 1


class Testtrain04():
    def test04(self):
        print("this is test04")
        assert 1==1


    def test07(self):
        print("this is test07")
        assert 1==1


def test05():
    print("this is test05")
    assert 1==1


def test06(env):
    print("this is test06")
    assert 1==1