def generate():
    i = 0
    name = "hgq"
    while i < 5:
        print("我在这。。")
        xx = yield i,name # 注意，python程序，碰到=，都是先从右往左执行
        print(xx)
        i += 1

g = generate()
# g.send(None)  # <==> next(g) 第一次启动，执行到yield i（此时i=0），挂起任务，主程序继续往下执行
#
# g.send("lalala")
print(g.__next__()) # __next__  方法调用 yield 相当  return 的作用， 所以会把 i 的值返回来，但是只执行了右边，左边没有执行
print(g.__next__())
print(g.__next__())
print(g.send('gmy'))
# 生成器 是 迭代器的一种   一边遍历一边计算
