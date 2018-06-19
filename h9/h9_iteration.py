# python的迭代  for in
list1=[0,1]
for i in list1:
    print(i)
dict1={'k2':123,'k3':False}
for key in dict1:  # 隐式调用了key()
    print(key,dict1[key])
for key in dict1.keys():  # 对键进行循环
    print(key)
for v in dict1.values():  # 对值进行循环
    print(v)
for item in dict1.items():  # 对键值对进行循环
    print(item[0],item[1])
for char in 'AB':
    print(char)




