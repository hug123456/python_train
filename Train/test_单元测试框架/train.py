# coding=utf-8
'''
Created on 2016-7-26
@author: Jennifer
Project:编写Web测试用例
'''
import unittest
from test_单元测试框架.baidu import BaiduTest
from test_单元测试框架.test_baidu import YoudaoTest

#构造测试集  测试用例执行顺序跟加载顺序相关
suite = unittest.TestSuite()
suite.addTest(BaiduTest('test_baidu01'))
suite.addTest(YoudaoTest('test_baidu02'))

if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)