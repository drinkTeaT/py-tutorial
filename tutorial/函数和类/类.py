class A:
    def __init__(self, name, age):
        # 无下划线表示公有属性
        self.name = name
        # 两条下划线表示私有属性
        self.__age = age
        # 一条下划线表示protected，不能直接访问
        self._wealth = "1 KG GOLD"

    def _card(self):
        print("name is ", self.name, " age is ", self.__age)


a = A('tom', 35)
print(a.name)


class B(A):
    def sub_card(self):
        # super()调用父类方法
        super()._card()

    def sub_card(self):
        print(self.name, self._wealth)


b = B("jack", 10)
b.sub_card()
