import requests
import yaml
import os

file_path = os.path.join(os.path.dirname(__file__))

def get_test_data(test_data_path):
    case = []  # 存储测试用例名称
    http = []  # 存储请求对象
    expected = []  # 存储预期结果
    with open(test_data_path,'r+',encoding='utf-8') as f:
        ha=f.read()
        dat = yaml.load(ha, Loader=yaml.SafeLoader)
        test = dat['tests']
        print(test)


get_test_data(file_path + "\\..\\data\\test_in_theaters.yaml")

li1=[{'case': '验证响应中start和count与请求中的参数一致',
      'http': {'method': 'GET',
               'headers': {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'},
               'params': {'apikey': None, 'start': None, 'count': None}},
      'expected': {'response': {'status_code': 200}
                   }
      }
     ]
#

