#argument parameter 参数

# 位置参数
def power(x):
    return x*x
print(power(2))

def cube(x):
    return x*x*x
print(cube(2))
# 一个数 多次方的运算
def power(x,n):
    p=1
    while(n>0):
        p=p*x
        n-=1
    return p
print(power(2,2))
print(power(2,3))
print(power(3,4))
# 默认参数 放在必选参数的后面
def power2(x,n=2):
    p=1
    while(n>0):
        p=p*x
        n-=1
    return p
print(power2(2))    #后面的参数是默认的


def print_student_info(name,age,gender='Male',loc='Beijing'):
    print(name,age,gender,loc)
print(print_student_info('Tom',18))
print(print_student_info('Tom',18,'Female'))
print(print_student_info('Tom',18,loc='shanghai'))

# 可变参数
# print(max(-1,-2,70))
def sum(*n):
    s=0
    for i in n:
        s+=i
    return s
print(sum(1,2,3))

list1=[1,2,3,4]
print(sum(*list1))