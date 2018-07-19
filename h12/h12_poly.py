# 多态：polymorphism


class Shape(object):
    def area(self):
        print('in Shape: area...')


class Circle(Shape):
    def area(self):
        print('in Circle: area...')


class Square(Shape):
    def area(self):
        print('in Square: area...')


x = list()

y = 123

z = 'Hello'


# isinstance

print(isinstance(x, list))

print(isinstance(y, int))

print(isinstance(z, str))

a = Circle()

b = Square()

c = Shape()

print(isinstance(a, Circle))

print(isinstance(b, Square))


# 子类是父类的实例
print(isinstance(c, Shape))

print(isinstance(a, Shape))

print(isinstance(b, Shape))

# a.area()
# b.area()


def test(shape):
    shape.area()

test(c)

test(a)

test(b)

# polymorphism 多态  就是传入不同的子类实例  输出不同的结果
# Python 是动态语言 Java是静态语言
# Triangle可以不继承shape父类 但必须要有area这个方法
class Triangle(object):
    def area(self):
        print('in triangle:area...')
d=Triangle()

test(d)

