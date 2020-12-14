# 不定长参数，会以元组的方式存储
def fun1(a, *b, c):
    """ *函数 """
    print(a, b, c)


fun1(1, 2, 3, 4, 5, c=3)


# **是以字典的方式导入
def fun2(a, b, **c):
    """ **函数 """
    print(a, b, c)


fun2(1, 2, name="tom", age=12)
