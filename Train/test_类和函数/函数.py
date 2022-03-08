# --------------------------------------- 函数传参--------------------------------------------

def test(b,a="hgq",*args,**kwargs):    ## 入参的顺序是固定的 第一个变量， 第二个是常量 这个常量(也可以变化) ，第三个是*args(元祖), 第四个是**kwargs(字典格式)
    print(b,a,args,kwargs)
# test("aolige")
test("haxi",1,2,3,{"name":"gmy"},name="hxy")

test("haxi","gmy",{"name":"hxy"})

test("haxi",[1,2,3,4],{"name":"hxy"})

test((1,2,3))

test({"name":"hxy"})

test(["黄国庆"])

# test(name="ha")   报错

# 
