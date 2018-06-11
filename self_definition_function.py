
# 自定义函数
def self_abs(n):
    if not isinstance(n,(int ,float)):  # n是否是这两种类型
        raise TypeError('bad operand type')
    if n > 0:
        return n
    else:
        return -n

print(self_abs(-123))

# 定义函数 area/perimiter 求圆形的面积和周长 并测试
def circle_area(r):
    return 3.14*r*r
print(circle_area(1.23))

def circle_perimeter(r):
    return 3.14*r*2
print(circle_perimeter(1.23))

def nothin():
    pass
print(nothin())
# 不返回值的情况
def none_retrun_func(x,y):
    x+y
    return
print(none_retrun_func(1,2))
def multiple_return_func(x,y):
    return x,y

a,b=multiple_return_func(1,2)
print(a,b)
print(multiple_return_func(1,2)) # tuple