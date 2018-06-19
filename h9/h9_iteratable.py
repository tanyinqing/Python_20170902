# 判断是否可以迭代
from collections import Iterable
print(isinstance('abcd',Iterable))
print(isinstance(['a',2,3],Iterable))
print(isinstance(('a',2,3),Iterable))
print(isinstance(1234,Iterable))
list1=['a','b']  # 输出下标
for index,value in enumerate(list1):
    print(index,value)
for x,y in [(1,2),(3,4)]: # 输出两个值的情况
    print(x,y)
