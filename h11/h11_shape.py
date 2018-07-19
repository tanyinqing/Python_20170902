
class Shape(object):
    def area(self):
        print('in shape:area...')
        pass
    def perimeter(self):
        print('in Shape:perimeter...')
        pass
class Circle(Shape):
    def area(self):
        print('in Circle:area...')
# 继承父类
class Square(Shape):
    def print_info(self):
        print('a new def in Square...')

class Triangle(Shape):
    def area(self):
        print('in Triangle:area...')

class Rectangle(Shape):
    def area(self):
        print('in Rectangle:area...')
    def perimeter(self):
        print('in Rectangle:perimeter..')


a_triangle=Triangle()
a_triangle.area()
a_circle=Circle();
a_square=Square();
a_circle.area()
a_circle.perimeter()
a_square.area()
a_square.perimeter()
a_square.print_info()