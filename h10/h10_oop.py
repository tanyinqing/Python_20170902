# 面向对象的编程
'''
Java  块注释
self 是python类中所有函数的第一个参数
调用函数时，不用给self传值
类和函数 之后必须有2个空行
'''

class Human(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print_info(self):
        print(self.name)
        print(self.age)


tom=Human('Tom',18)
tom.print_info()

print(tom.name)
print(tom.age)
print(tom)  # 输出一个16进制的地址