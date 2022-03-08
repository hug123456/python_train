import pytest
import os
import yaml


# @pytest.fixture(scope="session")
# def env(request):
#     config_path = os.path.join(request.config.rootdir,
#                                "api_pytest",
#                                "config",
#                                "test",
#                                "config.yaml")
#     with open(config_path) as f:
#         env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
#     return env_config

@pytest.fixture(scope='class')
def env(request):
    print("我是env函数")
    config_path = os.path.join(request.config.rootdir,
                               "api_pytest",
                               "config",
                               # "test",
                               request.config.getoption("environment"),
                               "config.yaml")
    with open(config_path) as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return env_config
#



def pytest_addoption(parser):
    print("我是钩子函数")
    parser.addoption("--env",
                     action="store",
                     dest="environment",
                     default="prod",
                     help="environment: test or prod")

# scope 范围  session, model, class, function
@pytest.fixture(scope="session",autouse=True)
def preparation():
    print("在数据库中准备测试数据")
    # test_data = "在数据库中准备测试数据"
    yield
    print("清理测试数据")

# fixture 可以传参
@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name": name, "orders": []}

    return _make_customer_record   #注意此处不加(),非函数调用

def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")


@pytest.fixture(scope='class')
def login():
    a = '123'
    print("fixture范围为class开始")
    yield
    print("fixture范围为class结束")


@pytest.fixture(scope='module')
def login_02():
    print("fixture范围为module开始")
    yield
    print("fixture范围为module结束")


# fixtrue作为参数，互相调用传入
@pytest.fixture()
def account():
    a = "account"
    print("第一层fixture")
    return a


# Fixture的相互调用一定是要在测试类里调用这层fixture才会生次，普通函数单独调用是不生效的
@pytest.fixture()
def login03(account):
    print("第二层fixture")


@pytest.fixture()
def logout01(account):
    print("logout01")


@pytest.fixture()
def logout02(account):
    print("logout02")








