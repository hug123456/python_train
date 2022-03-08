*******写框架遇到一些问题

      1.问题一  **模块的动态导入**
               import sys
               sys.path.append("D:\\测试开发\\Test\\test_pytest框架\\api_pytest")
               **读取配置文件相对目录**
               file_path = os.path.join(os.path.dirname(__file__))

2.问题二  命令不太熟悉
         pytest -s 可以打印print 信息
                -k   -k 选项允许你使用表达式指定希望运行的测试用例
                -x  -x选项的特点是， 一旦遇到测试失败，就会全局停止。如果你希望pytest失败几次后再停止，则可以使用--maxfail选项，明确指定要以失败几次。 如设置--maxfail=2，则需要遇到两次错误才会停止
                -m  标记（marker）用于标记测试并分组
                -q  它会简化输出信息
                -v  使用-v/--verbose选项，输出的信息会更详细 *跟version 跟完全不一样哦
        --tb=style  常用的style类型有short、line、no。short模式仅输出assert的一行以及系统判定内容（不显示上下文）；line模式只使用一行输出显示所有的错误信息；no模式则直接屏蔽全部回溯信息


3.问题三  读取文件格式
         xls,yaml,json 之间对比


4.pytest 框架运行骨架和钩子函数
         理解


5. conftest.py 文件 fixture函数不需要导入，直接可以使用




**********************************************************************pytest 知识点总结
      ******一测试准备与收尾
            fixture作用
             做测试前后的初始化设置，如测试数据准备，链接数据库，打开浏览器等这些操作都可以使用fixture来实现。
             测试用例的前置条件可以使用fixture实现 。
             支持经典的xunit fixture ，像unittest使用的setup和teardown。
             fixture可以实现unittest不能实现的功能，比如unittest中的测试用例和测试用例之间是无法传递参数和数据的，但是fixture却可以解决这个问题。


           1)调用fixture有三种方式
             Fixture名字作为测试用例的参数
             使用@pytest.mark.usefixtures('fixture')装饰器
             使用autouse参数
             **备注： 如果fixture有返回值，那么usefixture以及autouse就无法获取到返回值，这个是装饰器usefixture与用例直接传fixture参数的区别。 因此最常用的是通过参数传递的方法。
           fixture函数需要传递参数



      ****** 参数化


           @pytest.mark.parametrize("num1, num2, num3", {
                                                          (4, 2, 6),
                                                          (2, 4, 6),
                                                          (3, 5, 8),
                                                          })
           def test_01(num1, num2, num3):
               print('test_01')
               assert num3 == num1+num2

      ****** 作用域
            autouse=True 谨慎使用



*****************************************************失败重跑  pytest-rerunfailures是属于pytest的插件
            ****第一种方式
                 @pytest.mark.flaky(reruns=3, reruns_delay=2)




            ****第二种方式
                 pytest --reruns 3 --reruns-delay 2 或 pytest -vs --reruns=3 --reruns-delay=2
                 参数详解：其中reruns空格3 表示失败重新运行3次，reruns-delay空格2 表示重新执行需要等待2秒。这里也可以使用等于来进行表示




********************************************************************pytest 核心功能点
                                 1.多种插件(辅助多种功能 1.用例执行顺序 2.失败重跑  3.测试报告   4.用例并发执行(提高执行时间))
                                 2.灵活调用fixture
                                 3.钩子函数(辅助功能)  ***重点***
                                 4.命令启动测试用例范围
