# 访问限制修饰符
class Human:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  # age 是私有的属性
    def print_info(self):
        print(self.name,self.age)


tom=Human('Tom',18)
# tom.print_info()
print(tom.name)
print(tom.age)