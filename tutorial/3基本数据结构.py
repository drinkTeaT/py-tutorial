# 容器序列：list,tuple,collections.deque 存放引用
# 扁平序列:str,bytes,array.array 存放值
symbols = '123abc'
codes = []
# 列表推导，即for循环的语法糖。无圆括号。
codes = [i for i in symbols]
print(type(codes))
# 笛卡尔积，即嵌套for循环
codes = [(c, c1) for c in codes for c1 in codes]
print(type(codes))
# 生成器表达式。返回一个生成器的类。加了圆括号的列表推导。逐个产出元素，而不是先产出再遍历。一般放进构造函数里面
codes = (i for i in symbols)
codes = list((i for i in symbols))
# 元组
tu = tuple((i for i in symbols))
ini = ('tom', 'tokyo', 12)
# 元组拆包(平行赋值)
name, city, age = ini
# 交换变量
name, city, age = age, city, name


# 用*加元组变量名作为入参，以及用_接收元组不敢兴趣的参数
def plus(a, b):
    return a + b, b


tu = (1, 2)
res, _ = plus(*tu)

# *接收不确定参数
a, *b, c = range(5)
print(a, b, c)
