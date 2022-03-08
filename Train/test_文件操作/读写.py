# **********  with关键字  ******

"""
with 语句实质是上下文管理。
1、上下文管理协议。包含方法__enter__() 和 __exit__()，支持该协议对象要实现这两个方法。
2、上下文管理器，定义执行with语句时要建立的运行时上下文，负责执行with语句块上下文中的进入与退出操作。
3、进入上下文的时候执行__enter__方法，如果设置as var语句，var变量接受__enter__()方法返回值。
4、如果运行时发生了异常，就退出上下文管理器。调用管理器__exit__方法。
"""


# 总结  知识点with 上下文管理器， reade / readline / readlines 区别
#举例一
with open("test1.txt",encoding="utf-8") as f:
    response_txt = f.read()      #总结  文件全部都读取出来    内存资源充足下使用
    # response_txt1=f.readline()     #总结  一行一行的读取文件  资源不充足情况下使用
    # response_txt2=f.readlines()  #总结   每一行都放到文件列表中
    # print(response_txt2)
    # print(response_txt1)
    print(response_txt)

# 总结  知识点with 上下文管理器， reade / readline / readlines 区别




# 总结：r,w, a, r+,w+,a+ 区别
# 举例二
#     ***********************  r和r+   **********************************
with open("test2.txt",'r+',encoding="utf-8") as f1:
    print(f1.tell())
    response_readlines=f1.write("哈希我是r+写入")  # **总结：默认每次重文件开头重洗写入
    print(f1.tell())
    # f1.seek(0)
    # print(f1.read())                             **总结： 写完指针放到末尾

# with open("test2.txt",'r',encoding="utf-8") as f1:
#     print(f1.tell())
#     response_readlines=f1.write("哈希我是r+写入")  # **总结：写入失败 mode=r 只能读不能写
#     print(f1.tell())


#     ***********************  w和w+   **********************************

# with open("test3.txt",'w',encoding="utf-8") as f3:
#
#     # f3.write("哈希我是w写入")  # **总结：**首先清空文件内容，然后再写入.不能读
#     response_txt3=f3.readlines()
#     print(response_txt3)

#
#
# with open("test3.txt",'w+',encoding="utf-8") as f4:
#     response_readlines=f4.write("哈希我是w+写入")  # **总结：**首先清空文件内容，然后再写入。指针默认在末尾
#     # f4.seek(0)                                   # 把指针重新放到首位
#     response4_txt=f4.readlines()
#     print(response4_txt)                           # 文件指针在末尾，所以为[],f4.seek(0) 把指针重新设置为首位，才可以读取到内容

    #


with open("test4.txt","a",encoding="utf-8") as f5:
    f5.write("你是最棒的 /d")
    # print(f5.readlines())      # *** 总结 "a"追加写 不能读


with open("test5.txt", "a+", encoding="utf-8") as f6:
    f6.write("你是最棒的 /d")
    f6.seek(0)                # ** 写完指针放在文件最后
    print(f6.readlines())
    # readlines readlines readlines



