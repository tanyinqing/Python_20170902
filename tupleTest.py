
# tuple  元组
tuple1=('a','b','c','d')
print(tuple1)
# print[0]='x'  元素的值不可以改变

tuple2=()   # 空的元组
print(tuple2)

tuple3=(True,) #只有一个元素的写法
print(tuple3)

tuple4=('1','2','3',[4,5,6])
print(tuple4)
print(tuple4[-1])
tuple4[-1].append(7)  # 为列表中的元素增加元素
print(tuple4[-1])
