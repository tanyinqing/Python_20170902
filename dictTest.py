
# dictionary 字典类型
dict={'key1':'value1','key2':'value2'}
print(dict['key1'])
dict2={'k1':123,'k2':True,'k3':'value3',}
print(dict2['k2'])
dict2['k2']=False
print(dict2['k2'])
print(dict2.get('k11'))
print(dict2.get('k11',-1))
dict2.pop('k1')  # 删除键对应的值
print(dict2.get('k1',-1))

dict2['k4']=123.456
print(dict2['k4'])

print(dict2.keys())
print(dict2.values())
print(dict2.items())


