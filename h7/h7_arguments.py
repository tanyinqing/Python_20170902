
# 4 关键字参数
def student(name,age,**kw):
    print('name: ',name,':age:',age,':keywords: ',kw)
student('Tom',18)  # 空的大括号是字典 可以是任意个关键字
student('Jerry',18,loc='Beijing')  # 一个参数
student('Jerry',18,loc='Beijing',gender='Female') # 两个参数
dict1={'loc':'shanghai','gender':'Male','married':False} # 多个字典的值
student('Tester',20,**dict1) # 所有的关键字都进来了

# 命名关键字参数  参数必须要跟名字
def student1(name,age,**kw):
    if 'loc' in kw:
        print('loc',kw.get('loc'))
    if 'gender' in kw:
        print('gender',kw.get('gender'))
dict2={'loc':'Beijing','gender':'Male'}
print('loc' in dict2)
student1('Tom',18,**dict2)

def student2(name,age,*,loc,gender):  # *后的参数必须要有或是仅仅包含这两个键的字典
    print('loc',loc)
    print('gender',gender)
student2('jerry',18,loc='',gender='')
student2('tester',20,**dict2)

def student3(name,age,*args,loc,gender):  # 可变参数后的*可以省略
    print(name,age,args,loc,gender)
student3('Tom',18,loc='shanghai',gender='male')
student3('jeery',18,1,2,3,4,5,loc='guangzhou',gender='Female')
student3('jeery',18,1,loc='shanghai',gender='Female')


def student4(name,age,*args,loc,gender='Male'):# 命名关键字参数有一个默认值，可以不传值
    print(name,age,args,loc,gender)
student4('Tom',18,loc='Beijing')

# 函数的参数有位置 默认值 可变参数 关键字参数 d是命名关键字参数 5种
def test_function(a,b,c=0,*args,d,**kw):
    print(a,b,c,args,d,kw)
print(test_function(1,2,d=''))
print(test_function(1,2,3,4,5,6,d=7))
dict3={'k1':'v1','k2':'v2','k3':123,'k4':False}
print(test_function(1,2,3,4,5,6,d=7,**dict3))