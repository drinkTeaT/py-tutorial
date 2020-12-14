# 内置函数作用于类对象时，需要重写内置函数
class Tom:
    def __init__(self):
        self._name = 'tom'
        self._age = 12

    def __str__(self):
        return self._name + " " + str(self._age)


tom = Tom()
print(str(tom))

# 迭代器
v = list(range(5))
print(v)
