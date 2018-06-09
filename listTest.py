
# list  数组
list=['a','b','c','d']
print(list)
print(len(list))
print(list[0])
print(list[len(list)-1])
print(list[-1]) # 输出最后一个
print(list[-4]) # 反向是第几个
list.append('e')
list.insert(1,'x')
print(list) # 把x放到1的位置
print(list.pop())  # 删除结尾
print(list)
print(list.pop(1))  #删除坐标的值
print(list)

list2=[123,1.23,True,'string...']
print(list2)

list3=[123,'abcd',['e1','e2','e3']]
print(len(list3))  #多维数组的写法
print(list3)